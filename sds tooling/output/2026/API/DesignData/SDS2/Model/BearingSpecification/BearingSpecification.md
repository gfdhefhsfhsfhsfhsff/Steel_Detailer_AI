# Class BearingSpecification 

A bearing connection specification

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

BearingSpecification

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
public sealed class BearingSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5F%5Fctor)BearingSpecification()

A bearing connection specification

##### Declaration

```
public BearingSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5FAllowWashersOnShoeSlots)AllowWashersOnShoeSlots

If Yes, then allow long slot holes to be added to the plates on the joist. If Automatic, then this is determined by settings in setup

##### Declaration

```
public AutomaticYesNo AllowWashersOnShoeSlots { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5FBottomChordEmbed)BottomChordEmbed

The embed plate used for this bearing connection

##### Declaration

```
public Embed BottomChordEmbed { get; set; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5FBottomChordEmbedLocation)BottomChordEmbedLocation

Automatic specifies that the system apply a setup choice (Concrete Setup > Embed Schedule > "Plate location"). That setup choice sets whether the plate is located inside the concrete wall or flush to the surface of the wall.

```
         InsideWall embeds the plate in the concrete wall or tilt-up panel.

         OutsideWall locates the plate flush to the wall or panel.

```

##### Declaration

```
public EmbedLocation BottomChordEmbedLocation { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [EmbedLocation](DesignData.SDS2.Setup.EmbedLocation.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5FChordToSupport)ChordToSupport

Bolted instructs the system to add holes and bolts to the beam flange for bolting the joist to the flange. The holes are included on the beam's member detail. The bolts can be included on Field Bolt reports and, optionally, on the beam's bill of material. The "Input elevation" of the joist must be the elevation of the beam's top flange in order for holes to be generated. The distance between the two holes is the "Top chord gage" entered in the local material file. The choice made to "Wide flange beams, alternative gage for joist connections" or "Channel beams, alternative gage for joist connections" in Fabricator Setup > Standard Fabricator Connections > Joist Setup set the placement of the holes with respect to the center of the beam web. Hole size is set using the "NM bolt diameter" in the " Connection type" leaf on this window.

```
        Welded sets the joist to be field welded. A 3D field weld is not
        generated. The design calculations note, "Joist end welded to
        supporting member."

```

##### Declaration

```
public AttachmentMethod ChordToSupport { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [AttachmentMethod](DesignData.SDS2.Model.AttachmentMethod.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5FExtendBottomChord)ExtendBottomChord

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

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5FStabilizingMaterial)StabilizingMaterial

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

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5FTopChordEmbed)TopChordEmbed

The embed plate used for this bearing connection

##### Declaration

```
public Embed TopChordEmbed { get; set; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5FUseErectionHole)UseErectionHole

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

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5FUseVerticalStabilizerAngle)UseVerticalStabilizerAngle

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

#### [](#DesignData%5FSDS2%5FModel%5FBearingSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A bearing connection specification

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