# Working with lockables

SDS/2 connections expose many of their properties as `Lockable` objects. These objects are a combination of a boolean and a value (often a double, but not always). The value can locked, and then set by the user or API. Or it can be unlocked, and then it will be calculated by the system during process. When unlocked, the value is still available to be read by the user/API.

Internally these values are tracked by a unique key, as a string. And there are many possible keys across all of the different connection types.

So to access these you need the key/name. And the best way to do that is to write a quick little program to scan over all of the lockables on the same type of connection, looking for the right label (which can be seen on member edit) and getting the associated key.

![](../images/lockables_ns_clip.png) 

In the image you can see several lockables, as you would see them in member edit. We're going to try to grab the value for "A) Top of angle."

First we need to create a throwaway script to find this value.

```
//this is throw away code, just to figure out the key name we want.
string key = "";
string label = "Top of angle";
using(var transaction = new ReadOnlyTransaction(job))
{
    var member = Member.Get(job.Members[43]);
    var connectionComponent = member.Ends[0].ConnectionComponent;
    foreach(var keyValuePair in connectionComponent.GetLockables())
    {
        string lockableLable = connectionComponent.GetLabelForLockableName(keyValuePair.Key);
        if(lockableLable == label)
            key = keyValuePair.Key;
    }
}
Console.WriteLine(string.Format("The key: {0}", key));

```

Don't save and use this code each time, just print out `key` and use that string in your code. You'll notice we dropped the "A) " at the beginning of the label and the ":" at the end, these are not part of the label as returned by [ConnectionComponent.GetLabelForLockableName](../api/DesignData.SDS2.Model.ConnectionComponent.html#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FGetLabelForLockableName%5FSystem%5FString%5F).

Your final code should look more like the following:

```
//this is our final code to grab this specific lockable value.
using(var transaction = new ReadOnlyTransaction(job))
{
    var member = Member.Get(job.Members[43]);
    var connectionComponent = member.Ends[0].ConnectionComponent;
    LockableDouble lockableValue = connectionComponent.GetLockable("ns.top_of_angle") as LockableDouble;
    Console.WriteLine(string.Format("Locked: {0}  Value: {1}",
                                    lockableValue.IsLocked,
                                    lockableValue.Value));
}

```

You can see we've hard coded the name/key for our lockable: "ns.top\_of\_angle".

Now, if you want to change a lockable, it's much the same thing. Except you'll need to set the lock before changing the value, and you need to assign the lockable back to the connection since the lockables you retrieve are always copies.

```
using(var transaction = new Transaction(job, new ImmediateLockHandler()))
{
    var member = Member.Get(job.Members[43]);
    transaction.Add(member);
    var connectionComponent = member.Ends[0].ConnectionComponent;
    transaction.Add(connectionComponent);
    transaction.Lock();
    LockableDouble lockableValue = connectionComponent.GetLockable("ns.top_of_angle") as LockableDouble;
    lockableValue.LockType = LockType.ViaMemberEdit;
    lockableValue.Value = 2.0;
    connectionComponent.SetLockable("ns.top_of_angle", lockableValue);
    transaction.Commit();
}

```