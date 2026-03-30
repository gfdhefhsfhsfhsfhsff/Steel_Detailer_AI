# Class WeldPathSpecification 

Class representing all the weld information about how a new weld should be created

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

WeldPathSpecification

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
public sealed class WeldPathSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5F%5Fctor)WeldPathSpecification()

Class representing all the weld information about how a new weld should be created

##### Declaration

```
public WeldPathSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FArrowSide)ArrowSide

The 'arrow' side of the weld.

##### Declaration

```
public WeldSide ArrowSide { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldSide](DesignData.SDS2.Model.WeldSide.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FCreateDistinctWeldsPerSegment)CreateDistinctWeldsPerSegment

Indicates if each created segment is considered to be a distinct weld. In some cases, auto detailing is better able to recognize such welds, and they, therefore, may produce better details.

##### Declaration

```
public bool CreateDistinctWeldsPerSegment { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FIsOtherSideSeparable)IsOtherSideSeparable

Is the other weld side separable.

##### Declaration

```
public bool IsOtherSideSeparable { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FIsSpacerBarRequired)IsSpacerBarRequired

Indicates the supplementary symbol for a spacer bar ('M' inside a rectangle) will be drawn as a part of the weld symbol for V and Bevel groove welds

##### Declaration

```
public bool IsSpacerBarRequired { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FIsStitched)IsStitched

Is the weld stitched

##### Declaration

```
public bool IsStitched { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FIsWeldedAllAround)IsWeldedAllAround

Indicates if a continuous weld is generated around every edge of the material, including material radii

##### Declaration

```
public bool IsWeldedAllAround { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FJointDesignation)JointDesignation

A letter (1 character) prequalified weld tail joint designation.

##### Declaration

```
public string JointDesignation { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Exceptions

| Type                                                                           | Condition                                    |
| ------------------------------------------------------------------------------ | -------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown when designation is an invalid value. |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FMaterialChamferDepth)MaterialChamferDepth

The chamfer depth for the material being welded for bevel and v groove welds. Zero depth will not chamfer the material

##### Declaration

```
public double MaterialChamferDepth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FMaximumGap)MaximumGap

The distance in inches that to-be-welded materials must be closer than in order for welds to be generated

##### Declaration

```
public double MaximumGap { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FMinimumWeldLength)MinimumWeldLength

Specifies the minimum distance in inches that welds must have in order to be generated

##### Declaration

```
public double MinimumWeldLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FMoveTailTextToShopNote)MoveTailTextToShopNote

Determines whether tail text is shown on the detail as a 'Shop Note'

##### Declaration

```
public bool MoveTailTextToShopNote { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FOtherSide)OtherSide

The 'other' side of the weld.

##### Declaration

```
public WeldSide OtherSide { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldSide](DesignData.SDS2.Model.WeldSide.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FOtherStitchType)OtherStitchType

Stitch spacing type for the other side.

##### Declaration

```
public StitchType OtherStitchType { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [StitchType](DesignData.SDS2.Model.StitchType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FPenetration)Penetration

Class representing all the weld information about how a new weld should be created

##### Declaration

```
public WeldPenetrationType Penetration { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldPenetrationType](DesignData.SDS2.Model.WeldPenetrationType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FPosition)Position

Prequalified weld tail position

##### Declaration

```
public WeldPositionType Position { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [WeldPositionType](DesignData.SDS2.Model.WeldPositionType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FProcess)Process

Prequalified weld tail process

##### Declaration

```
public WeldProcessType Process { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [WeldProcessType](DesignData.SDS2.Model.WeldProcessType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FSegments)Segments

A deep copy of a weld layout. If the segments are not empty this indicates SDS2 will use the specified layout to generate welds.

##### Declaration

```
public WeldPathSegmentList Segments { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FUsePrequalifiedWeldTailText)UsePrequalifiedWeldTailText

Determines whether PrequalifiedTailText, WeldJointType, JointDesignation, Process, and Position are used

##### Declaration

```
public bool UsePrequalifiedWeldTailText { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FWeldInsideSurfaces)WeldInsideSurfaces

Indicates if both the inside and outside surfaces of HSS sections should generate welds

##### Declaration

```
public bool WeldInsideSurfaces { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FWeldJoint)WeldJoint

Prequalified weld tail joint

##### Declaration

```
public WeldJointType WeldJoint { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [WeldJointType](DesignData.SDS2.Model.WeldJointType.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FFinalize)\~WeldPathSpecification()

Class representing all the weld information about how a new weld should be created

##### Declaration

```
protected ~WeldPathSpecification()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSpecification%5FGenerateWelds%5FDesignData%5FSDS2%5FModel%5FMaterial%5FDesignData%5FSDS2%5FModel%5FMaterialList%5F)GenerateWelds(Material, MaterialList)

Adds welds to the member of the first material connecting that material to all the other materials. Must be called with an existing Transaction.

##### Declaration

```
public WeldList GenerateWelds(Material material, MaterialList weldTo)
```

##### Parameters

| Type                                                    | Name     | Description |
| ------------------------------------------------------- | -------- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html)         | material |             |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html) | weldTo   |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldList](DesignData.SDS2.Model.WeldList.html) |             |

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown if this is called outside of a writable Transaction.                                                                                                                                                                                                                                                                                                                                                                                                    |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)                 | Thrown when the member containing the material to weld has not beed added to the transaction                                                                                                                                                                                                                                                                                                                                                                   |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)               | Thrown when the member containing the material to weld is unlocked                                                                                                                                                                                                                                                                                                                                                                                             |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html)         | Thrown when any of the material parameters do not have valid and active handles, i.e. they must be a part on a member that is added to the job. Fillet welds will also throw if any of Segments define a ToFilletRoot equal to the cross product of the segment's ToGlobalCoordinates XAxis and YAxis. To avoid this create fillet segments via WeldPathSegment.FromFilletLayout, WeldPathSegment.FromFilletSegment, and WeldProfileFillet.GetWeldPathSegment. |