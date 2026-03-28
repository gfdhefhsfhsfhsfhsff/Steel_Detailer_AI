# Class GratingTread 

Derived class of StairTread. Used for tread schedules of type Grating.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[StairTread](DesignData.SDS2.Setup.StairTread.html)

GratingTread

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class GratingTread : StairTread
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FBOMRemarks)BOMRemarks

Any string(up to 23 characters). Strings will populate the "Remarks" column in the BOM of any stair that uses this tread definition.

##### Declaration

```
public string BOMRemarks { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FBearingBarDepth)BearingBarDepth

The depth(vertical) of any one bearing bar.

##### Declaration

```
public double BearingBarDepth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FBearingBarQuantity)BearingBarQuantity

The count of bearing bars.

##### Declaration

```
public int BearingBarQuantity { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FBearingBarSpacing)BearingBarSpacing

The center-to-center distance(horizontal) between one bearing bar to the next.

##### Declaration

```
public double BearingBarSpacing { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FBearingBarThickness)BearingBarThickness

The thickness(horizontal) of any one bearing bar.

##### Declaration

```
public double BearingBarThickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FBoltDiameter)BoltDiameter

The diameter of the bolts that are to be inserted into the holes in the end plates.

##### Declaration

```
public double BoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FBoltType)BoltType

The type of bolt to be used for fastening the tread to the stair stringers.

##### Declaration

```
public BoltType BoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FCrossBarDepth)CrossBarDepth

The height(vertical) of each cross bar.

##### Declaration

```
public double CrossBarDepth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FCrossBarSpacing)CrossBarSpacing

The center-to-center distance(horizontal) between one cross bar to the next.

##### Declaration

```
public double CrossBarSpacing { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FCrossBarThickness)CrossBarThickness

The thickness(horizontal) of any one cross bar.

##### Declaration

```
public double CrossBarThickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FEndPlateDepth)EndPlateDepth

The depth(vertical) of the end plate.

##### Declaration

```
public double EndPlateDepth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FEndPlateThickness)EndPlateThickness

The thickness(horizontal) of the end plate.

##### Declaration

```
public double EndPlateThickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FHoleHorizontalDistance)HoleHorizontalDistance

The distance(horizontal) from the end plate vertical edge nearest the nosing to the center of the nearest hole.

##### Declaration

```
public double HoleHorizontalDistance { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FHoleSpacing)HoleSpacing

The distance(horizontal) between the centers of adjacent holes.

##### Declaration

```
public double HoleSpacing { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FHoleVerticalDistance)HoleVerticalDistance

The distance(vertical) from the horizontal edge of the end plate to the center of the hole nearest the nosing.

##### Declaration

```
public double HoleVerticalDistance { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FMaterialGrade)MaterialGrade

The steel grade applied to grating treads.

##### Declaration

```
public SteelGrade MaterialGrade { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FName)Name

Returns a string containing the name associated with the specific tread schedule index.

##### Declaration

```
public override string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Overrides

[StairTread.Name](DesignData.SDS2.Setup.StairTread.html#DesignData%5FSDS2%5FSetup%5FStairTread%5FName)

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FNosingWidth)NosingWidth

The width of the nosing plate.

##### Declaration

```
public double NosingWidth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FTreadType)TreadType

Returns type of tread associated with the specific tread schedule index. It is recommended to cast StairTread to the relevant type before working with it.

##### Declaration

```
public override StairTreadType TreadType { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [StairTreadType](DesignData.SDS2.Setup.StairTreadType.html) |             |

##### Overrides

[StairTread.TreadType](DesignData.SDS2.Setup.StairTread.html#DesignData%5FSDS2%5FSetup%5FStairTread%5FTreadType)

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FGratingTread%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Derived class of StairTread. Used for tread schedules of type Grating.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[StairTread.Dispose(bool)](DesignData.SDS2.Setup.StairTread.html#DesignData%5FSDS2%5FSetup%5FStairTread%5FDispose%5FSystem%5FBoolean%5F)