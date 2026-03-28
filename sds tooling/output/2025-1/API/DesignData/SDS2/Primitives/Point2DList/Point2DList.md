# Class Point2DList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Point2DList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Point2D](DesignData.SDS2.Primitives.Point2D.html)\>

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
public class Point2DList : IEnumerable<Point2D>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5F%5Fctor)Point2DList()

##### Declaration

```
public Point2DList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPoint2DList%5F)Point2DList(Point2DList)

##### Declaration

```
public Point2DList(Point2DList other)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Point2DList](DesignData.SDS2.Primitives.Point2DList.html) | other |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5F%5F)Point2DList(IEnumerable<Point2D>)

##### Declaration

```
public Point2DList(IEnumerable<Point2D> c)
```

##### Parameters

| Type                                                                                                                                                | Name | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Point2D](DesignData.SDS2.Primitives.Point2D.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)Point2DList(IEnumerable)

##### Declaration

```
public Point2DList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5F%5Fctor%5FSystem%5FInt32%5F)Point2DList(int)

##### Declaration

```
public Point2DList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Point2D this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FAdd%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5F)Add(Point2D)

##### Declaration

```
public void Add(Point2D x)
```

##### Parameters

| Type                                               | Name | Description |
| -------------------------------------------------- | ---- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html) | x    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FAddRange%5FDesignData%5FSDS2%5FPrimitives%5FPoint2DList%5F)AddRange(Point2DList)

##### Declaration

```
public void AddRange(Point2DList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [Point2DList](DesignData.SDS2.Primitives.Point2DList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FCopyTo%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5F%5F%5F)CopyTo(Point2D\[\])

##### Declaration

```
public void CopyTo(Point2D[] array)
```

##### Parameters

| Type                                                   | Name  | Description |
| ------------------------------------------------------ | ----- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FCopyTo%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5F%5F%5FSystem%5FInt32%5F)CopyTo(Point2D\[\], int)

##### Declaration

```
public void CopyTo(Point2D[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html)\[\]     | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Point2D\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Point2D[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html)\[\]     | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FFinalize)\~Point2DList()

##### Declaration

```
protected ~Point2DList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public Point2DList.Point2DListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [Point2DList](DesignData.SDS2.Primitives.Point2DList.html).[Point2DListEnumerator](DesignData.SDS2.Primitives.Point2DList.Point2DListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public Point2DList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [Point2DList](DesignData.SDS2.Primitives.Point2DList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5F)Insert(int, Point2D)

##### Declaration

```
public void Insert(int index, Point2D x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html)         | x     |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPoint2DList%5F)InsertRange(int, Point2DList)

##### Declaration

```
public void InsertRange(int index, Point2DList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [Point2DList](DesignData.SDS2.Primitives.Point2DList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FRepeat%5FDesignData%5FSDS2%5FPrimitives%5FPoint2D%5FSystem%5FInt32%5F)Repeat(Point2D, int)

##### Declaration

```
public static Point2DList Repeat(Point2D value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html)         | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [Point2DList](DesignData.SDS2.Primitives.Point2DList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPoint2DList%5F)SetRange(int, Point2DList)

##### Declaration

```
public void SetRange(int index, Point2DList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [Point2DList](DesignData.SDS2.Primitives.Point2DList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint2DList%5FToArray)ToArray()

##### Declaration

```
public Point2D[] ToArray()
```

##### Returns

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [Point2D](DesignData.SDS2.Primitives.Point2D.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)