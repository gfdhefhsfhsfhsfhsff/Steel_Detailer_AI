# Class MemberEndList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MemberEndList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MemberEnd](DesignData.SDS2.Model.MemberEnd.html)\>

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
public class MemberEndList : IEnumerable<MemberEnd>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5F%5Fctor)MemberEndList()

##### Declaration

```
public MemberEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FMemberEndList%5F)MemberEndList(MemberEndList)

##### Declaration

```
public MemberEndList(MemberEndList other)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [MemberEndList](DesignData.SDS2.Model.MemberEndList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FMemberEnd%5F%5F)MemberEndList(IEnumerable<MemberEnd>)

##### Declaration

```
public MemberEndList(IEnumerable<MemberEnd> c)
```

##### Parameters

| Type                                                                                                                                               | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MemberEnd](DesignData.SDS2.Model.MemberEnd.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)MemberEndList(IEnumerable)

##### Declaration

```
public MemberEndList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5F%5Fctor%5FSystem%5FInt32%5F)MemberEndList(int)

##### Declaration

```
public MemberEndList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FItem%5FDesignData%5FSDS2%5FDatabase%5FColumnEnd%5F)this\[ColumnEnd\]

##### Declaration

```
public MemberEnd this[ColumnEnd end] { get; set; }
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [ColumnEnd](DesignData.SDS2.Database.ColumnEnd.html) | end  |             |

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [MemberEnd](DesignData.SDS2.Model.MemberEnd.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FItem%5FDesignData%5FSDS2%5FDatabase%5FMemberEnd%5F)this\[MemberEnd\]

##### Declaration

```
public MemberEnd this[MemberEnd end] { get; set; }
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [MemberEnd](DesignData.SDS2.Database.MemberEnd.html) | end  |             |

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [MemberEnd](DesignData.SDS2.Model.MemberEnd.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public MemberEnd this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [MemberEnd](DesignData.SDS2.Model.MemberEnd.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FAdd%5FDesignData%5FSDS2%5FModel%5FMemberEnd%5F)Add(MemberEnd)

##### Declaration

```
public void Add(MemberEnd x)
```

##### Parameters

| Type                                              | Name | Description |
| ------------------------------------------------- | ---- | ----------- |
| [MemberEnd](DesignData.SDS2.Model.MemberEnd.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FMemberEndList%5F)AddRange(MemberEndList)

##### Declaration

```
public void AddRange(MemberEndList values)
```

##### Parameters

| Type                                                      | Name   | Description |
| --------------------------------------------------------- | ------ | ----------- |
| [MemberEndList](DesignData.SDS2.Model.MemberEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMemberEnd%5F%5F%5F)CopyTo(MemberEnd\[\])

##### Declaration

```
public void CopyTo(MemberEnd[] array)
```

##### Parameters

| Type                                                  | Name  | Description |
| ----------------------------------------------------- | ----- | ----------- |
| [MemberEnd](DesignData.SDS2.Model.MemberEnd.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMemberEnd%5F%5F%5FSystem%5FInt32%5F)CopyTo(MemberEnd\[\], int)

##### Declaration

```
public void CopyTo(MemberEnd[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [MemberEnd](DesignData.SDS2.Model.MemberEnd.html)\[\]      | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMemberEnd%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, MemberEnd\[\], int, int)

##### Declaration

```
public void CopyTo(int index, MemberEnd[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [MemberEnd](DesignData.SDS2.Model.MemberEnd.html)\[\]      | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FFinalize)\~MemberEndList()

##### Declaration

```
protected ~MemberEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public MemberEndList.MemberEndListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [MemberEndList](DesignData.SDS2.Model.MemberEndList.html).[MemberEndListEnumerator](DesignData.SDS2.Model.MemberEndList.MemberEndListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public MemberEndList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [MemberEndList](DesignData.SDS2.Model.MemberEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMemberEnd%5F)Insert(int, MemberEnd)

##### Declaration

```
public void Insert(int index, MemberEnd x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [MemberEnd](DesignData.SDS2.Model.MemberEnd.html)          | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMemberEndList%5F)InsertRange(int, MemberEndList)

##### Declaration

```
public void InsertRange(int index, MemberEndList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [MemberEndList](DesignData.SDS2.Model.MemberEndList.html)  | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FMemberEnd%5FSystem%5FInt32%5F)Repeat(MemberEnd, int)

##### Declaration

```
public static MemberEndList Repeat(MemberEnd value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [MemberEnd](DesignData.SDS2.Model.MemberEnd.html)          | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [MemberEndList](DesignData.SDS2.Model.MemberEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMemberEndList%5F)SetRange(int, MemberEndList)

##### Declaration

```
public void SetRange(int index, MemberEndList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [MemberEndList](DesignData.SDS2.Model.MemberEndList.html)  | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberEndList%5FToArray)ToArray()

##### Declaration

```
public MemberEnd[] ToArray()
```

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [MemberEnd](DesignData.SDS2.Model.MemberEnd.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)