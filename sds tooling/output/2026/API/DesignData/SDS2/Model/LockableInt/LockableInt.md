# Class LockableInt 

A lockable value holding an integer

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableInt

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
public sealed class LockableInt : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableInt%5F%5Fctor)LockableInt()

A lockable value holding an integer

##### Declaration

```
public LockableInt()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableInt%5F%5Fctor%5FSystem%5FInt32%5F)LockableInt(int)

Create a locked ViaMemberEdit LockableInt from a int

##### Declaration

```
public LockableInt(int value)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableInt%5FValue)Value

The underlying integer value

##### Declaration

```
public int Value { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableInt%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A lockable value holding an integer

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

#### [](#DesignData%5FSDS2%5FModel%5FLockableInt%5Fop%5FAddition%5FDesignData%5FSDS2%5FModel%5FLockableInt%5FSystem%5FInt32%5F)operator +(LockableInt, int)

A lockable value holding an integer

##### Declaration

```
public static LockableInt operator +(LockableInt lhs, int rhs)
```

##### Parameters

| Type                                                       | Name | Description |
| ---------------------------------------------------------- | ---- | ----------- |
| [LockableInt](DesignData.SDS2.Model.LockableInt.html)      | lhs  |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | rhs  |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [LockableInt](DesignData.SDS2.Model.LockableInt.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableInt%5Fop%5FDivision%5FDesignData%5FSDS2%5FModel%5FLockableInt%5FSystem%5FInt32%5F)operator /(LockableInt, int)

A lockable value holding an integer

##### Declaration

```
public static LockableInt operator /(LockableInt lhs, int rhs)
```

##### Parameters

| Type                                                       | Name | Description |
| ---------------------------------------------------------- | ---- | ----------- |
| [LockableInt](DesignData.SDS2.Model.LockableInt.html)      | lhs  |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | rhs  |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [LockableInt](DesignData.SDS2.Model.LockableInt.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableInt%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockableInt%5F%5FSystem%5FInt32)implicit operator int(LockableInt)

Implicit conversion to value type

##### Declaration

```
public static implicit operator int(LockableInt value)
```

##### Parameters

| Type                                                  | Name  | Description |
| ----------------------------------------------------- | ----- | ----------- |
| [LockableInt](DesignData.SDS2.Model.LockableInt.html) | value |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableInt%5Fop%5FImplicit%5FSystem%5FInt32%5F%5FDesignData%5FSDS2%5FModel%5FLockableInt)implicit operator LockableInt(int)

Implicit conversion using the int constructor

##### Declaration

```
public static implicit operator LockableInt(int value)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | value |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [LockableInt](DesignData.SDS2.Model.LockableInt.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableInt%5Fop%5FMultiply%5FDesignData%5FSDS2%5FModel%5FLockableInt%5FSystem%5FInt32%5F)operator \*(LockableInt, int)

A lockable value holding an integer

##### Declaration

```
public static LockableInt operator *(LockableInt lhs, int rhs)
```

##### Parameters

| Type                                                       | Name | Description |
| ---------------------------------------------------------- | ---- | ----------- |
| [LockableInt](DesignData.SDS2.Model.LockableInt.html)      | lhs  |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | rhs  |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [LockableInt](DesignData.SDS2.Model.LockableInt.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableInt%5Fop%5FSubtraction%5FDesignData%5FSDS2%5FModel%5FLockableInt%5FSystem%5FInt32%5F)operator -(LockableInt, int)

A lockable value holding an integer

##### Declaration

```
public static LockableInt operator -(LockableInt lhs, int rhs)
```

##### Parameters

| Type                                                       | Name | Description |
| ---------------------------------------------------------- | ---- | ----------- |
| [LockableInt](DesignData.SDS2.Model.LockableInt.html)      | lhs  |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | rhs  |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [LockableInt](DesignData.SDS2.Model.LockableInt.html) |             |