# Class SurfaceList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

SurfaceList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Surface](DesignData.SDS2.Primitives.Surface.html)\>

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
public class SurfaceList : IEnumerable<Surface>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5F%5Fctor)SurfaceList()

##### Declaration

```
public SurfaceList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FSurfaceList%5F)SurfaceList(SurfaceList)

##### Declaration

```
public SurfaceList(SurfaceList other)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [SurfaceList](DesignData.SDS2.Primitives.SurfaceList.html) | other |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FPrimitives%5FSurface%5F%5F)SurfaceList(IEnumerable<Surface>)

##### Declaration

```
public SurfaceList(IEnumerable<Surface> c)
```

##### Parameters

| Type                                                                                                                                                | Name | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Surface](DesignData.SDS2.Primitives.Surface.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)SurfaceList(IEnumerable)

##### Declaration

```
public SurfaceList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5F%5Fctor%5FSystem%5FInt32%5F)SurfaceList(int)

##### Declaration

```
public SurfaceList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Surface this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FAdd%5FDesignData%5FSDS2%5FPrimitives%5FSurface%5F)Add(Surface)

##### Declaration

```
public void Add(Surface x)
```

##### Parameters

| Type                                               | Name | Description |
| -------------------------------------------------- | ---- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html) | x    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FAddRange%5FDesignData%5FSDS2%5FPrimitives%5FSurfaceList%5F)AddRange(SurfaceList)

##### Declaration

```
public void AddRange(SurfaceList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [SurfaceList](DesignData.SDS2.Primitives.SurfaceList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FCopyTo%5FDesignData%5FSDS2%5FPrimitives%5FSurface%5F%5F%5F)CopyTo(Surface\[\])

##### Declaration

```
public void CopyTo(Surface[] array)
```

##### Parameters

| Type                                                   | Name  | Description |
| ------------------------------------------------------ | ----- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FCopyTo%5FDesignData%5FSDS2%5FPrimitives%5FSurface%5F%5F%5FSystem%5FInt32%5F)CopyTo(Surface\[\], int)

##### Declaration

```
public void CopyTo(Surface[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html)\[\]     | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FSurface%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Surface\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Surface[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Surface](DesignData.SDS2.Primitives.Surface.html)\[\]     | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FFinalize)\~SurfaceList()

##### Declaration

```
protected ~SurfaceList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public SurfaceList.SurfaceListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [SurfaceList](DesignData.SDS2.Primitives.SurfaceList.html).[SurfaceListEnumerator](DesignData.SDS2.Primitives.SurfaceList.SurfaceListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public SurfaceList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [SurfaceList](DesignData.SDS2.Primitives.SurfaceList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FSurface%5F)Insert(int, Surface)

##### Declaration

```
public void Insert(int index, Surface x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Surface](DesignData.SDS2.Primitives.Surface.html)         | x     |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FSurfaceList%5F)InsertRange(int, SurfaceList)

##### Declaration

```
public void InsertRange(int index, SurfaceList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [SurfaceList](DesignData.SDS2.Primitives.SurfaceList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FRepeat%5FDesignData%5FSDS2%5FPrimitives%5FSurface%5FSystem%5FInt32%5F)Repeat(Surface, int)

##### Declaration

```
public static SurfaceList Repeat(Surface value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html)         | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [SurfaceList](DesignData.SDS2.Primitives.SurfaceList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FSurfaceList%5F)SetRange(int, SurfaceList)

##### Declaration

```
public void SetRange(int index, SurfaceList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [SurfaceList](DesignData.SDS2.Primitives.SurfaceList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FSurfaceList%5FToArray)ToArray()

##### Declaration

```
public Surface[] ToArray()
```

##### Returns

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)