# Class ReadOnlyTransaction 

This is effectively a read-only transaction object. Use it to get the most up to date data for each member.

Construct the object with the active job.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ReadOnlyTransaction

[Transaction](DesignData.SDS2.Database.Transaction.html)

##### Implements

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class ReadOnlyTransaction : IDisposable
```

##### **Remarks**

This object should be disposed when it's no longer in use, use this with a using statement.

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FReadOnlyTransaction%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FJob%5FSystem%5FBoolean%5F)ReadOnlyTransaction(Job, bool)

This is effectively a read-only transaction object. Use it to get the most up to date data for each member.

Construct the object with the active job.

##### Declaration

```
public ReadOnlyTransaction(Job activeJob, bool manualRefresh = false)
```

##### Parameters

| Type                                                          | Name          | Description                                                                   |
| ------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------- |
| [Job](DesignData.SDS2.Database.Job.html)                      | activeJob     | If it is not already opened, this job will be opened and made the active job. |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | manualRefresh | When set to true, you will need to make your own calls to RefreshTable.       |

##### Remarks

This object should be disposed when it's no longer in use, use this with a using statement.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FReadOnlyTransaction%5FDispose)Dispose()

This is effectively a read-only transaction object. Use it to get the most up to date data for each member.

Construct the object with the active job.

##### Declaration

```
public void Dispose()
```

##### Remarks

This object should be disposed when it's no longer in use, use this with a using statement.

#### [](#DesignData%5FSDS2%5FDatabase%5FReadOnlyTransaction%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

This is effectively a read-only transaction object. Use it to get the most up to date data for each member.

Construct the object with the active job.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Remarks

This object should be disposed when it's no longer in use, use this with a using statement.

#### [](#DesignData%5FSDS2%5FDatabase%5FReadOnlyTransaction%5FFinalize)\~ReadOnlyTransaction()

This is effectively a read-only transaction object. Use it to get the most up to date data for each member.

Construct the object with the active job.

##### Declaration

```
protected ~ReadOnlyTransaction()
```

##### Remarks

This object should be disposed when it's no longer in use, use this with a using statement.

#### [](#DesignData%5FSDS2%5FDatabase%5FReadOnlyTransaction%5FRefreshTable%5FDesignData%5FSDS2%5FDatabase%5FTable%5F)RefreshTable(Table)

Call this before accessing members (using Get or GetBrief). This will read all of the "fixed" data for all members, and ensure that we know whether members have been deleted or not.

Any data read here is subject to change as long as items (such as members) are not locked.

##### Declaration

```
public void RefreshTable(Table table)
```

##### Parameters

| Type                                         | Name  | Description |
| -------------------------------------------- | ----- | ----------- |
| [Table](DesignData.SDS2.Database.Table.html) | table |             |

##### Remarks

This object should be disposed when it's no longer in use, use this with a using statement.

##### Exceptions

| Type                                                                       | Condition                                          |
| -------------------------------------------------------------------------- | -------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html) | If another job has been Opened since this one was. |

### [](#implements)Implements

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)