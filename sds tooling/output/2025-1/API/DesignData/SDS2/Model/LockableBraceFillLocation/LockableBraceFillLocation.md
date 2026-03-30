# Class LockableBraceFillLocation 

A lockable value for BraceFillLocation

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableBraceFillLocation

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
public sealed class LockableBraceFillLocation : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableBraceFillLocation%5F%5Fctor)LockableBraceFillLocation()

A lockable value for BraceFillLocation

##### Declaration

```
public LockableBraceFillLocation()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableBraceFillLocation%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FBraceFillLocation%5F)LockableBraceFillLocation(BraceFillLocation)

Create a locked ViaMemberEdit LockableBraceFillLocation from a BraceFillLocation

##### Declaration

```
public LockableBraceFillLocation(BraceFillLocation value)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [BraceFillLocation](DesignData.SDS2.Model.BraceFillLocation.html) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableBraceFillLocation%5FValue)Value

The underlying value

##### Declaration

```
public BraceFillLocation Value { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [BraceFillLocation](DesignData.SDS2.Model.BraceFillLocation.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableBraceFillLocation%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A lockable value for BraceFillLocation

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

#### [](#DesignData%5FSDS2%5FModel%5FLockableBraceFillLocation%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FBraceFillLocation%5F%5FDesignData%5FSDS2%5FModel%5FLockableBraceFillLocation)implicit operator LockableBraceFillLocation(BraceFillLocation)

Implicit conversion using the BraceFillLocation constructor

##### Declaration

```
public static implicit operator LockableBraceFillLocation(BraceFillLocation value)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [BraceFillLocation](DesignData.SDS2.Model.BraceFillLocation.html) | value |             |

##### Returns

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [LockableBraceFillLocation](DesignData.SDS2.Model.LockableBraceFillLocation.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableBraceFillLocation%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockableBraceFillLocation%5F%5FDesignData%5FSDS2%5FModel%5FBraceFillLocation)implicit operator BraceFillLocation(LockableBraceFillLocation)

Implicit conversion to value type

##### Declaration

```
public static implicit operator BraceFillLocation(LockableBraceFillLocation value)
```

##### Parameters

| Type                                                                              | Name  | Description |
| --------------------------------------------------------------------------------- | ----- | ----------- |
| [LockableBraceFillLocation](DesignData.SDS2.Model.LockableBraceFillLocation.html) | value |             |

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [BraceFillLocation](DesignData.SDS2.Model.BraceFillLocation.html) |             |