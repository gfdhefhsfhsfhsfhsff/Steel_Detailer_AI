# Class InteractiveLockHandler 

Pass one of these to Transaction.Lock to get a GUI lock screen when locks aren't immediately available. Users will be able to abort waiting for locks which will cause your Lock() call to return false.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

InteractiveLockHandler

##### Implements

[ILockHandler](DesignData.SDS2.Database.ILockHandler.html)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[WinForms](DesignData.SDS2.WinForms.html)

###### **Assembly**: DesignData.SDS2.WinForms.dll

##### Syntax

```
public class InteractiveLockHandler : ILockHandler
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FWinForms%5FInteractiveLockHandler%5F%5Fctor)InteractiveLockHandler()

Pass one of these to Transaction.Lock to get a GUI lock screen when locks aren't immediately available. Users will be able to abort waiting for locks which will cause your Lock() call to return false.

##### Declaration

```
public InteractiveLockHandler()
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FWinForms%5FInteractiveLockHandler%5FEventLoop)EventLoop()

Pass one of these to Transaction.Lock to get a GUI lock screen when locks aren't immediately available. Users will be able to abort waiting for locks which will cause your Lock() call to return false.

##### Declaration

```
public bool EventLoop()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FWinForms%5FInteractiveLockHandler%5FLockFailed%5FDesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FSystem%5FString%5F)LockFailed(TableIndexHandle, string)

Pass one of these to Transaction.Lock to get a GUI lock screen when locks aren't immediately available. Users will be able to abort waiting for locks which will cause your Lock() call to return false.

##### Declaration

```
public void LockFailed(TableIndexHandle databaseItem, string userMessage)
```

##### Parameters

| Type                                                               | Name         | Description |
| ------------------------------------------------------------------ | ------------ | ----------- |
| [TableIndexHandle](DesignData.SDS2.Database.TableIndexHandle.html) | databaseItem |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string)     | userMessage  |             |

#### [](#DesignData%5FSDS2%5FWinForms%5FInteractiveLockHandler%5FLockSucceeded%5FDesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5F)LockSucceeded(TableIndexHandle)

Pass one of these to Transaction.Lock to get a GUI lock screen when locks aren't immediately available. Users will be able to abort waiting for locks which will cause your Lock() call to return false.

##### Declaration

```
public void LockSucceeded(TableIndexHandle databaseItem)
```

##### Parameters

| Type                                                               | Name         | Description |
| ------------------------------------------------------------------ | ------------ | ----------- |
| [TableIndexHandle](DesignData.SDS2.Database.TableIndexHandle.html) | databaseItem |             |

### [](#implements)Implements

[ILockHandler](DesignData.SDS2.Database.ILockHandler.html)