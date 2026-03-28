# Class HorzBracePlateSpecification 

A specification for connecting a horizontal brace to one or more supporting members via a gusset plate and possibly clip angles.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

HorzBracePlateSpecification

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
public sealed class HorzBracePlateSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5F%5Fctor)HorzBracePlateSpecification()

A specification for connecting a horizontal brace to one or more supporting members via a gusset plate and possibly clip angles.

##### Declaration

```
public HorzBracePlateSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FAngleAttachment)AngleAttachment

Specifies how the end of a single angle brace is attached to the gusset plate.

##### Declaration

```
public AttachmentMethod AngleAttachment { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [AttachmentMethod](DesignData.SDS2.Model.AttachmentMethod.html) |             |

##### Remarks

Applies for single angle braces. Double angles will be bolted.

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FAttachClipTo)AttachClipTo

Specifies what to attach clip connections to.

##### Declaration

```
public AutoGussetSupporting AttachClipTo { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [AutoGussetSupporting](DesignData.SDS2.Model.AutoGussetSupporting.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FBalancedWelds)BalancedWelds

Specifies whether the welds connecting a brace to the gussest are balanced.

##### Declaration

```
public AutomaticYesNo BalancedWelds { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

##### Remarks

Only applies when the brace is welded to the gusset plate.

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FBeamToClip)BeamToClip

Specifies the type of connection used for beam-to-clip.

##### Declaration

```
public BeamToClipAttachmentMethod BeamToClip { get; set; }
```

##### Property Value

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [BeamToClipAttachmentMethod](DesignData.SDS2.Model.BeamToClipAttachmentMethod.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FClipAngleBoltDiameter)ClipAngleBoltDiameter

Specifies the bolt diameter, in inches, for the bolts involved in connecting the clip angle to the supporting member and the brace gusset plate is using the value defined in setup.

##### Declaration

```
public double ClipAngleBoltDiameter { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FClipAngleBoltStagger)ClipAngleBoltStagger

Specifies if the bolts on the two legs of a clip angle connecting the supporting member and the brace gusset plate are staggered.

##### Declaration

```
public AutomaticYesNo ClipAngleBoltStagger { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FClipAngleBoltType)ClipAngleBoltType

Specifies the bolt type for the bolts involved in connecting the clip angle to the supporting member and the brace gusset plate.

##### Declaration

