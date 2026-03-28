# Class GridLineHandleList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

GridLineHandleList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html)\>

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
public class GridLineHandleList : IEnumerable<GridLineHandle>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5F%5Fctor)GridLineHandleList()

##### Declaration

```
public GridLineHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5F)GridLineHandleList(GridLineHandleList)

##### Declaration

```
public GridLineHandleList(GridLineHandleList other)
```

##### Parameters

| Type                                                                   | Name  | Description |
| ---------------------------------------------------------------------- | ----- | ----------- |
| [GridLineHandleList](DesignData.SDS2.Database.GridLineHandleList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandle%5F%5F)GridLineHandleList(IEnumerable<GridLineHandle>)

##### Declaration

```
public GridLineHandleList(IEnumerable<GridLineHandle> c)
```

##### Parameters

| Type                                                                                                                                                            | Name | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)GridLineHandleList(IEnumerable)

##### Declaration

```
public GridLineHandleList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5F%5Fctor%5FSystem%5FInt32%5F)GridLineHandleList(int)

##### Declaration

```
public GridLineHandleList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public GridLineHandle this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandle%5F)Add(GridLineHandle)

##### Declaration

```
public void Add(GridLineHandle x)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FAddRange%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5F)AddRange(GridLineHandleList)

##### Declaration

```
public void AddRange(GridLineHandleList values)
```

##### Parameters

| Type                                                                   | Name   | Description |
| ---------------------------------------------------------------------- | ------ | ----------- |
| [GridLineHandleList](DesignData.SDS2.Database.GridLineHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandle%5F%5F%5F)CopyTo(GridLineHandle\[\])

##### Declaration

```
public void CopyTo(GridLineHandle[] array)
```

##### Parameters

| Type                                                               | Name  | Description |
| ------------------------------------------------------------------ | ----- | ----------- |
| [GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandle%5F%5F%5FSystem%5FInt32%5F)CopyTo(GridLineHandle\[\], int)

##### Declaration

```
public void CopyTo(GridLineHandle[] array, int arrayIndex)
```

##### Parameters

| Type                                                               | Name       | Description |
| ------------------------------------------------------------------ | ---------- | ----------- |
| [GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandle%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, GridLineHandle\[\], int, int)

##### Declaration

```
public void CopyTo(int index, GridLineHandle[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                               | Name       | Description |
| ------------------------------------------------------------------ | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | index      |             |
| [GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | count      |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FFinalize)\~GridLineHandleList()

##### Declaration

```
protected ~GridLineHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public GridLineHandleList.GridLineHandleListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                 | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [GridLineHandleList](DesignData.SDS2.Database.GridLineHandleList.html).[GridLineHandleListEnumerator](DesignData.SDS2.Database.GridLineHandleList.GridLineHandleListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public GridLineHandleList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                   | Description |
| ---------------------------------------------------------------------- | ----------- |
| [GridLineHandleList](DesignData.SDS2.Database.GridLineHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandle%5F)Insert(int, GridLineHandle)

##### Declaration

```
public void Insert(int index, GridLineHandle x)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index |             |
| [GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html) | x     |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5F)InsertRange(int, GridLineHandleList)

##### Declaration

```
public void InsertRange(int index, GridLineHandleList values)
```

##### Parameters

| Type                                                                   | Name   | Description |
| ---------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)             | index  |             |
| [GridLineHandleList](DesignData.SDS2.Database.GridLineHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FRepeat%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandle%5FSystem%5FInt32%5F)Repeat(GridLineHandle, int)

##### Declaration

```
public static GridLineHandleList Repeat(GridLineHandle value, int count)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | count |             |

##### Returns

| Type                                                                   | Description |
| ---------------------------------------------------------------------- | ----------- |
| [GridLineHandleList](DesignData.SDS2.Database.GridLineHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5F)SetRange(int, GridLineHandleList)

##### Declaration

```
public void SetRange(int index, GridLineHandleList values)
```

##### Parameters

| Type                                                                   | Name   | Description |
| ---------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)             | index  |             |
| [GridLineHandleList](DesignData.SDS2.Database.GridLineHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGridLineHandleList%5FToArray)ToArray()

##### Declaration

```
public GridLineHandle[] ToArray()
```

##### Returns

| Type                                                               | Description |
| ------------------------------------------------------------------ | ----------- |
| [GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)