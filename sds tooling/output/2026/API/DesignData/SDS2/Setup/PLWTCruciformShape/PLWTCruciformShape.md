# Class PLWTCruciformShape 

Derived from the CruciformShape class.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

[CruciformShape](DesignData.SDS2.Setup.CruciformShape.html)

PLWTCruciformShape

##### Inherited Members

[CruciformShape.GetStructuralProperties(SteelGrade)](DesignData.SDS2.Setup.CruciformShape.html#DesignData%5FSDS2%5FSetup%5FCruciformShape%5FGetStructuralProperties%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F) 

[CruciformShape.CruciformSubType](DesignData.SDS2.Setup.CruciformShape.html#DesignData%5FSDS2%5FSetup%5FCruciformShape%5FCruciformSubType) 

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
public sealed class PLWTCruciformShape : CruciformShape
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5F%5Fctor)PLWTCruciformShape()

Derived from the CruciformShape class.

##### Declaration

```
public PLWTCruciformShape()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FBtmFlangeGauge)BtmFlangeGauge

Gauge of the Bottom Flange.

##### Declaration

```
public double BtmFlangeGauge { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FBtmFlangeThickness)BtmFlangeThickness

Thickness of the Bottom Flange.

##### Declaration

```
public double BtmFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FBtmFlangeWeldSize)BtmFlangeWeldSize

Weld size of the Bottom Flange.

##### Declaration

```
public double BtmFlangeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FBtmFlangeWeldType)BtmFlangeWeldType

Weld type of the Bottom Flange. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType BtmFlangeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FBtmFlangeWidth)BtmFlangeWidth

Width of the Bottom Flange.

##### Declaration

```
public double BtmFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FDepth)Depth

Main member width + Top flange thickness + Bottom flange thickness.

##### Declaration

```
public double Depth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FFSTeeSectionSize)FSTeeSectionSize

Section size of the W Tee material used in this shape.

##### Declaration

```
public string FSTeeSectionSize { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FFSTeeWeldSize)FSTeeWeldSize

Weld size of the FS Tee.

##### Declaration

```
public double FSTeeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FFSTeeWeldType)FSTeeWeldType

Weld Type of the FS Tee. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType FSTeeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FNSTeeSectionSize)NSTeeSectionSize

Section size of the W Tee material used in this shape.

##### Declaration

```
public string NSTeeSectionSize { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FNSTeeWeldSize)NSTeeWeldSize

Weld size of the NS Tee.

##### Declaration

```
public double NSTeeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FNSTeeWeldType)NSTeeWeldType

Weld type of the NS Tee. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType NSTeeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FTopFlangeGauge)TopFlangeGauge

Gauge of the Top Flange.

##### Declaration

```
public double TopFlangeGauge { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FTopFlangeThickness)TopFlangeThickness

Thickness of the Top Flange.

##### Declaration

```
public double TopFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FTopFlangeWeldSize)TopFlangeWeldSize

Weld size of the Top Flange.

##### Declaration

```
public double TopFlangeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FTopFlangeWeldType)TopFlangeWeldType

Weld type of the Top Flange. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType TopFlangeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FTopFlangeWidth)TopFlangeWidth

Width of the Top Flange.

##### Declaration

```
public double TopFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FWebThickness)WebThickness

Web thickness of the main member material.

##### Declaration

```
public double WebThickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FPLWTCruciformShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Derived from the CruciformShape class.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[CruciformShape.Dispose(bool)](DesignData.SDS2.Setup.CruciformShape.html#DesignData%5FSDS2%5FSetup%5FCruciformShape%5FDispose%5FSystem%5FBoolean%5F)