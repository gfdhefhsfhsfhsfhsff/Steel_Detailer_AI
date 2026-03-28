# Class Polygon 

A Polygon is piece of Surface and is composed of Edges. A Polygon must not be self-crossing and must have all its edges in a single plane.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Polygon

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class Polygon
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5F)Polygon(EdgeList)

Create a Polygon for a Surface.

##### Declaration

```
public Polygon(EdgeList edges)
```

##### Parameters

| Type                                                 | Name  | Description                                       |
| ---------------------------------------------------- | ----- | ------------------------------------------------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html) | edges | The sequence of Edges that comprise this Polygon. |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5FSystem%5FString%5F)Polygon(EdgeList, string)

Create a Polygon for a Surface.

##### Declaration

```
public Polygon(EdgeList edges, string hexcolor)
```

##### Parameters

| Type                                                           | Name     | Description                                                                        |
| -------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)           | edges    | The sequence of Edges that comprise this Polygon.                                  |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | hexcolor | A string beginning with "#" followed by six hexidecimal digits specifying a color. |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5FSystem%5FString%5FSystem%5FInt32%5F)Polygon(EdgeList, string, int)

Create a Polygon for a Surface.

##### Declaration

```
public Polygon(EdgeList edges, string hexcolor, int faceNumber)
```

##### Parameters

| Type                                                           | Name       | Description                                                                                                                 |
| -------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)           | edges      | The sequence of Edges that comprise this Polygon.                                                                           |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | hexcolor   | A string beginning with "#" followed by six hexidecimal digits specifying a color.                                          |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | faceNumber | FaceNumber is an integer specifying what face the polygon is a part of. If the polygon is not on any face, FaceNumber is 0. |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5FSystem%5FString%5FSystem%5FInt32%5FSystem%5FInt32%5F)Polygon(EdgeList, string, int, int)

Create a Polygon for a Surface.

##### Declaration

```
public Polygon(EdgeList edges, string hexcolor, int faceNumber, int neutralSurface)
```

##### Parameters

| Type                                                           | Name           | Description                                                                                                                 |
| -------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)           | edges          | The sequence of Edges that comprise this Polygon.                                                                           |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | hexcolor       | A string beginning with "#" followed by six hexidecimal digits specifying a color.                                          |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | faceNumber     | FaceNumber is an integer specifying what face the polygon is a part of. If the polygon is not on any face, FaceNumber is 0. |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | neutralSurface | Specifies which neutral axis the polygon belongs to, if any.                                                                |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5FSystem%5FString%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FBoolean%5F)Polygon(EdgeList, string, int, int, bool)

Create a Polygon for a Surface.

##### Declaration

```
public Polygon(EdgeList edges, string hexcolor, int faceNumber, int neutralSurface, bool radiusSurface)
```

##### Parameters

| Type                                                           | Name           | Description                                                                                                                 |
| -------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)           | edges          | The sequence of Edges that comprise this Polygon.                                                                           |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | hexcolor       | A string beginning with "#" followed by six hexidecimal digits specifying a color.                                          |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | faceNumber     | FaceNumber is an integer specifying what face the polygon is a part of. If the polygon is not on any face, FaceNumber is 0. |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | neutralSurface | Specifies which neutral axis the polygon belongs to, if any.                                                                |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | radiusSurface  | Indicates if the polygon is part of a curve.                                                                                |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5FSystem%5FString%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FBoolean%5FSystem%5FInt32%5F)Polygon(EdgeList, string, int, int, bool, int)

Create a Polygon for a Surface.

##### Declaration

```
public Polygon(EdgeList edges, string hexcolor, int faceNumber, int neutralSurface, bool radiusSurface, int surfaceType)
```

##### Parameters

| Type                                                           | Name           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)           | edges          | The sequence of Edges that comprise this Polygon.                                                                                                                                                  |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | hexcolor       | A string beginning with "#" followed by six hexidecimal digits specifying a color.                                                                                                                 |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | faceNumber     | FaceNumber is an integer specifying what face the polygon is a part of. If the polygon is not on any face, FaceNumber is 0.                                                                        |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | neutralSurface | Specifies which neutral axis the polygon belongs to, if any.                                                                                                                                       |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | radiusSurface  | Indicates if the polygon is part of a curve.                                                                                                                                                       |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | surfaceType    | SurfaceType is an integer indicating the polygon is an inside surface (1), cap (2), cross section(3), pattern (4), weld (5), hole face (6), hole side (8), neutral axis (7), or none of these (0). |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5FSystem%5FString%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FBoolean%5FSystem%5FInt32%5FSystem%5FInt32%5F)Polygon(EdgeList, string, int, int, bool, int, int)

