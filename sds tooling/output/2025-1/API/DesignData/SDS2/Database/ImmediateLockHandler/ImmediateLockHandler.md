# Class ImmediateLockHandler 

An ILockHandler that fails immediately when a lock cannot be taken.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ImmediateLockHandler

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

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class ImmediateLockHandler : ILockHandler
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FImmediateLockHandler%5F%5Fctor)ImmediateLockHandler()

An ILockHandler that fails immediately when a lock cannot be taken.

##### Declaration

```
public ImmediateLockHandler()
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FImmediateLockHandler%5FEventLoop)EventLoop()

An ILockHandler that fails immediately when a lock cannot be taken.

##### Declaration

```
public bool EventLoop()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FImmediateLockHandler%5FLockFailed%5FDesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FSystem%5FString%5F)LockFailed(TableIndexHandle, string)

Once this has been called, we will abort on the next call to EventLoop. This way, as soon as we fail to get any lock we abort.

##### Declaration

```
public void LockFailed(TableIndexHandle databaseItem, string userMessage)
```

##### Parameters

| Type                                                               | Name         | Description |
| ------------------------------------------------------------------ | ------------ | ----------- |
| [TableIndexHandle](DesignData.SDS2.Database.TableIndexHandle.html) | databaseItem |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string)     | userMessage  |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FImmediateLockHandler%5FLockSucceeded%5FDesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5F)LockSucceeded(TableIndexHandle)

Nothing special is done for a successful lock.

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