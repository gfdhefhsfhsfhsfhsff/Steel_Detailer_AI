# Class WeldedWideFlangeShape 

A Shape derived class.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

WeldedWideFlangeShape

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
public sealed class WeldedWideFlangeShape : Shape
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5F%5Fctor)WeldedWideFlangeShape()

A Shape derived class.

##### Declaration

```
public WeldedWideFlangeShape()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FBtmFlangeFarSideWeldSize)BtmFlangeFarSideWeldSize

Weld size on the bottom flange at the far side of the web.

##### Declaration

```
public double BtmFlangeFarSideWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FBtmFlangeFarSideWeldType)BtmFlangeFarSideWeldType

Weld type on the bottom flange at the far side of the web.

##### Declaration

```
public WeldedShapeWeldType BtmFlangeFarSideWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FBtmFlangeGage)BtmFlangeGage

Distance between the gage lines of the bottom flange. Half of this value would be the distance from the center of the web to either gage line.

##### Declaration

```
public double BtmFlangeGage { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FBtmFlangeNearSideWeldSize)BtmFlangeNearSideWeldSize

Weld size on the bottom flange at the near side of the web.

##### Declaration

```
public double BtmFlangeNearSideWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FBtmFlangeNearSideWeldType)BtmFlangeNearSideWeldType

Weld type on the bottom flange at the near side of the web.

##### Declaration

```
public WeldedShapeWeldType BtmFlangeNearSideWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FBtmFlangeThickness)BtmFlangeThickness

Thickness of the bottom flange

##### Declaration

```
public double BtmFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FBtmFlangeWidth)BtmFlangeWidth

Width of the bottom flange

##### Declaration

```
public double BtmFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FDepth)Depth

Depth of the shape.

##### Declaration

```
public double Depth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FNominalDepth)NominalDepth

The rounded depth value used in the typical section size string

##### Declaration

```
public double NominalDepth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FTopFlangeFarSideWeldSize)TopFlangeFarSideWeldSize

Weld size on the top flange at the far side of the web.

##### Declaration

```
public double TopFlangeFarSideWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FTopFlangeFarSideWeldType)TopFlangeFarSideWeldType

Weld type on the top flange at the far side of the web.

##### Declaration

```
public WeldedShapeWeldType TopFlangeFarSideWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FTopFlangeGage)TopFlangeGage

Distance between the gage lines of the top flange. Half of this value would be the distance from the center of the web to either gage line.

##### Declaration

```
public double TopFlangeGage { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FTopFlangeNearSideWeldSize)TopFlangeNearSideWeldSize

Weld size on the top flange at the near side of the web.

##### Declaration

```
public double TopFlangeNearSideWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FTopFlangeNearSideWeldType)TopFlangeNearSideWeldType

Weld type on the top flange at the near side of the web.

##### Declaration

```
public WeldedShapeWeldType TopFlangeNearSideWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FTopFlangeThickness)TopFlangeThickness

Thickness of the top flange

##### Declaration

```
public double TopFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FTopFlangeWidth)TopFlangeWidth

Width of the top flange

##### Declaration

```
public double TopFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FWebThickness)WebThickness

Thickness of the web

##### Declaration

```
public double WebThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FWeightPerUnitFoot)WeightPerUnitFoot

For extruded profile shapes, this is the weight for each foot of the shape. This will be 0.0 for some shapes where it does not apply.

##### Declaration

```
public double WeightPerUnitFoot { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

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

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedWideFlangeShape%5FGetStructuralProperties%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F)GetStructuralProperties(SteelGrade)

Get the structural properties, from the production standard, for a specific grade. To get the default standard pass null for the grade

##### Declaration

```
public CommonStructuralProperties GetStructuralProperties(SteelGrade forGrade)
```

##### Parameters

| Type                                                | Name     | Description                                                                                                                                                                                                                      |
| --------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | forGrade | Production standards are under grade names for many types, so passing in the grade lets us lookup StructuralProperties for a specific production standard for this grade. There is also always a default, pass null to get this. |

##### Returns

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [CommonStructuralProperties](DesignData.SDS2.Setup.CommonStructuralProperties.html) |             |