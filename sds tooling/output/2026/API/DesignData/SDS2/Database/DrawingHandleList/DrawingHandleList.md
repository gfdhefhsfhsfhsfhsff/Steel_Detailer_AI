# Class DrawingHandleList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DrawingHandleList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class DrawingHandleList : IEnumerable<DrawingHandle>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5F%5Fctor)DrawingHandleList()

##### Declaration

```
public DrawingHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5F)DrawingHandleList(DrawingHandleList)

##### Declaration

```
public DrawingHandleList(DrawingHandleList other)
```

##### Parameters

| Type                                                                 | Name  | Description |
| -------------------------------------------------------------------- | ----- | ----------- |
| [DrawingHandleList](DesignData.SDS2.Database.DrawingHandleList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F%5F)DrawingHandleList(IEnumerable<DrawingHandle>)

##### Declaration

```
public DrawingHandleList(IEnumerable<DrawingHandle> c)
```

##### Parameters

| Type                                                                                                                                                          | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)DrawingHandleList(IEnumerable)

##### Declaration

```
public DrawingHandleList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5F%5Fctor%5FSystem%5FInt32%5F)DrawingHandleList(int)

##### Declaration

```
public DrawingHandleList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public DrawingHandle this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F)Add(DrawingHandle)

##### Declaration

```
public void Add(DrawingHandle x)
```

##### Parameters

| Type                                                         | Name | Description |
| ------------------------------------------------------------ | ---- | ----------- |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FAddRange%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5F)AddRange(DrawingHandleList)

##### Declaration

```
public void AddRange(DrawingHandleList values)
```

##### Parameters

| Type                                                                 | Name   | Description |
| -------------------------------------------------------------------- | ------ | ----------- |
| [DrawingHandleList](DesignData.SDS2.Database.DrawingHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F%5F%5F)CopyTo(DrawingHandle\[\])

##### Declaration

```
public void CopyTo(DrawingHandle[] array)
```

##### Parameters

| Type                                                             | Name  | Description |
| ---------------------------------------------------------------- | ----- | ----------- |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F%5F%5FSystem%5FInt32%5F)CopyTo(DrawingHandle\[\], int)

##### Declaration

```
public void CopyTo(DrawingHandle[] array, int arrayIndex)
```

##### Parameters

| Type                                                             | Name       | Description |
| ---------------------------------------------------------------- | ---------- | ----------- |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)       | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, DrawingHandle\[\], int, int)

##### Declaration

```
public void CopyTo(int index, DrawingHandle[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                             | Name       | Description |
| ---------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)       | index      |             |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)       | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)       | count      |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FFinalize)\~DrawingHandleList()

##### Declaration

```
protected ~DrawingHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public DrawingHandleList.DrawingHandleListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                            | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [DrawingHandleList](DesignData.SDS2.Database.DrawingHandleList.html).[DrawingHandleListEnumerator](DesignData.SDS2.Database.DrawingHandleList.DrawingHandleListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public DrawingHandleList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [DrawingHandleList](DesignData.SDS2.Database.DrawingHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F)Insert(int, DrawingHandle)

##### Declaration

```
public void Insert(int index, DrawingHandle x)
```

##### Parameters

| Type                                                         | Name  | Description |
| ------------------------------------------------------------ | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)   | index |             |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html) | x     |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5F)InsertRange(int, DrawingHandleList)

##### Declaration

```
public void InsertRange(int index, DrawingHandleList values)
```

##### Parameters

| Type                                                                 | Name   | Description |
| -------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)           | index  |             |
| [DrawingHandleList](DesignData.SDS2.Database.DrawingHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FRepeat%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5FSystem%5FInt32%5F)Repeat(DrawingHandle, int)

##### Declaration

```
public static DrawingHandleList Repeat(DrawingHandle value, int count)
```

##### Parameters

| Type                                                         | Name  | Description |
| ------------------------------------------------------------ | ----- | ----------- |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)   | count |             |

##### Returns

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [DrawingHandleList](DesignData.SDS2.Database.DrawingHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5F)SetRange(int, DrawingHandleList)

##### Declaration

```
public void SetRange(int index, DrawingHandleList values)
```

##### Parameters

| Type                                                                 | Name   | Description |
| -------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)           | index  |             |
| [DrawingHandleList](DesignData.SDS2.Database.DrawingHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandleList%5FToArray)ToArray()

##### Declaration

```
public DrawingHandle[] ToArray()
```

##### Returns

| Type                                                             | Description |
| ---------------------------------------------------------------- | ----------- |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)