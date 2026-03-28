# Class VertBracePlateSpecification 

A specification for connecting a vertical brace to one or more supporting members via a gusset plate and possibly clip angles.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

VertBracePlateSpecification

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
public sealed class VertBracePlateSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5F%5Fctor)VertBracePlateSpecification()

A specification for connecting a vertical brace to one or more supporting members via a gusset plate and possibly clip angles.

##### Declaration

```
public VertBracePlateSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FAISC1stEdition2ptGussets)AISC1stEdition2ptGussets

Specifies AISC 1st edition 2 point gussets.

##### Declaration

```
public AutomaticYesNo AISC1stEdition2ptGussets { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FAngleAttachment)AngleAttachment

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

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FBalancedWelds)BalancedWelds

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

Applies when a non HSS brace is welded to the gusset plate.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FBeamClipSize)BeamClipSize

Specifies how the clip angle is sized when a vertical brace connects to a column and beam with a clip angle attachment.

##### Declaration

```
public VertBraceBeamClipSizeSpecification BeamClipSize { get; set; }
```

##### Property Value

| Type                                                                                                | Description |
| --------------------------------------------------------------------------------------------------- | ----------- |
| [VertBraceBeamClipSizeSpecification](DesignData.SDS2.Model.VertBraceBeamClipSizeSpecification.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FClipAngleBoltDiameter)ClipAngleBoltDiameter

Specifies the bolt diameter, in inches, for the bolts involved in connecting the clip angle to the supporting member and the brace gusset plate is using the value defined in setup.

##### Declaration

```
public double ClipAngleBoltDiameter { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FClipAngleBoltStagger)ClipAngleBoltStagger

Specifies if the bolts on the two legs of a clip angle connecting the supporting member and the brace gusset plate are staggered.

##### Declaration

```
public AutomaticYesNo ClipAngleBoltStagger { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FClipAngleBoltType)ClipAngleBoltType

Specifies the bolt type for the bolts involved in connecting the clip angle to the supporting member and the brace gusset plate.

##### Declaration

```
public BoltType ClipAngleBoltType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FClipAngleLongLegTo)ClipAngleLongLegTo

Specifies the long leg orientation of the clip angle connecting the gusset plate to the supporting member(s).

##### Declaration

```
public AutoSupportingSupported ClipAngleLongLegTo { get; set; }
```

##### Property Value

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [AutoSupportingSupported](DesignData.SDS2.Model.AutoSupportingSupported.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FClipAngleShape)ClipAngleShape

Specifies the clip angle shape for connecting a gusset plate and the supporting member when IsAutoClipAngleShape is False.

##### Declaration

```
public AngleShape ClipAngleShape { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [AngleShape](DesignData.SDS2.Setup.AngleShape.html) |             |

##### Remarks

See SDS2's help on vertical brace connections for more information.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FClipAngleSupportedHoleType)ClipAngleSupportedHoleType

Specifies the hole type on the leg of the clip angle connecting the gusset plate to the supported member.

##### Declaration

```
public ConnSpecHoleTypeSubset ClipAngleSupportedHoleType { get; set; }
```

##### Property Value

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [ConnSpecHoleTypeSubset](DesignData.SDS2.Model.ConnSpecHoleTypeSubset.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FClipAngleSupportingHoleType)ClipAngleSupportingHoleType

Specifies the hole type on the leg of the clip angle connecting the gusset plate to the supporting member.

##### Declaration

```
public ConnSpecHoleTypeSubset ClipAngleSupportingHoleType { get; set; }
```

##### Property Value

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [ConnSpecHoleTypeSubset](DesignData.SDS2.Model.ConnSpecHoleTypeSubset.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FClipAnglesAttachment)ClipAnglesAttachment

Specifies how the clip angles attatch to the gusset plate when the gusset plate bolts to the supporting member(s).

##### Declaration

```
public AttachmentMethodWithAutomatic ClipAnglesAttachment { get; set; }
```

##### Property Value

| Type                                                                                      | Description |
| ----------------------------------------------------------------------------------------- | ----------- |
| [AttachmentMethodWithAutomatic](DesignData.SDS2.Model.AttachmentMethodWithAutomatic.html) |             |

##### Remarks

See SDS2's help on vertical brace connections for more information.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FClipEndOperation)ClipEndOperation

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

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FErectionBolt)ErectionBolt

Specifies the number of erection bolts used to connect a welded HSS section to the gusset plate.

