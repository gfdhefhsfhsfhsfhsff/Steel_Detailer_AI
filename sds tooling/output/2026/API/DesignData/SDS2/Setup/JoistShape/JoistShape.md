# Class JoistShape 

A Shape derived class.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

JoistShape

##### Inherited Members

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
public class JoistShape : Shape
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FBottomChordReferenceSetback)BottomChordReferenceSetback

Setback from the end of the top shoe to the end of the bottom chord

##### Declaration

```
public double BottomChordReferenceSetback { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FBottomChordShape)BottomChordShape

The angle shape to use to create the bottom chord

##### Declaration

```
public AngleShape BottomChordShape { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [AngleShape](DesignData.SDS2.Setup.AngleShape.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FDepth)Depth

The distance from the top of the top chord to the bottom of the bottom chord

##### Declaration

```
public double Depth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FFillerThickness)FillerThickness

Thickness of the filler section of the joist, similar to a web thickness measurement on a W section

##### Declaration

```
public double FillerThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FJoistType)JoistType

A Shape derived class.

##### Declaration

```
public JoistType JoistType { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [JoistType](DesignData.SDS2.Setup.JoistType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FShoeDepth)ShoeDepth

A Shape derived class.

##### Declaration

```
public double ShoeDepth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FShoeGage)ShoeGage

The distance betwen the gage lines on the shoes, half of this value is the distance from the center of the joist to each gage line.

##### Declaration

```
public double ShoeGage { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FShoeLength)ShoeLength

The length of the shoe angle

##### Declaration

```
public double ShoeLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FShoeShape)ShoeShape

The angle shape to use to create the shoe

##### Declaration

```
public AngleShape ShoeShape { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [AngleShape](DesignData.SDS2.Setup.AngleShape.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FTopChordGage)TopChordGage

The distance between the gage lines on the top chord, half of this value is the distance from the center of the joist to each gage line.

##### Declaration

```
public double TopChordGage { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FTopChordShape)TopChordShape

The angle shape to use to create the top chord

##### Declaration

```
public AngleShape TopChordShape { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [AngleShape](DesignData.SDS2.Setup.AngleShape.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

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

#### [](#DesignData%5FSDS2%5FSetup%5FJoistShape%5FGetStructuralProperties%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F)GetStructuralProperties(SteelGrade)

Get the structural properties, from the production standard, for a specific grade. To get the default standard pass null for the grade

##### Declaration

```
public JoistStructuralProperties GetStructuralProperties(SteelGrade forGrade)
```

##### Parameters

| Type                                                | Name     | Description                                                                                                                                                                                                                      |
| --------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | forGrade | Production standards are under grade names for many types, so passing in the grade lets us lookup StructuralProperties for a specific production standard for this grade. There is also always a default, pass null to get this. |

##### Returns

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [JoistStructuralProperties](DesignData.SDS2.Setup.JoistStructuralProperties.html) |             |