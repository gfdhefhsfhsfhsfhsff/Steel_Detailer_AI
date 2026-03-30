# Class BoundingBox3D 

The BoundingBox3D class represents the axis-aligned area enclosed by a two points in 3D space.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BoundingBox3D

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class BoundingBox3D
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5F)BoundingBox3D(BoundingBox3D)

Instantiates a bounding box as a copy of another bounding box.

##### Declaration

```
public BoundingBox3D(BoundingBox3D other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [BoundingBox3D](DesignData.SDS2.Primitives.BoundingBox3D.html) | other |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)BoundingBox3D(Point3D, Point3D)

Instantiates a bounding box that contains both points

##### Declaration

```
public BoundingBox3D(Point3D p, Point3D q)
```

##### Parameters

| Type                                               | Name | Description |
| -------------------------------------------------- | ---- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | p    |             |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | q    |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FDepth)Depth

The difference bewteen the maximum Z and minimum Z

##### Declaration

```
public double Depth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FHeight)Height

The difference bewteen the maximum Y and minimum Y

##### Declaration

```
public double Height { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FMax)Max

The maximum X, Y, and Z-coordinate of the bounds

##### Declaration

```
public Point3D Max { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FMaxX)MaxX

The maximum X-coordinate of the bounds

##### Declaration

```
public double MaxX { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FMaxY)MaxY

The maximum Y-coordinate of the bounds

##### Declaration

```
public double MaxY { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FMaxZ)MaxZ

The maximum Z-coordinate of the bounds

##### Declaration

```
public double MaxZ { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FMin)Min

The minimum X, Y, and Z-coordinate of the bounds

##### Declaration

```
public Point3D Min { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FMinX)MinX

The minimum X-coordinate of the bounds

##### Declaration

```
public double MinX { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FMinY)MinY

The minimum Y-coordinate of the bounds

##### Declaration

```
public double MinY { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FMinZ)MinZ

The minimum Z-coordinate of the bounds

##### Declaration

```
public double MinZ { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FVolume)Volume

The volume of the bounds

##### Declaration

```
public double Volume { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FWidth)Width

The difference bewteen the maximum X and minimum X

##### Declaration

```
public double Width { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FDoesEnclose%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)DoesEnclose(Point3D)

True iff the specified point is within bounds

##### Declaration

```
public bool DoesEnclose(Point3D point)
```

##### Parameters

| Type                                               | Name  | Description |
| -------------------------------------------------- | ----- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | point |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FDoesOverlap%5FDesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5F)DoesOverlap(BoundingBox3D)

True iff the two bounds overlap

##### Declaration

```
public bool DoesOverlap(BoundingBox3D other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [BoundingBox3D](DesignData.SDS2.Primitives.BoundingBox3D.html) | other |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FEquals%5FSystem%5FObject%5F)Equals(object)

Checks to see if the Min and Max are equal using Double.Equals on each component. Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public override bool Equals(object obj)
```

##### Parameters

| Type                                                           | Name | Description              |
| -------------------------------------------------------------- | ---- | ------------------------ |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | obj  | The bounds to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FExpanded%5FSystem%5FDouble%5F)Expanded(double)

A new bounding box expanded on all sides by the specified amount

##### Declaration

```
public BoundingBox3D Expanded(double amount)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | amount |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [BoundingBox3D](DesignData.SDS2.Primitives.BoundingBox3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FFinalize)\~BoundingBox3D()

The BoundingBox3D class represents the axis-aligned area enclosed by a two points in 3D space.

##### Declaration

```
protected ~BoundingBox3D()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FGetHashCode)GetHashCode()

Returns the hash code for this instance.

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FShortestVectorToPoint%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)ShortestVectorToPoint(Point3D)

The shortest vector from the bounds to the specified point

##### Declaration

```
public Vector3D ShortestVectorToPoint(Point3D point)
```

##### Parameters

| Type                                               | Name  | Description |
| -------------------------------------------------- | ----- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | point |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FToString)ToString()

Formats the point into a string. Note that because the values are rounded for display, parsing them to retrieve the Min and Max values will not necessarily yield the same bounds.

##### Declaration

```
public override string ToString()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Overrides

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FUnioned%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)Unioned(Point3D)

A new bounding box that includes the current bounds and the specified point

##### Declaration

```
public BoundingBox3D Unioned(Point3D point)
```

##### Parameters

| Type                                               | Name  | Description |
| -------------------------------------------------- | ----- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | point |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [BoundingBox3D](DesignData.SDS2.Primitives.BoundingBox3D.html) |             |

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5Fop%5FEquality%5FDesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FDesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5F)operator ==(BoundingBox3D, BoundingBox3D)

Checks on Min and Max. Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public static bool operator ==(BoundingBox3D a, BoundingBox3D b)
```

##### Parameters

| Type                                                           | Name | Description              |
| -------------------------------------------------------------- | ---- | ------------------------ |
| [BoundingBox3D](DesignData.SDS2.Primitives.BoundingBox3D.html) | a    | The bounds to compare    |
| [BoundingBox3D](DesignData.SDS2.Primitives.BoundingBox3D.html) | b    | The bounds to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5Fop%5FInequality%5FDesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5FDesignData%5FSDS2%5FPrimitives%5FBoundingBox3D%5F)operator !=(BoundingBox3D, BoundingBox3D)

Checks inequality on Min and Max Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public static bool operator !=(BoundingBox3D a, BoundingBox3D b)
```

##### Parameters

| Type                                                           | Name | Description              |
| -------------------------------------------------------------- | ---- | ------------------------ |
| [BoundingBox3D](DesignData.SDS2.Primitives.BoundingBox3D.html) | a    | The bounds to compare    |
| [BoundingBox3D](DesignData.SDS2.Primitives.BoundingBox3D.html) | b    | The bounds to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |