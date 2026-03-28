# Class Point3DList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Point3DList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Point3D](DesignData.SDS2.Primitives.Point3D.html)\>

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
public class Point3DList : IEnumerable<Point3D>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5F%5Fctor)Point3DList()

##### Declaration

```
public Point3DList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPoint3DList%5F)Point3DList(Point3DList)

##### Declaration

```
public Point3DList(Point3DList other)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Point3DList](DesignData.SDS2.Primitives.Point3DList.html) | other |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F%5F)Point3DList(IEnumerable<Point3D>)

##### Declaration

```
public Point3DList(IEnumerable<Point3D> c)
```

##### Parameters

| Type                                                                                                                                                | Name | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Point3D](DesignData.SDS2.Primitives.Point3D.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)Point3DList(IEnumerable)

##### Declaration

```
public Point3DList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5F%5Fctor%5FSystem%5FInt32%5F)Point3DList(int)

##### Declaration

```
public Point3DList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Point3D this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FAdd%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)Add(Point3D)

##### Declaration

```
public void Add(Point3D x)
```

##### Parameters

| Type                                               | Name | Description |
| -------------------------------------------------- | ---- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) | x    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FAddRange%5FDesignData%5FSDS2%5FPrimitives%5FPoint3DList%5F)AddRange(Point3DList)

##### Declaration

```
public void AddRange(Point3DList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [Point3DList](DesignData.SDS2.Primitives.Point3DList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FCopyTo%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F%5F%5F)CopyTo(Point3D\[\])

##### Declaration

```
public void CopyTo(Point3D[] array)
```

##### Parameters

| Type                                                   | Name  | Description |
| ------------------------------------------------------ | ----- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FCopyTo%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F%5F%5FSystem%5FInt32%5F)CopyTo(Point3D\[\], int)

##### Declaration

```
public void CopyTo(Point3D[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)\[\]     | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Point3D\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Point3D[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)\[\]     | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FFinalize)\~Point3DList()

##### Declaration

```
protected ~Point3DList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public Point3DList.Point3DListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [Point3DList](DesignData.SDS2.Primitives.Point3DList.html).[Point3DListEnumerator](DesignData.SDS2.Primitives.Point3DList.Point3DListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public Point3DList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [Point3DList](DesignData.SDS2.Primitives.Point3DList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5F)Insert(int, Point3D)

##### Declaration

```
public void Insert(int index, Point3D x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)         | x     |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPoint3DList%5F)InsertRange(int, Point3DList)

##### Declaration

```
public void InsertRange(int index, Point3DList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [Point3DList](DesignData.SDS2.Primitives.Point3DList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FRepeat%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FSystem%5FInt32%5F)Repeat(Point3D, int)

##### Declaration

```
public static Point3DList Repeat(Point3D value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)         | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [Point3DList](DesignData.SDS2.Primitives.Point3DList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FPoint3DList%5F)SetRange(int, Point3DList)

##### Declaration

```
public void SetRange(int index, Point3DList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [Point3DList](DesignData.SDS2.Primitives.Point3DList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FToArray)ToArray()

##### Declaration

```
public Point3D[] ToArray()
```

##### Returns

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)