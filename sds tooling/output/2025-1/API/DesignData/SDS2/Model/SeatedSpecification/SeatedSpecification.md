# Class SeatedSpecification 

A seated connection

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

SeatedSpecification

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
public sealed class SeatedSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5F%5Fctor)SeatedSpecification()

A seated connection

##### Declaration

```
public SeatedSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FBottomChordEmbed)BottomChordEmbed

The embed plate used for this bearing connection

##### Declaration

```
public Embed BottomChordEmbed { get; set; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FEmbedLocation)EmbedLocation

Specifies the location of an embed plate when the framing situation calls for one.

##### Declaration

```
public EmbedLocation EmbedLocation { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [EmbedLocation](DesignData.SDS2.Setup.EmbedLocation.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FGrade)Grade

The grade to set on the seat material for this connection.

##### Declaration

```
public SteelGrade Grade { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

##### Remarks

Setting this fill flip AutoGrade to false

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FHasRestrainingAngle)HasRestrainingAngle

Specifies whether a restraining angle is used in the connection.

##### Declaration

```
public bool HasRestrainingAngle { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FIsAngleSeatStiffened)IsAngleSeatStiffened

Specifies wheter an angle seat is stiffened

##### Declaration

```
public bool IsAngleSeatStiffened { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FIsAutoGrade)IsAutoGrade

If true, the system determines the seat grade. If false, the value specified in the Grade property will be used.

##### Declaration

```
public bool IsAutoGrade { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FIsJoistBottomChordExtended)IsJoistBottomChordExtended

Specifies whether the bottom chord of a joist is extended to the supporting member

##### Declaration

```
public bool IsJoistBottomChordExtended { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FIsRestrainingAngleOnWeb)IsRestrainingAngleOnWeb

True if the restraining angle is attached to the web of the supporting material. False when the restraining angle is attached to the flange of the supporting material.

##### Declaration

```
public bool IsRestrainingAngleOnWeb { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FJoistBottomChordPlateRestraintErectionHoles)JoistBottomChordPlateRestraintErectionHoles

Specifies whether erection holes are used on joist bottom chord plate restraints

##### Declaration

```
public AutomaticYesNo JoistBottomChordPlateRestraintErectionHoles { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FJoistBottomChordRestraint)JoistBottomChordRestraint

The type of joist bottom chord restraint material.

##### Declaration

```
public SeatSpecificationBottomChordRestraintMaterial JoistBottomChordRestraint { get; set; }
```

##### Property Value

| Type                                                                                                                      | Description |
| ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [SeatSpecificationBottomChordRestraintMaterial](DesignData.SDS2.Model.SeatSpecificationBottomChordRestraintMaterial.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FSeatAttachmentMethod)SeatAttachmentMethod

Specifies how the seat is connected to the supporting member

##### Declaration

```
public AttachmentMethodWithAutomatic SeatAttachmentMethod { get; set; }
```

##### Property Value

| Type                                                                                      | Description |
| ----------------------------------------------------------------------------------------- | ----------- |
| [AttachmentMethodWithAutomatic](DesignData.SDS2.Model.AttachmentMethodWithAutomatic.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FSeatMaterial)SeatMaterial

The type of connection material for the seat

##### Declaration

```
public SeatSpecificationMaterial SeatMaterial { get; set; }
```

##### Property Value

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [SeatSpecificationMaterial](DesignData.SDS2.Model.SeatSpecificationMaterial.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FTopChordEmbed)TopChordEmbed

The embed plate used for this bearing connection

##### Declaration

```
public Embed TopChordEmbed { get; set; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FWashersAllowedOnShoeSlots)WashersAllowedOnShoeSlots

Specifies whether washers are allowed on joist shoe slots.

##### Declaration

```
public AutomaticYesNo WashersAllowedOnShoeSlots { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FSeatedSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A seated connection

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