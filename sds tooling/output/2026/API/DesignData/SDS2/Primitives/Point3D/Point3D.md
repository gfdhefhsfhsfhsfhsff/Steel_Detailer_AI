# Class Point3D 

The Point3D class can represent a position in 3D space, or a vector in 3D space. Some operations assume that the interpretation is a vector.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Point3D

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class Point3D
```

##### **Remarks**

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5F%5Fctor)Point3D()

Instantiates a point with X, Y, and Z all zero

##### Declaration

```
public Point3D()
```

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)Point3D(Point3D)

Instantiates a point equal to the given point

##### Declaration

```
public Point3D(Point3D pt)
```

##### Parameters

| Type                                               | Name | Description                   |
| -------------------------------------------------- | ---- | ----------------------------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | pt   | The point whose value to copy |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5F)Point3D(Vector3D)

Instantiates a point with the X, Y, and Z values of the given vector

##### Declaration

```
public Point3D(Vector3D vector)
```

##### Parameters

| Type                                                 | Name   | Description                   |
| ---------------------------------------------------- | ------ | ----------------------------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) | vector | The point whose value to copy |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5F%5Fctor%5FSystem%5FDouble%5FSystem%5FDouble%5FSystem%5FDouble%5F)Point3D(double, double, double)

Instantiates a point with the given X, Y, and Z values

##### Declaration

```
public Point3D(double x, double y, double z)
```

##### Parameters

| Type                                                           | Name | Description                   |
| -------------------------------------------------------------- | ---- | ----------------------------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | x    | The X value for the new point |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | y    | The Y value for the new point |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | z    | The Z value for the new point |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5FX)X

The X-coordinate of the point

##### Declaration

```
public double X { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5FY)Y

The Y-coordinate of the point

##### Declaration

```
public double Y { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5FZ)Z

The Z-coordinate of the point

##### Declaration

```
public double Z { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5FBinEquals%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FSystem%5FDouble%5F)BinEquals(Point3D, double)

Returns true if this point and the given point fall within the same "bin". A "bin" is a cubic region of space approximately binSize on a side.

##### Declaration

```
public bool BinEquals(Point3D other, double binSize)
```

##### Parameters

| Type                                                           | Name    | Description        |
| -------------------------------------------------------------- | ------- | ------------------ |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)             | other   | The other point    |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | binSize | The size of a bin. |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Unlike EpsilonEquals, BinEquals maintains the transitive rule of equality, but some points which are arbitrarily close together in distance are unequal according got EpsilonEquals, because they fall into different bins. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5FEpsilonEquals%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FSystem%5FDouble%5F)EpsilonEquals(Point3D, double)

Returns true if the squared distance between this point and the given point is less than distance\_squared.

##### Declaration

```
public bool EpsilonEquals(Point3D other, double distanceSquared)
```

##### Parameters

| Type                                                           | Name            | Description                                                                   |
| -------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)             | other           | The other point                                                               |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | distanceSquared | The square of the smallest distance value that should be considered different |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Note that EpsilonEquals can violate the transitivity rule of equality comparison, because there are many groups of points (p, q, r) where p.EpsilonEquals(q) and p.EpsilonEquals(r) but not q.EpsilonEquals(r). 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5FEquals%5FSystem%5FObject%5F)Equals(object)

Checks if each element of the points are equal using Double.Equals on each component. Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public override bool Equals(object obj)
```

##### Parameters

| Type                                                           | Name | Description             |
| -------------------------------------------------------------- | ---- | ----------------------- |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | obj  | The point to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5FFinalize)\~Point3D()

The Point3D class can represent a position in 3D space, or a vector in 3D space. Some operations assume that the interpretation is a vector.

##### Declaration

```
protected ~Point3D()
```

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5FGetHashCode)GetHashCode()

Returns the hash code for this instance. True for instances which are Equals(), otherwise False with high probability. Specific hash values are implementation-dependent.

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

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5FInterpolate%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FSystem%5FDouble%5F)Interpolate(Point3D, double)

Performs linear interpolation between this point and the `other`

##### Declaration

```
public Point3D Interpolate(Point3D other, double t)
```

##### Parameters

| Type                                                           | Name  | Description                                                                                                                                                                                                     |
| -------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)             | other | The other point                                                                                                                                                                                                 |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | t     | Controls the mixing between the two points. This function is defined for all values of t, though strictly speaking only values in the interval \[0,1\] are interpolations, and other values are extrapolations. |

##### Returns

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

##### Remarks

This is equal to `this + (other - this) * t`. 

Note that due to floating point arithmetic, `p.project(q, 1.0)`may not be exactly equal to `q`. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5FToString)ToString()

Formats the point into a string. Note that because the values are rounded for display, parsing them to retrieve the X, Y, and Z values will not necessarily yield the same point.

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

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5Fop%5FEquality%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)operator ==(Point3D, Point3D)

Checks if each element of the points are equal using == on each component. Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public static bool operator ==(Point3D p, Point3D q)
```

##### Parameters

| Type                                               | Name | Description             |
| -------------------------------------------------- | ---- | ----------------------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | p    | The point to compare    |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | q    | The point to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5Fop%5FInequality%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)operator !=(Point3D, Point3D)

Checks if any element of the points are unequal using != on each component. Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public static bool operator !=(Point3D p, Point3D q)
```

##### Parameters

| Type                                               | Name | Description             |
| -------------------------------------------------- | ---- | ----------------------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | p    | The point to compare    |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | q    | The point to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3D%5Fop%5FSubtraction%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)operator -(Point3D, Point3D)

Return a vector which is the difference of the two given points

##### Declaration

```
public static Vector3D operator -(Point3D arg0, Point3D arg1)
```

##### Parameters

| Type                                               | Name | Description |
| -------------------------------------------------- | ---- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | arg0 |             |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | arg1 |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic.