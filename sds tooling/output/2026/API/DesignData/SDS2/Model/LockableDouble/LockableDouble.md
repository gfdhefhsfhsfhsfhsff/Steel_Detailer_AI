# Class LockableDouble 

A lockable value holding a double

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableDouble

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
public sealed class LockableDouble : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableDouble%5F%5Fctor)LockableDouble()

A lockable value holding a double

##### Declaration

```
public LockableDouble()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableDouble%5F%5Fctor%5FSystem%5FDouble%5F)LockableDouble(double)

Create a locked ViaMemberEdit LockableDouble from a double

##### Declaration

```
public LockableDouble(double value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableDouble%5FValue)Value

The underlying floating point value

##### Declaration

```
public double Value { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableDouble%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A lockable value holding a double

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

#### [](#DesignData%5FSDS2%5FModel%5FLockableDouble%5Fop%5FAddition%5FDesignData%5FSDS2%5FModel%5FLockableDouble%5FSystem%5FDouble%5F)operator +(LockableDouble, double)

A lockable value holding a double

##### Declaration

```
public static LockableDouble operator +(LockableDouble lhs, double rhs)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html)    | lhs  |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | rhs  |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDouble%5Fop%5FDivision%5FDesignData%5FSDS2%5FModel%5FLockableDouble%5FSystem%5FDouble%5F)operator /(LockableDouble, double)

A lockable value holding a double

##### Declaration

```
public static LockableDouble operator /(LockableDouble lhs, double rhs)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html)    | lhs  |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | rhs  |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDouble%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockableDouble%5F%5FSystem%5FDouble)implicit operator double(LockableDouble)

Implicit conversion to value type

##### Declaration

```
public static implicit operator double(LockableDouble value)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) | value |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDouble%5Fop%5FImplicit%5FSystem%5FDouble%5F%5FDesignData%5FSDS2%5FModel%5FLockableDouble)implicit operator LockableDouble(double)

Implicit conversion using the double constructor

##### Declaration

```
public static implicit operator LockableDouble(double value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDouble%5Fop%5FMultiply%5FDesignData%5FSDS2%5FModel%5FLockableDouble%5FSystem%5FDouble%5F)operator \*(LockableDouble, double)

A lockable value holding a double

##### Declaration

```
public static LockableDouble operator *(LockableDouble lhs, double rhs)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html)    | lhs  |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | rhs  |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDouble%5Fop%5FSubtraction%5FDesignData%5FSDS2%5FModel%5FLockableDouble%5FSystem%5FDouble%5F)operator -(LockableDouble, double)

A lockable value holding a double

##### Declaration

```
public static LockableDouble operator -(LockableDouble lhs, double rhs)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html)    | lhs  |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | rhs  |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |