# Transaction Model

## [](#preface)Preface

SDS2 uses an immediate multi-user model. Where many programs operate by having each user take a copy of the model, and occasionally upload their changes to a central version; SDS2 has all users work inside that central model. Every change a user makes instantly applies and impacts every other user.

To facilicate this SDS2 makes extensive use of locking before an attempt is made to make a change. Assuming you can get all locks we know you can proceed to make a change.

So, inside SDS2, to make a change we:

1. Refresh tables
2. Find things (members, materials, etc) we want to modify
3. Lock needed items
4. Refresh tables
5. Make our changes
6. Lock any additional items to account for interdependencies for those changes.
7. Write out changes

For API users this is simplified and looks like:

1. Find things (members, materials, etc) we want to modify
2. Lock needed items
3. Make our changes
4. Commit changes

## [](#overview)Overview

The transaction model used in SDS2 has to solve several problems:

1. **Stale data** \- SDS2 has one copy of the job in memory, but another copy exists on disk. And as other users may also be in the job, they also have a copy in memory. We do something called "refreshing" to efficiently update the in memory copy and load in any changes on disk.
2. **Mutual exclusion/locking** \- When we want to make a change, in order to make sure we don't overwrite changes another user is making, we lock items in the model. Members, group members, etc.
3. **Interconnectedness** \- Many elements of an SDS2 job are interconnected. Some by spatial relationships, and others are batched because they're similar. Spatial relationships would be things like a beam connecting to a column, and batching would be things like two beams sharing a piecemark. This forms of interconnectedness are maintained with every change. As a result, we sometimes have to refresh and lock items which aren't obvious.

## [](#stale-data---refreshing)Stale Data - Refreshing

For API users, you should generally stick to the automatic mechanism for this. The transaction constructors have a default argument `manualRefresh=false`. Leave that false and SDS2 will do one refresh of each table as it's needed for the life of that transaction object.

But you can set this to manual, and then you'll need to call `RefreshTable` on the appropriate tables.

## [](#mutual-exclusion---locking)Mutual Exclusion - Locking

SDS2's multi-user model is real time. Every change is immediately visible to every user of the job. Every user is modifying the same copy of the job at the same time.

To make this work, we lock parts of the database. Generally, SDS2 handles this by locking members, but the API requires users to lock every element: Members, materials, welds, bolts, etc. Often these will, behind the scenes, lock additional members for reasons which often depend on setup options.

Since locks can fail, and a decision must be made about how long to try and wait for that lock, we have a [LockHandler](../api/DesignData.SDS2.Database.ILockHandler.html). Users can implement their own, or use one we've already implemented.

It's expected that it will often be best to use an interactive lock handler, which will present the user with a dialog asking if they'd like to keep waiting for locks or if they'd like to give up an abort the operation. Because of this, it's important to make a minimal number of lock attempts to avoid showing this dialog over and over.

### [](#tables)Tables

SDS2 refreshes operate on what we call tables. These are tables in a database. There is a table of all members. A table of all group members. A table of all member piecemarks, etc.

So when working with members, you need to refresh the member table. When working with groups, the group table. If you leave it set to automatic, the default behaviour, this is all handled for you.

### [](#lockhandler)LockHandler

We have several lock handlers to choose from, and users can create their own.

#### [](#builtin-lockhandlers)Builtin LockHandlers

1. [ImmediateLockHandler](../api/DesignData.SDS2.Database.ImmediateLockHandler.html) \- This is an easy one for us to use in examples, but it's rarely what you want. This handler gives up as soon as it finds an element is locked by another user.
2. [InteractiveLockHandler](../api/DesignData.SDS2.WinForms.InteractiveLockHandler.html) \- This is a GUI lock handler which prompts the user. The user can abort at any time, otherwise it continues to keep trying to get a lock. The GUI is built in Windows Forms.

#### [](#custom-lockhandlers)Custom LockHandlers

Simply create a class which implements [ILockHandler](../api/DesignData.SDS2.Database.ILockHandler.html) and implement the three methods:

```
public void LockSucceeded(TableIndexHandle databaseItem)
{
    //This is called when this process successfully locks something
}

```

```
public void LockFailed(TableIndexHandle databaseItem, string userMessage)
{
    //This is called when something cannot be locked because it's
    //locked by another user.
}

```

