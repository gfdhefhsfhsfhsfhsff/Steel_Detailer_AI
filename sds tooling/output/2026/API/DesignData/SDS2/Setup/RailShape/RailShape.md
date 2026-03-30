# Class RailShape 

A Shape derived class.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

RailShape

##### Inherited Members

[Shape.GetHashCode()](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FGetHashCode) 

[Shape.Equals(object)](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FEquals%5FSystem%5FObject%5F) 

[Shape.SectionSize](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FSectionSize) 

[Shape.IsAvailable](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FIsAvailable) 

[Shape.SourceReference](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FSourceReference) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class RailShape : Shape
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5F%5Fctor)RailShape()

A Shape derived class.

##### Declaration

```
public RailShape()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FBaseInsideRadius)BaseInsideRadius

The radius of the edge of the lower end of the web

##### Declaration

```
public double BaseInsideRadius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FBaseThicknessAtCenter)BaseThicknessAtCenter

The rail thickness at the center of the rail, technically inside the web of the rail

##### Declaration

```
public double BaseThicknessAtCenter { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FBaseThicknessAtEdge)BaseThicknessAtEdge

The distance from the ground to the tip of the edge of the rail. Roughly the thinnest part of the base.

##### Declaration

```
public double BaseThicknessAtEdge { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FBaseTopRadius)BaseTopRadius

The radius of the edge on the top of the base

##### Declaration

```
public double BaseTopRadius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FBaseWidth)BaseWidth

The width of the base of the rail

##### Declaration

```
public double BaseWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FDepth)Depth

The depth, the distance from the top of the rail to the bottom

##### Declaration

```
public double Depth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FHeadInsideRadius)HeadInsideRadius

The radius of the edge of the upper end of the web

##### Declaration

```
public double HeadInsideRadius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FHeadRadius)HeadRadius

The distance from the center of the base of the head, to the center of the top of the head. This radius applies at multiple points along the top of the head near the center, but not all of it.

##### Declaration

```
public double HeadRadius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FHeadTopRadius)HeadTopRadius

The radius of the edge on the top of the head

##### Declaration

```
public double HeadTopRadius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FHeadWidthBottom)HeadWidthBottom

The width of the rail at the base of the head, or top section

##### Declaration

```
public double HeadWidthBottom { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FHeadWidthTop)HeadWidthTop

The width of the rail at the top of the head, or top section

##### Declaration

```
public double HeadWidthTop { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FWebGage)WebGage

Distance to gage line from the bottom of the rail

##### Declaration

```
public double WebGage { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FWebLength)WebLength

The distance from the top of the base to the bottom of the head

##### Declaration

```
public double WebLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FWebRadius)WebRadius

The radius that describes the curve of the web. This point is the center of the rail on the Y axis, and on the X axis it is aligned with the edge of the base on either side. This distance is from that point to define the curve on that side of the web.

##### Declaration

```
public double WebRadius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FWebThickness)WebThickness

The thickness of the web at its thinnest point

##### Declaration

```
public double WebThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FWeightPerUnitYard)WeightPerUnitYard

The weight for one foot of this rail shape

##### Declaration

```
public double WeightPerUnitYard { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FRailShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A Shape derived class.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[Shape.Dispose(bool)](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FDispose%5FSystem%5FBoolean%5F)