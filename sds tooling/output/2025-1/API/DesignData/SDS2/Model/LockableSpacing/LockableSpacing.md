# Class LockableSpacing 

Variable spacings describe the spacings between a row of bolts, possibly varying between each bolt

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableSpacing

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
public sealed class LockableSpacing : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5F%5Fctor)LockableSpacing()

Create a variable spacing with no spacings set

##### Declaration

```
public LockableSpacing()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FAssumedRows)AssumedRows

The number of rows of bolts described by this set of spacings

##### Declaration

```
public int AssumedRows { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FCount)Count

Get count of spacings

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FFirst)First

The first spacing

##### Declaration

```
public double First { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FIsVariable)IsVariable

True is the spacing list is variable, not uniform

##### Declaration

```
public bool IsVariable { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FItem%5FSystem%5FInt32%5F)this\[int\]

Get the nth spacing

##### Declaration

```
public double this[int index] { get; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FLast)Last

The last spacing

##### Declaration

```
public double Last { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FMax)Max

The largest spacing

##### Declaration

```
public double Max { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FMin)Min

The smallest spacing

##### Declaration

```
public double Min { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Variable spacings describe the spacings between a row of bolts, possibly varying between each bolt

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

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FFromString%5FSystem%5FString%5F)FromString(string)

Parse spacings from a user input string

##### Declaration

```
public void FromString(string value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | value |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FGetEnumerator)GetEnumerator()

Get the enumerator object

##### Declaration

```
public IEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                 | Description |
| ------------------------------------------------------------------------------------ | ----------- |
| [IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FGetIsVariable)GetIsVariable()

True is the spacing list is variable, not uniform

##### Declaration

```
public bool GetIsVariable()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5FSetAll%5FSystem%5FDouble%5F)SetAll(double)

Set all spacings to this same value, keep the same number of rows of bolts

##### Declaration

```
public void SetAll(double value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value |             |

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5Fop%5FAddition%5FDesignData%5FSDS2%5FModel%5FLockableSpacing%5FSystem%5FDouble%5F)operator +(LockableSpacing, double)

Variable spacings describe the spacings between a row of bolts, possibly varying between each bolt

##### Declaration

```
public static LockableSpacing operator +(LockableSpacing lhs, double rhs)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [LockableSpacing](DesignData.SDS2.Model.LockableSpacing.html)  | lhs  |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | rhs  |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [LockableSpacing](DesignData.SDS2.Model.LockableSpacing.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5Fop%5FDivision%5FDesignData%5FSDS2%5FModel%5FLockableSpacing%5FSystem%5FDouble%5F)operator /(LockableSpacing, double)

Variable spacings describe the spacings between a row of bolts, possibly varying between each bolt

##### Declaration

```
public static LockableSpacing operator /(LockableSpacing lhs, double rhs)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [LockableSpacing](DesignData.SDS2.Model.LockableSpacing.html)  | lhs  |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | rhs  |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [LockableSpacing](DesignData.SDS2.Model.LockableSpacing.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5Fop%5FMultiply%5FDesignData%5FSDS2%5FModel%5FLockableSpacing%5FSystem%5FDouble%5F)operator \*(LockableSpacing, double)

Variable spacings describe the spacings between a row of bolts, possibly varying between each bolt

##### Declaration

```
public static LockableSpacing operator *(LockableSpacing lhs, double rhs)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [LockableSpacing](DesignData.SDS2.Model.LockableSpacing.html)  | lhs  |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | rhs  |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [LockableSpacing](DesignData.SDS2.Model.LockableSpacing.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableSpacing%5Fop%5FSubtraction%5FDesignData%5FSDS2%5FModel%5FLockableSpacing%5FSystem%5FDouble%5F)operator -(LockableSpacing, double)

Variable spacings describe the spacings between a row of bolts, possibly varying between each bolt

##### Declaration

```
public static LockableSpacing operator -(LockableSpacing lhs, double rhs)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [LockableSpacing](DesignData.SDS2.Model.LockableSpacing.html)  | lhs  |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | rhs  |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [LockableSpacing](DesignData.SDS2.Model.LockableSpacing.html) |             |