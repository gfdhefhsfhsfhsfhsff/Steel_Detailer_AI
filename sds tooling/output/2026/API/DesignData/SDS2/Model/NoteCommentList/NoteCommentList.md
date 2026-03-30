# Class NoteCommentList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

NoteCommentList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[NoteComment](DesignData.SDS2.Model.NoteComment.html)\>

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
public class NoteCommentList : IEnumerable<NoteComment>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5F%5Fctor)NoteCommentList()

##### Declaration

```
public NoteCommentList()
```

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FNoteCommentList%5F)NoteCommentList(NoteCommentList)

##### Declaration

```
public NoteCommentList(NoteCommentList other)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [NoteCommentList](DesignData.SDS2.Model.NoteCommentList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FNoteComment%5F%5F)NoteCommentList(IEnumerable<NoteComment>)

##### Declaration

```
public NoteCommentList(IEnumerable<NoteComment> c)
```

##### Parameters

| Type                                                                                                                                                   | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[NoteComment](DesignData.SDS2.Model.NoteComment.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)NoteCommentList(IEnumerable)

##### Declaration

```
public NoteCommentList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5F%5Fctor%5FSystem%5FInt32%5F)NoteCommentList(int)

##### Declaration

```
public NoteCommentList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public NoteComment this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FAdd%5FDesignData%5FSDS2%5FModel%5FNoteComment%5F)Add(NoteComment)

##### Declaration

```
public void Add(NoteComment x)
```

##### Parameters

| Type                                                  | Name | Description |
| ----------------------------------------------------- | ---- | ----------- |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FNoteCommentList%5F)AddRange(NoteCommentList)

##### Declaration

```
public void AddRange(NoteCommentList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [NoteCommentList](DesignData.SDS2.Model.NoteCommentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FNoteComment%5F%5F%5F)CopyTo(NoteComment\[\])

##### Declaration

```
public void CopyTo(NoteComment[] array)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FNoteComment%5F%5F%5FSystem%5FInt32%5F)CopyTo(NoteComment\[\], int)

##### Declaration

```
public void CopyTo(NoteComment[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FNoteComment%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, NoteComment\[\], int, int)

##### Declaration

```
public void CopyTo(int index, NoteComment[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FFinalize)\~NoteCommentList()

##### Declaration

```
protected ~NoteCommentList()
```

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public NoteCommentList.NoteCommentListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                            | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [NoteCommentList](DesignData.SDS2.Model.NoteCommentList.html).[NoteCommentListEnumerator](DesignData.SDS2.Model.NoteCommentList.NoteCommentListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public NoteCommentList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [NoteCommentList](DesignData.SDS2.Model.NoteCommentList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FNoteComment%5F)Insert(int, NoteComment)

##### Declaration

```
public void Insert(int index, NoteComment x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html)      | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FNoteCommentList%5F)InsertRange(int, NoteCommentList)

##### Declaration

```
public void InsertRange(int index, NoteCommentList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [NoteCommentList](DesignData.SDS2.Model.NoteCommentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FNoteComment%5FSystem%5FInt32%5F)Repeat(NoteComment, int)

##### Declaration

```
public static NoteCommentList Repeat(NoteComment value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html)      | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [NoteCommentList](DesignData.SDS2.Model.NoteCommentList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FNoteCommentList%5F)SetRange(int, NoteCommentList)

##### Declaration

```
public void SetRange(int index, NoteCommentList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [NoteCommentList](DesignData.SDS2.Model.NoteCommentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FToArray)ToArray()

##### Declaration

```
public NoteComment[] ToArray()
```

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)