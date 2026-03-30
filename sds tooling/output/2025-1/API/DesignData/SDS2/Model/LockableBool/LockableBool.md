# Class LockableBool 

A lockable value holding an boolean

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableBool

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
public sealed class LockableBool : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableBool%5F%5Fctor)LockableBool()

A lockable value holding an boolean

##### Declaration

```
public LockableBool()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableBool%5F%5Fctor%5FSystem%5FBoolean%5F)LockableBool(bool)

Create a locked ViaMemberEdit LockableBool from a bool

##### Declaration

```
public LockableBool(bool value)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableBool%5FValue)Value

The underlying boolean value

##### Declaration

```
public bool Value { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableBool%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A lockable value holding an boolean

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

#### [](#DesignData%5FSDS2%5FModel%5FLockableBool%5Fop%5FAddition%5FDesignData%5FSDS2%5FModel%5FLockableBool%5FSystem%5FBoolean%5F)operator +(LockableBool, bool)

A lockable value holding an boolean

##### Declaration

```
public static LockableBool operator +(LockableBool lhs, bool rhs)
```

##### Parameters

| Type                                                          | Name | Description |
| ------------------------------------------------------------- | ---- | ----------- |
| [LockableBool](DesignData.SDS2.Model.LockableBool.html)       | lhs  |             |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | rhs  |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [LockableBool](DesignData.SDS2.Model.LockableBool.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableBool%5Fop%5FDivision%5FDesignData%5FSDS2%5FModel%5FLockableBool%5FSystem%5FBoolean%5F)operator /(LockableBool, bool)

A lockable value holding an boolean

##### Declaration

```
public static LockableBool operator /(LockableBool lhs, bool rhs)
```

##### Parameters

| Type                                                          | Name | Description |
| ------------------------------------------------------------- | ---- | ----------- |
| [LockableBool](DesignData.SDS2.Model.LockableBool.html)       | lhs  |             |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | rhs  |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [LockableBool](DesignData.SDS2.Model.LockableBool.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableBool%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockableBool%5F%5FSystem%5FBoolean)implicit operator bool(LockableBool)

Implicit conversion to value type

##### Declaration

```
public static implicit operator bool(LockableBool value)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [LockableBool](DesignData.SDS2.Model.LockableBool.html) | value |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableBool%5Fop%5FImplicit%5FSystem%5FBoolean%5F%5FDesignData%5FSDS2%5FModel%5FLockableBool)implicit operator LockableBool(bool)

Implicit conversion using the bool constructor

##### Declaration

```
public static implicit operator LockableBool(bool value)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | value |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [LockableBool](DesignData.SDS2.Model.LockableBool.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableBool%5Fop%5FMultiply%5FDesignData%5FSDS2%5FModel%5FLockableBool%5FSystem%5FBoolean%5F)operator \*(LockableBool, bool)

A lockable value holding an boolean

##### Declaration

```
public static LockableBool operator *(LockableBool lhs, bool rhs)
```

##### Parameters

| Type                                                          | Name | Description |
| ------------------------------------------------------------- | ---- | ----------- |
| [LockableBool](DesignData.SDS2.Model.LockableBool.html)       | lhs  |             |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | rhs  |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [LockableBool](DesignData.SDS2.Model.LockableBool.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableBool%5Fop%5FSubtraction%5FDesignData%5FSDS2%5FModel%5FLockableBool%5FSystem%5FBoolean%5F)operator -(LockableBool, bool)

A lockable value holding an boolean

##### Declaration

```
public static LockableBool operator -(LockableBool lhs, bool rhs)
```

##### Parameters

| Type                                                          | Name | Description |
| ------------------------------------------------------------- | ---- | ----------- |
| [LockableBool](DesignData.SDS2.Model.LockableBool.html)       | lhs  |             |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | rhs  |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [LockableBool](DesignData.SDS2.Model.LockableBool.html) |             |