# Class Surface 

A Surface is composed of Polygons. The Polygons of a Surface must be connected. Adjacent coplanar Polygons must not form a "T" with their shared edges. The Polygons of a Surface typically enclose a volume, have no overlaps, and touch only at Edges.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Surface

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class Surface
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5F%5Fctor)Surface()

Create an empty Surface.

##### Declaration

```
public Surface()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPolygonList%5F)Surface(PolygonList)

Create a Surface from Polygons.

##### Declaration

```
public Surface(PolygonList polygons)
```

##### Parameters

| Type                                                       | Name     | Description                                                    |
| ---------------------------------------------------------- | -------- | -------------------------------------------------------------- |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html) | polygons | polygons is a list of Polygons from which to create a surface. |

##### Exceptions

| Type                                                                               | Condition                                                                     |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [InvalidPolygonException](DesignData.SDS2.Exceptions.InvalidPolygonException.html) | If edges of a Polygon are not coplanar or a Polygon has less than 2 vertices. |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPolygonList%5FSystem%5FBoolean%5F)Surface(PolygonList, bool)

Create a Surface from Polygons.

##### Declaration

```
public Surface(PolygonList polygons, bool updateGeometry)
```

##### Parameters

| Type                                                          | Name           | Description                                                                       |
| ------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------- |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html)    | polygons       | polygons is a list of Polygons from which to create a surface.                    |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | updateGeometry | UpdateGeometry() is called at the end of construction when updateGeometry is true |

##### Exceptions

| Type                                                                               | Condition                                                                     |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [InvalidPolygonException](DesignData.SDS2.Exceptions.InvalidPolygonException.html) | If edges of a Polygon are not coplanar or a Polygon has less than 2 vertices. |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FSurface%5F)Surface(Surface)

Create a Surface equal to the given Surface.

##### Declaration

```
public Surface(Surface surface)
```

##### Parameters

| Type                                               | Name    | Description                  |
| -------------------------------------------------- | ------- | ---------------------------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html) | surface | This is the Surface to copy. |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FBoundBLF)BoundBLF

This point is the bottom, left, front point of the Surface bounding box.

##### Declaration

```
public Point3D BoundBLF { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FBoundTRB)BoundTRB

This point is the top, right, back point of the Surface bounding box.

##### Declaration

```
public Point3D BoundTRB { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FIsValidGeometry)IsValidGeometry

Indicates BoundBLF and BoundTRB are valid.

##### Declaration

```
public bool IsValidGeometry { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FEquals%5FDesignData%5FSDS2%5FPrimitives%5FSurface%5FSystem%5FDouble%5F)Equals(Surface, double)

A Surface is composed of Polygons. The Polygons of a Surface must be connected. Adjacent coplanar Polygons must not form a "T" with their shared edges. The Polygons of a Surface typically enclose a volume, have no overlaps, and touch only at Edges.

##### Declaration

```
public bool Equals(Surface surface, double accy = 1.1920928955078125E-07)
```

##### Parameters

| Type                                                           | Name    | Description |
| -------------------------------------------------------------- | ------- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html)             | surface |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | accy    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FEquals%5FSystem%5FObject%5F)Equals(object)

A Surface is composed of Polygons. The Polygons of a Surface must be connected. Adjacent coplanar Polygons must not form a "T" with their shared edges. The Polygons of a Surface typically enclose a volume, have no overlaps, and touch only at Edges.

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FFinalize)\~Surface()

A Surface is composed of Polygons. The Polygons of a Surface must be connected. Adjacent coplanar Polygons must not form a "T" with their shared edges. The Polygons of a Surface typically enclose a volume, have no overlaps, and touch only at Edges.

##### Declaration

```
protected ~Surface()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FGetHashCode)GetHashCode()

A Surface is composed of Polygons. The Polygons of a Surface must be connected. Adjacent coplanar Polygons must not form a "T" with their shared edges. The Polygons of a Surface typically enclose a volume, have no overlaps, and touch only at Edges.

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FGetPolygons)GetPolygons()

Get the list of Polygons that comprise the Surface.

##### Declaration

```
public PolygonList GetPolygons()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FTransform%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5F)Transform(Matrix)

Transform the Surface to a new coordinate system.

##### Declaration

```
public void Transform(Matrix matrix)
```

##### Parameters

| Type                                             | Name   | Description                                              |
| ------------------------------------------------ | ------ | -------------------------------------------------------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | matrix | This is the matrix specfiying the new coordinate system. |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FTriangulate)Triangulate()

Decompose Polygons into triangles.

##### Declaration

```
public void Triangulate()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FUpdateGeometry)UpdateGeometry()

Update bounding box and Polygon plane fields.

##### Declaration

```
public void UpdateGeometry()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FValidate)Validate()

Analyze the surface for errors and fix them if possible.

##### Declaration

```
public string Validate()
```

##### Returns

| Type                                                           | Description                       |
| -------------------------------------------------------------- | --------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | Analysis of errors in the Surface |

##### Remarks

This method is slow and should typically be used only for debugging purposes, and not in production code. The content and format of the returned analysis string may not be consistent between SDS2 versions.

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FValidate%5FSystem%5FString%5F)Validate(string)

Analyze the surface for errors and fix them if possible.

##### Declaration

```
public string Validate(string prefix)
```

##### Parameters

| Type                                                           | Name   | Description                                                                                                                                           |
| -------------------------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | prefix | prefix is added to the beginning of most lines of the analysis. This is useful for distinguishing between surfaces when validating multiple surfaces. |

##### Returns

| Type                                                           | Description                       |
| -------------------------------------------------------------- | --------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | Analysis of errors in the Surface |

##### Remarks

This method is slow and should typically be used only for debugging purposes, and not in production code. The content and format of the returned analysis string may not be consistent between SDS2 versions.

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurface%5FValidate%5FSystem%5FString%5FSystem%5FBoolean%5F)Validate(string, bool)

Analyze the surface for errors and fix them if possible.

##### Declaration

```
public string Validate(string prefix, bool verbose)
```

##### Parameters

| Type                                                           | Name    | Description                                                                                                                                           |
| -------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | prefix  | prefix is added to the beginning of most lines of the analysis. This is useful for distinguishing between surfaces when validating multiple surfaces. |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | verbose | Output updated polygons for each error.                                                                                                               |

##### Returns

| Type                                                           | Description                       |
| -------------------------------------------------------------- | --------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | Analysis of errors in the Surface |

##### Remarks

This method is slow and should typically be used only for debugging purposes, and not in production code. The content and format of the returned analysis string may not be consistent between SDS2 versions.