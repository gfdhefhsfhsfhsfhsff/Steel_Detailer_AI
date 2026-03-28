# Class SeismicCopeShopWeld 

A cope for seismic shop welds.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html)

SeismicCopeShopWeld

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
public sealed class SeismicCopeShopWeld : FlangeCutOperation
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FSeismicCopeShopWeld%5F%5Fctor)SeismicCopeShopWeld()

A cope for seismic shop welds.

##### Declaration

```
public SeismicCopeShopWeld()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FSeismicCopeShopWeld%5FClipWeb)ClipWeb

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

#### [](#DesignData%5FSDS2%5FModel%5FSeismicCopeShopWeld%5FCopeLength)CopeLength

The length of the cope along the work point line

##### Declaration

```
public LockableDouble CopeLength { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FSeismicCopeShopWeld%5FFlangeFlushLength)FlangeFlushLength

Distance from the end of the flange to the beginning of the reentrant cut on the flange.

##### Declaration

```
public LockableDouble FlangeFlushLength { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FSeismicCopeShopWeld%5FGrooveAngle)GrooveAngle

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

#### [](#DesignData%5FSDS2%5FModel%5FSeismicCopeShopWeld%5FReEntrantDepth)ReEntrantDepth

Length of the reentrant cut.

##### Declaration

```
public LockableDouble ReEntrantDepth { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FSeismicCopeShopWeld%5FReEntrantHoleDistance)ReEntrantHoleDistance

Depth of the center of the reentrant cut hole from the inside of the flange.

##### Declaration

```
public LockableDouble ReEntrantHoleDistance { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FSeismicCopeShopWeld%5FReEntrantLength)ReEntrantLength

Depth of the cope from the inside of the flange.

##### Declaration

```
public LockableDouble ReEntrantLength { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FSeismicCopeShopWeld%5FReEntrantRadius)ReEntrantRadius

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

#### [](#DesignData%5FSDS2%5FModel%5FSeismicCopeShopWeld%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A cope for seismic shop welds.

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