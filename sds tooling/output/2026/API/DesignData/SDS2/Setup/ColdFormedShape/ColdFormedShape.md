# Class ColdFormedShape 

An abstract class for cold formed shapes.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

[RolledShape](DesignData.SDS2.Setup.RolledShape.html)

ColdFormedShape

[ColdFormedChannelShape](DesignData.SDS2.Setup.ColdFormedChannelShape.html)

[ColdFormedZShape](DesignData.SDS2.Setup.ColdFormedZShape.html)

##### Inherited Members

[RolledShape.Depth](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FDepth) 

[RolledShape.NominalDepth](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FNominalDepth) 

[RolledShape.WeightPerUnitFoot](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FWeightPerUnitFoot) 

[Shape.GetHashCode()](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FGetHashCode) 

[Shape.Equals(object)](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FEquals%5FSystem%5FObject%5F) 

[Shape.SectionSize](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FSectionSize) 

[Shape.IsAvailable](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FIsAvailable) 

[Shape.SourceReference](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FSourceReference) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class ColdFormedShape : RolledShape
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FBottomFlangeWidth)BottomFlangeWidth

The distance in inches from the backside of the web -- update 'backside'??? to the farthest edge of the bottom flange.

##### Declaration

```
public double BottomFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FBottomLipLength)BottomLipLength

The length in inches of the bottom flange lip, where 0.0 represents no lip.

##### Declaration

```
public double BottomLipLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FBottomLipReturnAngle)BottomLipReturnAngle

An angle in the range (0.0, pi) between the bottom flange lip and its return material. Perpendicular is specified as pi/2.0 radians. An angle between (0.0, pi/2.0) forms an obtuse relationship and (pi/2.0, pi) is acute.

##### Declaration

```
public double BottomLipReturnAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FBottomLipReturnLength)BottomLipReturnLength

The length of the bottom lip return length, where 0.0 represents no return.

##### Declaration

```
public double BottomLipReturnLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FRadius)Radius

Inside radius in inches for the bends of the material.

##### Declaration

```
public double Radius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FThickness)Thickness

Material thickness in inches.

##### Declaration

```
public double Thickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FTopFlangeWidth)TopFlangeWidth

The distance in inches from the backside of the web to the farthest edge of the top flange.

##### Declaration

```
public double TopFlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FTopLipLength)TopLipLength

The length in inches of the top flange lip, where 0.0 represents no lip.

##### Declaration

```
public double TopLipLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FTopLipReturnAngle)TopLipReturnAngle

An angle in the range (0.0, pi) between the top flange lip and its return material. Perpendicular is specified as pi/2.0 radians. An angle between (0.0, pi/2.0) forms an obtuse relationship and (pi/2.0, pi) is actue.

##### Declaration

```
public double TopLipReturnAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FTopLipReturnLength)TopLipReturnLength

The length in inches of the top lip return length, where 0.0 represents no return.

##### Declaration

```
public double TopLipReturnLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FWebGage1)WebGage1

The distance in inches from the bottom most edge of the web to the first gage line of the web.

##### Declaration

```
public double WebGage1 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FWebGage2)WebGage2

The distance in inches from the first gage line of the web to second gage line of the web.

##### Declaration

```
public double WebGage2 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FWebGage3)WebGage3

The distance in inches from the second gage line of the web to third gage line of the web.

##### Declaration

```
public double WebGage3 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

An abstract class for cold formed shapes.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[RolledShape.Dispose(bool)](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FGetBottomFlangeBends)GetBottomFlangeBends()

A list of bottom flange bends specified on the cold formed shape

##### Declaration

```
public ColdFormedBendList GetBottomFlangeBends()
```

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [ColdFormedBendList](DesignData.SDS2.Setup.ColdFormedBendList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FGetTopFlangeBends)GetTopFlangeBends()

A list of top flange bends specified on the cold formed shape

##### Declaration

```
public ColdFormedBendList GetTopFlangeBends()
```

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [ColdFormedBendList](DesignData.SDS2.Setup.ColdFormedBendList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedShape%5FGetWebBends)GetWebBends()

A list of web bends specified on the cold formed shape

##### Declaration

```
public ColdFormedBendList GetWebBends()
```

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [ColdFormedBendList](DesignData.SDS2.Setup.ColdFormedBendList.html) |             |