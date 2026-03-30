# Class NoteHandleList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

NoteHandleList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[NoteHandle](DesignData.SDS2.Database.NoteHandle.html)\>

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
public class NoteHandleList : IEnumerable<NoteHandle>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5F%5Fctor)NoteHandleList()

##### Declaration

```
public NoteHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FNoteHandleList%5F)NoteHandleList(NoteHandleList)

##### Declaration

```
public NoteHandleList(NoteHandleList other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [NoteHandleList](DesignData.SDS2.Database.NoteHandleList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDatabase%5FNoteHandle%5F%5F)NoteHandleList(IEnumerable<NoteHandle>)

##### Declaration

```
public NoteHandleList(IEnumerable<NoteHandle> c)
```

##### Parameters

| Type                                                                                                                                                    | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[NoteHandle](DesignData.SDS2.Database.NoteHandle.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)NoteHandleList(IEnumerable)

##### Declaration

```
public NoteHandleList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5F%5Fctor%5FSystem%5FInt32%5F)NoteHandleList(int)

##### Declaration

```
public NoteHandleList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public NoteHandle this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FNoteHandle%5F)Add(NoteHandle)

##### Declaration

```
public void Add(NoteHandle x)
```

##### Parameters

| Type                                                   | Name | Description |
| ------------------------------------------------------ | ---- | ----------- |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FAddRange%5FDesignData%5FSDS2%5FDatabase%5FNoteHandleList%5F)AddRange(NoteHandleList)

##### Declaration

```
public void AddRange(NoteHandleList values)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [NoteHandleList](DesignData.SDS2.Database.NoteHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FNoteHandle%5F%5F%5F)CopyTo(NoteHandle\[\])

##### Declaration

```
public void CopyTo(NoteHandle[] array)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FNoteHandle%5F%5F%5FSystem%5FInt32%5F)CopyTo(NoteHandle\[\], int)

##### Declaration

```
public void CopyTo(NoteHandle[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FNoteHandle%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, NoteHandle\[\], int, int)

##### Declaration

```
public void CopyTo(int index, NoteHandle[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FFinalize)\~NoteHandleList()

##### Declaration

```
protected ~NoteHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public NoteHandleList.NoteHandleListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                             | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [NoteHandleList](DesignData.SDS2.Database.NoteHandleList.html).[NoteHandleListEnumerator](DesignData.SDS2.Database.NoteHandleList.NoteHandleListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public NoteHandleList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [NoteHandleList](DesignData.SDS2.Database.NoteHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FNoteHandle%5F)Insert(int, NoteHandle)

##### Declaration

```
public void Insert(int index, NoteHandle x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html)     | x     |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FNoteHandleList%5F)InsertRange(int, NoteHandleList)

##### Declaration

```
public void InsertRange(int index, NoteHandleList values)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index  |             |
| [NoteHandleList](DesignData.SDS2.Database.NoteHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FRepeat%5FDesignData%5FSDS2%5FDatabase%5FNoteHandle%5FSystem%5FInt32%5F)Repeat(NoteHandle, int)

##### Declaration

```
public static NoteHandleList Repeat(NoteHandle value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html)     | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [NoteHandleList](DesignData.SDS2.Database.NoteHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FNoteHandleList%5F)SetRange(int, NoteHandleList)

##### Declaration

```
public void SetRange(int index, NoteHandleList values)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index  |             |
| [NoteHandleList](DesignData.SDS2.Database.NoteHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FNoteHandleList%5FToArray)ToArray()

##### Declaration

```
public NoteHandle[] ToArray()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)