##### Declaration

```
public ErectionBoltSpecification ErectionBolt { get; set; }
```

##### Property Value

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [ErectionBoltSpecification](DesignData.SDS2.Model.ErectionBoltSpecification.html) |             |

##### Remarks

Applies to welded HSS brace connections.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FGageOnSupporting)GageOnSupporting

Specifies the center-to-center dimension between columns of holes on the outstanding legs of clip angles.

##### Declaration

```
public double GageOnSupporting { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Applies when IsAutoGageOnSupporting is false. Does not apply when the brace frames to a column and beam. If the specified gage does not work, e.g. 0, the system will determine a correct gage. See SDS2 help on vertical brace connections for more information.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FGrade)Grade

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

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FHssAttachment)HssAttachment

Specifies how a HSS brace attaches to the gusset plate.

##### Declaration

```
public VertBraceHssAttachmentMethod HssAttachment { get; set; }
```

##### Property Value

| Type                                                                                    | Description |
| --------------------------------------------------------------------------------------- | ----------- |
| [VertBraceHssAttachmentMethod](DesignData.SDS2.Model.VertBraceHssAttachmentMethod.html) |             |

##### Remarks

Applies to HSS braces.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FIncludeEndWeld)IncludeEndWeld

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

Applies when a non HSS brace is welded to the gusset plate.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FIsAutoClipAngleBoltDiameter)IsAutoClipAngleBoltDiameter

Specifies if the bolt diameter for the bolts involved in connecting the clip angle to the supporting member and the brace gusset plate is using the value defined in setup.

##### Declaration

```
public bool IsAutoClipAngleBoltDiameter { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FIsAutoClipAngleBoltType)IsAutoClipAngleBoltType

Specifies if the bolt type for the bolts involved in connecting the clip angle to the supporting member and the brace gusset plate is using the value defined in setup.

##### Declaration

```
public bool IsAutoClipAngleBoltType { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FIsAutoClipAngleShape)IsAutoClipAngleShape

Specifies whether the clip angle shape connecting a gusset plate to the supporting member(s) is based on setup.

##### Declaration

```
public bool IsAutoClipAngleShape { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FIsAutoClipAngleSupportedHoleType)IsAutoClipAngleSupportedHoleType

Specifies if the hole type on the leg of the clip angle connecting the gusset plate to the supported member is determined by setup.

##### Declaration

```
public bool IsAutoClipAngleSupportedHoleType { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FIsAutoClipAngleSupportingHoleType)IsAutoClipAngleSupportingHoleType

Specifies if the hole type on the leg of the clip angle connecting the gusset plate to the supporting member is determined by setup.

##### Declaration

```
public bool IsAutoClipAngleSupportingHoleType { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FIsAutoGageOnSupporting)IsAutoGageOnSupporting

Specifies whether setup determines the center-to-center dimension between columns of holes on the outstanding legs of clip angles or whether this specification does.

##### Declaration

```
public bool IsAutoGageOnSupporting { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FIsAutoGrade)IsAutoGrade

If true, the system determines the plate grade. If false, the value specified in the Grade property will be used.

##### Declaration

```
public bool IsAutoGrade { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FIsAutoUFMSpecialCase2PercentTransfer)IsAutoUFMSpecialCase2PercentTransfer

Specifies whether setup determines the UFM special case 2 transfer percent.

##### Declaration

```
public bool IsAutoUFMSpecialCase2PercentTransfer { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FNotchClearance)NotchClearance

Specifies the distance, in inches, that the notch on a welded HSS section extends past the gusset plate.

##### Declaration

```
public double NotchClearance { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Applies to non bolted HSS brace connections.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FSupportingAttachment)SupportingAttachment

Specifies how the gusset plate is attached to the supporting member(s).

##### Declaration

```
public VertBraceSupportingAttachmentMethod SupportingAttachment { get; set; }
```

##### Property Value

| Type                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------- | ----------- |
| [VertBraceSupportingAttachmentMethod](DesignData.SDS2.Model.VertBraceSupportingAttachmentMethod.html) |             |

##### Remarks

Some values do not apply in certain situations. See SDS2's help on vertical brace connections for more information.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FSupportingMemberFlangeBendingCheck)SupportingMemberFlangeBendingCheck

Specifies how the limit state is incorporated as a check within connection design that can potentially cause the connection to fail.

##### Declaration

