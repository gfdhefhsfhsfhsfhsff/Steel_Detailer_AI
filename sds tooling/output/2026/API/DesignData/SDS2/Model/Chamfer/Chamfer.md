# Class Chamfer 

A class representing a chamfer segment

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Chamfer

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
public sealed class Chamfer
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5F%5Fctor)Chamfer()

A class representing a chamfer segment

##### Declaration

```
public Chamfer()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FAngle)Angle

Leftmost, deepest point of the chamfer

##### Declaration

```
public double Angle { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FDepth)Depth

Depth dimension of the chamfer

##### Declaration

```
public double Depth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FDepthDirection)DepthDirection

Unit vector in the direction of the chamfer depth for a straight edge chamfer

##### Declaration

```
public Vector3D DepthDirection { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FIsRadiusChamfer)IsRadiusChamfer

True when the chamfer represents a chamfer along a radiused edge, like the end of a pipe or hss tube

##### Declaration

```
public bool IsRadiusChamfer { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FLeft)Left

Leftmost point of the chamfer segment

##### Declaration

```
public Point3D Left { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FRadiusCenterPoint)RadiusCenterPoint

A center radius point for chamfers on a radius, if it exists (see IsRadiusChamfer). Otherwise this point should be ignored.

##### Declaration

```
public Point3D RadiusCenterPoint { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FRight)Right

Rightmost point of the chamfer segment

##### Declaration

```
public Point3D Right { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FRootFace)RootFace

Root face of the chamfer

##### Declaration

```
public double RootFace { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FWidth)Width

Width dimension of the chamfer

##### Declaration

```
public double Width { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FWidthDirection)WidthDirection

Unit vector in the direction of the chamfer width for a straight edge chamfer

##### Declaration

```
public Vector3D WidthDirection { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FFinalize)\~Chamfer()

A class representing a chamfer segment

##### Declaration

```
protected ~Chamfer()
```

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FTransform%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5F)Transform(Matrix)

Transform the chamfer points by the transformation matrix

##### Declaration

```
public void Transform(Matrix matrix)
```

##### Parameters

| Type                                             | Name   | Description |
| ------------------------------------------------ | ------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | matrix |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamfer%5FTransformed%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5F)Transformed(Matrix)

Return a new chamfer that is transformed by the transformation matrix

##### Declaration

```
public Chamfer Transformed(Matrix matrix)
```

##### Parameters

| Type                                             | Name   | Description |
| ------------------------------------------------ | ------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | matrix |             |

##### Returns

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [Chamfer](DesignData.SDS2.Model.Chamfer.html) |             |