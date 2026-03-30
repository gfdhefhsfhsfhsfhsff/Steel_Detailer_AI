# Class MemberEndBrief 

The fixed length (rapid access) data on a member.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MemberEndBrief

[MemberEnd](DesignData.SDS2.Model.MemberEnd.html)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class MemberEndBrief
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FCompressionLoad)CompressionLoad

A compression load tends to compress or shorten the member.

```
         An entry of '0' (zero) prevents the system from using compression
         in its calculations for the design of the connection on this end
         of the beam.

         A non-zero load will be combined with the "Compression load"
         entered to the "Gusset Interface Forces" column for use in the
         design of a clip angle or end plate or shear thru plate or
         single-plate shear (shear tab) connection. Before entering a
         load, see the warning.

```

##### Declaration

```
public double CompressionLoad { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FDisableFramingSituationChecks)DisableFramingSituationChecks

When true, prevent the system from performing checks on the framing situation that impact this connection. When false, the system will perform framing situation checks and adjust this connection for erectability purposes.

##### Declaration

```
public bool DisableFramingSituationChecks { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FIsAutoMomentLoad)IsAutoMomentLoad

If true, then the system will calculate a default load based on setup values.

##### Declaration

```
public bool IsAutoMomentLoad { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FIsAutoNonMomentBoltDiameter)IsAutoNonMomentBoltDiameter

If true, then NonMomentBoltDiameter is determined by the system based on setup values. If false, then the user/API must set NonMomentBoltDiameter.

##### Declaration

```
public bool IsAutoNonMomentBoltDiameter { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FIsAutoNonMomentBoltTypeToSupported)IsAutoNonMomentBoltTypeToSupported

If true, then NonMomentBoltTypeToSupported is determined by the system based on setup values. If false, then the user/API must set NonMomentBoltTypeToSupported

##### Declaration

```
public bool IsAutoNonMomentBoltTypeToSupported { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FIsAutoNonMomentBoltTypeToSupporting)IsAutoNonMomentBoltTypeToSupporting

If true, then NonMomentBoltTypeToSupporting is determined by the system based on setup values. If false, then the user/API must set NonMomentBoltTypeToSupporting

##### Declaration

```
public bool IsAutoNonMomentBoltTypeToSupporting { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

This field only applies to beam connections

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FIsAutoPanelMomentLoad)IsAutoPanelMomentLoad

If true, then the system will calculate a default panel moment load based on setup values.

##### Declaration

```
public bool IsAutoPanelMomentLoad { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FIsAutoShearLoad)IsAutoShearLoad

If true, then the system will calculate a default load based on setup values.

##### Declaration

```
public bool IsAutoShearLoad { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FIsAutoTieForce)IsAutoTieForce

If true, then the system will calculate a default load based on setup values.

##### Declaration

```
public bool IsAutoTieForce { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FIsConnectionForced)IsConnectionForced

On a system connection, when true, forces the system to apply a connection, even if it fails during connection design. A solids model will be generated.

##### Declaration

```
public bool IsConnectionForced { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FLocation)Location

The exact location of this member end, in global coordinates.

##### Declaration

```
public Point3D Location { get; set; }
```

##### Property Value

| Type                                               | Description                                   |
| -------------------------------------------------- | --------------------------------------------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | Exact point in global coordinates, in inches. |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FMinimumCopeDepth)MinimumCopeDepth

Automatic specifies that the system create the connection on this end of the beam based on the choice made to Fabricator Setup > Member Detailing Settings > the "Beams" section > "Provide minimum cope depth."

```
        Yes instructs the system to ignore the k distance of the
        supporting member when calculating the depth of the cope. This
        will provide a cope of minimum depth.

        No configures the system to cope the supported beam so
        that it clears the k distance of the supporting member.

```

##### Declaration

```
public AutomaticYesNo MinimumCopeDepth { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FMinimumSetupConnection)MinimumSetupConnection

If all loads are set to auto, then the auto loads will match the capacity of the connection instead of the allowable loads

##### Declaration

```
public AutomaticYesNo MinimumSetupConnection { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FMomentLoad)MomentLoad

The moment entered here is used in the design of the connection on this end of the beam if " Moment" settings have been applied. This option is disabled (grayed-out) when the "Moment type" for this end is set to 'Non-moment,' unless the "User defined connection" for this end is a moment connection, for which case this field is enabled (editable). For moment splice plates, connection design attempts to synchronize the moment load on each of the two beams being spliced so that each load is the same value. If one beam has an 'Auto' moment load and the other beam has a user-entered moment load, the load on both beam are set equal to the user-entered "Moment load." If both beams have user-entered moment loads and those loads are not the same, the connection fails.

##### Declaration

```
public double MomentLoad { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

This can always be read, but can only be set if AutoMomentLoad is false.

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FNonMomentBoltDiameter)NonMomentBoltDiameter

The diameter of bolts to use when there is no moment

##### Declaration

```
public double NonMomentBoltDiameter { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FNonMomentBoltTypeToSupported)NonMomentBoltTypeToSupported

The type of bolt to use, when there is no moment, to fasten connection material to this (the supported) member

##### Declaration

```
public BoltType NonMomentBoltTypeToSupported { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FNonMomentBoltTypeToSupporting)NonMomentBoltTypeToSupporting

The type of bolt to use, when there is no moment, to fasten connection material to the supporting member.

##### Declaration

```
public BoltType NonMomentBoltTypeToSupporting { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FPanelMomentLoad)PanelMomentLoad

If true, panel moment load is determined by this system. Only applies to seismic frame members. If it is not seismic, the moment load and panel moment load are the same. When framing to another beam, this value will be 0\. If it is a standard moment connection to a column, this value is disabled, and the panel moment load is the same as the moment load.

##### Declaration

```
public double PanelMomentLoad { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

This can always be read, but can only be set if AutoPanelMomentLoad is false.

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FShearLoad)ShearLoad

The shear end reaction entered here -- under " Loads" -- will be combined with the "Shear load" entered to the "Gusset Interface Forces" column and then will used in the design of the "System designed connection" on this end of the beam.

##### Declaration

```
public double ShearLoad { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

This can always be read, but can only be set if AutoShearLoad is false.

```
         For beam splices, connection design attempts to synchronize the
         shear load on each of the two beams being spliced so that each
         load is the same value. If one beam has an 'Auto' shear load and
         the other beam has a user-entered shear load, the load on both
         beam are set equal to the user-entered "Shear load."  If both
         beams have user-entered shear loads and those loads are not the
         same, the connection fails.

```

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FStoryShearLoad)StoryShearLoad

only valid for moment connections.

```
         An entry of '0' (zero) prevents the system from using story load
         in its calculations for moment connections on this end of the
         beam.

         A non-zero applies to the design of the connection on this end of
         a beam if this end of the beam frames to a column flange and "
         Moment" options have been applied.

```

##### Declaration

```
public double StoryShearLoad { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FTensionLoad)TensionLoad

A tension load tends to stretch a member in the direction of its length.

```
         An entry of '0' (zero) prevents the system from using tension in
         its calculations for the design of the connection on this end of
         the beam.

         A non-zero load will be combined with the "Tension load" entered
         to the "Gusset Interface Forces" column for use in the design of
         a clip angle or end plate or shear thru plate or single-plate
         shear (shear tab) connection. Before entering a load, see the
         warning.

```

##### Declaration

```
public double TensionLoad { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FTieForce)TieForce

This " Loads" option is available for most "Connection design methods."

```
         An entry of '0' (zero) prevents the system from using the tying
         force to check the structural integrity of the connection on this
         end of the beam.

         A non-zero load instructs connection design to use this tying
         force to check the structural integrity of the connection on this
         end of the beam, as required by Section 1615 of the International
         Building Code (2015) for high-rise buildings.

```

##### Declaration

```
public double TieForce { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

This can always be read, but can only be set if AutoTieForce is false.

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FUseMiscPlatesList)UseMiscPlatesList

If true, the sytem looks to the appropriate section in Fabricator Setup > Standard Fabricator Connections > Plates to determine the plate thicknesses to be used for end plates, shear plates, beam web doublers, column web doubler plates for moment connections, column stiffeners for moment connections, flange plates for bolted or welded moment connections, plates used for extended tees, web extension plates for extended clip angles, bent plates, plate seats, stiffeners for angle seats and splice plates. First the system calculates the thickness of the plate required to stand up to the load, then it chooses a plate from the list that is the calculated required thickness or the next thicker. If the plate from the list results in material interferences or too narrow a clearance or a thickness outside of AISC guidelines, the system fails the connection and gives you the failure message, "Suitable plate thickness not found."

```
        If false, the system rounds the calculated required thickness of
        plates as based on the load to the next 1/16 inch (or 1/8 inch if
        the calculated required thickness is greater than 5/16 inch).

```

##### Declaration

```
public bool UseMiscPlatesList { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

The fixed length (rapid access) data on a member.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FFinalize)\~MemberEndBrief()

The fixed length (rapid access) data on a member.

##### Declaration

```
protected ~MemberEndBrief()
```

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FGetAutoCompPermanent)GetAutoCompPermanent()

If true, then the system will calculate a default load based on setup values.

##### Declaration

```
public bool GetAutoCompPermanent()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FGetCompPermanent)GetCompPermanent()

The fixed length (rapid access) data on a member.

##### Declaration

```
public double GetCompPermanent()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FSetAutoCompPermanent%5FSystem%5FBoolean%5F)SetAutoCompPermanent(bool)

The fixed length (rapid access) data on a member.

##### Declaration

```
public void SetAutoCompPermanent(bool automatic)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | automatic |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndBrief%5FSetCompPermanent%5FSystem%5FDouble%5F)SetCompPermanent(double)

The fixed length (rapid access) data on a member.

##### Declaration

```
public void SetCompPermanent(double load)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | load |             |