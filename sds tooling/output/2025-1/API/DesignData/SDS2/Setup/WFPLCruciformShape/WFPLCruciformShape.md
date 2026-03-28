# Class WFPLCruciformShape 

Derived from the CruciformShape class.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

[CruciformShape](DesignData.SDS2.Setup.CruciformShape.html)

WFPLCruciformShape

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
public sealed class WFPLCruciformShape : CruciformShape
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5F%5Fctor)WFPLCruciformShape()

Derived from the CruciformShape class.

##### Declaration

```
public WFPLCruciformShape()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FFSTeeDepth)FSTeeDepth

Depth of the FS Tee.

##### Declaration

```
public double FSTeeDepth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FFSTeeFlangeGauge)FSTeeFlangeGauge

Flange gauge of the FS Tee.

##### Declaration

```
public double FSTeeFlangeGauge { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FFSTeeFlangeThickness)FSTeeFlangeThickness

Flange thickness of the FS Tee.

##### Declaration

```
public double FSTeeFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FFSTeeFlangeWeldSize)FSTeeFlangeWeldSize

Weld size of the FS Tee Flange.

##### Declaration

```
public double FSTeeFlangeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FFSTeeFlangeWeldType)FSTeeFlangeWeldType

Weld type of the FS Tee Flange. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType FSTeeFlangeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FFSTeeFlangeWidth)FSTeeFlangeWidth

Flange width of the FS Tee.

##### Declaration

```
public double FSTeeFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FFSTeeWebThickness)FSTeeWebThickness

Web thickness of the FS Tee.

##### Declaration

```
public double FSTeeWebThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FFSTeeWeldSize)FSTeeWeldSize

Weld size of the FS Tee.

##### Declaration

```
public double FSTeeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FFSTeeWeldType)FSTeeWeldType

Weld type of the FS Tee. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType FSTeeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FNSTeeDepth)NSTeeDepth

Depth of the NS Tee.

##### Declaration

```
public double NSTeeDepth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FNSTeeFlangeGauge)NSTeeFlangeGauge

Flange gauge of the NS Tee.

##### Declaration

```
public double NSTeeFlangeGauge { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FNSTeeFlangeThickness)NSTeeFlangeThickness

Flange thickness of the NS Tee.

##### Declaration

```
public double NSTeeFlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FNSTeeFlangeWeldSize)NSTeeFlangeWeldSize

Weld size of the NSTee Flange.

##### Declaration

```
public double NSTeeFlangeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FNSTeeFlangeWeldType)NSTeeFlangeWeldType

Weld type of the NS Tee Flange. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType NSTeeFlangeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FNSTeeFlangeWidth)NSTeeFlangeWidth

Flange width of the NS Tee.

##### Declaration

```
public double NSTeeFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FNSTeeWebThickness)NSTeeWebThickness

Web thickness of the NS Tee.

##### Declaration

```
public double NSTeeWebThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FNSTeeWeldSize)NSTeeWeldSize

Weld size of the NS Tee.

##### Declaration

```
public double NSTeeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FNSTeeWeldType)NSTeeWeldType

Weld type of the NS Tee. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType NSTeeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FWideFlangeSectionSize)WideFlangeSectionSize

Section size of the Wide Flange material used for this shape.

##### Declaration

```
public string WideFlangeSectionSize { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FWFPLCruciformShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

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