# Class EdgeList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

EdgeList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Edge](DesignData.SDS2.Primitives.Edge.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public class EdgeList : IEnumerable<Edge>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5F%5Fctor)EdgeList()

##### Declaration

```
public EdgeList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5F)EdgeList(EdgeList)

##### Declaration

```
public EdgeList(EdgeList other)
```

##### Parameters

| Type                                                 | Name  | Description |
| ---------------------------------------------------- | ----- | ----------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html) | other |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FPrimitives%5FEdge%5F%5F)EdgeList(IEnumerable<Edge>)

##### Declaration

```
public EdgeList(IEnumerable<Edge> c)
```

##### Parameters

| Type                                                                                                                                          | Name | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Edge](DesignData.SDS2.Primitives.Edge.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)EdgeList(IEnumerable)

##### Declaration

```
public EdgeList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5F%5Fctor%5FSystem%5FInt32%5F)EdgeList(int)

##### Declaration

```
public EdgeList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Edge this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                         | Description |
| -------------------------------------------- | ----------- |
| [Edge](DesignData.SDS2.Primitives.Edge.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FAdd%5FDesignData%5FSDS2%5FPrimitives%5FEdge%5F)Add(Edge)

##### Declaration

```
public void Add(Edge x)
```

##### Parameters

| Type                                         | Name | Description |
| -------------------------------------------- | ---- | ----------- |
| [Edge](DesignData.SDS2.Primitives.Edge.html) | x    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FAddRange%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5F)AddRange(EdgeList)

##### Declaration

```
public void AddRange(EdgeList values)
```

##### Parameters

| Type                                                 | Name   | Description |
| ---------------------------------------------------- | ------ | ----------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FCopyTo%5FDesignData%5FSDS2%5FPrimitives%5FEdge%5F%5F%5F)CopyTo(Edge\[\])

##### Declaration

```
public void CopyTo(Edge[] array)
```

##### Parameters

| Type                                             | Name  | Description |
| ------------------------------------------------ | ----- | ----------- |
| [Edge](DesignData.SDS2.Primitives.Edge.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FCopyTo%5FDesignData%5FSDS2%5FPrimitives%5FEdge%5F%5F%5FSystem%5FInt32%5F)CopyTo(Edge\[\], int)

##### Declaration

```
public void CopyTo(Edge[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Edge](DesignData.SDS2.Primitives.Edge.html)\[\]           | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FEdge%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Edge\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Edge[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Edge](DesignData.SDS2.Primitives.Edge.html)\[\]           | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FFinalize)\~EdgeList()

##### Declaration

```
protected ~EdgeList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public EdgeList.EdgeListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                   | Description |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html).[EdgeListEnumerator](DesignData.SDS2.Primitives.EdgeList.EdgeListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public EdgeList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FEdge%5F)Insert(int, Edge)

##### Declaration

```
public void Insert(int index, Edge x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Edge](DesignData.SDS2.Primitives.Edge.html)               | x     |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5F)InsertRange(int, EdgeList)

##### Declaration

```
public void InsertRange(int index, EdgeList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)       | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FRepeat%5FDesignData%5FSDS2%5FPrimitives%5FEdge%5FSystem%5FInt32%5F)Repeat(Edge, int)

##### Declaration

```
public static EdgeList Repeat(Edge value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Edge](DesignData.SDS2.Primitives.Edge.html)               | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5F)SetRange(int, EdgeList)

##### Declaration

```
public void SetRange(int index, EdgeList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html)       | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FToArray)ToArray()

##### Declaration

```
public Edge[] ToArray()
```

##### Returns

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Edge](DesignData.SDS2.Primitives.Edge.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)