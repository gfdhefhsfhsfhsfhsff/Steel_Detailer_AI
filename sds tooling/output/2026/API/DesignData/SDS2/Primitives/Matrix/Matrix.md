# Class Matrix 

The Matrix class represents a transformation matrix.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Matrix

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class Matrix
```

##### **Remarks**

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5F%5Fctor)Matrix()

Create an identity matrix.

##### Declaration

```
public Matrix()
```

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5F)Matrix(Matrix)

Create a matrix equal to the given matrix

##### Declaration

```
public Matrix(Matrix arg0)
```

##### Parameters

| Type                                             | Name | Description |
| ------------------------------------------------ | ---- | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | arg0 |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FOrigin)Origin

Get the coordinate system origin.

##### Declaration

```
public Point3D Origin { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FXAxis)XAxis

Get the coordinate system X axis.

##### Declaration

```
public Vector3D XAxis { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FYAxis)YAxis

Get the coordinate system Y axis.

##### Declaration

```
public Vector3D YAxis { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FZAxis)ZAxis

Get the coordinate system Z axis.

##### Declaration

```
public Vector3D ZAxis { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FBetweenSystems%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5F)BetweenSystems(Matrix, Matrix)

Create a transformation matrix from the first coordinate system to the second coordinate system

##### Declaration

```
public static Matrix BetweenSystems(Matrix from, Matrix to)
```

##### Parameters

| Type                                             | Name | Description                  |
| ------------------------------------------------ | ---- | ---------------------------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | from | The "from" coordinate system |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | to   | The "to" coordinate system   |

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FBinEquals%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5FSystem%5FDouble%5F)BinEquals(Matrix, double)

Returns BinEquals() on each sub component of the matrix

##### Declaration

```
public bool BinEquals(Matrix other, double binSize)
```

##### Parameters

| Type                                                           | Name    | Description        |
| -------------------------------------------------------------- | ------- | ------------------ |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html)               | other   | The other matrix   |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | binSize | The size of a bin. |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Unlike EpsilonEquals, BinEquals maintains the transitive rule of equality. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FEpsilonEquals%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5FSystem%5FDouble%5F)EpsilonEquals(Matrix, double)

Returns EpsilonEquals() on each sub component of the matrix

##### Declaration

```
public bool EpsilonEquals(Matrix other, double distanceSquared)
```

##### Parameters

| Type                                                           | Name            | Description                                                                   |
| -------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html)               | other           | The other matrix                                                              |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | distanceSquared | The square of the smallest distance value that should be considered different |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Note that EpsilonEquals can violate the transitivity rule of equality comparison, because there are many groups of matrices (p, q, r) where p.EpsilonEquals(q) and p.EpsilonEquals(r) but not q.EpsilonEquals(r). 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FEquals%5FSystem%5FObject%5F)Equals(object)

Checks if each element of the matrix are equal using Equals on each component. Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public override bool Equals(object obj)
```

##### Parameters

| Type                                                           | Name | Description              |
| -------------------------------------------------------------- | ---- | ------------------------ |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | obj  | The matrix to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FFinalize)\~Matrix()

The Matrix class represents a transformation matrix.

##### Declaration

```
protected ~Matrix()
```

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FGetHashCode)GetHashCode()

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

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FInverse)Inverse()

Return the inverse of this matrix

##### Declaration

```
public Matrix Inverse()
```

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FMirrorZ)MirrorZ()

Create a Matrix mirrored about the XY plane.

##### Declaration

```
public static Matrix MirrorZ()
```

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FRotation%5FSystem%5FDouble%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5F)Rotation(double, Vector3D)

Create a rotation matrix

##### Declaration

```
public static Matrix Rotation(double angle, Vector3D axis)
```

##### Parameters

| Type                                                           | Name  | Description                          |
| -------------------------------------------------------------- | ----- | ------------------------------------ |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | angle | Counterclockwise rotation in radians |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html)           | axis  | Axis of rotation                     |

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FToCoordinateSystemXY%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5F)ToCoordinateSystemXY(Point3D, Vector3D, Vector3D)

Create a coordinate system from X axis, Y axis, and origin location.

##### Declaration

```
public static Matrix ToCoordinateSystemXY(Point3D origin, Vector3D xAxis, Vector3D yAxis)
```