```
public BoltType ClipAngleBoltType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FClipAngleLocation)ClipAngleLocation

Specifies the location of the clip angle connecting a gusset plate the supporting member.

##### Declaration

```
public BothNearFar ClipAngleLocation { get; set; }
```

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [BothNearFar](DesignData.SDS2.Model.BothNearFar.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FClipAngleLongLegTo)ClipAngleLongLegTo

Specifies the long leg orientation of the clip angle connecting the gusset plate to the supporting member(s).

##### Declaration

```
public AutoSupportingSupported ClipAngleLongLegTo { get; set; }
```

##### Property Value

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [AutoSupportingSupported](DesignData.SDS2.Model.AutoSupportingSupported.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FClipAngleShape)ClipAngleShape

Specifies the clip angle shape for connecting a gusset plate and the supporting member when IsAutoClipAngleShape is False.

##### Declaration

```
public AngleShape ClipAngleShape { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [AngleShape](DesignData.SDS2.Setup.AngleShape.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FClipAngleSupportedHoleType)ClipAngleSupportedHoleType

Specifies the hole type on the leg of the clip angle connecting the gusset plate to the supported member.

##### Declaration

```
public ConnSpecHoleTypeSubset ClipAngleSupportedHoleType { get; set; }
```

##### Property Value

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [ConnSpecHoleTypeSubset](DesignData.SDS2.Model.ConnSpecHoleTypeSubset.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FClipAngleSupportingHoleType)ClipAngleSupportingHoleType

Specifies the hole type on the leg of the clip angle connecting the gusset plate to the supporting member.

##### Declaration

```
public ConnSpecHoleTypeSubset ClipAngleSupportingHoleType { get; set; }
```

##### Property Value

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [ConnSpecHoleTypeSubset](DesignData.SDS2.Model.ConnSpecHoleTypeSubset.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FClipAnglesAttachment)ClipAnglesAttachment

Specifies how the gusset plate is attached to the clip angles when a the gusset plate is bolted to the supporting member(s).

##### Declaration

```
public AttachmentMethodWithAutomatic ClipAnglesAttachment { get; set; }
```

##### Property Value

| Type                                                                                      | Description |
| ----------------------------------------------------------------------------------------- | ----------- |
| [AttachmentMethodWithAutomatic](DesignData.SDS2.Model.AttachmentMethodWithAutomatic.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FClipEndOperation)ClipEndOperation

Specifies if the corner of the gusset plate connected to the brace is clipped.

##### Declaration

```
public AutomaticYesNo ClipEndOperation { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

##### Remarks

Only applies to certain brace types, e.g angle, tee, and wide flange.

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FErectionBolt)ErectionBolt

Specifies the number of erection bolts used to connect a welded hss section to the gusset plate.

##### Declaration

```
public ErectionBoltSpecification ErectionBolt { get; set; }
```

##### Property Value

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [ErectionBoltSpecification](DesignData.SDS2.Model.ErectionBoltSpecification.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FGrade)Grade

The grade to set on the plate material for this connection.

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

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FGussetCut)GussetCut

The end cut for the corner of the gusset plate that meets at the supporting member(s).

##### Declaration

```
public AutoClipCope GussetCut { get; set; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [AutoClipCope](DesignData.SDS2.Model.AutoClipCope.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FGussetToBeamAndEndPlate)GussetToBeamAndEndPlate

Specifies whether gusset can weld to beam web and end plate in a Europoean job.

##### Declaration

```
public AutomaticYesNo GussetToBeamAndEndPlate { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FHssAttachment)HssAttachment

Specifies how the end of a hss brace is attached to the gusset plate.

##### Declaration

```
public HorzBraceHssAttachmentMethod HssAttachment { get; set; }
```

##### Property Value

| Type                                                                                    | Description |
| --------------------------------------------------------------------------------------- | ----------- |
| [HorzBraceHssAttachmentMethod](DesignData.SDS2.Model.HorzBraceHssAttachmentMethod.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FIncludeEndWeld)IncludeEndWeld

Specifies whether an additional weld is applied to the end of a brace that runs perpendicular to the longitudinal axis of the brace.

##### Declaration

```
public AutomaticYesNo IncludeEndWeld { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

##### Remarks

Only applies when the brace is welded to the gusset plate.

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FIsAutoClipAngleBoltDiameter)IsAutoClipAngleBoltDiameter

Specifies if the bolt diameter for the bolts involved in connecting the clip angle to the supporting member and the brace gusset plate is using the value defined in setup.

##### Declaration

```
public bool IsAutoClipAngleBoltDiameter { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FIsAutoClipAngleBoltType)IsAutoClipAngleBoltType

Specifies if the bolt type for the bolts involved in connecting the clip angle to the supporting member and the brace gusset plate is using the value defined in setup.

##### Declaration

```
public bool IsAutoClipAngleBoltType { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FIsAutoClipAngleLocation)IsAutoClipAngleLocation

Specifies whether the location of the clip angle connecting a gusset plate to the supporting member(s) is based on setup.

##### Declaration

```
public bool IsAutoClipAngleLocation { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FIsAutoClipAngleShape)IsAutoClipAngleShape

Specifies whether the clip angle shape connecting a gusset plate to the supporting member(s) is based on setup.

##### Declaration

```
public bool IsAutoClipAngleShape { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FIsAutoClipAngleSupportedHoleType)IsAutoClipAngleSupportedHoleType

Specifies if the hole type on the leg of the clip angle connecting the gusset plate to the supported member is determined by setup.

##### Declaration

```
public bool IsAutoClipAngleSupportedHoleType { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FIsAutoClipAngleSupportingHoleType)IsAutoClipAngleSupportingHoleType

Specifies if the hole type on the leg of the clip angle connecting the gusset plate to the supporting member is determined by setup.

##### Declaration

```
public bool IsAutoClipAngleSupportingHoleType { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FIsAutoGrade)IsAutoGrade

If true, the system determines the plate grade. If false, the value specified in the Grade property will be used.

##### Declaration

```
public bool IsAutoGrade { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FNotchClearance)NotchClearance

Specifies the distance, in inches, that the notch on a welded hss section extends past the gusset plate.

##### Declaration

```
public double NotchClearance { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FSupportingAttachment)SupportingAttachment

Specifies how the gusset plate is attached to the supporting member(s).

##### Declaration

```
public AttachmentMethodWithAutomatic SupportingAttachment { get; set; }
```

##### Property Value

| Type                                                                                      | Description |
| ----------------------------------------------------------------------------------------- | ----------- |
| [AttachmentMethodWithAutomatic](DesignData.SDS2.Model.AttachmentMethodWithAutomatic.html) |             |

##### Remarks

Some values do not apply in certain situations. For example, Welded does not apply when connecting to the web of two beams. See SDS2's help on horizontal brace connections for more information.

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FSupportingMemberWebStressCheck)SupportingMemberWebStressCheck

Specifies how the limit state is incorporated as a check within connection design that can potentially cause the connection to fail.

##### Declaration

```
public IfRequiredNever SupportingMemberWebStressCheck { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [IfRequiredNever](DesignData.SDS2.Model.IfRequiredNever.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FUseOversizedHoles)UseOversizedHoles

Specifies whether oversized round holes should be used for the brace-to-gusset interface.

##### Declaration

```
public bool UseOversizedHoles { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

As per AISC guidelines, connection design will use slip critical bolts for oversized holes

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FHorzBracePlateSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A specification for connecting a horizontal brace to one or more supporting members via a gusset plate and possibly clip angles.

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