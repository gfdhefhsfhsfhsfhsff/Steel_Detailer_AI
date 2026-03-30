# Class GridLine 

Grid lines appear as lines, segments, circles, and arcs of a circle in the model.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

GridLine

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class GridLine
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FArcType)ArcType

Arc type, only applies for curved grids

##### Declaration

```
public ArcType ArcType { get; set; }
```

##### Property Value

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [ArcType](DesignData.SDS2.Model.ArcType.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FDepthIn)DepthIn

The distance in inches from this grid's work plane to a plane farther away than the viewer.

##### Declaration

```
public double DepthIn { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FDepthOut)DepthOut

The distance in inches from this grid's work plane to a plane closer to the viewer.

##### Declaration

```
public double DepthOut { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FGridBubbleOffset)GridBubbleOffset

Positive factor by which by which finite grid lines will be extended in proportion to the diameter of its grid bubble.

##### Declaration

```
public double GridBubbleOffset { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FGridType)GridType

Grid type

##### Declaration

```
public GridType GridType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [GridType](DesignData.SDS2.Model.GridType.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FIsAutoPinPermitted)IsAutoPinPermitted

True when the grid line is permitted to be automatically pinned to

##### Declaration

```
public bool IsAutoPinPermitted { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FIsForDetail)IsForDetail

True when the grid line is allowed for detailing

##### Declaration

```
public bool IsForDetail { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FLineType)LineType

Grid line type

##### Declaration

```
public LineType LineType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [LineType](DesignData.SDS2.Model.LineType.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FName)Name

Name of the erection view defined by the grid line

##### Declaration

```
public string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Exceptions

| Type                                                                           | Condition                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FPen)Pen

Grid line pen color

##### Declaration

```
public PenColor Pen { get; set; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [PenColor](DesignData.SDS2.Primitives.PenColor.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FRadius)Radius

Radius, in inches, of curved grid lines

##### Declaration

```
public double Radius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FToGlobalCoordinates)ToGlobalCoordinates

Matrix, in inches, representing a transformation from view coordinates to global coordinates for the grid line

##### Declaration

```
public Matrix ToGlobalCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FToViewCoordinates)ToViewCoordinates

Matrix, in inches, representing a transformation from global coordinates to the view coordinates for the grid line

##### Declaration

```
public Matrix ToViewCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FViewBounds2D)ViewBounds2D

2D viewing bounds in view coordinates.

##### Declaration

```
public BoundingBox2D ViewBounds2D { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [BoundingBox2D](DesignData.SDS2.Primitives.BoundingBox2D.html) |             |

##### Remarks

When the model is transformed from global coordinates to view coordinates, only the portion of the model that falls into the area defined by these bounds combined with the depth in and out is visible to the view defined by this gride line. 

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FViewType)ViewType

The type of view defined by the grid line.

##### Declaration

```
public ErectionViewType ViewType { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [ErectionViewType](DesignData.SDS2.Model.ErectionViewType.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid.                                                 |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Grid lines appear as lines, segments, circles, and arcs of a circle in the model.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FEquals%5FSystem%5FObject%5F)Equals(object)

Grid lines appear as lines, segments, circles, and arcs of a circle in the model.

##### Declaration

```
public override bool Equals(object other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | other |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FFinalize)\~GridLine()

Grid lines appear as lines, segments, circles, and arcs of a circle in the model.

##### Declaration

```
protected ~GridLine()
```

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FGet%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandle%5F)Get(GridLineHandle)

Get a GridLine object for the GridLineHandle passed in.

##### Declaration

```
public static GridLine Get(GridLineHandle handle)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html) | handle |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [GridLine](DesignData.SDS2.Model.GridLine.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FGetHashCode)GetHashCode()

Grid lines appear as lines, segments, circles, and arcs of a circle in the model.

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FIsNearlyPlanView%5FSystem%5FDouble%5F)IsNearlyPlanView(double)

True when the grid represents a plan view. Specifically, this is when the the viewing direction is within `tan_tol` of being parallel to vertical in global coordinates. If tan\_tol is 0.01745, it tests that the vectors are within approximately 1 degree of parallel.

##### Declaration

```
public bool IsNearlyPlanView(double tan_tol)
```

##### Parameters

| Type                                                           | Name     | Description                                                                                                                                                            |
| -------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | tan\_tol | The tangent of the angle that specifies the desired tolerance. Note that for small angles x, tan x \~= x, so you can also think of this nearly a tolerance in radians. |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FGridLine%5FRefreshDatabaseTable)RefreshDatabaseTable()

Refresh the the primary table for objects of this type.

##### Declaration

```
public static void RefreshDatabaseTable()
```