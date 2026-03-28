# Class BaseCapRoundPlate 

A round base/cap plate

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html)

BaseCapRoundPlate

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
public class BaseCapRoundPlate : BaseCapPlate
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRoundPlate%5FDiameter)Diameter

The diameter of the base cap plate

##### Declaration

```
public double Diameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRoundPlate%5FHoleCount)HoleCount

The number of holes on this round plate

##### Declaration

```
public uint HoleCount { get; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRoundPlate%5FHolePatternOffset)HolePatternOffset

The offset between each hole in the pattern

##### Declaration

```
public double HolePatternOffset { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRoundPlate%5FHolePatternRadius)HolePatternRadius

The radius of the hole pattern - distance from center of plate to center of every hole.

##### Declaration

```
public double HolePatternRadius { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapRoundPlate%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A round base/cap plate

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