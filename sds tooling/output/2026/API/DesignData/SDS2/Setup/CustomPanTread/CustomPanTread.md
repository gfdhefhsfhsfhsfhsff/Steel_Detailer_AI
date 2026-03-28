# Class CustomPanTread 

Derived class of StairTread. Used for tread schedules of type Pan.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[StairTread](DesignData.SDS2.Setup.StairTread.html)

CustomPanTread

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
public class CustomPanTread : StairTread
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FAbrasiveSetback)AbrasiveSetback

The distance(vertical) that the pan treads are to be offset from the workline of the stair.

##### Declaration

```
public double AbrasiveSetback { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FBOMRemarks)BOMRemarks

Any string(up to 23 characters). Strings will populate the "Remarks" column in the BOM of any stair that uses this tread definition.

##### Declaration

```
public string BOMRemarks { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FCoveWidth)CoveWidth

The distance(horizontal) from the sanitary cove's inside bend to its upper bend.

##### Declaration

```
public double CoveWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FMaterialDescription)MaterialDescription

An angle section size, plate description, flat bar description, or ben plate description.

##### Declaration

```
public Shape MaterialDescription { get; set; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FMaterialGrade)MaterialGrade

Returns the grade of stell of the bent plate layout material that is used to model the pan treads.

##### Declaration

```
public SteelGrade MaterialGrade { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FName)Name

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

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FNosingDepth)NosingDepth

The distance(vertical) from the top edge of the nosing to the back bend.

##### Declaration

```
public double NosingDepth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FNosingReturnBottom)NosingReturnBottom

The distance(horizontal) from the top nosing bend to the main bend or the first intermediary bend.

##### Declaration

```
public double NosingReturnBottom { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FNosingReturnTop)NosingReturnTop

The distance(horizontal) from the top nosing bend to the nearest vertical edge.

##### Declaration

```
public double NosingReturnTop { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FNosingReturnType)NosingReturnType

Type of nosing used for Pan tread definitions.

##### Declaration

```
public StairNosingReturnType NosingReturnType { get; set; }
```

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [StairNosingReturnType](DesignData.SDS2.Setup.StairNosingReturnType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FPanDepth)PanDepth

The distance(vertical) from the top of the pan to the top of the adjacent nosing return.

##### Declaration

```
public double PanDepth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FPlateThickness)PlateThickness

The thickness of plate material to be used for the bent plate stair tread.

##### Declaration

```
public double PlateThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FRemoveBends)RemoveBends

Determines if pan tread will have bends.

##### Declaration

```
public bool RemoveBends { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FReturnLength)ReturnLength

The distance(actual) from the pan return bend to the top edge of the pan return.

##### Declaration

```
public double ReturnLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FRiserFace)RiserFace

The distance(diagonal) from the end of the bent plate leg that attaches to the riser to the heel of the tread.

##### Declaration

```
public double RiserFace { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FSupportLongLegTo)SupportLongLegTo

Stringer or Tread. This applies when an angle with unequal lengs has been entered as the "Material Description".

##### Declaration

```
public StairTreadSupportLongLegTo SupportLongLegTo { get; set; }
```

##### Property Value

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [StairTreadSupportLongLegTo](DesignData.SDS2.Setup.StairTreadSupportLongLegTo.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FSupportPlateType)SupportPlateType

Angle, Plate, Flat.

##### Declaration

```
public StairSupportMtrlType SupportPlateType { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [StairSupportMtrlType](DesignData.SDS2.Setup.StairSupportMtrlType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FSupportThickness)SupportThickness

Support plate thickness for flat/plate supports.

##### Declaration

```
public double SupportThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FSupportType)SupportType

None, Single Support, Dual Supports, or Bent Plate. For any choice other than 'None', be sure to enter an appropriate "Material Description".

##### Declaration

```
public StairSupportType SupportType { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [StairSupportType](DesignData.SDS2.Setup.StairSupportType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FSupportWidth)SupportWidth

Support plate width for flat/plate supports.

##### Declaration

```
public double SupportWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FTreadFace)TreadFace

The distance(horizontal) from the inside face of the riser to the end of the bent plate leg that attaches to the tread.

##### Declaration

```
public double TreadFace { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FTreadType)TreadType

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

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPanTread%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Derived class of StairTread. Used for tread schedules of type Pan.

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