##### Parameters

| Type                                                 | Name   | Description                                                                |
| ---------------------------------------------------- | ------ | -------------------------------------------------------------------------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)   | origin | The origin for the coordinate system                                       |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) | xAxis  | The X axis for the coordinate system, a unit vector                        |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) | yAxis  | The Y axis for the coordinate system, a unit vector perpendicular to XAxis |

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

Note that the X and Y axes must be perpendicular unit vectors to within about 1 part in 1e-7

##### Exceptions

| Type                                                                           | Condition                                             |
| ------------------------------------------------------------------------------ | ----------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | If basis vectors are not normalized or perpendicular. |

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FToString)ToString()

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

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FTranslation%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)Translation(Point3D)

Create a translation matrix

##### Declaration

```
public static Matrix Translation(Point3D origin)
```

##### Parameters

| Type                                               | Name   | Description                               |
| -------------------------------------------------- | ------ | ----------------------------------------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | origin | The translation applied by the new matrix |

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FXRotation%5FSystem%5FDouble%5F)XRotation(double)

Create a rotation matrix around the X axis

##### Declaration

```
public static Matrix XRotation(double angle)
```

##### Parameters

| Type                                                           | Name  | Description                          |
| -------------------------------------------------------------- | ----- | ------------------------------------ |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | angle | Counterclockwise rotation in radians |

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FYRotation%5FSystem%5FDouble%5F)YRotation(double)

Create a rotation matrix around the Y axis

##### Declaration

```
public static Matrix YRotation(double angle)
```

##### Parameters

| Type                                                           | Name  | Description                          |
| -------------------------------------------------------------- | ----- | ------------------------------------ |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | angle | Counterclockwise rotation in radians |

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5FZRotation%5FSystem%5FDouble%5F)ZRotation(double)

Create a rotation matrix around the Z axis

##### Declaration

```
public static Matrix ZRotation(double angle)
```

##### Parameters

| Type                                                           | Name  | Description                          |
| -------------------------------------------------------------- | ----- | ------------------------------------ |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | angle | Counterclockwise rotation in radians |

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5Fop%5FEquality%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5F)operator ==(Matrix, Matrix)

Checks if each element of the matrices are equal using == on each component. Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public static bool operator ==(Matrix a, Matrix b)
```

##### Parameters

| Type                                             | Name | Description              |
| ------------------------------------------------ | ---- | ------------------------ |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | a    | The matrix to compare    |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | b    | The matrix to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5Fop%5FInequality%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5F)operator !=(Matrix, Matrix)

Checks if any element of the matrices are unequal using != on each component. Note that this is an "exact" comparison method, and only appropriate in special circumstances.

##### Declaration

```
public static bool operator !=(Matrix a, Matrix b)
```

##### Parameters

| Type                                             | Name | Description              |
| ------------------------------------------------ | ---- | ------------------------ |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | a    | The matrix to compare    |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | b    | The matrix to compare to |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5Fop%5FMultiply%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5F)operator \*(Matrix, Matrix)

Return a new matrix which composes the two matrices

##### Declaration

```
public static Matrix operator *(Matrix arg0, Matrix arg1)
```

##### Parameters

| Type                                             | Name | Description |
| ------------------------------------------------ | ---- | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | arg0 |             |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | arg1 |             |

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5Fop%5FMultiply%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)operator \*(Matrix, Point3D)

Return the point transformed by the matrix

##### Declaration

```
public static Point3D operator *(Matrix arg0, Point3D arg1)
```

##### Parameters

| Type                                               | Name | Description |
| -------------------------------------------------- | ---- | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html)   | arg0 |             |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | arg1 |             |

##### Returns

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations. 

#### [](#DesignData%5FSDS2%5FPrimitives%5FMatrix%5Fop%5FMultiply%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5F)operator \*(Matrix, Vector3D)

Return the vector transformed by the matrix

##### Declaration

```
public static Vector3D operator *(Matrix arg0, Vector3D arg1)
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html)     | arg0 |             |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) | arg1 |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

##### Remarks

A Matrix has 4x3 floating point elements, and many routines exhibit undefined behavior if the elements of the matrix cannot be composed into a combination of rotations and translations.