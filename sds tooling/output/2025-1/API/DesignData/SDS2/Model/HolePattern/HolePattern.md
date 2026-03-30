# Class HolePattern 

HolePattern encapsulates information to create holes in the model. The local coordinate system of a HolePattern is an XY plane that can be translated to global coordinates and used to create holes on materials.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

HolePattern

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public sealed class HolePattern
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5F%5Fctor)HolePattern()

HolePattern encapsulates information to create holes in the model. The local coordinate system of a HolePattern is an XY plane that can be translated to global coordinates and used to create holes on materials.

##### Declaration

```
public HolePattern()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FBoltDiameter)BoltDiameter

Bolt diameter, in inches, for the pattern.

##### Declaration

```
public double BoltDiameter { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                              |
| ------------------------------------------------------------------------------ | -------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Throw when passed a negative diameter. |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FCombineOnDetail)CombineOnDetail

Indicates if this pattern should be combined with others, when possible, on details.

##### Declaration

```
public bool CombineOnDetail { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FDrillBothSidesOfHollowSection)DrillBothSidesOfHollowSection

Indicates if this pattern should be drilled through both sides of hollow section materials.

##### Declaration

```
public bool DrillBothSidesOfHollowSection { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FGlobalHoles)GlobalHoles

Hole locations in global coordinates.

##### Declaration

```
public Point3DList GlobalHoles { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [Point3DList](DesignData.SDS2.Primitives.Point3DList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FHoleDiameter)HoleDiameter

Hole diameter, in inches, for the pattern.

##### Declaration

```
public double HoleDiameter { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                              |
| ------------------------------------------------------------------------------ | -------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Throw when passed a negative diameter. |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FHoleType)HoleType

The hole type for the pattern

##### Declaration

```
public HoleType HoleType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [HoleType](DesignData.SDS2.Setup.HoleType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FIsAutoPreferredBoltType)IsAutoPreferredBoltType

Specifies if the preferred bolt type for the pattern should use the default bolt type defined in setup.

##### Declaration

```
public bool IsAutoPreferredBoltType { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Assigning PreferredBoltType to null will turn on IsAutoPreferredBoltType. Setting it to a non-null bolt type will turn off IsAutoPreferredBoltType.

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FIsMatchable)IsMatchable

Indicates if this pattern can be used to "match" against other material, which would create a corresponding hole on that material in line with this hole. If this is false, then this hole will be ignored during hole matching.

##### Declaration

```
public bool IsMatchable { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FIsValidCNC)IsValidCNC

Indicates if this pattern can be downloaded to a CNC file If this is false, then the pattern will not appear in the CNC file which is one way to avoid error messages for holes that would otherwise generate errors.

##### Declaration

```
public bool IsValidCNC { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FLocalHoles)LocalHoles

Hole locations in local coordinates.

##### Declaration

```
public Point2DList LocalHoles { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [Point2DList](DesignData.SDS2.Primitives.Point2DList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FMaximumSurfaceGap)MaximumSurfaceGap

Maximum gap between pattern and material surface that will allow pattern to drill holes.

##### Declaration

```
public double MaximumSurfaceGap { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                         |
| ------------------------------------------------------------------------------ | --------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Throw when passed a negative gap. |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FPlugType)PlugType

Hole plug type for this pattern

##### Declaration

```
public PlugType PlugType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [PlugType](DesignData.SDS2.Model.PlugType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FPreferredBoltType)PreferredBoltType

The bolt type for the pattern

##### Declaration

```
public BoltType PreferredBoltType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

##### Remarks

Assigning PreferredBoltType to null will turn on IsAutoPreferredBoltType. Setting it to a non-null bolt type will turn off IsAutoPreferredBoltType.

##### Exceptions

| Type                                                                           | Condition                                                   |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Throw when passed a bolt type that is not defined in setup. |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FSlotLength)SlotLength

Slot length, in inches, for the pattern.

##### Declaration

```
public double SlotLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                            |
| ------------------------------------------------------------------------------ | ------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Throw when passed a negative length. |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FSlotRotation)SlotRotation

Slot rotation, in radians, for the pattern.

##### Declaration

```
public double SlotRotation { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FToGlobalCoordinates)ToGlobalCoordinates

Represents the transformation from the pattern in local coordinates to global coordinates.

##### Declaration

