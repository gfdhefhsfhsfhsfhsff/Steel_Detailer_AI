# Class ClipAngleSpecification 

A clip angle connection

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

ClipAngleSpecification

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
public sealed class ClipAngleSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5F%5Fctor)ClipAngleSpecification()

A clip angle connection

##### Declaration

```
public ClipAngleSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FAttachToMember)AttachToMember

How to attach the connection to the supporting member

##### Declaration

```
public AttachToMember AttachToMember { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AttachToMember](DesignData.SDS2.Model.AttachToMember.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FAttachmentMethodToSupported)AttachmentMethodToSupported

How to attach the connection to the beam being supported

##### Declaration

```
public AttachmentMethod AttachmentMethodToSupported { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [AttachmentMethod](DesignData.SDS2.Model.AttachmentMethod.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FAttachmentMethodToSupporting)AttachmentMethodToSupporting

How to attach the connection to the supporting member

##### Declaration

```
public AttachmentMethod AttachmentMethodToSupporting { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [AttachmentMethod](DesignData.SDS2.Model.AttachmentMethod.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FCombineBeamAndVBraceClipAngles)CombineBeamAndVBraceClipAngles

applies when this end of this beam has a clip angle connection and a vertical brace frames to this beam and to the same column that this beam frames to. In such a framing situation, connection design can create one or two pairs of clip angles.

```
         Automatic specifies that connection design apply the choice made
         to Fabricator Setup > Standard Fabricator Connections > Clip
         Angle Setup > "Combine beam and vertical brace clip angles."

         Yes instructs connection design to create a single pair of clip
         angles that connects both the beam and vertical brace gusset
         plate to the column. The clip angles use the "NM bolt diameter"
         and "NM bolt type to supported" and "NM bolt type to supporting"
         that are set for the beam.

         No instructs connection design to create two separate pairs of
         clip angles, one pair to connect the beam to the column, the
         other pair to connect the vertical brace gusset plate to the
         column.

```

##### Declaration

```
public AutomaticYesNo CombineBeamAndVBraceClipAngles { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FCreateWebDoublers)CreateWebDoublers

Forces a connection to have no web doublers, otherwise create them if necessary.

##### Declaration

```
public AutomaticYesNo CreateWebDoublers { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FEmbedLocation)EmbedLocation

can apply when a beam frames to a concrete wall and the beam's "Input connection type" is 'Clip angle' and an "Embed schedule entry" has been made in the " Connection type" leaf. The option can also be found in Job Setup > Auto Standard Connections and in Job Setup > User Defined Connections.

```
        Automatic instructs connection design to apply the choice made to
        Concrete Setup > Embed Schedule > "Plate location."

        InsideWall embeds the plate in the concrete wall.

        OutsideWall locates the plate flush to the wall.

```

##### Declaration

```
public EmbedLocation EmbedLocation { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [EmbedLocation](DesignData.SDS2.Setup.EmbedLocation.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FExtendPastFlange)ExtendPastFlange

can apply to a clip angle on a beam framing to a column. Regardless of the choice made here, " Web Extension Plate" the system locks are available. These locks have null values (distances of 0) if a web extehension plate is not required and when 'Never' is specified.

##### Declaration

```
[Obsolete("Model.ClipAngleSpecification.ExtendPastFlange renamed to UseWebExtensionPlate", false)]
public IfRequiredNever ExtendPastFlange { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [IfRequiredNever](DesignData.SDS2.Model.IfRequiredNever.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FFlangePlatesOn)FlangePlatesOn

applies only for moment connections.

```
         This specifies which of the two connections that share flange
         plates will get the plates.  Either the beam where the connection
         is on the right end, or the beam where the connection is on the
         left end.  Both connections should have the same value for
         this.

```

##### Declaration

```
public RightOrLeftEnd FlangePlatesOn { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [RightOrLeftEnd](DesignData.SDS2.Model.RightOrLeftEnd.html) |             |

##### Remarks

This does not take swapped member ends into account

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FGage)Gage

Specify whether this is a heavy, wide, or narrow gage clip

##### Declaration

```
public ClipAngleGage Gage { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ClipAngleGage](DesignData.SDS2.Model.ClipAngleGage.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FIsFullDepthTee)IsFullDepthTee

If true, the system creates a built-up tee that is the full depth of the supporting beam.

```
         If false, the built-up tee is designed to the depth of the
         connection if the top and bottom flanges of the supported beam
         (this beam) are entirely below or entirely above the half-depth
         of the supporting beam. If the depth of the supported beam is
         greater than half the depth of the supporting beam, the built-up
         tee is designed to the full depth of the supporting beam.

```

##### Declaration

```
public bool IsFullDepthTee { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FIsWeldedExtendedTee)IsWeldedExtendedTee

can apply to a wide flange, welded plate wide flange or channel beam with a clip angle connection framing perpendicular or sloping to a supporting beam.

```
         If true, generates a built-up tee (two plates welded together)
         for the clip angles to bolt to. The check box for "Full depth
         extended tee" controls (for some framing situations) whether the
         tee will be designed to the depth of the connection or to the
         full depth of the supporting beam.

```

##### Declaration

```
public bool IsWeldedExtendedTee { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FReplaceDoublerWithLargerClip)ReplaceDoublerWithLargerClip

If true, and web doublers are required, connection design looks for an angle in Fabricator Setup > Standard Fabricator Connections > Angles. If an angle is not found, the system fails the connection, and the Beam Edit window displays the following failure message: Option to replace web doubler with large clip L fails.

##### Declaration

```
public bool ReplaceDoublerWithLargerClip { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FSide)Side

Which side of the supported member to put clip angles on, or both.

##### Declaration

```
public ClipAngleSide Side { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ClipAngleSide](DesignData.SDS2.Model.ClipAngleSide.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FSkewHolesInAngle)SkewHolesInAngle

applies to bolted clip angles on sloping beams when the box is checked for Fabricator Setup > Member Detailing Settings. > the "Beams" section > " Square cut ends of sloped beams."

```
         Automatic specifies that connection design apply the choice made
         to Fabricator Setup > Standard Fabricator Connections > Clip
         Angle Setup > "Skew holes in clip angles."


         Yes instructs the system to create clip angles with bolts
         skewed in the leg to the supported beam's web so that the bolts
         run perpendicular to the beam's flanges.

         No instructs the system to create clip angles with bolts that run
         parallel to the length of the angle.

```

##### Declaration

```
public AutomaticYesNo SkewHolesInAngle { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FStagger)Stagger

See documentation on the returned ClipAngleStagger enumeration

##### Declaration

```
public ClipAngleStagger Stagger { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [ClipAngleStagger](DesignData.SDS2.Model.ClipAngleStagger.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FUseErectionBolts)UseErectionBolts

applies when both "Attachment to supported" and "Attachment to supporting" are set to 'Welded.' In other words, it applies to all-welded clip angles.

```
         Automatic specifies that connection design apply the choice made
         to Fabricator Setup > Standard Fabricator Connections > Attached
         to Supporting Member > "Provide erection bolts" If "Attached to"
         (on this window) is set to 'Supporting.' If "Attached to" is set
         to 'Supported,' then connection design applies the choice made to
         Fabricator Setup > Standard Fabricator Connections > Attached to
         Supported Member > "Provide erection bolts."

         Yes instructs connection design to design the welded-welded
         double clip angle connection with erection bolts to facilitate
         the field welding of the connection. The erection bolts are field
         bolts. For a beam end connection that is not auto standard, the
         bolts are the " Connection type" > "NM bolt type to supporting"
         (or "NM bolt type to supported") and "NM bolt diameter" that are
         specified for that beam connection's end. For an auto standard
         beam connection, the bolts are the "NM bolt type" and "NM bolt
         diameter" that are specified for the relevant framing condition
         in Fabricator Setup > Auto Standard Connections. If the
         welded-welded clip angle shop welds to the supporting, two
         erection bolts are provided. If it shop welds to the supported,
         four erection bolts are provided, two for the NS OSL, two for the
         FS OSL.

         No instructs connection design to design the welded-welded double
         clip angle without erection bolts.

```

##### Declaration

```
public AutomaticYesNo UseErectionBolts { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FUseExpandedVerticalBoltSpacing)UseExpandedVerticalBoltSpacing

can apply to a beam with clip angles to a beam or column so long as the "Moment type" is set to 'Non-moment' in the beam end's " Moment" leaf.

```
         Automatic specifies that connection design apply the choice made
         to Fabricator Setup > Standard Fabricator Connections > Clip
         Angle Setup > "Use expanded vertical bolt spacing."

         Yes permits connection design to expand the vertical spacing of
         bolts to 1.5 times or 2 times the Fabricator Setup > Connection
         Detailing/Fabricator Options > "Bolt spacing" that is set per
         bolt diameter. The program may also adjust to a spacing other
         than 1.5 or 2 times the standard bolt spacing in order to
         accommodate piecemarking issues, loading conditions and unusual
         geometries.

         No instructs connection design to use the Fabricator Setup >
         Connection Erectability Settings > "Bolt spacing" that is
         set per bolt diameter.

```

##### Declaration

```
public AutomaticYesNo UseExpandedVerticalBoltSpacing { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FUsePaddlePlate)UsePaddlePlate

applies when an HSS/TS beam frames to a column or a beam. It permits the design of bolted-bolted or bolted-welded clip angles. The option is disabled (grayed out) when -- here in " Connection specifications" -- the clip angle's "Attachment to supported" is set to 'Welded.'

```
         If true, the clip angles weld or bolt to the supporting member
         and bolt to the paddle plate, which shop welds to the supported
         beam. The end of the supported beam is notched for insertion of
         the paddle plate.

         If false, the clip angles attach to the outside walls of the
         supported HSS rectangular beam.

```

##### Declaration

```
public bool UsePaddlePlate { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FUseSafetyConnection)UseSafetyConnection

applies to clip angles on two opposing beams on opposite sides of a supporting web (beam or column) so that the clip angle connections on both supported beams share bolts.

```
         If true, specifies that the clip angles be designed so that one
         bolt on each angle is shared by the beam and column but not
         shared by the clip angle of the opposing beam. Whether the clip
         angles on a beam are vertically offset with respect to the angles
         on the opposing beam or staggered with respect to each other
         depends on the choice made to Fabricator Setup > Clip Angle Settings
         > "Safety connection angles."

```

##### Declaration

```
public bool UseSafetyConnection { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FUseWebExtensionPlate)UseWebExtensionPlate

can apply to a clip angle on a beam framing to a column. Regardless of the choice made here, " Web Extension Plate" the system locks are available. These locks have null values (distances of 0) if a web extehension plate is not required and when 'Never' is specified.

##### Declaration

```
public IfRequiredNever UseWebExtensionPlate { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [IfRequiredNever](DesignData.SDS2.Model.IfRequiredNever.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FClipAngleSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A clip angle connection

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