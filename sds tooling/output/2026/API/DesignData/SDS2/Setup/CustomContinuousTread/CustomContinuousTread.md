# Class CustomContinuousTread 

Derived class of StairTread. Used for tread schedules of type Continuous Plate.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[StairTread](DesignData.SDS2.Setup.StairTread.html)

CustomContinuousTread

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
public class CustomContinuousTread : StairTread
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FBOMRemarks)BOMRemarks

Any string(up to 23 characters). Strings will populate the "Remarks" column in the BOM of any stair that uses this tread definition.

##### Declaration

```
public string BOMRemarks { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FCheckered)Checkered

If true, each continuous stair tread becomes a checkered plate, which is a steel plate with raised ribs on its near-side to prevent slippage on the stair treads.

##### Declaration

```
public bool Checkered { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FClearance)Clearance

THe distance(actual) from the top of a riser to the bottom of the adjacent tread that is immediately above that riser.

##### Declaration

```
public double Clearance { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FGap)Gap

The distance(actual) from the riser for one tread to the lef for the adjacent tread that is immediately above that tread.

##### Declaration

```
public double Gap { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FLegLength)LegLength

The distance(actual) from the corner at the leg bend to the end of the leg.

##### Declaration

```
public double LegLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FMaterialDescription)MaterialDescription

A plate description, or flat bar description, or angle description.

##### Declaration

```
public Shape MaterialDescription { get; set; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FMaterialGrade)MaterialGrade

The grade of steel for the bent plate layout material that is used to model the continuous stair treads.

##### Declaration

```
public SteelGrade MaterialGrade { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FName)Name

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

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FPatternSetback)PatternSetback

The distance(vertical) that the continuous stair treads are to be offset from the workline of the stair.

##### Declaration

```
public double PatternSetback { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FPlateThickness)PlateThickness

The thickness("Material Thickness" of the bent plate layout material that is used to model the continuous stair treads.

##### Declaration

```
public double PlateThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FReturnBottom)ReturnBottom

The distance(horizontal) that you want the tread to be extended.

##### Declaration

```
public double ReturnBottom { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FReturnTop)ReturnTop

The distance(horizontal) from the top bend to the end of the top return.

##### Declaration

```
public double ReturnTop { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FSupportLongLegTo)SupportLongLegTo

Stringer of Tread. This applies when an angle with unequal legs has been entered as the "Material Description".

##### Declaration

```
public StairTreadSupportLongLegTo SupportLongLegTo { get; set; }
```

##### Property Value

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [StairTreadSupportLongLegTo](DesignData.SDS2.Setup.StairTreadSupportLongLegTo.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FSupportPlateType)SupportPlateType

None, Single Support, or Dual Support.

##### Declaration

```
public StairSupportMtrlType SupportPlateType { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [StairSupportMtrlType](DesignData.SDS2.Setup.StairSupportMtrlType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FSupportThickness)SupportThickness

Support plate thickness for flat/plate supports.

##### Declaration

```
public double SupportThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FSupportType)SupportType

None, Single Support, or Dual Support.

##### Declaration

```
public StairSupportType SupportType { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [StairSupportType](DesignData.SDS2.Setup.StairSupportType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FSupportWidth)SupportWidth

Support plate width for flat/plate supports.

##### Declaration

```
public double SupportWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FTreadType)TreadType

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

#### [](#DesignData%5FSDS2%5FSetup%5FCustomContinuousTread%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Derived class of StairTread. Used for tread schedules of type Continuous Plate.

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