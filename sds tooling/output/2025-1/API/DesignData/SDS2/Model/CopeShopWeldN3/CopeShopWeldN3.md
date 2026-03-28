# Class CopeShopWeldN3 

Designates weld preparation and/or a cut to remove part of the top/bottom flange plus part of the web.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html)

CopeShopWeldN3

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
public sealed class CopeShopWeldN3 : FlangeCutOperation
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FCopeShopWeldN3%5F%5Fctor)CopeShopWeldN3()

Designates weld preparation and/or a cut to remove part of the top/bottom flange plus part of the web.

##### Declaration

```
public CopeShopWeldN3()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FCopeShopWeldN3%5FClipWeb)ClipWeb

How many inches to clip back the web at the edge of the cope.

##### Declaration

```
public LockableDouble ClipWeb { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FCopeShopWeldN3%5FDepth)Depth

The depth of the cope from the flange, perpindicular to the length

##### Declaration

```
public LockableDouble Depth { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FCopeShopWeldN3%5FGrooveAngle)GrooveAngle

Angle of the bevel on the flange.

##### Declaration

```
public LockableDouble GrooveAngle { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

Beware this returns degrees or radians based on the underlying type. Types that are built into SDS2 binary return radians. Most types implemented in Python such as embed return degrees. A future API that always returns radians is forecasted.

#### [](#DesignData%5FSDS2%5FModel%5FCopeShopWeldN3%5FLength)Length

The length of the cope along the work point line

##### Declaration

```
public LockableDouble Length { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FCopeShopWeldN3%5FReEntrantRadius)ReEntrantRadius

The radius of the corner of the cope

##### Declaration

```
public LockableDouble ReEntrantRadius { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FCopeShopWeldN3%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Designates weld preparation and/or a cut to remove part of the top/bottom flange plus part of the web.

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