# Class LockablePlateSide 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockablePlateSide

##### Inherited Members

[Lockable.Unlock()](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FUnlock) 

[Lockable.GetIsLocked()](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FGetIsLocked) 

[Lockable.ToString()](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FToString) 

[Lockable.LockType](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FLockType) 

[Lockable.IsLocked](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FIsLocked) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public sealed class LockablePlateSide : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockablePlateSide%5F%5Fctor)LockablePlateSide()

##### Declaration

```
public LockablePlateSide()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockablePlateSide%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FPlateSide%5F)LockablePlateSide(PlateSide)

Create a locked ViaMemberEdit LockablePlateSide from a PlateSide

##### Declaration

```
public LockablePlateSide(PlateSide value)
```

##### Parameters

| Type                                              | Name  | Description |
| ------------------------------------------------- | ----- | ----------- |
| [PlateSide](DesignData.SDS2.Model.PlateSide.html) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockablePlateSide%5FValue)Value

The underlying value

##### Declaration

```
public PlateSide Value { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [PlateSide](DesignData.SDS2.Model.PlateSide.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockablePlateSide%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[Lockable.Dispose(bool)](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FDispose%5FSystem%5FBoolean%5F)

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FModel%5FLockablePlateSide%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockablePlateSide%5F%5FDesignData%5FSDS2%5FModel%5FPlateSide)implicit operator PlateSide(LockablePlateSide)

Implicit conversion to value type

##### Declaration

```
public static implicit operator PlateSide(LockablePlateSide value)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [LockablePlateSide](DesignData.SDS2.Model.LockablePlateSide.html) | value |             |

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [PlateSide](DesignData.SDS2.Model.PlateSide.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockablePlateSide%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FPlateSide%5F%5FDesignData%5FSDS2%5FModel%5FLockablePlateSide)implicit operator LockablePlateSide(PlateSide)

Implicit conversion using the PlateSide constructor

##### Declaration

```
public static implicit operator LockablePlateSide(PlateSide value)
```

##### Parameters

| Type                                              | Name  | Description |
| ------------------------------------------------- | ----- | ----------- |
| [PlateSide](DesignData.SDS2.Model.PlateSide.html) | value |             |

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [LockablePlateSide](DesignData.SDS2.Model.LockablePlateSide.html) |             |