Create a Polygon for a Surface.

##### Declaration

```
public Polygon(EdgeList edges, string hexcolor, int faceNumber, int neutralSurface, bool radiusSurface, int surfaceType, int intensity)
```

##### Parameters

| Type                                                           | Name           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)           | edges          | The sequence of Edges that comprise this Polygon.                                                                                                                                                  |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | hexcolor       | A string beginning with "#" followed by six hexidecimal digits specifying a color.                                                                                                                 |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | faceNumber     | FaceNumber is an integer specifying what face the polygon is a part of. If the polygon is not on any face, FaceNumber is 0.                                                                        |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | neutralSurface | Specifies which neutral axis the polygon belongs to, if any.                                                                                                                                       |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | radiusSurface  | Indicates if the polygon is part of a curve.                                                                                                                                                       |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | surfaceType    | SurfaceType is an integer indicating the polygon is an inside surface (1), cap (2), cross section(3), pattern (4), weld (5), hole face (6), hole side (8), neutral axis (7), or none of these (0). |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | intensity      | Specifies color intensity.                                                                                                                                                                         |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5FSystem%5FString%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FBoolean%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FInt32%5F)Polygon(EdgeList, string, int, int, bool, int, int, int)

Create a Polygon for a Surface.

##### Declaration

```
public Polygon(EdgeList edges, string hexcolor, int faceNumber, int neutralSurface, bool radiusSurface, int surfaceType, int intensity, int cutOperation)
```

##### Parameters

| Type                                                           | Name           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)           | edges          | The sequence of Edges that comprise this Polygon.                                                                                                                                                  |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | hexcolor       | A string beginning with "#" followed by six hexidecimal digits specifying a color.                                                                                                                 |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | faceNumber     | FaceNumber is an integer specifying what face the polygon is a part of. If the polygon is not on any face, FaceNumber is 0.                                                                        |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | neutralSurface | Specifies which neutral axis the polygon belongs to, if any.                                                                                                                                       |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | radiusSurface  | Indicates if the polygon is part of a curve.                                                                                                                                                       |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | surfaceType    | SurfaceType is an integer indicating the polygon is an inside surface (1), cap (2), cross section(3), pattern (4), weld (5), hole face (6), hole side (8), neutral axis (7), or none of these (0). |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | intensity      | Specifies color intensity.                                                                                                                                                                         |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | cutOperation   | Indicates the type of cut that created this polygon.                                                                                                                                               |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5FSystem%5FString%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FBoolean%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FBoolean%5F)Polygon(EdgeList, string, int, int, bool, int, int, int, bool)

Create a Polygon for a Surface.

##### Declaration

```
public Polygon(EdgeList edges, string hexcolor, int faceNumber, int neutralSurface, bool radiusSurface, int surfaceType, int intensity, int cutOperation, bool cutSurface)
```

##### Parameters

| Type                                                           | Name           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)           | edges          | The sequence of Edges that comprise this Polygon.                                                                                                                                                  |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | hexcolor       | A string beginning with "#" followed by six hexidecimal digits specifying a color.                                                                                                                 |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | faceNumber     | FaceNumber is an integer specifying what face the polygon is a part of. If the polygon is not on any face, FaceNumber is 0.                                                                        |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | neutralSurface | Specifies which neutral axis the polygon belongs to, if any.                                                                                                                                       |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | radiusSurface  | Indicates if the polygon is part of a curve.                                                                                                                                                       |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | surfaceType    | SurfaceType is an integer indicating the polygon is an inside surface (1), cap (2), cross section(3), pattern (4), weld (5), hole face (6), hole side (8), neutral axis (7), or none of these (0). |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | intensity      | Specifies color intensity.                                                                                                                                                                         |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | cutOperation   | Indicates the type of cut that created this polygon.                                                                                                                                               |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | cutSurface     | Indicates if the polygon is part of a surface created by a cut.                                                                                                                                    |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5FSystem%5FString%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FBoolean%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FBoolean%5FSystem%5FBoolean%5F)Polygon(EdgeList, string, int, int, bool, int, int, int, bool, bool)

Create a Polygon for a Surface.

##### Declaration

```
public Polygon(EdgeList edges, string hexcolor, int faceNumber, int neutralSurface, bool radiusSurface, int surfaceType, int intensity, int cutOperation, bool cutSurface, bool layout)
```

##### Parameters

