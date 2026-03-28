# Class Layout3D 

Represents a list of points in 3-dimensional space, in order, often forming a closed loop.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Layout3D

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class Layout3D : IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5F%5Fctor)Layout3D()

An empty layout

##### Declaration

```
public Layout3D()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FCount)Count

The number of nodes in this layout

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FItem%5FSystem%5FInt32%5F)this\[int\]

Get the node at index

##### Declaration

```
public Layout3DNode this[int index] { get; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [Layout3DNode](DesignData.SDS2.Primitives.Layout3DNode.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FLayoutLength)LayoutLength

Gets the sum of the length of every side of the layout

##### Declaration

```
public double LayoutLength { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FAdd%5FDesignData%5FSDS2%5FPrimitives%5FLayout3DNode%5F)Add(Layout3DNode)

Add a node to the end of the layout

##### Declaration

```
public void Add(Layout3DNode node)
```

##### Parameters

| Type                                                         | Name | Description |
| ------------------------------------------------------------ | ---- | ----------- |
| [Layout3DNode](DesignData.SDS2.Primitives.Layout3DNode.html) | node |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FClear)Clear()

Clear all nodes from the layout

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FCloseLayout)CloseLayout()

Add a node which would make this a closed loop

##### Declaration

```
public void CloseLayout()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FEquals%5FSystem%5FObject%5F)Equals(object)

Represents a list of points in 3-dimensional space, in order, often forming a closed loop.

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FFinalize)\~Layout3D()

Represents a list of points in 3-dimensional space, in order, often forming a closed loop.

##### Declaration

```
protected ~Layout3D()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FGetEnumerator)GetEnumerator()

Get the enumerator object

##### Declaration

```
public IEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                 | Description |
| ------------------------------------------------------------------------------------ | ----------- |
| [IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FGetHashCode)GetHashCode()

Represents a list of points in 3-dimensional space, in order, often forming a closed loop.

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

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FGetIsClosed)GetIsClosed()

True if this is a losed loop

##### Declaration

```
public bool GetIsClosed()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FPop)Pop()

Remove the node at the end of the layout

##### Declaration

```
public void Pop()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

Remove a node at the given index

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FSetDepthVectors%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5F)SetDepthVectors(Vector3D)

Set the depth vectors on each Layout3DNode. If uniform is true, all nodes will be given the specified vector. If uniform is false, the specified vector will be given to the first node, and vectors subsequent nodes will bisect the angle between adjacent layout segments at the rotation of the depth vector on the previous node.

##### Declaration

```
public void SetDepthVectors(Vector3D depth)
```

##### Parameters

| Type                                                 | Name  | Description |
| ---------------------------------------------------- | ----- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) | depth |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FSetDepthVectors%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5FSystem%5FBoolean%5F)SetDepthVectors(Vector3D, bool)

Set the depth vectors on each Layout3DNode. If uniform is true, all nodes will be given the specified vector. If uniform is false, the specified vector will be given to the first node, and vectors subsequent nodes will bisect the angle between adjacent layout segments at the rotation of the depth vector on the previous node.

##### Declaration

```
public void SetDepthVectors(Vector3D depth, bool uniform)
```

##### Parameters

| Type                                                          | Name    | Description |
| ------------------------------------------------------------- | ------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html)          | depth   |             |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | uniform |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FLayout3D%5FTransform%5FDesignData%5FSDS2%5FPrimitives%5FMatrix%5F)Transform(Matrix)

Move and rotate this whole layout using the given matrix

##### Declaration

```
public void Transform(Matrix transformation)
```

##### Parameters

| Type                                             | Name           | Description |
| ------------------------------------------------ | -------------- | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) | transformation |             |

### [](#implements)Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)