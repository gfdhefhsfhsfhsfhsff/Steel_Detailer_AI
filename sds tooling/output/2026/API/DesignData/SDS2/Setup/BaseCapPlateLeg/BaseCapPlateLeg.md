# Class BaseCapPlateLeg 

One leg off a base/cap plate

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BaseCapPlateLeg

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
public class BaseCapPlateLeg
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FLatitudeHoleCount)LatitudeHoleCount

Number of columns of holes

##### Declaration

```
public int LatitudeHoleCount { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FLatitudeHoleSpacing)LatitudeHoleSpacing

Distance between each hole column

##### Declaration

```
public double LatitudeHoleSpacing { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FLatitudeToFirstHole)LatitudeToFirstHole

The distance from the center of the base cap plate to the center of the first hole, on this leg, on the X axis.

##### Declaration

```
public double LatitudeToFirstHole { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FLength)Length

The length of the leg - how far it juts out from the edge of the base cap plate

##### Declaration

```
public double Length { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FLongitudeFarSideHoleCount)LongitudeFarSideHoleCount

Number of rows of holes for the far side group

##### Declaration

```
public int LongitudeFarSideHoleCount { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FLongitudeHoleSpacingFarSide)LongitudeHoleSpacingFarSide

Distance between each hole row, on the far side group.

##### Declaration

```
public double LongitudeHoleSpacingFarSide { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FLongitudeHoleSpacingNearSide)LongitudeHoleSpacingNearSide

Distance between each hole row, on the near side group.

##### Declaration

```
public double LongitudeHoleSpacingNearSide { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FLongitudeNearSideHoleCount)LongitudeNearSideHoleCount

Number of rows of holes for the near side group

##### Declaration

```
public int LongitudeNearSideHoleCount { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FLongitudeToFirstHoleFarSide)LongitudeToFirstHoleFarSide

The distance from the center of the base cap plate to the center of the first hole, on this leg, in the Y axis on the far side.

##### Declaration

```
public double LongitudeToFirstHoleFarSide { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FLongitudeToFirstHoleNearSide)LongitudeToFirstHoleNearSide

The distance from the center of the base cap plate to the center of the first hole, on this leg, in the Y axis on the near side.

##### Declaration

```
public double LongitudeToFirstHoleNearSide { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

One leg off a base/cap plate

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateLeg%5FFinalize)\~BaseCapPlateLeg()

One leg off a base/cap plate

##### Declaration

```
protected ~BaseCapPlateLeg()
```