```
public bool EventLoop()
{
    //This is called after each attempt to get all locks
    //You can abort the lock operation by returning false,
    //or request another attempt by returning true.
    //Before returning you can do interactive things, or sleep
    //or log or whatever you need to do.
}

```

To implement a custom handler you need to combine the `LockSucceeded` callback with the `LockFailed` callback and implement something useful in the `EventLoop` callback using that information.

A useful LockHandler you might implement might be one that tries for 60 seconds and then gives up. Another useful type might be one similar to the builtin [InteractiveLockHandler](../api/DesignData.SDS2.WinForms.InteractiveLockHandler.html) where the interface conforms to your standards.

## [](#interconnectedness---piecemarkingconnection-design)Interconnectedness - Piecemarking/Connection design

There are many surprising relationships between things in SDS2\. Changing a column will often require locking all of the beams connecting to it. Changing those beams will require a lock of that column, but usually only other beams if they connect at the same location on the column.

Each member has a piecemark, and modifications may require locking other members with that piecemark.

## [](#read-example)Read Example

```
using(var xaction = new ReadOnlyTransaction(job))
{
    var member = Member.Get(job.Members[3]);
    var material = member.GetMaterial()[0] as RolledShapeMaterial;
    Console.WriteLine(material.Usage);
}

```

Even when performing read operations we prefer that users use a [ReadOnlyTransaction](../api/DesignData.SDS2.Database.ReadOnlyTransaction.html). This object functions to help work with the model at a single point in time.

There is no need to lock in a [ReadOnlyTransaction](../api/DesignData.SDS2.Database.ReadOnlyTransaction.html) and because there are no changes being made there is nothing to `Commit`.

You can read without a ReadOnlyTransaction. However, each property you check, each object you grab, SDS2 will refresh tables. This can lead to reduced performance. So if performance is a consideration, you should use a ReadOnlyTransaction. This will limit use to one refresh per table for the life of your ReadOnlyTransaction.

## [](#write-example)Write Example

```
//To start, we must use a transaction in a using statement
//SDS2 depends on the RAII behaviour the using statement provides us.
//We've chosen an ImmediateLockHandler here, which will give up
//as soon as any lock is not available.  This is likely not the best
//choice for must use cases.
using(var xaction = new Transaction(job, new ImmediateLockHandler()))
{
    //Get our member:
    var member = Member.Get(job.Members[3]);
    //Get the material on it
    var material = member.GetMaterial()[0] as RolledShapeMaterial;
    //Lock our member and material by adding them to
    //the transaction before calling Lock
    xaction.Add(member);
    xaction.Add(material);
    if(xaction.Lock())
    {
        //finally make the change we were interested in
        material.Usage = "example";

        //Commit our change
        if(!xaction.Commit())
            Console.WriteLine("We couldn't commit the change we needed!");
    }
    else
        Console.WriteLine("We couldn't get the lock we needed!");
}

```

You can queue up as many changes before calling Commit as you like, but there are some things to consider with that:

1. Locks are held from when they're taken on the transaction, until the transaction is disposed (the end of the using statement).
2. If the commit fails, all queued changes will be abandoned.

Once you've called `Commit`, assuming it returns true, your changes have been made to the model and cannot be undone. You can continue to make more changes and call `Commit` again, assuming all of the locks you already took are still held. In general, it's better to finish after a `Commit` and start a new transaction rather than continueing to use the same one to avoid the accumulation of unneeded locks. But there are cases where it makes sense to `Commit` multiple times with the same transaction.

## [](#handling-failure)Handling Failure

Since locks and transactions can fail, API users will need to handle failures in calls to `Lock` and `Commit`. `Lock` can return false, indicating a lock failed. 'Commit\` returns a [TransactionFailure](../api/DesignData.SDS2.Database.TransactionFailure.html) which may either indicate that the transaction succeeded or document a reason for failure.

For `TransactionFailure` objects, you can simply cast them to a bool. True means it succeeded, and False means it failed. The `TransactionFailure` object also has a enumeration value indicating the cause of the failure, and a string which could be displayed to the user to indicate the cause of the failure.

Generally the only option is to back out and notify the user that the change couldn't be made. For `Lock` this can be handled by using an interactive [LockHandler](../api/DesignData.SDS2.Database.ILockHandler.html); because it's interactive the user will already know they aborted the lock operation. For `Commit` you may have to notify the user that the operation couldn't complete for unknown reasons.