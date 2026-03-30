# Class Transaction 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ReadOnlyTransaction](DesignData.SDS2.Database.ReadOnlyTransaction.html)

Transaction

##### Implements

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

##### Inherited Members

[ReadOnlyTransaction.Dispose()](DesignData.SDS2.Database.ReadOnlyTransaction.html#DesignData%5FSDS2%5FDatabase%5FReadOnlyTransaction%5FDispose) 

[ReadOnlyTransaction.RefreshTable(Table)](DesignData.SDS2.Database.ReadOnlyTransaction.html#DesignData%5FSDS2%5FDatabase%5FReadOnlyTransaction%5FRefreshTable%5FDesignData%5FSDS2%5FDatabase%5FTable%5F) 

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
public class Transaction : ReadOnlyTransaction, IDisposable
```

##### **Remarks**

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FJob%5FDesignData%5FSDS2%5FDatabase%5FILockHandler%5FSystem%5FBoolean%5F)Transaction(Job, ILockHandler, bool)

##### Declaration

```
public Transaction(Job activeJob, ILockHandler lockHandler, bool manualRefresh = false)
```

##### Parameters

| Type                                                          | Name          | Description                                                                                                 |
| ------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------- |
| [Job](DesignData.SDS2.Database.Job.html)                      | activeJob     | If it is not already opened, this job will be opened and made the active job.                               |
| [ILockHandler](DesignData.SDS2.Database.ILockHandler.html)    | lockHandler   | See documentation for this interface, callbacks will be called on this as we go through the locking process |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | manualRefresh | When set to true, you will need to make your own calls to RefreshTable.                                     |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FBoltHandle%5F)Add(BoltHandle)

Add a bolt to the transaction so that it can be modified. You will need to Lock() again after adding bolts.

##### Declaration

```
public void Add(BoltHandle bolt)
```

##### Parameters

| Type                                                   | Name | Description |
| ------------------------------------------------------ | ---- | ----------- |
| [BoltHandle](DesignData.SDS2.Database.BoltHandle.html) | bolt |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FComponentHandle%5F)Add(ComponentHandle)

Add a component to the transaction so that it can be modified. You will need to Lock() again after adding components.

##### Declaration

```
public void Add(ComponentHandle component)
```

##### Parameters

| Type                                                             | Name      | Description |
| ---------------------------------------------------------------- | --------- | ----------- |
| [ComponentHandle](DesignData.SDS2.Database.ComponentHandle.html) | component |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FCustomPropertyMapHandle%5F)Add(CustomPropertyMapHandle)

Add a custom property map to the transaction so that it can be modified. You will need to Lock() again after adding maps.

##### Declaration

```
public void Add(CustomPropertyMapHandle handle)
```

##### Parameters

| Type                                                                             | Name   | Description |
| -------------------------------------------------------------------------------- | ------ | ----------- |
| [CustomPropertyMapHandle](DesignData.SDS2.Database.CustomPropertyMapHandle.html) | handle |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F)Add(DrawingHandle)

Add a drawing to the transaction so that it can be modified. You will need to Lock() again after adding drawings.

##### Declaration

```
public void Add(DrawingHandle drawing)
```

##### Parameters

| Type                                                         | Name    | Description |
| ------------------------------------------------------------ | ------- | ----------- |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html) | drawing |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FFabricatorHandle%5F)Add(FabricatorHandle)

Add fabricator to the transaction so that it can be modified. You will need to Lock() again after adding fabricator.

##### Declaration

```
public void Add(FabricatorHandle handle)
```

##### Parameters

| Type                                                               | Name   | Description |
| ------------------------------------------------------------------ | ------ | ----------- |
| [FabricatorHandle](DesignData.SDS2.Database.FabricatorHandle.html) | handle |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandle%5F)Add(GridLineHandle)

Add a grid line to the transaction before locking so that it can be modified.

##### Declaration

```
public void Add(GridLineHandle handle)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html) | handle |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandle%5F)Add(GroupMemberHandle)

Add a group member to the transaction before locking so that it can be modified.

##### Declaration

```
public void Add(GroupMemberHandle handle)
```

##### Parameters

| Type                                                                 | Name   | Description |
| -------------------------------------------------------------------- | ------ | ----------- |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html) | handle |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FHoleHandle%5F)Add(HoleHandle)

Add a hole to the transaction so that it can be modified. You will need to Lock() again after adding holes.

##### Declaration

```
public void Add(HoleHandle hole)
```

##### Parameters

| Type                                                   | Name | Description |
| ------------------------------------------------------ | ---- | ----------- |
| [HoleHandle](DesignData.SDS2.Database.HoleHandle.html) | hole |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FJobSetupHandle%5F)Add(JobSetupHandle)

