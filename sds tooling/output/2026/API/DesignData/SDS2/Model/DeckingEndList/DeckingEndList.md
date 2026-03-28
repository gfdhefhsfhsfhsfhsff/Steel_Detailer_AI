# Class DeckingEndList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DeckingEndList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class DeckingEndList : IEnumerable<DeckingEnd>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5F%5Fctor)DeckingEndList()

##### Declaration

```
public DeckingEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FDeckingEndList%5F)DeckingEndList(DeckingEndList)

##### Declaration

```
public DeckingEndList(DeckingEndList other)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [DeckingEndList](DesignData.SDS2.Model.DeckingEndList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FDeckingEnd%5F%5F)DeckingEndList(IEnumerable<DeckingEnd>)

##### Declaration

```
public DeckingEndList(IEnumerable<DeckingEnd> c)
```

##### Parameters

| Type                                                                                                                                                 | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)DeckingEndList(IEnumerable)

##### Declaration

```
public DeckingEndList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5F%5Fctor%5FSystem%5FInt32%5F)DeckingEndList(int)

##### Declaration

```
public DeckingEndList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public DeckingEnd this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FAdd%5FDesignData%5FSDS2%5FModel%5FDeckingEnd%5F)Add(DeckingEnd)

##### Declaration

```
public void Add(DeckingEnd x)
```

##### Parameters

| Type                                                | Name | Description |
| --------------------------------------------------- | ---- | ----------- |
| [DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FDeckingEndList%5F)AddRange(DeckingEndList)

##### Declaration

```
public void AddRange(DeckingEndList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [DeckingEndList](DesignData.SDS2.Model.DeckingEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FDeckingEnd%5F%5F%5F)CopyTo(DeckingEnd\[\])

##### Declaration

```
public void CopyTo(DeckingEnd[] array)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FDeckingEnd%5F%5F%5FSystem%5FInt32%5F)CopyTo(DeckingEnd\[\], int)

##### Declaration

```
public void CopyTo(DeckingEnd[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html)\[\]    | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FDeckingEnd%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, DeckingEnd\[\], int, int)

##### Declaration

```
public void CopyTo(int index, DeckingEnd[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html)\[\]    | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FFinalize)\~DeckingEndList()

##### Declaration

```
protected ~DeckingEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public DeckingEndList.DeckingEndListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                       | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [DeckingEndList](DesignData.SDS2.Model.DeckingEndList.html).[DeckingEndListEnumerator](DesignData.SDS2.Model.DeckingEndList.DeckingEndListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public DeckingEndList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [DeckingEndList](DesignData.SDS2.Model.DeckingEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FDeckingEnd%5F)Insert(int, DeckingEnd)

##### Declaration

```
public void Insert(int index, DeckingEnd x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html)        | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FDeckingEndList%5F)InsertRange(int, DeckingEndList)

##### Declaration

```
public void InsertRange(int index, DeckingEndList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index  |             |
| [DeckingEndList](DesignData.SDS2.Model.DeckingEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FDeckingEnd%5FSystem%5FInt32%5F)Repeat(DeckingEnd, int)

##### Declaration

```
public static DeckingEndList Repeat(DeckingEnd value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html)        | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [DeckingEndList](DesignData.SDS2.Model.DeckingEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FDeckingEndList%5F)SetRange(int, DeckingEndList)

##### Declaration

```
public void SetRange(int index, DeckingEndList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index  |             |
| [DeckingEndList](DesignData.SDS2.Model.DeckingEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FDeckingEndList%5FToArray)ToArray()

##### Declaration

```
public DeckingEnd[] ToArray()
```

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)