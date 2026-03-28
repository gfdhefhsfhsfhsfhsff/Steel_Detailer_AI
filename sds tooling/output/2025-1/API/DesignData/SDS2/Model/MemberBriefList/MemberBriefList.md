# Class MemberBriefList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MemberBriefList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MemberBrief](DesignData.SDS2.Model.MemberBrief.html)\>

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
public class MemberBriefList : IEnumerable<MemberBrief>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5F%5Fctor)MemberBriefList()

##### Declaration

```
public MemberBriefList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FMemberBriefList%5F)MemberBriefList(MemberBriefList)

##### Declaration

```
public MemberBriefList(MemberBriefList other)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [MemberBriefList](DesignData.SDS2.Model.MemberBriefList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FMemberBrief%5F%5F)MemberBriefList(IEnumerable<MemberBrief>)

##### Declaration

```
public MemberBriefList(IEnumerable<MemberBrief> c)
```

##### Parameters

| Type                                                                                                                                                   | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MemberBrief](DesignData.SDS2.Model.MemberBrief.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)MemberBriefList(IEnumerable)

##### Declaration

```
public MemberBriefList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5F%5Fctor%5FSystem%5FInt32%5F)MemberBriefList(int)

##### Declaration

```
public MemberBriefList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public MemberBrief this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FAdd%5FDesignData%5FSDS2%5FModel%5FMemberBrief%5F)Add(MemberBrief)

##### Declaration

```
public void Add(MemberBrief x)
```

##### Parameters

| Type                                                  | Name | Description |
| ----------------------------------------------------- | ---- | ----------- |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FMemberBriefList%5F)AddRange(MemberBriefList)

##### Declaration

```
public void AddRange(MemberBriefList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [MemberBriefList](DesignData.SDS2.Model.MemberBriefList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMemberBrief%5F%5F%5F)CopyTo(MemberBrief\[\])

##### Declaration

```
public void CopyTo(MemberBrief[] array)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMemberBrief%5F%5F%5FSystem%5FInt32%5F)CopyTo(MemberBrief\[\], int)

##### Declaration

```
public void CopyTo(MemberBrief[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMemberBrief%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, MemberBrief\[\], int, int)

##### Declaration

```
public void CopyTo(int index, MemberBrief[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FFinalize)\~MemberBriefList()

##### Declaration

```
protected ~MemberBriefList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public MemberBriefList.MemberBriefListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                            | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [MemberBriefList](DesignData.SDS2.Model.MemberBriefList.html).[MemberBriefListEnumerator](DesignData.SDS2.Model.MemberBriefList.MemberBriefListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public MemberBriefList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [MemberBriefList](DesignData.SDS2.Model.MemberBriefList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMemberBrief%5F)Insert(int, MemberBrief)

##### Declaration

```
public void Insert(int index, MemberBrief x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html)      | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMemberBriefList%5F)InsertRange(int, MemberBriefList)

##### Declaration

```
public void InsertRange(int index, MemberBriefList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [MemberBriefList](DesignData.SDS2.Model.MemberBriefList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FMemberBrief%5FSystem%5FInt32%5F)Repeat(MemberBrief, int)

##### Declaration

```
public static MemberBriefList Repeat(MemberBrief value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html)      | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [MemberBriefList](DesignData.SDS2.Model.MemberBriefList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMemberBriefList%5F)SetRange(int, MemberBriefList)

##### Declaration

```
public void SetRange(int index, MemberBriefList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [MemberBriefList](DesignData.SDS2.Model.MemberBriefList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBriefList%5FToArray)ToArray()

##### Declaration

```
public MemberBrief[] ToArray()
```

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)