Add job setup to the transaction so that it can be modified. You will need to Lock() again after adding job setup.

##### Declaration

```
public void Add(JobSetupHandle handle)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [JobSetupHandle](DesignData.SDS2.Database.JobSetupHandle.html) | handle |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FMaterialFileHandle%5F)Add(MaterialFileHandle)

Add a material file to the transaction so that it can be modified. You will need to Lock() again after adding a material file.

##### Declaration

```
public void Add(MaterialFileHandle handle)
```

##### Parameters

| Type                                                                   | Name   | Description |
| ---------------------------------------------------------------------- | ------ | ----------- |
| [MaterialFileHandle](DesignData.SDS2.Database.MaterialFileHandle.html) | handle |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FMaterialHandle%5F)Add(MaterialHandle)

Add a material to the transaction so that it can be modified. You will need to Lock() again after adding materials.

##### Declaration

```
public void Add(MaterialHandle material)
```

##### Parameters

| Type                                                           | Name     | Description |
| -------------------------------------------------------------- | -------- | ----------- |
| [MaterialHandle](DesignData.SDS2.Database.MaterialHandle.html) | material |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F)Add(MemberHandle)

Add a member to the transaction before locking so that it can be modified.

##### Declaration

```
public void Add(MemberHandle memberHandle)
```

##### Parameters

| Type                                                       | Name         | Description |
| ---------------------------------------------------------- | ------------ | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) | memberHandle |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FNoteHandle%5F)Add(NoteHandle)

Add a note to the transaction before locking so that it can be modified.

##### Declaration

```
public void Add(NoteHandle handle)
```

##### Parameters

| Type                                                   | Name   | Description |
| ------------------------------------------------------ | ------ | ----------- |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html) | handle |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandle%5F)Add(UserDefinedConnectionHandle)

Add a new user defined connection to the list of user defined connections on commit. Once you've done this, and then Committed, then you can use this connection on the end of a member.

##### Declaration

```
public void Add(UserDefinedConnectionHandle handle)
```

##### Parameters

| Type                                                                                     | Name   | Description |
| ---------------------------------------------------------------------------------------- | ------ | ----------- |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html) | handle |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FWeldHandle%5F)Add(WeldHandle)

Add a weld to the transaction so that it can be modified. You will need to Lock() again after adding welds.

##### Declaration

```
public void Add(WeldHandle weld)
```

##### Parameters

| Type                                                   | Name | Description |
| ------------------------------------------------------ | ---- | ----------- |
| [WeldHandle](DesignData.SDS2.Database.WeldHandle.html) | weld |             |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FCommit%5FSystem%5FBoolean%5F)Commit(bool)

Commit changes made inside this transaction.

##### Declaration

```
public TransactionFailure Commit(bool processMembers = false)
```

##### Parameters

| Type                                                          | Name           | Description |
| ------------------------------------------------------------- | -------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | processMembers |             |

##### Returns

| Type                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [TransactionFailure](DesignData.SDS2.Database.TransactionFailure.html) | A TransactionFailure object, which is implicitly castable to a boolean to indicate if the commit succeeded (true). Or to a string for the user presentable reason it failed (or the empty string if it passed). Or to a TransactionFailureCode to indicate why it failed. So you can write: if(transaction.Commit()) {    //only happens if the commit passes! } Or: var failure = transaction.Commit(); if(failure.TransactionFailed) {     //only happens if the commit fails!     Console.WriteLine(failure.Reason); } |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[ReadOnlyTransaction.Dispose(bool)](DesignData.SDS2.Database.ReadOnlyTransaction.html#DesignData%5FSDS2%5FDatabase%5FReadOnlyTransaction%5FDispose%5FSystem%5FBoolean%5F)

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

#### [](#DesignData%5FSDS2%5FDatabase%5FTransaction%5FLock)Lock()

Lock everything which has been added to this transaction. Once it's been locked you can safely use Get and GetBrief and then modify data before committing.

##### Declaration

```
public bool Lock()
```

##### Returns

| Type                                                          | Description                                                    |
| ------------------------------------------------------------- | -------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | false if we couldn't get all locks, otherwise true is returned |

##### Remarks

A Transaction must be used in a using statement so that it will be properly disposed at the end of that block of code. Otherwise, the locks held by the Transaction may be held until the Transaction is garbage-collected.

Transaction objects may be reused after a commit. Handles that have been added to a Transaction are kept through the commit. Handles cannot be removed from a Transaction.

### [](#implements)Implements

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)