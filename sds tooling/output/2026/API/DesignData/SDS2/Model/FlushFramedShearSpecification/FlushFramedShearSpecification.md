# Class FlushFramedShearSpecification 

A flush framed shear connection for joists.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

FlushFramedShearSpecification

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
public sealed class FlushFramedShearSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5F%5Fctor)FlushFramedShearSpecification()

A flush framed shear connection for joists.

##### Declaration

```
public FlushFramedShearSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FAttachToMember)AttachToMember

Which member to attach connection material to, supported or supporting.

##### Declaration

```
public AttachToMember AttachToMember { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AttachToMember](DesignData.SDS2.Model.AttachToMember.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FAxialLoadCheck)AxialLoadCheck

The "Supporting member web stress" will be reported as a "Left/Right end limit state" when a "Tension load" has been applied to the supported beam's shear plate connection end. This option affects whether or not that limit state is incorporated as a check within connection design that can potentially cause the shear plate connection to fail

##### Declaration

```
public AxialLoadCheckOption AxialLoadCheck { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [AxialLoadCheckOption](DesignData.SDS2.Model.AxialLoadCheckOption.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FBevelShearTab)BevelShearTab

Per AISC, beveling of a 5/16- to 3/8-inch shear plate is required when the dihedral angle is between 45 and 60 degrees. A 1/2-inch shear plate is required to be beveled from 22° to 45° from perpendicular. Yes will bevel as needed, where No will never bevel. Automatic pulls this option from setup.

##### Declaration

```
public AutomaticYesNo BevelShearTab { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FExtendBottomChord)ExtendBottomChord

If true, the bottom chord of the joist is extended and "Bottom chord" is set to ' Auto' so that the appropriate field clearance is applied. "Stabilizing material" is optional.

```
         If false, you can still apply a "Bottom chord" setback to get a
         bottom chord. However, "Stabilizing material" cannot be
         applied.

```

##### Declaration

```
public bool ExtendBottomChord { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FExtendPastFlange)ExtendPastFlange

Set the supported beam back beyond the flange of the supporting column (when connecting to the column web) if true. If false, clip the supported beam so that it fits inside the column flange.

##### Declaration

```
public bool ExtendPastFlange { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FExtendToWebByForce)ExtendToWebByForce

Only applies if ExtendPastFlange is true. If true, this will force the stabilizer plates to be extended to the web. If false, the system will decide if that is necessary and do so if required.

##### Declaration

```
public bool ExtendToWebByForce { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FSide)Side

Which side of the supported member to put the shear plate on.

##### Declaration

```
public ShearPlateSide Side { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [ShearPlateSide](DesignData.SDS2.Model.ShearPlateSide.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FSkewPlateHoles)SkewPlateHoles

If set to yes, the rows of holes will be parallel with the supported beam flange. If set to no, they will be parallel with the supporting column. Automatic will pull this setting from setup.

##### Declaration

```
public AutomaticYesNo SkewPlateHoles { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FStabilizingMaterial)StabilizingMaterial

None results in no joist bottom chord stabilizing material being created by the system.

```
         Angle instructs the system to use the Fabricator Setup > Standard
         Fabricator Connections > "Bottom chord extension seat angle" as
         the angle seat for the extended bottom chord.

         Plate instructs the system to use the Fabricator Setup >
         Standard Fabricator Connections > "Bottom chord extension plate"
         as the stabilizing material for the extended bottom chord. Per
         the OSHA standard, the plate includes a 13/16 inch (21 mm) hole
         (click here) for guying or plumbing cables. The hole is placed 1
         1/2 inch from the bottom edge and joist edge of the plate.

```

##### Declaration

```
public JoistStabilizingMaterial StabilizingMaterial { get; set; }
```

##### Property Value

| Type                                                                            | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [JoistStabilizingMaterial](DesignData.SDS2.Model.JoistStabilizingMaterial.html) |             |

##### Remarks

Only valid of ExtendBottomChord is true

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FTryTwoBoltColumnShearTabs)TryTwoBoltColumnShearTabs

If set to true, connection attempts to create a non-moment shear plate with two columns of bolts.

##### Declaration

```
public bool TryTwoBoltColumnShearTabs { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FUseAlternateEccentricity)UseAlternateEccentricity

Applies when 'ASD13' or 'LRFD13' or a newer AISC method is the "Connection design method." It applies to " Extend past flange" shear connections. Per the AISC 13th Edition, p 10-103 and AISC 14th Edition, p 10-104, "alternate considerations of the design eccentricity are acceptable when justified by rational analysis.

##### Declaration

```
public AutomaticYesNo UseAlternateEccentricity { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FUseBackupBar)UseBackupBar

Applies to skewed beam-to-beam or beam-to-column single-plate shear connections with angles to the supported member of less than 45 degrees. Standard AISC practices call for a back-up bar to be used for such welds.

##### Declaration

```
public AutomaticYesNo UseBackupBar { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FUseErectionHole)UseErectionHole

Automatic instructs the system to use the entry ('Yes' or 'No') that is made to the relevant cell in Fabricator Setup > Standard Fabricator Connections > Joist Setup > "Use erection hole" on the "Joist type specific settings" table. That setup table can configure an erection hole to be used or not used on a per-joist-type basis.

```
        Yes instructs the system to add a hole for guying or plumbing
        cables to the bottom chord stabilizer plate. Per OSHA, the hole
        is placed 1 1/2 inch from the bottom edge and joist edge of the
        plate. A connection design lock for specifying the "Erection hole
        diameter" is made available in the " Joist Stabilizer Plate"
        leaf.

        No instructs the system to not add an erection hole.

```

##### Declaration

```
public AutomaticYesNo UseErectionHole { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

##### Remarks

Only valid if StabilizingMaterial is set to Plate

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FUseExpandedVerticalBoltSpacing)UseExpandedVerticalBoltSpacing

Applies to 'Non-moment' shear plates or shear tees to a beam or a column. If Yes, permits the system to expand the vertical spacing of bolts to 1.5 times or 2 times the Fabricator Setup > Connection Detailing/Fabricator Options > "Bolt spacing" that is set per bolt diameter. The system may also adjust to a spacing other than 1.5 or 2 times the standard bolt spacing in order to accommodate piecemarking issues, loading conditions and unusual geometries.

##### Declaration

```
public AutomaticYesNo UseExpandedVerticalBoltSpacing { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FUseStiffenerOppositeShearTab)UseStiffenerOppositeShearTab

If true, put a stiffener on the opposite the shear tab when framing into the web of a beam

##### Declaration

```
public bool UseStiffenerOppositeShearTab { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FUseVerticalStabilizerAngle)UseVerticalStabilizerAngle

If true, the bottom chord stabilizer angle is oriented with both legs vertical. That angle is vertically centered with respect to the bottom of the joist bottom chord.

```
        If false, the stabilizer angle is oriented so that one leg is
        horizontal so that it can support the joist bottom chord.

```

##### Declaration

```
public bool UseVerticalStabilizerAngle { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Only valid if StabilizingMaterial is set to Angle

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FFlushFramedShearSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A flush framed shear connection for joists.

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