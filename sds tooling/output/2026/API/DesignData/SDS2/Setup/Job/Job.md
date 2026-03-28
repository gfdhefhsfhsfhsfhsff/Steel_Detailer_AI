# Class Job 

Setup options for the job that are not fabricator specific

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Job

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
public class Job
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FAngleShapeSteelGrades)AngleShapeSteelGrades

Available steel grade list for angle sections

##### Declaration

```
public SteelGradeList AngleShapeSteelGrades { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FAvailableBoltDiameterUnits)AvailableBoltDiameterUnits

The maximum gap, in inches, allowed between materials with matching holes that is allowed for shop bolts.

##### Declaration

```
public AvailableBoltDiameterUnits AvailableBoltDiameterUnits { get; }
```

##### Property Value

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [AvailableBoltDiameterUnits](DesignData.SDS2.Setup.AvailableBoltDiameterUnits.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FAvailableImperialBoltDiameters)AvailableImperialBoltDiameters

The the avaiable imperial bolts, in inches.

##### Declaration

```
public DoubleList AvailableImperialBoltDiameters { get; }
```

##### Property Value

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [DoubleList](DesignData.SDS2.Primitives.DoubleList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FAvailableMetricBoltDiameters)AvailableMetricBoltDiameters

The the avaiable metric bolts, in inches.

##### Declaration

```
public DoubleList AvailableMetricBoltDiameters { get; }
```

##### Property Value

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [DoubleList](DesignData.SDS2.Primitives.DoubleList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FBaseCapPlateSchedule)BaseCapPlateSchedule

The list of available base/cap plates in the job

##### Declaration

```
public BaseCapPlateList BaseCapPlateSchedule { get; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [BaseCapPlateList](DesignData.SDS2.Setup.BaseCapPlateList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FBoltTypes)BoltTypes

Available bolt types for the currently set design method

##### Declaration

```
public BoltTypeList BoltTypes { get; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [BoltTypeList](DesignData.SDS2.Setup.BoltTypeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FChannelShapeSteelGrades)ChannelShapeSteelGrades

Available steel grade list for channel sections

##### Declaration

```
public SteelGradeList ChannelShapeSteelGrades { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultBGJoistBoltDiameter)DefaultBGJoistBoltDiameter

The default BG joist connection bolt diameter, in inches.

##### Declaration

```
public double DefaultBGJoistBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultBGJoistBoltType)DefaultBGJoistBoltType

The default BG joist connection bolt type.

##### Declaration

```
public BoltType DefaultBGJoistBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultDLHJoistBoltDiameter)DefaultDLHJoistBoltDiameter

The default DLH joist connection bolt diameter, in inches.

##### Declaration

```
public double DefaultDLHJoistBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultDLHJoistBoltType)DefaultDLHJoistBoltType

The default DLH joist connection bolt type.

##### Declaration

```
public BoltType DefaultDLHJoistBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultGJoistBoltDiameter)DefaultGJoistBoltDiameter

The default G joist connection bolt diameter, in inches.

##### Declaration

```
public double DefaultGJoistBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultGJoistBoltType)DefaultGJoistBoltType

The default G joist connection bolt type.

##### Declaration

```
public BoltType DefaultGJoistBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultHSSWeldedBraceErectorBoltDiameter)DefaultHSSWeldedBraceErectorBoltDiameter

The default HSS welded brace erector bolt diameter, in inches.

##### Declaration

```
public double DefaultHSSWeldedBraceErectorBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultHSSWeldedBraceErectorBoltType)DefaultHSSWeldedBraceErectorBoltType

The default HSS welded brace erector bolt type.

##### Declaration

```
public BoltType DefaultHSSWeldedBraceErectorBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultHorizontalBraceBoltDiameter)DefaultHorizontalBraceBoltDiameter

The default horizontal brace gusset to supporting bolt diameter, in inches.

##### Declaration

```
public double DefaultHorizontalBraceBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultHorizontalBraceBoltType)DefaultHorizontalBraceBoltType

The default horizontal brace gusset to supporting bolt type.

##### Declaration

```
public BoltType DefaultHorizontalBraceBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultKCSJoistBoltDiameter)DefaultKCSJoistBoltDiameter

The default KCS joist connection bolt diameter, in inches.

##### Declaration

```
public double DefaultKCSJoistBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultKCSJoistBoltType)DefaultKCSJoistBoltType

The default KCS joist connection bolt type.

##### Declaration

```
public BoltType DefaultKCSJoistBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultKJoistBoltDiameter)DefaultKJoistBoltDiameter

The default K joist connection bolt diameter, in inches.

##### Declaration

```
public double DefaultKJoistBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultKJoistBoltType)DefaultKJoistBoltType

The default K joist connection bolt type.

##### Declaration

```
public BoltType DefaultKJoistBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultLHJoistBoltDiameter)DefaultLHJoistBoltDiameter

The default LH joist connection bolt diameter, in inches.

##### Declaration

```
public double DefaultLHJoistBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultLHJoistBoltType)DefaultLHJoistBoltType

The default LH joist connection bolt type.

##### Declaration

```
public BoltType DefaultLHJoistBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultModelingColors)DefaultModelingColors

