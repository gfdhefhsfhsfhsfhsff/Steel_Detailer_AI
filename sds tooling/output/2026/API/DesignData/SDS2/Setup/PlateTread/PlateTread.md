# Class PlateTread 

Derived class of StairTread. Used for tread schedules of type Plate.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[StairTread](DesignData.SDS2.Setup.StairTread.html)

PlateTread

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
public class PlateTread : StairTread
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FBOMRemarks)BOMRemarks

Any string(up to 23 characters). Strings will populate the "Remarks" column in the BOM of any stair that uses this tread definition.

##### Declaration

```
public string BOMRemarks { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FBoltDiameter)BoltDiameter

The diameter(inches or mm) of the shank of the bolt.

##### Declaration

```
public double BoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FBoltType)BoltType

This is the type of bolt to be used for fastening the vertical leg of the plate tread angle support to the stringer.

##### Declaration

```
public BoltType BoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FCheckered)Checkered

If true, this tread becomes a checkered plate, which is a steel plate with raised ribs on its top horizontal surface to prevent slippage on the stair treads.

##### Declaration

```
public bool Checkered { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FHoleHorizontalDistance)HoleHorizontalDistance

The distance(horizontal) from the corner of the support angle that is nearest the nosing point to the nearest hole in the angle.

##### Declaration

```
public double HoleHorizontalDistance { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FHoleSpacing)HoleSpacing

The distance(horizontal) from the center of one hole in the leg to the stringer to the center of the other hole in the leg to the stringer.

##### Declaration

```
public double HoleSpacing { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FHoleVerticalDistance)HoleVerticalDistance

The distance(vertical) from the top face of the horizontal leg of the angle(the leg to the tread) to the nearest hole in the leg to the stringer.

##### Declaration

```
public double HoleVerticalDistance { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FLengthInsideLeg)LengthInsideLeg

The distance(horizontal) from the bottom bend in the vertical leg(either vertical leg) to the toe of the horizontal leg(either horizontal leg) of the cold-formed channel tread.

##### Declaration

```
public double LengthInsideLeg { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FLengthLegOne)LengthLegOne

Leg length for dunbar plate treads.

##### Declaration

```
public double LengthLegOne { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FLengthLegTwo)LengthLegTwo

Leg length for dunbar plate treads.

##### Declaration

```
public double LengthLegTwo { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FName)Name

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

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FNosingLegAngle)NosingLegAngle

The angle(in degrees) between the bottom of the tread and the inside face of the nosing leg.

##### Declaration

```
public double NosingLegAngle { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FPatternSetback)PatternSetback

The distance(vertical) that the C-shaped plate treads are to be offset from the workline of the stair.

##### Declaration

```
public double PatternSetback { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FPlateMaterialDescription)PlateMaterialDescription

A plate description, flat bar description, or angle section size.

##### Declaration

```
public Shape PlateMaterialDescription { get; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FPlateMaterialGrade)PlateMaterialGrade

The grade of steel for the bent plate layout material that is used to model the treads.

##### Declaration

```
public SteelGrade PlateMaterialGrade { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FPlateThickness)PlateThickness

The thickness("Material Thickness") of the bent plate layout material that is used to model the C-shaped treads.

##### Declaration

```
public double PlateThickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FRiserLegAngle)RiserLegAngle

The distance(actual) from the bottom of the tread to the top of the riser leg.

##### Declaration

```
public double RiserLegAngle { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FRolledCFChannelMaterialGrade)RolledCFChannelMaterialGrade

The grade of steel for the bent plate layout material that is used to model the treads.

##### Declaration

```
public SteelGrade RolledCFChannelMaterialGrade { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FRolledCFChannelSectionSize)RolledCFChannelSectionSize

A section for a cold formed channel material that is listed in the local material file.

##### Declaration

```
public Shape RolledCFChannelSectionSize { get; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FRolledCFZMaterialGrade)RolledCFZMaterialGrade

The grade of steel for the bent plate layout material that is used to model the treads.

##### Declaration

```
public SteelGrade RolledCFZMaterialGrade { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FRolledCFZSectionSize)RolledCFZSectionSize

A section for a cold formed z material that is listed in the local material file.

##### Declaration

```
public Shape RolledCFZSectionSize { get; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FRolledChannelMaterialGrade)RolledChannelMaterialGrade

The grade of steel for the bent plate layout material that is used to model the treads.

##### Declaration

```
public SteelGrade RolledChannelMaterialGrade { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FRolledChannelSectionSize)RolledChannelSectionSize

A section for channel material that is listed in the local material file.

##### Declaration

```
public Shape RolledChannelSectionSize { get; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FShape)Shape

C-shaped(up/down), Cold Formed Channel, Other, Rolled Channel, Rolled Cold Formed Channel, or Rolled Cold Formed Z.

##### Declaration

```
public StairPlateTreadShape Shape { get; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [StairPlateTreadShape](DesignData.SDS2.Setup.StairPlateTreadShape.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FSupportLength)SupportLength

The distance(horizontal) that the support, when installed, will be flush to the bottom of the tread.

##### Declaration

```
public double SupportLength { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FSupportLongLegTo)SupportLongLegTo

Stringer or Tread. This applies when an angle with unequal legs has been entered as the "Material Description". If the legs are equal the choice does not matter.

##### Declaration

```
public StairTreadSupportLongLegTo SupportLongLegTo { get; }
```

##### Property Value

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [StairTreadSupportLongLegTo](DesignData.SDS2.Setup.StairTreadSupportLongLegTo.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FSupportPlateType)SupportPlateType

Angle, Plate, Flat.

##### Declaration

```
public StairSupportMtrlType SupportPlateType { get; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [StairSupportMtrlType](DesignData.SDS2.Setup.StairSupportMtrlType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FSupportSetback)SupportSetback

The distance(horizontal) from the nosing point to the support.

##### Declaration

```
public double SupportSetback { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FSupportThickness)SupportThickness

Support plate thickness for flat/plate supports.

##### Declaration

```
public double SupportThickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FSupportType)SupportType

None of Single Support. A tread support can be applied to any tread that can be defined when the "Type of Tread" is 'Plate'.

##### Declaration

```
public StairSupportType SupportType { get; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [StairSupportType](DesignData.SDS2.Setup.StairSupportType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FSupportWidth)SupportWidth

Support plate width for flat/plate supports.

##### Declaration

```
public double SupportWidth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FTreadType)TreadType

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

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FTreadWidth)TreadWidth

The distance(horizontal) between the two outside corners of the heel of the C-shaped tread.

##### Declaration

```
public double TreadWidth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FPlateTread%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Derived class of StairTread. Used for tread schedules of type Plate.

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