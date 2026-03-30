# Namespace DesignData.SDS2.Primitives 

### [](#classes)Classes 

#### [](#boundingbox2d)[BoundingBox2D](DesignData.SDS2.Primitives.BoundingBox2D.html)

The BoundingBox2D class represents the axis-aligned area enclosed by a two points in 2D space.

#### [](#boundingbox3d)[BoundingBox3D](DesignData.SDS2.Primitives.BoundingBox3D.html)

The BoundingBox3D class represents the axis-aligned area enclosed by a two points in 3D space.

#### [](#color)[Color](DesignData.SDS2.Primitives.Color.html)

A color compatible with SDS2's colors. This object knows how to translate to and from SDS2 pen numbers. It works on a 0-255 rgba color scale.

#### [](#doublelist)[DoubleList](DesignData.SDS2.Primitives.DoubleList.html)

#### [](#doublelist-doublelistenumerator)[DoubleList.DoubleListEnumerator](DesignData.SDS2.Primitives.DoubleList.DoubleListEnumerator.html)

#### [](#edge)[Edge](DesignData.SDS2.Primitives.Edge.html)

Edge represents the side of a Polygon. An Edge contains only the first point of the side; the second point is the point on the next edge of a Polygon.

#### [](#edgelist)[EdgeList](DesignData.SDS2.Primitives.EdgeList.html)

#### [](#edgelist-edgelistenumerator)[EdgeList.EdgeListEnumerator](DesignData.SDS2.Primitives.EdgeList.EdgeListEnumerator.html)

#### [](#layout3d)[Layout3D](DesignData.SDS2.Primitives.Layout3D.html)

Represents a list of points in 3-dimensional space, in order, often forming a closed loop.

#### [](#layout3dnode)[Layout3DNode](DesignData.SDS2.Primitives.Layout3DNode.html)

Represents one node in a Layout3D

#### [](#matrix)[Matrix](DesignData.SDS2.Primitives.Matrix.html)

The Matrix class represents a transformation matrix.

#### [](#point2d)[Point2D](DesignData.SDS2.Primitives.Point2D.html)

The Point2D class can represent a position in 2D space, or a vector in 2D space. Some operations assume that the interpretation is a vector.

#### [](#point2dlist)[Point2DList](DesignData.SDS2.Primitives.Point2DList.html)

#### [](#point2dlist-point2dlistenumerator)[Point2DList.Point2DListEnumerator](DesignData.SDS2.Primitives.Point2DList.Point2DListEnumerator.html)

#### [](#point3d)[Point3D](DesignData.SDS2.Primitives.Point3D.html)

The Point3D class can represent a position in 3D space, or a vector in 3D space. Some operations assume that the interpretation is a vector.

#### [](#point3dlist)[Point3DList](DesignData.SDS2.Primitives.Point3DList.html)

#### [](#point3dlist-point3dlistenumerator)[Point3DList.Point3DListEnumerator](DesignData.SDS2.Primitives.Point3DList.Point3DListEnumerator.html)

#### [](#polygon)[Polygon](DesignData.SDS2.Primitives.Polygon.html)

A Polygon is piece of Surface and is composed of Edges. A Polygon must not be self-crossing and must have all its edges in a single plane.

#### [](#polygonlist)[PolygonList](DesignData.SDS2.Primitives.PolygonList.html)

#### [](#polygonlist-polygonlistenumerator)[PolygonList.PolygonListEnumerator](DesignData.SDS2.Primitives.PolygonList.PolygonListEnumerator.html)

#### [](#stringlist)[StringList](DesignData.SDS2.Primitives.StringList.html)

#### [](#stringlist-stringlistenumerator)[StringList.StringListEnumerator](DesignData.SDS2.Primitives.StringList.StringListEnumerator.html)

#### [](#surface)[Surface](DesignData.SDS2.Primitives.Surface.html)

A Surface is composed of Polygons. The Polygons of a Surface must be connected. Adjacent coplanar Polygons must not form a "T" with their shared edges. The Polygons of a Surface typically enclose a volume, have no overlaps, and touch only at Edges.

#### [](#utility)[Utility](DesignData.SDS2.Primitives.Utility.html)

#### [](#vector2d)[Vector2D](DesignData.SDS2.Primitives.Vector2D.html)

The Vector2D class represents a vector in 2D space.

#### [](#vector3d)[Vector3D](DesignData.SDS2.Primitives.Vector3D.html)

The Vector3D class represents a vector in 3D space.

### [](#enums)Enums 

#### [](#pencolor)[PenColor](DesignData.SDS2.Primitives.PenColor.html)

Pens tied to specific SDS2 colors.