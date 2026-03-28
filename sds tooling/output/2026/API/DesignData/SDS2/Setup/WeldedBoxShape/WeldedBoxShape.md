# Class WeldedBoxShape 

A Shape derived class.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

WeldedBoxShape

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
public sealed class WeldedBoxShape : Shape
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5F%5Fctor)WeldedBoxShape()

A Shape derived class.

##### Declaration

```
public WeldedBoxShape()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FBtmFlangeThickness)BtmFlangeThickness

Thickness of the bottom flange

##### Declaration

```
public double BtmFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FBtmFlangeWeldSize)BtmFlangeWeldSize

Weld size on the bottom flange.

##### Declaration

```
public double BtmFlangeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FBtmFlangeWeldType)BtmFlangeWeldType

Weld type on the bottom flange.

##### Declaration

```
public WeldedShapeWeldType BtmFlangeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FBtmFlangeWidth)BtmFlangeWidth

Width of the bottom flange

##### Declaration

```
public double BtmFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FDepth)Depth

Depth of the shape.

##### Declaration

```
public double Depth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FOutToOut)OutToOut

Distance from the near side of the near web plate to the far side of the far web plate.

##### Declaration

```
public double OutToOut { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FTopFlangeThickness)TopFlangeThickness

Thickness of the top flange

##### Declaration

```
public double TopFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FTopFlangeWeldSize)TopFlangeWeldSize

Weld size on the top flange.

##### Declaration

```
public double TopFlangeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FTopFlangeWeldType)TopFlangeWeldType

Weld type on the top flange.

##### Declaration

```
public WeldedShapeWeldType TopFlangeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FTopFlangeWidth)TopFlangeWidth

Width of the top flange

##### Declaration

```
public double TopFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FWebThickness)WebThickness

Thickness of the web

##### Declaration

```
public double WebThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FWeightPerUnitFoot)WeightPerUnitFoot

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

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

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

#### [](#DesignData%5FSDS2%5FSetup%5FWeldedBoxShape%5FGetStructuralProperties%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F)GetStructuralProperties(SteelGrade)

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