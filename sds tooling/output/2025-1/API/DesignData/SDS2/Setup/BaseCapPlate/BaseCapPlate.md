# Class BaseCapPlate 

A single entry on the base/cap plate schedule.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BaseCapPlate

[BaseCapRectangularPlate](DesignData.SDS2.Setup.BaseCapRectangularPlate.html)

[BaseCapRoundPlate](DesignData.SDS2.Setup.BaseCapRoundPlate.html)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class BaseCapPlate
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FAdditionalHoles)AdditionalHoles

Additional holes on the base plate. Up to 8.

##### Declaration

```
public BaseCapPlateAdditionalHoleList AdditionalHoles { get; }
```

##### Property Value

| Type                                                                                        | Description |
| ------------------------------------------------------------------------------------------- | ----------- |
| [BaseCapPlateAdditionalHoleList](DesignData.SDS2.Setup.BaseCapPlateAdditionalHoleList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FBoltDiameter)BoltDiameter

The diameter of bolts to use in the holes of this base plate

##### Declaration

```
public double BoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FColumnWeldPrep)ColumnWeldPrep

Get the column end prep options for BevelGroove welds

##### Declaration

```
public BaseCapPlateColumnFlangePrep ColumnWeldPrep { get; }
```

##### Property Value

| Type                                                                                    | Description |
| --------------------------------------------------------------------------------------- | ----------- |
| [BaseCapPlateColumnFlangePrep](DesignData.SDS2.Setup.BaseCapPlateColumnFlangePrep.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FGrade)Grade

A single entry on the base/cap plate schedule.

##### Declaration

```
public SteelGrade Grade { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FHoleDiameter)HoleDiameter

The diameter of holes in the center of this base plate

##### Declaration

```
public double HoleDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FHoleType)HoleType

The hole type used for the holes in this base plate. Note that the only valid options are AnchorBolt, StandardRound, and Oversize

##### Declaration

```
public HoleType HoleType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [HoleType](DesignData.SDS2.Setup.HoleType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FPiecemark)Piecemark

The piecemark which will be assigned to base/cap plates in the model like this. This also serves as a unique name for this plate in the schedule.

##### Declaration

```
public string Piecemark { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FThickness)Thickness

The thickness of the base cap plate

##### Declaration

```
public double Thickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FVentDrainPattern)VentDrainPattern

A single entry on the base/cap plate schedule.

##### Declaration

```
public VentDrainHolePattern VentDrainPattern { get; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [VentDrainHolePattern](DesignData.SDS2.Setup.VentDrainHolePattern.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FWeldsAsBasePlate)WeldsAsBasePlate

Get the weld options to weld this base plate to the column

##### Declaration

```
public BaseCapPlateWelds WeldsAsBasePlate { get; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [BaseCapPlateWelds](DesignData.SDS2.Setup.BaseCapPlateWelds.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FWeldsAsCapPlate)WeldsAsCapPlate

Get the weld options to weld this cap plate to the column

##### Declaration

```
public BaseCapPlateWelds WeldsAsCapPlate { get; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [BaseCapPlateWelds](DesignData.SDS2.Setup.BaseCapPlateWelds.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A single entry on the base/cap plate schedule.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FEquals%5FSystem%5FObject%5F)Equals(object)

A single entry on the base/cap plate schedule.

##### Declaration

```
public override bool Equals(object other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | other |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FFinalize)\~BaseCapPlate()

A single entry on the base/cap plate schedule.

##### Declaration

```
protected ~BaseCapPlate()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FGetHashCode)GetHashCode()

A single entry on the base/cap plate schedule.

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)