# Class PolygonList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

PolygonList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Polygon](DesignData.SDS2.Primitives.Polygon.html)\>

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
public class PolygonList : IEnumerable<Polygon>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5F%5Fctor)PolygonList()

##### Declaration

```
public PolygonList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPolygonList%5F)PolygonList(PolygonList)

##### Declaration

```
public PolygonList(PolygonList other)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html) | other |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5F)PolygonList(IEnumerable<Polygon>)

##### Declaration

```
public PolygonList(IEnumerable<Polygon> c)
```

##### Parameters

| Type                                                                                                                                                | Name | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Polygon](DesignData.SDS2.Primitives.Polygon.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)PolygonList(IEnumerable)

##### Declaration

```
public PolygonList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5F%5Fctor%5FSystem%5FInt32%5F)PolygonList(int)

##### Declaration

```
public PolygonList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Polygon this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Polygon](DesignData.SDS2.Primitives.Polygon.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FAdd%5FDesignData%5FSDS2%5FPrimitives%5FPolygon%5F)Add(Polygon)

##### Declaration

```
public void Add(Polygon x)
```

##### Parameters

| Type                                               | Name | Description |
| -------------------------------------------------- | ---- | ----------- |
| [Polygon](DesignData.SDS2.Primitives.Polygon.html) | x    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FAddRange%5FDesignData%5FSDS2%5FPrimitives%5FPolygonList%5F)AddRange(PolygonList)

##### Declaration

```
public void AddRange(PolygonList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FCopyTo%5FDesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5F%5F)CopyTo(Polygon\[\])

##### Declaration

```
public void CopyTo(Polygon[] array)
```

##### Parameters

| Type                                                   | Name  | Description |
| ------------------------------------------------------ | ----- | ----------- |
| [Polygon](DesignData.SDS2.Primitives.Polygon.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FCopyTo%5FDesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5F%5FSystem%5FInt32%5F)CopyTo(Polygon\[\], int)

##### Declaration

```
public void CopyTo(Polygon[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Polygon](DesignData.SDS2.Primitives.Polygon.html)\[\]     | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPolygon%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Polygon\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Polygon[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Polygon](DesignData.SDS2.Primitives.Polygon.html)\[\]     | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FFinalize)\~PolygonList()

##### Declaration

```
protected ~PolygonList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public PolygonList.PolygonListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html).[PolygonListEnumerator](DesignData.SDS2.Primitives.PolygonList.PolygonListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public PolygonList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPolygon%5F)Insert(int, Polygon)

##### Declaration

```
public void Insert(int index, Polygon x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Polygon](DesignData.SDS2.Primitives.Polygon.html)         | x     |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPolygonList%5F)InsertRange(int, PolygonList)

##### Declaration

```
public void InsertRange(int index, PolygonList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FRepeat%5FDesignData%5FSDS2%5FPrimitives%5FPolygon%5FSystem%5FInt32%5F)Repeat(Polygon, int)

##### Declaration

```
public static PolygonList Repeat(Polygon value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Polygon](DesignData.SDS2.Primitives.Polygon.html)         | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPolygonList%5F)SetRange(int, PolygonList)

##### Declaration

```
public void SetRange(int index, PolygonList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FToArray)ToArray()

##### Declaration

```
public Polygon[] ToArray()
```

##### Returns

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [Polygon](DesignData.SDS2.Primitives.Polygon.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)