# Class WeldSide 

WeldSide provides access to the arrow and other side information of a weld

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

WeldSide

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
public class WeldSide
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FContour)Contour

The weld contour.

##### Declaration

```
public WeldContour Contour { get; set; }
```

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [WeldContour](DesignData.SDS2.Model.WeldContour.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist.                                         |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FEffectiveThroat)EffectiveThroat

In a fillet weld, this is the inches from the root to the face of the weld. The distance is measured in the plane where the weld is most likely to fail. An "Effective throat" distance may be applied to weld symbols for bevel and groove welds, not just fillet welds.

##### Declaration

```
public double EffectiveThroat { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FFinishSymbol)FinishSymbol

A letter (1 character) to appear on the weld symbol to designate the finish.

##### Declaration

```
public string FinishSymbol { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FGrooveAngle)GrooveAngle

Radians \[-1.309 (75 degrees), 1.309\] that define the angle for bevel groove or V groove welds.

##### Declaration

```
public double GrooveAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist.                                         |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FIsArrowSide)IsArrowSide

Is this side the arrow side of the weld.

##### Declaration

```
public bool IsArrowSide { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FIsLengthOnSymbol)IsLengthOnSymbol

Show weld length on the symbol.

##### Declaration

```
public bool IsLengthOnSymbol { get; set; }
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

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FIsSizeOnSymbol)IsSizeOnSymbol

Show weld size on the symbol.

##### Declaration

```
public bool IsSizeOnSymbol { get; set; }
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

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FLeftSetback)LeftSetback

Inches the left end of the weld is set back from the edge of the material. Zero makes the left end of the weld go to the edge of the material.

##### Declaration

```
public double LeftSetback { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FRightSetback)RightSetback

Inches the right end of the weld is set back from the edge of the material. Zero makes the right end of the weld go to the edge of the material.

##### Declaration

```
public double RightSetback { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FRootFace)RootFace

Inches of a prepared edge that is not beveled or grooved for groove welds.

##### Declaration

```
public double RootFace { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FRootOpening)RootOpening

The weld root opening in inches for groove welds.

##### Declaration

```
public double RootOpening { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FStitchLeftTermination)StitchLeftTermination

The weld stitch left termination in inches.

##### Declaration

```
public double StitchLeftTermination { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FStitchLength)StitchLength

Inches between the beginning of each weld stitch.

##### Declaration

```
public double StitchLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FStitchRightTermination)StitchRightTermination

The weld stitch right termination in inches.

##### Declaration

```
public double StitchRightTermination { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FStitchSpacing)StitchSpacing

The weld stitch spacing in inches.

##### Declaration

```
public double StitchSpacing { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FUseFilletBackupWeld)UseFilletBackupWeld

Apply a fillet backup weld to a square, bevel, or J groove weld.

##### Declaration

```
public bool UseFilletBackupWeld { get; set; }
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

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FWeldLength)WeldLength

The weld length in inches. To adjust the length change the setbacks.

##### Declaration

```
public double WeldLength { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FWeldSize)WeldSize

Indicates depth of preparation, size or strength of the weld in inches.

##### Declaration

```
public double WeldSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist or is set to an invalid value.           |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FWeldType)WeldType

The weld type.

##### Declaration

```
public WeldType WeldType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldType](DesignData.SDS2.Setup.WeldType.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the weld does not exist.                                         |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

WeldSide provides access to the arrow and other side information of a weld

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FFinalize)\~WeldSide()

WeldSide provides access to the arrow and other side information of a weld

##### Declaration

```
protected ~WeldSide()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldSide%5FGetSegments)GetSegments()

The weld path.

##### Declaration

```
public WeldSegmentList GetSegments()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [WeldSegmentList](DesignData.SDS2.Model.WeldSegmentList.html) |             |