The list of default modeling colors

##### Declaration

```
public DefaultModelingColor DefaultModelingColors { get; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [DefaultModelingColor](DesignData.SDS2.Setup.DefaultModelingColor.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultMomentBoltDiameter)DefaultMomentBoltDiameter

The default moment bolt diameter, in inches.

##### Declaration

```
public double DefaultMomentBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultMomentBoltType)DefaultMomentBoltType

The default moment bolt type.

##### Declaration

```
public BoltType DefaultMomentBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultNonMomentBoltDiameter)DefaultNonMomentBoltDiameter

The default non moment bolt diameter, in inches.

##### Declaration

```
public double DefaultNonMomentBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultNonMomentBoltType)DefaultNonMomentBoltType

The default non moment bolt type.

##### Declaration

```
public BoltType DefaultNonMomentBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultSLHJoistBoltDiameter)DefaultSLHJoistBoltDiameter

The default SLH joist connection bolt diameter, in inches.

##### Declaration

```
public double DefaultSLHJoistBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultSLHJoistBoltType)DefaultSLHJoistBoltType

The default SLH joist connection bolt type.

##### Declaration

```
public BoltType DefaultSLHJoistBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultSurfaceFinish)DefaultSurfaceFinish

Default surface finish defined for the job

##### Declaration

```
public SurfaceFinish DefaultSurfaceFinish { get; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [SurfaceFinish](DesignData.SDS2.Setup.SurfaceFinish.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultVGJoistBoltDiameter)DefaultVGJoistBoltDiameter

The default VG joist connection bolt diameter, in inches.

##### Declaration

```
public double DefaultVGJoistBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultVGJoistBoltType)DefaultVGJoistBoltType

The default VG joist connection bolt type.

##### Declaration

```
public BoltType DefaultVGJoistBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultVerticalBraceBoltDiameter)DefaultVerticalBraceBoltDiameter

The default vertical brace gusset to supporting bolt diameter, in inches.

##### Declaration

```
public double DefaultVerticalBraceBoltDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDefaultVerticalBraceBoltType)DefaultVerticalBraceBoltType

The default vertical brace gusset to supporting bolt type.

##### Declaration

```
public BoltType DefaultVerticalBraceBoltType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FEmbedSchedule)EmbedSchedule

The list of embed plates in order.

##### Declaration

```
public EmbedList EmbedSchedule { get; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [EmbedList](DesignData.SDS2.Setup.EmbedList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FGratingSteelGrades)GratingSteelGrades

Available steel grade list for grating and grating tread materials

##### Declaration

```
public SteelGradeList GratingSteelGrades { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FHandle)Handle

The handle for this fabricator

##### Declaration

```
public JobSetupHandle Handle { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [JobSetupHandle](DesignData.SDS2.Database.JobSetupHandle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FJobNorth)JobNorth

Radians representing the job's north in plan views. Zero radians corresponds to north being on the top of the screen with positive radians moving counter clockwise and negative radians moving clockwise. Pi and -Pi being on the bottom of the screen.

##### Declaration

```
public double JobNorth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                       | Condition                                                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html) | If Open() hasn't been called on this job, or if that call returned false, or if another job has been Opened since this one was. |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FMaterialUsages)MaterialUsages

List of all MaterialUsage for this job

##### Declaration

```
public MaterialUsageList MaterialUsages { get; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [MaterialUsageList](DesignData.SDS2.Setup.MaterialUsageList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FMaximumFieldBoltGap)MaximumFieldBoltGap

The maximum gap, in inches, allowed between materials with matching holes that is allowed for field bolts.

##### Declaration

```
public double MaximumFieldBoltGap { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FMaximumShopBoltGap)MaximumShopBoltGap

The maximum gap, in inches, allowed between materials with matching holes that is allowed for shop bolts.

##### Declaration

```
public double MaximumShopBoltGap { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FMemberRevisions)MemberRevisions

An ordered list of all member revisions available in this job.

##### Declaration

```
public MemberRevisionList MemberRevisions { get; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [MemberRevisionList](DesignData.SDS2.Setup.MemberRevisionList.html) |             |

##### Exceptions

| Type                                                                       | Condition                                                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html) | If Open() hasn't been called on this job, or if that call returned false, or if another job has been Opened since this one was. |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FNamedColors)NamedColors

The list of named colors

##### Declaration

```
public NamedColorList NamedColors { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [NamedColorList](DesignData.SDS2.Setup.NamedColorList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FPipeShapeSteelGrades)PipeShapeSteelGrades

Available steel grade list for pipe sections

##### Declaration

```
public SteelGradeList PipeShapeSteelGrades { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FPlateSteelGrades)PlateSteelGrades

Available steel grade list for plates

##### Declaration

```
public SteelGradeList PlateSteelGrades { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FRolledSectionSteelGrades)RolledSectionSteelGrades

Available steel grade list for any rolled steel sections, besides tee, tube, pipe, channel and angle

##### Declaration

```
public SteelGradeList RolledSectionSteelGrades { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FSequences)Sequences

