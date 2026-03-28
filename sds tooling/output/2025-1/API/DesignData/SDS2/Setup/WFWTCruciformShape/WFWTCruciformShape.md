# Class WFWTCruciformShape 

Derived from the CruciformShape class.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

[CruciformShape](DesignData.SDS2.Setup.CruciformShape.html)

WFWTCruciformShape

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
public sealed class WFWTCruciformShape : CruciformShape
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FWFWTCruciformShape%5F%5Fctor)WFWTCruciformShape()

Derived from the CruciformShape class.

##### Declaration

```
public WFWTCruciformShape()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FWFWTCruciformShape%5FFSTeeSectionSize)FSTeeSectionSize

Section size of the W Tee material used for this shape.

##### Declaration

```
public string FSTeeSectionSize { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFWTCruciformShape%5FFSTeeWeldSize)FSTeeWeldSize

Weld size used for FS Tee.

##### Declaration

```
public double FSTeeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFWTCruciformShape%5FFSTeeWeldType)FSTeeWeldType

Weld type used for FS Tee. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType FSTeeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFWTCruciformShape%5FNSTeeSectionSize)NSTeeSectionSize

Section size of the W Tee material used for this shape.

##### Declaration

```
public string NSTeeSectionSize { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFWTCruciformShape%5FNSTeeWeldSize)NSTeeWeldSize

Weld size used for NS Tee.

##### Declaration

```
public double NSTeeWeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFWTCruciformShape%5FNSTeeWeldType)NSTeeWeldType

Weld type used for NS Tee. Uses WeldedShapeWeldType.

##### Declaration

```
public WeldedShapeWeldType NSTeeWeldType { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldedShapeWeldType](DesignData.SDS2.Setup.WeldedShapeWeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FWFWTCruciformShape%5FWideFlangeSectionSize)WideFlangeSectionSize

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

#### [](#DesignData%5FSDS2%5FSetup%5FWFWTCruciformShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

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