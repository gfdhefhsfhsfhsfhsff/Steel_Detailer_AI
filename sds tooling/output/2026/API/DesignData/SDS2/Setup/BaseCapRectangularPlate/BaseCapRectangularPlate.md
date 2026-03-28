# Class BaseCapRectangularPlate 

A rectangular base/cap plate

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html)

BaseCapRectangularPlate

##### Inherited Members

[BaseCapPlate.GetHashCode()](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FGetHashCode) 

[BaseCapPlate.Equals(object)](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FEquals%5FSystem%5FObject%5F) 

[BaseCapPlate.Piecemark](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FPiecemark) 

[BaseCapPlate.Thickness](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FThickness) 

[BaseCapPlate.BoltDiameter](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FBoltDiameter) 

[BaseCapPlate.HoleDiameter](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FHoleDiameter) 

[BaseCapPlate.HoleType](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FHoleType) 

[BaseCapPlate.Grade](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FGrade) 

[BaseCapPlate.AdditionalHoles](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FAdditionalHoles) 

[BaseCapPlate.VentDrainPattern](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FVentDrainPattern) 

[BaseCapPlate.WeldsAsBasePlate](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FWeldsAsBasePlate) 

[BaseCapPlate.WeldsAsCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FWeldsAsCapPlate) 

[BaseCapPlate.ColumnWeldPrep](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FColumnWeldPrep) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class BaseCapRectangularPlate : BaseCapPlate
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FBottomLeft)BottomLeft

Leg holes for the bottom leg

##### Declaration

```
public BaseCapPlateLeg BottomLeft { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [BaseCapPlateLeg](DesignData.SDS2.Setup.BaseCapPlateLeg.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FCenterHoleColumns)CenterHoleColumns

Number of columns of holes

##### Declaration

```
public uint CenterHoleColumns { get; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FCenterHoleRows)CenterHoleRows

Number of rows of holes

##### Declaration

```
public uint CenterHoleRows { get; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FHoleSpacingX)HoleSpacingX

Space between the center holes in the X direction, horizontal spacing, column spacing.

##### Declaration

```
public double HoleSpacingX { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FHoleSpacingY)HoleSpacingY

Space between the center holes in the Y direction, vertical spacing, row spacing.

##### Declaration

```
public double HoleSpacingY { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FLeftLeg)LeftLeg

Leg holes for the left side leg

##### Declaration

```
public BaseCapPlateLeg LeftLeg { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [BaseCapPlateLeg](DesignData.SDS2.Setup.BaseCapPlateLeg.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FLength)Length

The length of the base cap plate

##### Declaration

```
public double Length { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FRightLeft)RightLeft

Leg holes for the right side leg

##### Declaration

```
public BaseCapPlateLeg RightLeft { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [BaseCapPlateLeg](DesignData.SDS2.Setup.BaseCapPlateLeg.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FTopLeft)TopLeft

Leg holes for the top leg

##### Declaration

```
public BaseCapPlateLeg TopLeft { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [BaseCapPlateLeg](DesignData.SDS2.Setup.BaseCapPlateLeg.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FWidth)Width

The width of the base cap plate

##### Declaration

```
public double Width { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRectangularPlate%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A rectangular base/cap plate

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[BaseCapPlate.Dispose(bool)](DesignData.SDS2.Setup.BaseCapPlate.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FDispose%5FSystem%5FBoolean%5F)