```
public Matrix ToGlobalCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FAddLocalHole%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5F)AddLocalHole(Point2D)

Add a hole location in local coordinates to the pattern.

##### Declaration

```
public void AddLocalHole(Point2D hole)
```

##### Parameters

| Type                                               | Name | Description |
| -------------------------------------------------- | ---- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html) | hole |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FFinalize)\~HolePattern()

HolePattern encapsulates information to create holes in the model. The local coordinate system of a HolePattern is an XY plane that can be translated to global coordinates and used to create holes on materials.

##### Declaration

```
protected ~HolePattern()
```

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FGetHashCode)GetHashCode()

HolePattern encapsulates information to create holes in the model. The local coordinate system of a HolePattern is an XY plane that can be translated to global coordinates and used to create holes on materials.

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

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FGetOperations)GetOperations()

A deep copy of the the machine/tool operations for the hole pattern

##### Declaration

```
public HoleMachineOperations GetOperations()
```

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [HoleMachineOperations](DesignData.SDS2.Model.HoleMachineOperations.html) |             |

##### Remarks

The pattern HoleType must be set to StandardRound at the time of drilling into a material for the operations to apply.

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FGridPattern%5FDesignData%5FSDS2%5FModel%5FHolePatternRelativeGridPosition%5FSystem%5FInt32%5FSystem%5FDouble%5FSystem%5FDouble%5FSystem%5FInt32%5FSystem%5FDouble%5FSystem%5FDouble%5F)GridPattern(HolePatternRelativeGridPosition, int, double, double, int, double, double)

Factory to create a HolePattern for the grid patterns that the SDS2 hole create tool supports. This will return a hole pattern with (x\_count \* y\_count) locations even if some of the locations overlap due to how the spacing is defined.

##### Declaration

```
public static HolePattern GridPattern(HolePatternRelativeGridPosition grid_position, int x_count, double x_offset, double x_spacing, int y_count, double y_offset, double y_spacing)
```

##### Parameters

| Type                                                                                          | Name           | Description                                                                            |
| --------------------------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------- |
| [HolePatternRelativeGridPosition](DesignData.SDS2.Model.HolePatternRelativeGridPosition.html) | grid\_position | Specifies how 1, 2, or 4 grids of holes are positioned relative to the pattern origin. |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                    | x\_count       | The number of horizontal columns in a pattern.                                         |
| [double](https://learn.microsoft.com/dotnet/api/system.double)                                | x\_offset      | The distance along the x axis the first column is from the origin.                     |
| [double](https://learn.microsoft.com/dotnet/api/system.double)                                | x\_spacing     | The distance along the x axis between columns.                                         |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                    | y\_count       | The number of vertical rows in a pattern.                                              |
| [double](https://learn.microsoft.com/dotnet/api/system.double)                                | y\_offset      | The distance along the y axis the first row is from the origin.                        |
| [double](https://learn.microsoft.com/dotnet/api/system.double)                                | y\_spacing     | The distance along the y axis between rows.                                            |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [HolePattern](DesignData.SDS2.Model.HolePattern.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FHoleMatchedPattern)HoleMatchedPattern()

Return a new pattern that is suitable to be used as a hole match to this pattern. The returned pattern will use StandardRound holes with nominal dimensions based on the this pattern and there will be no operations applied. If this pattern is not Matchable then the returned pattern will have no holes.

##### Declaration

```
public HolePattern HoleMatchedPattern()
```

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [HolePattern](DesignData.SDS2.Model.HolePattern.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FSetNominalHoleDimensions%5FDesignData%5FSDS2%5FSetup%5FHoleType%5FDesignData%5FSDS2%5FSetup%5FBoltType%5FSystem%5FDouble%5F)SetNominalHoleDimensions(HoleType, BoltType, double)

Set the hole diameter and slot length based on the hole type, bolt type and bolt diameter. Also, sets the hole type, bolt type, and bolt diameter to the specified values.

##### Declaration

```
public void SetNominalHoleDimensions(HoleType holeType, BoltType boltType, double boltDiameter)
```

##### Parameters

| Type                                                           | Name         | Description |
| -------------------------------------------------------------- | ------------ | ----------- |
| [HoleType](DesignData.SDS2.Setup.HoleType.html)                | holeType     |             |
| [BoltType](DesignData.SDS2.Setup.BoltType.html)                | boltType     |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | boltDiameter |             |

#### [](#DesignData%5FSDS2%5FModel%5FHolePattern%5FSetOperations%5FDesignData%5FSDS2%5FModel%5FHoleMachineOperations%5F)SetOperations(HoleMachineOperations)

A deep copy of the the machine/tool operations for the hole pattern

##### Declaration

```
public void SetOperations(HoleMachineOperations operations)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [HoleMachineOperations](DesignData.SDS2.Model.HoleMachineOperations.html) | operations |             |

##### Remarks

The pattern HoleType must be set to StandardRound at the time of drilling into a material for the operations to apply.