```
public AxialLoadCheckOption SupportingMemberFlangeBendingCheck { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [AxialLoadCheckOption](DesignData.SDS2.Model.AxialLoadCheckOption.html) |             |

##### Remarks

See SDS2's help on vertical brace connections for more information.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FSupportingMemberWebCripplingCheck)SupportingMemberWebCripplingCheck

Specifies how the limit state is incorporated as a check within connection design that can potentially cause the connection to fail.

##### Declaration

```
public AxialLoadCheckOption SupportingMemberWebCripplingCheck { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [AxialLoadCheckOption](DesignData.SDS2.Model.AxialLoadCheckOption.html) |             |

##### Remarks

See SDS2's help on vertical brace connections for more information.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FSupportingMemberWebShearCheck)SupportingMemberWebShearCheck

Specifies how the limit state is incorporated as a check within connection design that can potentially cause the connection to fail.

##### Declaration

```
public IfRequiredNever SupportingMemberWebShearCheck { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [IfRequiredNever](DesignData.SDS2.Model.IfRequiredNever.html) |             |

##### Remarks

See SDS2's help on vertical brace connections for more information.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FSupportingMemberWebStressCheck)SupportingMemberWebStressCheck

Specifies how the limit state is incorporated as a check within connection design that can potentially cause the connection to fail.

##### Declaration

```
public IfRequiredNever SupportingMemberWebStressCheck { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [IfRequiredNever](DesignData.SDS2.Model.IfRequiredNever.html) |             |

##### Remarks

See SDS2's help on vertical brace connections for more information.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FUFMSpecialCase)UFMSpecialCase

Specifies how the system spreads the load across a connection between a supporting column and beam.

##### Declaration

```
public UFMSpecialCase UFMSpecialCase { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [UFMSpecialCase](DesignData.SDS2.Model.UFMSpecialCase.html) |             |

##### Remarks

See SDS2 help on vertical brace connections for more information.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FUFMSpecialCase2PercentTransfer)UFMSpecialCase2PercentTransfer

Specifies the UFM special case 2 transfer percent.

##### Declaration

```
public double UFMSpecialCase2PercentTransfer { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Does not apply when IsAutoUFMSpecialCase2\_PercentTransfer is true.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FUseOversizedHoles)UseOversizedHoles

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

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FUseReinforcementPlate)UseReinforcementPlate

Specifies whether a reinforcement plate is used between the gusset plate and a HSS column face.

##### Declaration

```
public AutomaticYesNo UseReinforcementPlate { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

##### Remarks

Only applies when framing to a HHS tube column with a thin wall.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FWideFlangeAttachment)WideFlangeAttachment

Specifies how the flanges of a vertical wide flange brace attach to the gusset plate.

##### Declaration

```
public VertBraceWideFlangeAttachmentMethod WideFlangeAttachment { get; set; }
```

##### Property Value

| Type                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------- | ----------- |
| [VertBraceWideFlangeAttachmentMethod](DesignData.SDS2.Model.VertBraceWideFlangeAttachmentMethod.html) |             |

##### Remarks

Applies to vertical wide flange braces.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FWideFlangeConnectionArrangement)WideFlangeConnectionArrangement

Specifies the horizontal wide flange brace connection arrangement to the gusset plate.

##### Declaration

```
public VertBraceWideFlangeHorzConnectionArrangement WideFlangeConnectionArrangement { get; set; }
```

##### Property Value

| Type                                                                                                                    | Description |
| ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| [VertBraceWideFlangeHorzConnectionArrangement](DesignData.SDS2.Model.VertBraceWideFlangeHorzConnectionArrangement.html) |             |

##### Remarks

Applies to horizontal wide flange braces.

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FWideFlangeWebAttachment)WideFlangeWebAttachment

Specifies how the web of a vertical wide flange brace attaches to the gusset plate.

##### Declaration

```
public VertBraceWideFlangeWebAttachmentMethod WideFlangeWebAttachment { get; set; }
```

##### Property Value

| Type                                                                                                        | Description |
| ----------------------------------------------------------------------------------------------------------- | ----------- |
| [VertBraceWideFlangeWebAttachmentMethod](DesignData.SDS2.Model.VertBraceWideFlangeWebAttachmentMethod.html) |             |

##### Remarks

Applies to vertical wide flange braces.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FVertBracePlateSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A specification for connecting a vertical brace to one or more supporting members via a gusset plate and possibly clip angles.

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