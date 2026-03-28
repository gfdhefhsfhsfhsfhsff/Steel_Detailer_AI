# Class ColdFormedChannelShape 

Cold formed channel shape

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

[RolledShape](DesignData.SDS2.Setup.RolledShape.html)

[ColdFormedShape](DesignData.SDS2.Setup.ColdFormedShape.html)

ColdFormedChannelShape

##### Inherited Members

[ColdFormedShape.GetWebBends()](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FGetWebBends) 

[ColdFormedShape.GetTopFlangeBends()](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FGetTopFlangeBends) 

[ColdFormedShape.GetBottomFlangeBends()](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FGetBottomFlangeBends) 

[ColdFormedShape.Thickness](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FThickness) 

[ColdFormedShape.Radius](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FRadius) 

[ColdFormedShape.WebGage1](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FWebGage1) 

[ColdFormedShape.WebGage2](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FWebGage2) 

[ColdFormedShape.WebGage3](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FWebGage3) 

[ColdFormedShape.BottomFlangeWidth](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FBottomFlangeWidth) 

[ColdFormedShape.BottomLipLength](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FBottomLipLength) 

[ColdFormedShape.BottomLipReturnAngle](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FBottomLipReturnAngle) 

[ColdFormedShape.BottomLipReturnLength](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FBottomLipReturnLength) 

[ColdFormedShape.TopFlangeWidth](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FTopFlangeWidth) 

[ColdFormedShape.TopLipLength](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FTopLipLength) 

[ColdFormedShape.TopLipReturnAngle](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FTopLipReturnAngle) 

[ColdFormedShape.TopLipReturnLength](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FTopLipReturnLength) 

[RolledShape.Depth](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FDepth) 

[RolledShape.NominalDepth](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FNominalDepth) 

[RolledShape.WeightPerUnitFoot](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FWeightPerUnitFoot) 

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
public sealed class ColdFormedChannelShape : ColdFormedShape
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5F%5Fctor)ColdFormedChannelShape()

Cold formed channel shape

##### Declaration

```
public ColdFormedChannelShape()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5FBottomFlangeAngle)BottomFlangeAngle

The angle in the range (radians equivalent of -80 degrees, radian equivalent of 80 degrees) between the web and bottom flange. Perpendicular is specified as 0.0 radians. An angle between (0.0, pi/2.0) forms an acute relationship and (-pi/2.0, 0.0) is obtuse.

##### Declaration

```
public double BottomFlangeAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5FBottomFlangeGage1)BottomFlangeGage1

The distance in inches from the backside of the web to the first gage line of the bottom flange.

##### Declaration

```
public double BottomFlangeGage1 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5FBottomFlangeGage2)BottomFlangeGage2

The distance in inches from the first bottom flange gage line to the second gage line of the bottom flange.

##### Declaration

```
public double BottomFlangeGage2 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5FBottomLipAngle)BottomLipAngle

The angle in the range (-pi/2.0, pi/2.0) between the bottom flange and its lip. Perpendicular is specified as 0.0 radians. A positive angle forms an acute relationship. A negative angle forms an obtuse relationship.

##### Declaration

```
public double BottomLipAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5FTopFlangeAngle)TopFlangeAngle

The angle in the range (radians equivalent of -80 degrees, radian equivalent of 80 degrees) between the web and top flange. Perpendicular is specified as 0.0 radians. An angle between (0.0, pi/2.0) forms an obtuse relationship and (-pi/2.0, 0.0) is acute.

##### Declaration

```
public double TopFlangeAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5FTopFlangeGage1)TopFlangeGage1

The distance in inches from the backside of the web to the first gage line of the top flange.

##### Declaration

```
public double TopFlangeGage1 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5FTopFlangeGage2)TopFlangeGage2

The distance in inches from the first top flange gage line to the second gage line of the top flange.

##### Declaration

```
public double TopFlangeGage2 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5FTopLipAngle)TopLipAngle

The angle in the range (-pi/2.0, pi/2.0) between the bottom flange and its lip. Perpendicular is specified as 0.0 radians. A positive angle forms an acute relationship. A negative angle forms an obtuse relationship.

##### Declaration

```
public double TopLipAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Cold formed channel shape

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[ColdFormedShape.Dispose(bool)](DesignData.SDS2.Setup.ColdFormedShape.html#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedChannelShape%5FGetStructuralProperties%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F)GetStructuralProperties(SteelGrade)

Get the structural properties, from the production standard, for a specific grade. To get the default standard pass null for the grade

##### Declaration

```
public ChannelTeeStructuralProperties GetStructuralProperties(SteelGrade forGrade)
```

##### Parameters

| Type                                                | Name     | Description                                                                                                                                                                                                                      |
| --------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | forGrade | Production standards are under grade names for many types, so passing in the grade lets us lookup StructuralProperties for a specific production standard for this grade. There is also always a default, pass null to get this. |

##### Returns

| Type                                                                                        | Description |
| ------------------------------------------------------------------------------------------- | ----------- |
| [ChannelTeeStructuralProperties](DesignData.SDS2.Setup.ChannelTeeStructuralProperties.html) |             |