| Type                                                           | Name           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)           | edges          | The sequence of Edges that comprise this Polygon.                                                                                                                                                  |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | hexcolor       | A string beginning with "#" followed by six hexidecimal digits specifying a color.                                                                                                                 |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | faceNumber     | FaceNumber is an integer specifying what face the polygon is a part of. If the polygon is not on any face, FaceNumber is 0.                                                                        |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | neutralSurface | Specifies which neutral axis the polygon belongs to, if any.                                                                                                                                       |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | radiusSurface  | Indicates if the polygon is part of a curve.                                                                                                                                                       |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | surfaceType    | SurfaceType is an integer indicating the polygon is an inside surface (1), cap (2), cross section(3), pattern (4), weld (5), hole face (6), hole side (8), neutral axis (7), or none of these (0). |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | intensity      | Specifies color intensity.                                                                                                                                                                         |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | cutOperation   | Indicates the type of cut that created this polygon.                                                                                                                                               |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | cutSurface     | Indicates if the polygon is part of a surface created by a cut.                                                                                                                                    |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | layout         | Indicates if the polygon specifies a layout.                                                                                                                                                       |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FA)A

A is a coefficient of the plane equation specifying the plane that the polygon is in.

##### Declaration

```
public double A { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FB)B

B is a coefficient of the plane equation specifying the plane that the polygon is in.

##### Declaration

```
public double B { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FBoundBLF)BoundBLF

This point is the bottom, left, front point of the Polygon bounding box.

##### Declaration

```
public Point3D BoundBLF { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FBoundTRB)BoundTRB

This point is the top, right, back point of the Polygon bounding box.

##### Declaration

```
public Point3D BoundTRB { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FC)C

C is a coefficient of the plane equation specifying the plane that the polygon is in.

##### Declaration

```
public double C { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FCutOperation)CutOperation

CutOperation indicates the type of cut that created this polygon: CUT\_{NONE,BURN,SAW,SHEAR,SQUARE,MILL,GENERIC}

##### Declaration

```
public int CutOperation { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FD)D

D is a coefficient of the plane equation specifying the plane that the polygon is in.

##### Declaration

```
public double D { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FEdges)Edges

The sequence of Edges that comprise this Polygon.

##### Declaration

```
public EdgeList Edges { get; set; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FFaceNumber)FaceNumber

FaceNumber is an integer specifying what face the polygon is a part of. If the polygon is not on any face, FaceNumber is 0.

##### Declaration

```
public int FaceNumber { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FHexcolor)Hexcolor

Hexcolor is a string beginning with "#" followed by six hexidecimal digits specifying a color.

##### Declaration

```
public string Hexcolor { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FIntensity)Intensity

Intensity is an integer specifying color intensity.

##### Declaration

```
public int Intensity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FIsCutSurface)IsCutSurface

IsCutSurface indicates if the polygon is part of a cut.

##### Declaration

```
public bool IsCutSurface { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FIsLayout)IsLayout

IsLayout indicates if the polygon specifies a layout.

##### Declaration

```
public bool IsLayout { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FIsRadiusSurface)IsRadiusSurface

IsRadiusSurface indicates if the polygon is part of a curve.

##### Declaration

```
public bool IsRadiusSurface { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FIsValidGeometry)IsValidGeometry

Indicates if A, B, C, D, BoundBLF, BoundTRB are valid.

##### Declaration

```
public bool IsValidGeometry { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FNeutralSurface)NeutralSurface

NeutralSurface specifies which neutral axis the polygon belongs to, if any.

##### Declaration

```
public int NeutralSurface { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FSurfaceType)SurfaceType

SurfaceType is an integer indicating the polygon is an inside surface (1), cap (2), cross section(3), pattern (4), weld (5), hole face (6), hole side (8), neutral axis (7), or none of these (0).

##### Declaration

```
public int SurfaceType { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FEquals%5FDesignData%5FSDS2%5FPrimitives%5FPolygon%5FSystem%5FDouble%5F)Equals(Polygon, double)

A Polygon is piece of Surface and is composed of Edges. A Polygon must not be self-crossing and must have all its edges in a single plane.

##### Declaration

```
public bool Equals(Polygon polygon, double accy = 1.1920928955078125E-07)
```

##### Parameters

| Type                                                           | Name    | Description |
| -------------------------------------------------------------- | ------- | ----------- |
| [Polygon](DesignData.SDS2.Primitives.Polygon.html)             | polygon |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | accy    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FEquals%5FSystem%5FObject%5F)Equals(object)

A Polygon is piece of Surface and is composed of Edges. A Polygon must not be self-crossing and must have all its edges in a single plane.

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FFinalize)\~Polygon()

A Polygon is piece of Surface and is composed of Edges. A Polygon must not be self-crossing and must have all its edges in a single plane.

##### Declaration

```
protected ~Polygon()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygon%5FGetHashCode)GetHashCode()

A Polygon is piece of Surface and is composed of Edges. A Polygon must not be self-crossing and must have all its edges in a single plane.

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