# Class ShearTabSpecification 

A shear tab connection

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

ShearTabSpecification

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public sealed class ShearTabSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5F%5Fctor)ShearTabSpecification()

A shear tab connection

##### Declaration

```
public ShearTabSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FAttachToMember)AttachToMember

Which member to attach connection material to, supported or supporting.

##### Declaration

```
public AttachToMember AttachToMember { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AttachToMember](DesignData.SDS2.Model.AttachToMember.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FAttachmentMethod)AttachmentMethod

The attachment method for the shear tab, to the supporting material. This is only used if the MaterialType is set to a Wtee for a built-up plate.

##### Declaration

```
public AttachmentMethod AttachmentMethod { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [AttachmentMethod](DesignData.SDS2.Model.AttachmentMethod.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FAxialLoadCheck)AxialLoadCheck

The "Supporting member web stress" will be reported as a "Left/Right end limit state" when a "Tension load" has been applied to the supported beam's shear plate connection end. This option affects whether or not that limit state is incorporated as a check within connection design that can potentially cause the shear plate connection to fail

##### Declaration

```
public AxialLoadCheckOption AxialLoadCheck { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [AxialLoadCheckOption](DesignData.SDS2.Model.AxialLoadCheckOption.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FBevelShearTab)BevelShearTab

Per AISC, beveling of a 5/16- to 3/8-inch shear plate is required when the dihedral angle is between 45 and 60 degrees. A 1/2-inch shear plate is required to be beveled from 22° to 45° from perpendicular. Yes will bevel as needed, where No will never bevel. Automatic pulls this option from setup.

##### Declaration

```
public AutomaticYesNo BevelShearTab { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FBottomExtension)BottomExtension

A shear tab connection

##### Declaration

```
public ConnectionExtensionType BottomExtension { get; set; }
```

##### Property Value

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [ConnectionExtensionType](DesignData.SDS2.Model.ConnectionExtensionType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FCombineShearTab)CombineShearTab

When this end of this beam frames to a column with a single-plate shear connection and a vertical brace frames to this beam and that same column, the system can either create one combined shear plate or two shear plates (one for the beam-to-column interface, the second for the gusset-to-column interface).

##### Declaration

```
public AutomaticYesNo CombineShearTab { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FDisablePlastificationCheck)DisablePlastificationCheck

A shear tab connection

##### Declaration

```
public bool DisablePlastificationCheck { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FEmbedLocation)EmbedLocation

Applies when a beam frames to a concrete wall. If InsideWall, then the embed plate will be modeled inside the concrete wall. When OutsideWall, it is attached to the outside of the wall. Automatic will pull this option from setup.

##### Declaration

```
public EmbedLocation EmbedLocation { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [EmbedLocation](DesignData.SDS2.Setup.EmbedLocation.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FExtendPastFlange)ExtendPastFlange

Set the supported beam back beyond the flange of the supporting column (when connecting to the column web) if true. If false, clip the supported beam so that it fits inside the column flange.

##### Declaration

```
public bool ExtendPastFlange { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FExtendToWebByForce)ExtendToWebByForce

Only applies if ExtendPastFlange is true. If true, this will force the stabilizer plates to be extended to the web. If false, the system will decide if that is necessary and do so if required.

##### Declaration

```
public bool ExtendToWebByForce { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FFlangePlateEnd)FlangePlateEnd

A shear tab connection

##### Declaration

```
public FlangePlateOnShearTabEnd FlangePlateEnd { get; set; }
```

##### Property Value

| Type                                                                            | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [FlangePlateOnShearTabEnd](DesignData.SDS2.Model.FlangePlateOnShearTabEnd.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FShearMaterialType)ShearMaterialType

The material type to use to make the shear tab

##### Declaration

```
public ShearMaterialType ShearMaterialType { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [ShearMaterialType](DesignData.SDS2.Model.ShearMaterialType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FSide)Side

Which side of the supported member to put the shear plate on.

##### Declaration

```
public ShearPlateSide Side { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [ShearPlateSide](DesignData.SDS2.Model.ShearPlateSide.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FSkewPlateHoles)SkewPlateHoles

If set to yes, the rows of holes will be parallel with the supported beam flange. If set to no, they will be parallel with the supporting column. Automatic will pull this setting from setup.

##### Declaration

```
public AutomaticYesNo SkewPlateHoles { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FSupportCondition)SupportCondition

For ASD9 and LRFD3 only

##### Declaration

```
public ShearSupportCondition SupportCondition { get; set; }
```

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [ShearSupportCondition](DesignData.SDS2.Model.ShearSupportCondition.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FTopExtension)TopExtension

A shear tab connection

##### Declaration

```
public ConnectionExtensionType TopExtension { get; set; }
```

##### Property Value

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [ConnectionExtensionType](DesignData.SDS2.Model.ConnectionExtensionType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FUseAlternateEccentricity)UseAlternateEccentricity

Applies when 'ASD13' or 'LRFD13' or a newer AISC method is the "Connection design method." It applies to " Extend past flange" shear connections. Per the AISC 13th Edition, p 10-103 and AISC 14th Edition, p 10-104, "alternate considerations of the design eccentricity are acceptable when justified by rational analysis.

##### Declaration

```
public AutomaticYesNo UseAlternateEccentricity { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FUseBackupBar)UseBackupBar

Applies to skewed beam-to-beam or beam-to-column single-plate shear connections with angles to the supported member of less than 45 degrees. Standard AISC practices call for a back-up bar to be used for such welds.

##### Declaration

```
public AutomaticYesNo UseBackupBar { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FUseExpandedVerticalBoltSpacing)UseExpandedVerticalBoltSpacing

Applies to 'Non-moment' shear plates or shear tees to a beam or a column. If Yes, permits the system to expand the vertical spacing of bolts to 1.5 times or 2 times the Fabricator Setup > Connection Erectability Settings > "Bolt spacing" that is set per bolt diameter. The system may also adjust to a spacing other than 1.5 or 2 times the standard bolt spacing in order to accommodate piecemarking issues, loading conditions and unusual geometries.

##### Declaration

```
public AutomaticYesNo UseExpandedVerticalBoltSpacing { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FUseHSSReinforcementPlate)UseHSSReinforcementPlate

When set to Yes, column reinforcement plates are designed, as needed, for non-moment shear plates or welded moment connections to an HSS rectangular or TS column. If No and column wall reinforcement is needed, you will get the end connection failure.

##### Declaration

```
public AutomaticYesNo UseHSSReinforcementPlate { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FUsePaddlePlate)UsePaddlePlate

If the supported beam is a tube, when true this will use a paddle plate to connect the tube, rather than shear tabs on each side of the tube.

##### Declaration

```
public bool UsePaddlePlate { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FUseStiffenerOppositeShearTab)UseStiffenerOppositeShearTab

If true, put a stiffener on the opposite the shear tab when framing into the web of a beam

##### Declaration

```
public bool UseStiffenerOppositeShearTab { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FUseThroughPlate)UseThroughPlate

If the supporting column is a tube, run the shear plate through the wall of the tube.

##### Declaration

```
public ShearThroughPlate UseThroughPlate { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [ShearThroughPlate](DesignData.SDS2.Model.ShearThroughPlate.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FShearTabSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A shear tab connection

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[ConnectionSpecification.Dispose(bool)](DesignData.SDS2.Model.ConnectionSpecification.html#DesignData%5FSDS2%5FModel%5FConnectionSpecification%5FDispose%5FSystem%5FBoolean%5F)