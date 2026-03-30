# Class Vector2D 

The Vector2D class represents a vector in 2D space.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Vector2D

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class Vector2D
```

##### **Remarks**

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5F%5Fctor)Vector2D()

Instantiates a vector with X and Y set to zero

##### Declaration

```
public Vector2D()
```

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5F)Vector2D(Point2D)

Instantiates a vector with the same X and Y values as the given point

##### Declaration

```
public Vector2D(Point2D point)
```

##### Parameters

| Type                                               | Name  | Description                   |
| -------------------------------------------------- | ----- | ----------------------------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html) | point | The point whose value to copy |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)Vector2D(Vector2D)

Instantiates a vector equal to the given vector

##### Declaration

```
public Vector2D(Vector2D vector)
```

##### Parameters

| Type                                                 | Name   | Description                    |
| ---------------------------------------------------- | ------ | ------------------------------ |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | vector | The vector whose value to copy |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5F%5Fctor%5FSystem%5FDouble%5FSystem%5FDouble%5F)Vector2D(double, double)

Instantiates a vector with the given X and Y values

##### Declaration

```
public Vector2D(double x, double y)
```

##### Parameters

| Type                                                           | Name | Description                    |
| -------------------------------------------------------------- | ---- | ------------------------------ |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | x    | The X value for the new vector |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | y    | The Y value for the new vector |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FLength)Length

The length (magnitude) of this vector, or the distance from the origin to this vector

##### Declaration

```
public double Length { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FX)X

The X-coordinate of the vector

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FY)Y

The Y-coordinate of the vector

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

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FAngle%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)Angle(Vector2D)

Return the angle in radians from this vector to a given vector. The returned value is always within the range \[0,pi\].

##### Declaration

```
public double Angle(Vector2D pt)
```

##### Parameters

| Type                                                 | Name | Description      |
| ---------------------------------------------------- | ---- | ---------------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | pt   | The other vector |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FBinEquals%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FSystem%5FDouble%5F)BinEquals(Vector2D, double)

Returns true if this vector and the given vector fall within the same "bin". A "bin" is a cubic region of vector space approximately binSize on a side.

##### Declaration

```
public bool BinEquals(Vector2D other, double binSize)
```

##### Parameters

| Type                                                           | Name    | Description        |
| -------------------------------------------------------------- | ------- | ------------------ |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html)           | other   | The other vector   |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | binSize | The size of a bin. |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Unlike EpsilonEquals, BinEquals maintains the transitive rule of equality, but some vectors which are arbitrarily close together in distance are unequal accorind got EpsilonEquals, because they fall into different bins. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FBisector%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)Bisector(Vector2D)

Return a unit vector that bisects the two given vectors

##### Declaration

```
public Vector2D Bisector(Vector2D other)
```

##### Parameters

| Type                                                 | Name  | Description      |
| ---------------------------------------------------- | ----- | ---------------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | other | The other vector |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FDot%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)Dot(Vector2D)

Compute the dot product between this vector and another given vector,

##### Declaration

```
public double Dot(Vector2D pt)
```

##### Parameters

| Type                                                 | Name | Description      |
| ---------------------------------------------------- | ---- | ---------------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | pt   | The other vector |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FEpsilonEquals%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FSystem%5FDouble%5F)EpsilonEquals(Vector2D, double)

Returns true if the squared difference between this vector and the given vector is less than difference\_squared.

##### Declaration

```
public bool EpsilonEquals(Vector2D other, double differenceSquared)
```

##### Parameters

| Type                                                           | Name              | Description                                                                     |
| -------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html)           | other             | The other vector                                                                |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | differenceSquared | The square of the smallest difference value that should be considered different |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Note that EpsilonEquals can violate the transitivity rule of equality comparison, because there are many groups of points (p, q, r) where p.EpsilonEquals(q) and p.EpsilonEquals(r) but not q.EpsilonEquals(r). 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FEquals%5FSystem%5FObject%5F)Equals(object)

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FFinalize)\~Vector2D()

The Vector2D class represents a vector in 2D space.

##### Declaration

```
protected ~Vector2D()
```

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FGetHashCode)GetHashCode()

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FGetLength)GetLength()

The length (magnitude) of this vector, or the distance from the origin to this vector

##### Declaration

```
public double GetLength()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FGetX)GetX()

The X-coordinate of the vector

##### Declaration

```
public double GetX()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FGetY)GetY()

The Y-coordinate of the vector

##### Declaration

