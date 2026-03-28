# Class NotchFlange 

Notch the Top/Bottom sides of a hollow section.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html)

NotchFlange

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public sealed class NotchFlange : FlangeCutOperation
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FNotchFlange%5F%5Fctor)NotchFlange()

Notch the Top/Bottom sides of a hollow section.

##### Declaration

```
public NotchFlange()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FNotchFlange%5FLength)Length

Length of the notch.

##### Declaration

```
public LockableDouble Length { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNotchFlange%5FOffset)Offset

Offset from center of the notch.

##### Declaration

```
public LockableDouble Offset { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FNotchFlange%5FRadius)Radius

Radius of the end of the notch. When the radius is 0, the notch is cut square.

##### Declaration

```
public LockableDouble Radius { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FNotchFlange%5FWidth)Width

Width of the notch.

##### Declaration

```
public LockableDouble Width { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FNotchFlange%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Notch the Top/Bottom sides of a hollow section.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[FlangeCutOperation.Dispose(bool)](DesignData.SDS2.Model.FlangeCutOperation.html#DesignData%5FSDS2%5FModel%5FFlangeCutOperation%5FDispose%5FSystem%5FBoolean%5F)