# Class DrawingList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DrawingList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Drawing](DesignData.SDS2.Detail.Drawing.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Detail](DesignData.SDS2.Detail.html)

###### **Assembly**: DesignData.SDS2.Detail.dll

##### Syntax

```
public class DrawingList : IEnumerable<Drawing>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5F%5Fctor)DrawingList()

##### Declaration

```
public DrawingList()
```

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5F%5Fctor%5FDesignData%5FSDS2%5FDetail%5FDrawingList%5F)DrawingList(DrawingList)

##### Declaration

```
public DrawingList(DrawingList other)
```

##### Parameters

| Type                                                   | Name  | Description |
| ------------------------------------------------------ | ----- | ----------- |
| [DrawingList](DesignData.SDS2.Detail.DrawingList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDetail%5FDrawing%5F%5F)DrawingList(IEnumerable<Drawing>)

##### Declaration

```
public DrawingList(IEnumerable<Drawing> c)
```

##### Parameters

| Type                                                                                                                                            | Name | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Drawing](DesignData.SDS2.Detail.Drawing.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)DrawingList(IEnumerable)

##### Declaration

```
public DrawingList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5F%5Fctor%5FSystem%5FInt32%5F)DrawingList(int)

##### Declaration

```
public DrawingList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Drawing this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                           | Description |
| ---------------------------------------------- | ----------- |
| [Drawing](DesignData.SDS2.Detail.Drawing.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FAdd%5FDesignData%5FSDS2%5FDetail%5FDrawing%5F)Add(Drawing)

##### Declaration

```
public void Add(Drawing x)
```

##### Parameters

| Type                                           | Name | Description |
| ---------------------------------------------- | ---- | ----------- |
| [Drawing](DesignData.SDS2.Detail.Drawing.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FAddRange%5FDesignData%5FSDS2%5FDetail%5FDrawingList%5F)AddRange(DrawingList)

##### Declaration

```
public void AddRange(DrawingList values)
```

##### Parameters

| Type                                                   | Name   | Description |
| ------------------------------------------------------ | ------ | ----------- |
| [DrawingList](DesignData.SDS2.Detail.DrawingList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FCopyTo%5FDesignData%5FSDS2%5FDetail%5FDrawing%5F%5F%5F)CopyTo(Drawing\[\])

##### Declaration

```
public void CopyTo(Drawing[] array)
```

##### Parameters

| Type                                               | Name  | Description |
| -------------------------------------------------- | ----- | ----------- |
| [Drawing](DesignData.SDS2.Detail.Drawing.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FCopyTo%5FDesignData%5FSDS2%5FDetail%5FDrawing%5F%5F%5FSystem%5FInt32%5F)CopyTo(Drawing\[\], int)

##### Declaration

```
public void CopyTo(Drawing[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Drawing](DesignData.SDS2.Detail.Drawing.html)\[\]         | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FDrawing%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Drawing\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Drawing[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Drawing](DesignData.SDS2.Detail.Drawing.html)\[\]         | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FFinalize)\~DrawingList()

##### Declaration

```
protected ~DrawingList()
```

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public DrawingList.DrawingListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                          | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [DrawingList](DesignData.SDS2.Detail.DrawingList.html).[DrawingListEnumerator](DesignData.SDS2.Detail.DrawingList.DrawingListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public DrawingList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [DrawingList](DesignData.SDS2.Detail.DrawingList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FDrawing%5F)Insert(int, Drawing)

##### Declaration

```
public void Insert(int index, Drawing x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Drawing](DesignData.SDS2.Detail.Drawing.html)             | x     |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FDrawingList%5F)InsertRange(int, DrawingList)

##### Declaration

```
public void InsertRange(int index, DrawingList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [DrawingList](DesignData.SDS2.Detail.DrawingList.html)     | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FRepeat%5FDesignData%5FSDS2%5FDetail%5FDrawing%5FSystem%5FInt32%5F)Repeat(Drawing, int)

##### Declaration

```
public static DrawingList Repeat(Drawing value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Drawing](DesignData.SDS2.Detail.Drawing.html)             | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [DrawingList](DesignData.SDS2.Detail.DrawingList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FDrawingList%5F)SetRange(int, DrawingList)

##### Declaration

```
public void SetRange(int index, DrawingList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [DrawingList](DesignData.SDS2.Detail.DrawingList.html)     | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FToArray)ToArray()

##### Declaration

```
public Drawing[] ToArray()
```

##### Returns

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Drawing](DesignData.SDS2.Detail.Drawing.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)