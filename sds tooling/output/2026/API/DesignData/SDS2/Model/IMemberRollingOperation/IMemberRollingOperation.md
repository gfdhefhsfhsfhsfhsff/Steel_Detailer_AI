# Interface IMemberRollingOperation 

Interface for rolling operation properties.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public interface IMemberRollingOperation
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FIMemberRollingOperation%5FIncludedAngleRoll)IncludedAngleRoll

The included angle of the rolling operation. This can be set for any operation besides a camber roll

##### Declaration

```
double IncludedAngleRoll { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FIMemberRollingOperation%5FMidOrdinateRoll)MidOrdinateRoll

The measurement from the center of the curved member to point halfway between the left and right end. For Camber, this is the only valid value to set.

##### Declaration

```
double MidOrdinateRoll { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FIMemberRollingOperation%5FRollType)RollType

The type of roll on this material, or None if there is no roll on this material.

##### Declaration

```
RollType RollType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [RollType](DesignData.SDS2.Model.RollType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FIMemberRollingOperation%5FRollingRadius)RollingRadius

The rolling radius for any roll operation besides a camber roll.

##### Declaration

```
double RollingRadius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FIMemberRollingOperation%5FSpiralRollOffset)SpiralRollOffset

The positive or negative distance that the right end will be offset from the right work point in the member's Z axis.

##### Declaration

```
double SpiralRollOffset { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |