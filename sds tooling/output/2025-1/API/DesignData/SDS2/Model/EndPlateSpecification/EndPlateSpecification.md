# Class EndPlateSpecification 

An end plate connection

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

EndPlateSpecification

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
public sealed class EndPlateSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5F%5Fctor)EndPlateSpecification()

An end plate connection

##### Declaration

```
public EndPlateSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FAxialLoadCheck)AxialLoadCheck

The "Supporting member web stress (T)" will be reported as a "Left/Right end limit state" when a "Tension" load has been applied to the supported beam's end plate connection end. This option affects whether or not that limit state is incorporated as a check within the system that can potentially cause the end plate connection to fail.

##### Declaration

```
public AxialLoadCheckOption AxialLoadCheck { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [AxialLoadCheckOption](DesignData.SDS2.Model.AxialLoadCheckOption.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FCombineBeamAndVBraceEndPlates)CombineBeamAndVBraceEndPlates

For an angle, W tee or channel vertical brace framing to a beam and column, the system creates an end plate for the gusset-to-column interface if the beam connects to the column with an end plate. This " Connection specifications" option sets whether or not the end plates can be combined into a single end plate.

```
         Automatic specifies that the system apply the choice made to
         Fabricator Setup > Standard Fabricator Connections > End Plate
         Setup > "Combine beam and vertical brace end plates."

         Yes instructs the system to create a single end plate to connect
         both the beam and the vertical brace gusset plate to the column.

         No instructs the system to create two separate end plates, one to
         connect the beam to the column, the other to connect the vertical
         brace gusset plate to the column.

```

##### Declaration

```
public AutomaticYesNo CombineBeamAndVBraceEndPlates { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FExtendToBeamFlanges)ExtendToBeamFlanges

option can apply to a 'Non-moment' end plate on a wide flange or HSS rectangular/tube beam when an axial load ("Tension" or "Compression") has been entered on this end of the beam. The option is also available for non-monent end plates that are specified in Job Setup > User Defined Connections. It does not apply to auto standard connections.

```
         If true, the system attempts to create an end plate that welds to
         the flanges (as well as the web) of the beam. The end plate is
         extended the "Extension dimension" distance above/below the
         top/bottom flanges of the beam.

         If false, the system is instructed to create the end plate so
         that its upper and lower edges are inside the top and bottom
         flanges of the beam.

```

##### Declaration

```
public bool ExtendToBeamFlanges { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FExtensionDimension)ExtensionDimension

The distance the system is instructed to extend the end plate above/below the top/bottom flanges of the beam. For this to apply, ExtendToBeamFlanges must be true.

##### Declaration

```
public double ExtensionDimension { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FIsFullDepthTee)IsFullDepthTee

applies when -- here in " Connection specifications" -- the box is checked for " Welded extended tee."

```
         If true, the system is instructed to a built-up tee that is the
         full depth of the supporting beam.

         If false, the built-up tee is designed to the depth of the end
         plate if the top and bottom flanges of the supported beam (this
         beam) are entirely below or entirely above the half-depth of the
         supporting beam. If the depth of the supported beam is greater
         than half the depth of the supporting beam, the built-up tee is
         designed to the full depth of the supporting beam.

```

##### Declaration

```
public bool IsFullDepthTee { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FIsWeldedExtendedTee)IsWeldedExtendedTee

can apply to a beam with an end plate connection framing perpendicular or sloping or skewed to a supporting beam. "Moment type" must be set to 'Non-moment' in the beam's " Moment" leaf. The option is also available for non-monent end plates that are specified in Job Setup > User Defined Connections or Auto Standard Connections.

```
         If true, the system is instructed to generate a built-up tee (two
         plates welded together) for the end plate to bolt to. For some
         framing situations, the check box for "Full depth extended tee"
         controls whether the tee is designed to the depth of the
         connection or to the full depth of the supporting beam.

         If false, the end plate bolts directly to the supporting beam's
         web.

```

##### Declaration

```
public bool IsWeldedExtendedTee { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FIsWideGage)IsWideGage

true, which is 'wide,' specifies that the system to create a wide gage end plate per the center-to-center distance entered in setup (Fabricator Setup > Standard Fabricator Connections > End Plate Settings > "Center to center holes, wide gage").

```
         false, which is 'narrow,' instructs the system to create a
         narrow gage end plate per the center-to-center distance entered
         in setup (Fabricator Setup > Standard Fabricator Connections >
         End Plate Settings > "Center to center holes, narrow gage").

```

##### Declaration

```
public bool IsWideGage { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FSafetyConnection)SafetyConnection

applies when two beams with end plates frame to opposite sides of a supporting column web (or a beam web). In such a framing situation, the end plates on the two beams will share bolts.

```
         See documentation on enumeration for individual settings

```

##### Declaration

```
public EndPlateSafetyConnection SafetyConnection { get; set; }
```

##### Property Value

| Type                                                                            | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [EndPlateSafetyConnection](DesignData.SDS2.Model.EndPlateSafetyConnection.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FUseExpandedVerticalBoltSpacing)UseExpandedVerticalBoltSpacing

option applies to end plates on beams whose "Moment type" is set to 'Non-moment' in this beam end's " Moment" leaf. The option is also available for non-monent end plates that are specified in Job Setup > User Defined Connections or Auto Standard Connections.

```
         Automatic specifies that the system apply the choice made
         to Fabricator Setup > Standard Fabricator Connections > End Plate
         Setup > "Use expanded vertical bolt spacing."

         Yes instructs the system to expand the vertical spacing of
         bolts to 1.5 times or 2 times the Fabricator Setup > Connection
         Detailing/Fabricator Options > "Bolt spacing" that is set per
         bolt diameter. A spacing other than 1.5 or 2 times the standard
         bolt spacing may be used in order to accommodate piecemarking
         issues, loading conditions and unusual geometries.

         No instructs the system to use the Fabricator Setup >
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

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FUseWebExtensionPlate)UseWebExtensionPlate

can apply to an end plate on a beam framing to a column. Regardless of the choice made here, " Web Extension Plate" the system locks are available. These locks have null values (distances of 0) if a web extehension plate is not required and when 'Never' is specified.

##### Declaration

```
public IfRequiredNever UseWebExtensionPlate { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [IfRequiredNever](DesignData.SDS2.Model.IfRequiredNever.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FEndPlateSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

An end plate connection

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