Get the list of sequences in this job. These will be returned in order, so that sequence 0 is the first in the returned list.

##### Declaration

```
public JobSequenceList Sequences { get; }
```

##### Property Value

| Type                                                          | Description                                             |
| ------------------------------------------------------------- | ------------------------------------------------------- |
| [JobSequenceList](DesignData.SDS2.Setup.JobSequenceList.html) | An ordered list of all sequences available in this job. |

##### Exceptions

| Type                                                                       | Condition                                                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html) | If Open() hasn't been called on this job, or if that call returned false, or if another job has been Opened since this one was. |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FStudSteelGrades)StudSteelGrades

Available steel grade list for studs

##### Declaration

```
public SteelGradeList StudSteelGrades { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FTeeShapeSteelGrades)TeeShapeSteelGrades

Available steel grade list for tee sections

##### Declaration

```
public SteelGradeList TeeShapeSteelGrades { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FTubeShapeSteelGrades)TubeShapeSteelGrades

Available steel grade list for tube sections

##### Declaration

```
public SteelGradeList TubeShapeSteelGrades { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FTurnbuckleAndClevisSteelGrades)TurnbuckleAndClevisSteelGrades

Available steel grade list for clevis and turnbuckles

##### Declaration

```
public SteelGradeList TurnbuckleAndClevisSteelGrades { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FZones)Zones

Get a list of zones in this job. These will be returned in order, so that zone 0 is first in the returned list.

##### Declaration

```
public JobZoneList Zones { get; }
```

##### Property Value

| Type                                                  | Description                                         |
| ----------------------------------------------------- | --------------------------------------------------- |
| [JobZoneList](DesignData.SDS2.Setup.JobZoneList.html) | An ordered list of all zones available in this job. |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FAdd%5FDesignData%5FSDS2%5FSetup%5FMaterialUsage%5F)Add(MaterialUsage)

Add a new material usage to this job

##### Declaration

```
public void Add(MaterialUsage usage)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html) | usage |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FAdd%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5F)Add(MemberRevision)

Add a new member revision to the job. Sets the new line number on the added revision.

##### Declaration

```
public void Add(MemberRevision revision)
```

##### Parameters

| Type                                                        | Name     | Description |
| ----------------------------------------------------------- | -------- | ----------- |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html) | revision |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FAdd%5FDesignData%5FSDS2%5FSetup%5FSurfaceFinish%5F)Add(SurfaceFinish)

Add a new surface to this job

##### Declaration

```
public void Add(SurfaceFinish finish)
```

##### Parameters

| Type                                                      | Name   | Description |
| --------------------------------------------------------- | ------ | ----------- |
| [SurfaceFinish](DesignData.SDS2.Setup.SurfaceFinish.html) | finish |             |

##### Remarks

The added finish is a copy. Subsequent changes to the passed in finish will not be reflected in setup

##### Exceptions

| Type                                                                           | Condition                                                                                                                       |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html)     | If Open() hasn't been called on this job, or if that call returned false, or if another job has been Opened since this one was. |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown if finish.DisplayName is not unique.                                                               |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when a transaction is not locked when Add is called                                                                      |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when the job setup has not been added to the transaction                                                                 |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FAddSequence%5FSystem%5FString%5FSystem%5FString%5F)AddSequence(string, string)

Add a new sequence to a zone. Specify an existing zone name to add the new sequence to an existing zone. Specify a unique zone name to add the new sequence to a new zone with the specified name. Or use the default empty string to add the new sequence to a new zone that will be named using the default naming convention for new zones.

##### Declaration

```
public JobSequence AddSequence(string sequenceName = "", string zoneName = "")
```

##### Parameters

| Type                                                           | Name         | Description                                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | sequenceName | The specified name of the new sequence. The empty string indicates the system should name the sequence with the default naming convention for new sequences.                                                                                                                                              |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | zoneName     | The specified name of the zone that the new sequence should be belong. The empty string indicates the sequence should belong to a new zone named with the default naming conventions for new zones. Specifying a unique non empty string will add the new sequence to a new zone with the specified name. |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Setup options for the job that are not fabricator specific

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FFinalize)\~Job()

Setup options for the job that are not fabricator specific

##### Declaration

```
protected ~Job()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FGet)Get()

Get the job setup object for the currently opened/active job.

##### Declaration

```
public static Job Get()
```

##### Returns

| Type                                  | Description |
| ------------------------------------- | ----------- |
| [Job](DesignData.SDS2.Setup.Job.html) |             |

##### Exceptions

| Type                                                                       | Condition                                                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html) | If Open() hasn't been called on this job, or if that call returned false, or if another job has been Opened since this one was. |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FGetStandardNoteTags)GetStandardNoteTags()

The standard note tags

##### Declaration

```
public TagCategoryList GetStandardNoteTags()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [TagCategoryList](DesignData.SDS2.Setup.TagCategoryList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJob%5FGetSurfaceFinishes)GetSurfaceFinishes()

Surface finishes defined for the job

##### Declaration

```
public SurfaceFinishList GetSurfaceFinishes()
```

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [SurfaceFinishList](DesignData.SDS2.Setup.SurfaceFinishList.html) |             |