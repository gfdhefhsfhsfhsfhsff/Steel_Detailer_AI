# Class LockableCutLocation 

Lockable value for CutLocation

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableCutLocation

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
public sealed class LockableCutLocation : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutLocation%5F%5Fctor)LockableCutLocation()

Lockable value for CutLocation

##### Declaration

```
public LockableCutLocation()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutLocation%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FCutLocation%5F)LockableCutLocation(CutLocation)

Create a locked ViaMemberEdit LockableCutLocation from a CutLocation

##### Declaration

```
public LockableCutLocation(CutLocation value)
```

##### Parameters

| Type                                                  | Name  | Description |
| ----------------------------------------------------- | ----- | ----------- |
| [CutLocation](DesignData.SDS2.Model.CutLocation.html) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutLocation%5FValue)Value

The underlying value

##### Declaration

```
public CutLocation Value { get; set; }
```

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [CutLocation](DesignData.SDS2.Model.CutLocation.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutLocation%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Lockable value for CutLocation

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

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutLocation%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FCutLocation%5F%5FDesignData%5FSDS2%5FModel%5FLockableCutLocation)implicit operator LockableCutLocation(CutLocation)

Implicit conversion using the CutLocation constructor

##### Declaration

```
public static implicit operator LockableCutLocation(CutLocation value)
```

##### Parameters

| Type                                                  | Name  | Description |
| ----------------------------------------------------- | ----- | ----------- |
| [CutLocation](DesignData.SDS2.Model.CutLocation.html) | value |             |

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [LockableCutLocation](DesignData.SDS2.Model.LockableCutLocation.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutLocation%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockableCutLocation%5F%5FDesignData%5FSDS2%5FModel%5FCutLocation)implicit operator CutLocation(LockableCutLocation)

Implicit conversion to value type

##### Declaration

```
public static implicit operator CutLocation(LockableCutLocation value)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [LockableCutLocation](DesignData.SDS2.Model.LockableCutLocation.html) | value |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [CutLocation](DesignData.SDS2.Model.CutLocation.html) |             |