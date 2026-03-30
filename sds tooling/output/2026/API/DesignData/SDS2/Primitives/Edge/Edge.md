# Class Edge 

Edge represents the side of a Polygon. An Edge contains only the first point of the side; the second point is the point on the next edge of a Polygon.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Edge

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class Edge
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FUInt32%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FBoolean%5FSystem%5FBoolean%5F)Edge(Point3D, bool, bool, uint, int, int, bool, bool)

Create an Edge for a Polygon.

##### Declaration

```
public Edge(Point3D vertexLocation, bool noShort = true, bool onRadius = false, uint vertexName = 0, int edgeType = 0, int radiusNumber = 0, bool duplicate = false, bool fit = false)
```

##### Parameters

| Type                                                          | Name           | Description                                                                |
| ------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)            | vertexLocation | Assigned to first vertex of an Edge                                        |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | noShort        | Indicates the edge will not be shortened by the Shorten tool in Detailing. |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | onRadius       | Indicates edge is on a rounded surface.                                    |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32)  | vertexName     | A bit field containing information used by template detailing.             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | edgeType       | Typically 1 for lengthwise edges and 0 otherwise.                          |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | radiusNumber   | The number of an edge on a curved surface.                                 |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | duplicate      | Indicates a duplicate edge.                                                |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | fit            | Indicates an edge has been created by a cut or fit operation.              |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FEdgeType)EdgeType

Typically 1 for lengthwise edges and 0 otherwise.

##### Declaration

```
public int EdgeType { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FIsDuplicate)IsDuplicate

Indicates a duplicate edge. IsDuplicate edges are not drawn.

##### Declaration

```
public bool IsDuplicate { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FIsFitted)IsFitted

Indicates an edge has been created by a cut or fit operation.

##### Declaration

```
public bool IsFitted { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FIsNoShort)IsNoShort

Indicates the edge will not be shortened by the Shorten tool in Detailing.

##### Declaration

```
public bool IsNoShort { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FIsOnRadius)IsOnRadius

Indicates edge is on a rounded surface. For example, lengthwise edges in the K of a Wide Flange, but not edges in the K on cap polygons. IsOnRadius edges are not drawn.

##### Declaration

```
public bool IsOnRadius { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FRadiusNumber)RadiusNumber

Edges of a rounded surface may be numbered consecutively. For example, lengthwise edges in the K of a Wide Flange, but not edges in the K on cap polygons.

##### Declaration

```
public int RadiusNumber { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FVertexLocation)VertexLocation

VertexLocation is the location of the first vertex of an Edge. The second vertex is the vertex specified by the next Edge.

##### Declaration

```
public Point3D VertexLocation { get; set; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FVertexName)VertexName

A bit field containing information used by template detailing.

##### Declaration

```
public uint VertexName { get; set; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FEquals%5FDesignData%5FSDS2%5FPrimitives%5FEdge%5FSystem%5FDouble%5F)Equals(Edge, double)

Edge represents the side of a Polygon. An Edge contains only the first point of the side; the second point is the point on the next edge of a Polygon.

##### Declaration

```
public bool Equals(Edge edge, double accy = 1.1920928955078125E-07)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [Edge](DesignData.SDS2.Primitives.Edge.html)                   | edge |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | accy |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FEquals%5FSystem%5FObject%5F)Equals(object)

Edge represents the side of a Polygon. An Edge contains only the first point of the side; the second point is the point on the next edge of a Polygon.

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FFinalize)\~Edge()

Edge represents the side of a Polygon. An Edge contains only the first point of the side; the second point is the point on the next edge of a Polygon.

##### Declaration

```
protected ~Edge()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdge%5FGetHashCode)GetHashCode()

Edge represents the side of a Polygon. An Edge contains only the first point of the side; the second point is the point on the next edge of a Polygon.

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