# Class LockableShearWeldType 

Lockable value for ShearWeldType

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableShearWeldType

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
public sealed class LockableShearWeldType : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableShearWeldType%5F%5Fctor)LockableShearWeldType()

Lockable value for ShearWeldType

##### Declaration

```
public LockableShearWeldType()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableShearWeldType%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FShearWeldType%5F)LockableShearWeldType(ShearWeldType)

Create a locked ViaMemberEdit LockableShearWeldType from a ShearWeldType

##### Declaration

```
public LockableShearWeldType(ShearWeldType value)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [ShearWeldType](DesignData.SDS2.Model.ShearWeldType.html) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableShearWeldType%5FValue)Value

The underlying value

##### Declaration

```
public ShearWeldType Value { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ShearWeldType](DesignData.SDS2.Model.ShearWeldType.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableShearWeldType%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Lockable value for ShearWeldType

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

#### [](#DesignData%5FSDS2%5FModel%5FLockableShearWeldType%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockableShearWeldType%5F%5FDesignData%5FSDS2%5FModel%5FShearWeldType)implicit operator ShearWeldType(LockableShearWeldType)

Implicit conversion to value type

##### Declaration

```
public static implicit operator ShearWeldType(LockableShearWeldType value)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [LockableShearWeldType](DesignData.SDS2.Model.LockableShearWeldType.html) | value |             |

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ShearWeldType](DesignData.SDS2.Model.ShearWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableShearWeldType%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FShearWeldType%5F%5FDesignData%5FSDS2%5FModel%5FLockableShearWeldType)implicit operator LockableShearWeldType(ShearWeldType)

Implicit conversion using the ShearWeldType constructor

##### Declaration

```
public static implicit operator LockableShearWeldType(ShearWeldType value)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [ShearWeldType](DesignData.SDS2.Model.ShearWeldType.html) | value |             |

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [LockableShearWeldType](DesignData.SDS2.Model.LockableShearWeldType.html) |             |