# Class Layout3DNode 

Represents one node in a Layout3D

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Layout3DNode

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class Layout3DNode
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5F%5Fctor)Layout3DNode()

Create an empty Layout3DNode

##### Declaration

```
public Layout3DNode()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FSystem%5FUInt32%5FSystem%5FUInt32%5FSystem%5FBoolean%5FSystem%5FDouble%5FSystem%5FInt32%5F)Layout3DNode(Point3D, uint, uint, bool, double, int)

Create a layout node from existing data

##### Declaration

```
public Layout3DNode(Point3D point, uint name = 0, uint face = 0, bool isInteriorEdge = false, double radius = 0, int segmentCount = 0)
```

##### Parameters

| Type                                                           | Name           | Description |
| -------------------------------------------------------------- | -------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)             | point          |             |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32)   | name           |             |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32)   | face           |             |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | isInteriorEdge |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | radius         |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | segmentCount   |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FDepth)Depth

The direction of depth for the layout between the current and next node. Typically this should be perpendicular to the segment

##### Declaration

```
public Vector3D Depth { get; set; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FFace)Face

Represents one node in a Layout3D

##### Declaration

```
public uint Face { get; set; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FIsInteriorEdge)IsInteriorEdge

Represents one node in a Layout3D

##### Declaration

```
public bool IsInteriorEdge { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FName)Name

The "name" of the vertex generated for detailing purposes. Inside detailing templates, this vertex can be referred to by this numeric identifier

##### Declaration

```
public uint Name { get; set; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FPoint)Point

The point, in 3-dimensional space, that this node exists at

##### Declaration

```
public Point3D Point { get; set; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FRadius)Radius

When set, this makes this a radiused corner with a radius of radius. The final layout will be segmented to approximate this radius.

##### Declaration

```
public double Radius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Don't forget to set SegmentCount to something greater than 1

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FSegmentCount)SegmentCount

The number of segments to use for this radiused corner

##### Declaration

```
public int SegmentCount { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FEquals%5FSystem%5FObject%5F)Equals(object)

Represents one node in a Layout3D

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FFinalize)\~Layout3DNode()

Represents one node in a Layout3D

##### Declaration

```
protected ~Layout3DNode()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FGetHashCode)GetHashCode()

Represents one node in a Layout3D

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5FTransform%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5F)Transform(Matrix)

Move and rotate this node using the given matrix

##### Declaration

```
public void Transform(Matrix transformation)
```

##### Parameters

| Type                                             | Name           | Description |
| ------------------------------------------------ | -------------- | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | transformation |             |