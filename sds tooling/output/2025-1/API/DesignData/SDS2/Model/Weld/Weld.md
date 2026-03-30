# Class Weld 

Weld provides access to information about welds on a member.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Weld

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
public class Weld
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FArrowSide)ArrowSide

The 'arrow' side of the weld.

##### Declaration

```
public WeldSide ArrowSide { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldSide](DesignData.SDS2.Model.WeldSide.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FCustomPropertyMapHandle)CustomPropertyMapHandle

A handle to the custom properties for this weld.

##### Declaration

```
public CustomPropertyMapHandle CustomPropertyMapHandle { get; }
```

##### Property Value

| Type                                                                             | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [CustomPropertyMapHandle](DesignData.SDS2.Database.CustomPropertyMapHandle.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                     |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the weld handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FGuid)Guid

The SDS2 Guid/UUID for this weld.

##### Declaration

```
public Guid? Guid { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [Guid](https://learn.microsoft.com/dotnet/api/system.guid)? |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FHandle)Handle

Weld provides access to information about welds on a member.

##### Declaration

```
public WeldHandle Handle { get; }
```

##### Property Value

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [WeldHandle](DesignData.SDS2.Database.WeldHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FIsFieldWeld)IsFieldWeld

True indicates if a weld is applied in the field. False indicates the weld is applied in the shop.

##### Declaration

```
public bool IsFieldWeld { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FIsOtherSideSeparable)IsOtherSideSeparable

Is the other weld side separable.

##### Declaration

```
public bool IsOtherSideSeparable { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FIsSpacerBarRequired)IsSpacerBarRequired

Indicates the supplementary symbol for a spacer bar ('M' inside a rectangle) will be drawn as a part of the weld symbol for V and Bevel groove welds

##### Declaration

```
public bool IsSpacerBarRequired { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FIsStitched)IsStitched

Is the weld stitched

##### Declaration

```
public bool IsStitched { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist.                                         |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FIsSystemGenerated)IsSystemGenerated

Is the weld system generated.

##### Declaration

```
public bool IsSystemGenerated { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FIsWeldedAllAround)IsWeldedAllAround

Indicates a weld-all-around weld

##### Declaration

```
public bool IsWeldedAllAround { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FJointDesignation)JointDesignation

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

| Type                                                                           | Condition                                                                                      |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FMaterial)Material

One of the materials welded by this weld

##### Declaration

```
public Material Material { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FMoveTailTextToShopNote)MoveTailTextToShopNote

Determines whether tail text is shown on the detail as a 'Shop Note'

##### Declaration

```
public bool MoveTailTextToShopNote { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FNormal1)Normal1

One of the normal directions, in global coordinates, for the weld

##### Declaration

```
public Vector3D Normal1 { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FNormal2)Normal2

One of the normal directions, in global coordinates, for the weld

##### Declaration

```
public Vector3D Normal2 { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FOrigin)Origin

The origin, in global inches, of the weld

##### Declaration

```
public Point3D Origin { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FOtherSide)OtherSide

The 'other' side of the weld.

##### Declaration

```
public WeldSide OtherSide { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldSide](DesignData.SDS2.Model.WeldSide.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FOtherStitchType)OtherStitchType

Stitch spacing type for the other side.

##### Declaration

```
public StitchType OtherStitchType { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [StitchType](DesignData.SDS2.Model.StitchType.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist.                                         |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FPenetration)Penetration

Prequalified weld tail penetration

##### Declaration

```
public WeldPenetrationType Penetration { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldPenetrationType](DesignData.SDS2.Model.WeldPenetrationType.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FPosition)Position

Prequalified weld tail position

##### Declaration

```
public WeldPositionType Position { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [WeldPositionType](DesignData.SDS2.Model.WeldPositionType.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FProcess)Process

Prequalified weld tail process

##### Declaration

```
public WeldProcessType Process { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [WeldProcessType](DesignData.SDS2.Model.WeldProcessType.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FTailText)TailText

Prequalified weld tail text

##### Declaration

```
public string TailText { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FToGlobalCoordinates)ToGlobalCoordinates

Matrix, in inches, representing a transformation from weld coordinates to global coordinates

##### Declaration

```
public Matrix ToGlobalCoordinates { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FToMemberCoordinates)ToMemberCoordinates

Matrix, in inches, representing a transformation from weld coordinates to member coordinates

##### Declaration

```
public Matrix ToMemberCoordinates { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FUsePrequalifiedWeldTailText)UsePrequalifiedWeldTailText

Determines whether PrequalifiedTailText, WeldJointType, JointDesignation, Process, and Position are used

##### Declaration

```
public bool UsePrequalifiedWeldTailText { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FWeldJoint)WeldJoint

Prequalified weld tail joint

##### Declaration

```
public WeldJointType WeldJoint { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [WeldJointType](DesignData.SDS2.Model.WeldJointType.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Weld provides access to information about welds on a member.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FFinalize)\~Weld()

Weld provides access to information about welds on a member.

##### Declaration

```
protected ~Weld()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeld%5FGetSurface)GetSurface()

The Surface, or polygons, for this weld, in weld coordinates, which also happens to be global coordinates.

##### Declaration

```
public Surface GetSurface()
```

##### Returns

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist. |