```
public double GetY()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FIsNearlyParallel%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FSystem%5FDouble%5F)IsNearlyParallel(Vector2D, double)

Return `true` when the absolute value of the tangent of the angle between the two vectors is less than `tan_tol`. For instance, if `tan_tol`is 0.01745, it tests that the vectors are within approximately 1 degree of parallel.

##### Declaration

```
public bool IsNearlyParallel(Vector2D other, double tan_tol)
```

##### Parameters

| Type                                                           | Name     | Description                                                                                                                                                            |
| -------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html)           | other    | The other vector                                                                                                                                                       |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | tan\_tol | The tangent of the angle that specifies the desired tolerance. Note that for small angles x, tan x \~= x, so you can also think of this nearly a tolerance in radians. |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Note that vectors in the exact opposite direction are considered "parallel" for the purposes of this test. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FIsNearlyPerpendicular%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FSystem%5FDouble%5F)IsNearlyPerpendicular(Vector2D, double)

Return `true` when the tangent of the difference between the vectors' angles and a right angle is within less than `tan_tol`. For instance, if tan\_tol is 0.01745, it tests that the vectors are within approximately 1 degree of perpendicular.

##### Declaration

```
public bool IsNearlyPerpendicular(Vector2D other, double tan_tol)
```

##### Parameters

| Type                                                           | Name     | Description                                                                                                                                                            |
| -------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html)           | other    | The other vector                                                                                                                                                       |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | tan\_tol | The tangent of the angle that specifies the desired tolerance. Note that for small angles x, tan x \~= x, so you can also think of this nearly a tolerance in radians. |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FNormalize)Normalize()

Return a vector with the same direction as this vector, but with length 1.0.

##### Declaration

```
public Vector2D Normalize()
```

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) |             |

##### Remarks

Note: If the vector is a zero-vector or any element is not a finite value, the result is undefined. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FScalarProjection%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)ScalarProjection(Vector2D)

Returns the scalar projection of this vector onto `other`

##### Declaration

```
public double ScalarProjection(Vector2D other)
```

##### Parameters

| Type                                                 | Name  | Description      |
| ---------------------------------------------------- | ----- | ---------------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | other | The other vector |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FToString)ToString()

Formats the point into a string. Note that because the values are rounded for display, parsing them to retrieve the X and Y values will not necessarily yield the same point.

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5FVectorProjection%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)VectorProjection(Vector2D)

Returns the vector projection of this vector onto `other`

##### Declaration

```
public Vector2D VectorProjection(Vector2D other)
```

##### Parameters

| Type                                                 | Name  | Description      |
| ---------------------------------------------------- | ----- | ---------------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | other | The other vector |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FAddition%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)operator +(Point2D, Vector2D)

Return a point which is the sum of the given point and given vector

##### Declaration

```
public static Point2D operator +(Point2D arg0, Vector2D arg1)
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html)   | arg0 |             |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | arg1 |             |

##### Returns

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FAddition%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5F)operator +(Vector2D, Point2D)

Return a point which is the sum of the given point and given vector

##### Declaration

```
public static Point2D operator +(Vector2D arg0, Point2D arg1)
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | arg0 |             |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html)   | arg1 |             |

##### Returns

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FAddition%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)operator +(Vector2D, Vector2D)

Return a vector which is the sum of the two given vectors

##### Declaration

```
public static Vector2D operator +(Vector2D arg0, Vector2D arg1)
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | arg0 |             |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | arg1 |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FDivision%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FSystem%5FDouble%5F)operator /(Vector2D, double)

Return a vector with each element divided by the given scalar

##### Declaration

```
public static Vector2D operator /(Vector2D arg0, double arg1)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html)           | arg0 |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | arg1 |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FEquality%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)operator ==(Vector2D, Vector2D)

Checks if each element of the points are equal using == on each component. Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public static bool operator ==(Vector2D p, Vector2D q)
```

##### Parameters

| Type                                                 | Name | Description             |
| ---------------------------------------------------- | ---- | ----------------------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | p    | The point to compare    |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | q    | The point to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FInequality%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)operator !=(Vector2D, Vector2D)

Checks if any element of the points are unequal using != on each component. Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public static bool operator !=(Vector2D p, Vector2D q)
```

##### Parameters

| Type                                                 | Name | Description             |
| ---------------------------------------------------- | ---- | ----------------------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | p    | The point to compare    |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | q    | The point to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FMultiply%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FSystem%5FDouble%5F)operator \*(Vector2D, double)

Return a vector with each element multiplied by the given scalar

##### Declaration

```
public static Vector2D operator *(Vector2D arg0, double arg1)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html)           | arg0 |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | arg1 |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FMultiply%5FSystem%5FDouble%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)operator \*(double, Vector2D)

Return a vector with each element multiplied by the given scalar

##### Declaration

```
public static Vector2D operator *(double lhs, Vector2D rhs)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | lhs  |             |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html)           | rhs  |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FSubtraction%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)operator -(Point2D, Vector2D)

Return a point which is the difference of the given point and given vector

##### Declaration

```
public static Point2D operator -(Point2D arg0, Vector2D arg1)
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html)   | arg0 |             |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | arg1 |             |

##### Returns

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FSubtraction%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)operator -(Vector2D, Vector2D)

Return a vector which is the difference of the two given vectors

##### Declaration

```
public static Vector2D operator -(Vector2D arg0, Vector2D arg1)
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | arg0 |             |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | arg1 |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FVector2D%5Fop%5FUnaryNegation%5FDesignData%5FSDS2%5FPrimitives%5FVector2D%5F)operator -(Vector2D)

Return the element-wise negation of the vector

##### Declaration

```
public static Vector2D operator -(Vector2D p)
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) | p    |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector2D](DesignData.SDS2.Primitives.Vector2D.html) |             |

##### Remarks

Note that intermediate arithmetic is done in floating point, and thus some operations may have intermediate results that overflow, underflow or experience cancellation error, like all floating-point arithmetic.