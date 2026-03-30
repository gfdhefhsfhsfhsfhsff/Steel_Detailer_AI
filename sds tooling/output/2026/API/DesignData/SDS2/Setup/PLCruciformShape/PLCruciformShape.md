# Class PLCruciformShape 

Derived from the CruciformShape class.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

[CruciformShape](DesignData.SDS2.Setup.CruciformShape.html)

PLCruciformShape

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
public sealed class PLCruciformShape : CruciformShape
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5F%5Fctor)PLCruciformShape()

Derived from the CruciformShape class.

##### Declaration

```
public PLCruciformShape()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FBtmFlangeGauge)BtmFlangeGauge

Gauge of the Bottom Flange.

##### Declaration

```
public double BtmFlangeGauge { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FBtmFlangeThickness)BtmFlangeThickness

Thickness of the Bottom Flange.

##### Declaration

```
public double BtmFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FBtmFlangeWeldSize)BtmFlangeWeldSize

Weld size for the Bottom Flange.

##### Declaration

```
public double BtmFlangeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FBtmFlangeWeldType)BtmFlangeWeldType

Weld type of the Bottom Flange. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType BtmFlangeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FBtmFlangeWidth)BtmFlangeWidth

Width of the Bottom Flange.

##### Declaration

```
public double BtmFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FDepth)Depth

Main member width + Top flange thickness + Bottom flange thickness.

##### Declaration

```
public double Depth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FFSTeeDepth)FSTeeDepth

Depth of the FS Tee.

##### Declaration

```
public double FSTeeDepth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FFSTeeFlangeGauge)FSTeeFlangeGauge

Gauge of the FS Tee Flange.

##### Declaration

```
public double FSTeeFlangeGauge { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FFSTeeFlangeThickness)FSTeeFlangeThickness

Thickness of the FS Tee Flange.

##### Declaration

```
public double FSTeeFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FFSTeeFlangeWeldSize)FSTeeFlangeWeldSize

Weld size for the FS Tee Flange.

##### Declaration

```
public double FSTeeFlangeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FFSTeeFlangeWeldType)FSTeeFlangeWeldType

Weld type for the FS Tee Flange. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType FSTeeFlangeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FFSTeeFlangeWidth)FSTeeFlangeWidth

Width of the FS Tee Flange.

##### Declaration

```
public double FSTeeFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FFSTeeWebThickness)FSTeeWebThickness

Web Thickness of the FS Tee.

##### Declaration

```
public double FSTeeWebThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FFSTeeWeldSize)FSTeeWeldSize

Weld size for the FS Tee.

##### Declaration

```
public double FSTeeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FFSTeeWeldType)FSTeeWeldType

Weld Type for the FS Tee. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType FSTeeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FNSTeeDepth)NSTeeDepth

Depth of the NS Tee.

##### Declaration

```
public double NSTeeDepth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FNSTeeFlangeGauge)NSTeeFlangeGauge

Guage of the NS Tee Flange.

##### Declaration

```
public double NSTeeFlangeGauge { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FNSTeeFlangeThickness)NSTeeFlangeThickness

Thickness of the NS Tee Flange.

##### Declaration

```
public double NSTeeFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FNSTeeFlangeWeldSize)NSTeeFlangeWeldSize

Weld size for the NS Tee Flange.

##### Declaration

```
public double NSTeeFlangeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FNSTeeFlangeWeldType)NSTeeFlangeWeldType

Weld type for the NS Tee Flange. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType NSTeeFlangeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FNSTeeFlangeWidth)NSTeeFlangeWidth

Width of the NS Tee Flange.

##### Declaration

```
public double NSTeeFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FNSTeeWebThickness)NSTeeWebThickness

Web thickness of the NS Tee.

##### Declaration

```
public double NSTeeWebThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FNSTeeWeldSize)NSTeeWeldSize

Weld size for NS Tee.

##### Declaration

```
public double NSTeeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FNSTeeWeldType)NSTeeWeldType

Weld type for the NS Tee. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType NSTeeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FTopFlangeGauge)TopFlangeGauge

Gauge of the Top Flange.

##### Declaration

```
public double TopFlangeGauge { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FTopFlangeThickness)TopFlangeThickness

Thickness of the Top Flange.

##### Declaration

```
public double TopFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FTopFlangeWeldSize)TopFlangeWeldSize

Weld size of the Top Flange.

##### Declaration

```
public double TopFlangeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FTopFlangeWeldType)TopFlangeWeldType

Weld type of the Top Flange. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType TopFlangeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FTopFlangeWidth)TopFlangeWidth

Width of the Top Flange.

##### Declaration

```
public double TopFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FWebThickness)WebThickness

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

#### [](#DesignData%5FSDS2%5FSetup%5FPLCruciformShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

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