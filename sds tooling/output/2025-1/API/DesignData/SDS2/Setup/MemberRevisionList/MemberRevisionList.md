# Class MemberRevisionList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MemberRevisionList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MemberRevision](DesignData.SDS2.Setup.MemberRevision.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class MemberRevisionList : IEnumerable<MemberRevision>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5F%5Fctor)MemberRevisionList()

##### Declaration

```
public MemberRevisionList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FMemberRevisionList%5F)MemberRevisionList(MemberRevisionList)

##### Declaration

```
public MemberRevisionList(MemberRevisionList other)
```

##### Parameters

| Type                                                                | Name  | Description |
| ------------------------------------------------------------------- | ----- | ----------- |
| [MemberRevisionList](DesignData.SDS2.Setup.MemberRevisionList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5F%5F)MemberRevisionList(IEnumerable<MemberRevision>)

##### Declaration

```
public MemberRevisionList(IEnumerable<MemberRevision> c)
```

##### Parameters

| Type                                                                                                                                                         | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MemberRevision](DesignData.SDS2.Setup.MemberRevision.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)MemberRevisionList(IEnumerable)

##### Declaration

```
public MemberRevisionList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5F%5Fctor%5FSystem%5FInt32%5F)MemberRevisionList(int)

##### Declaration

```
public MemberRevisionList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public MemberRevision this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5F)Add(MemberRevision)

##### Declaration

```
public void Add(MemberRevision x)
```

##### Parameters

| Type                                                        | Name | Description |
| ----------------------------------------------------------- | ---- | ----------- |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FMemberRevisionList%5F)AddRange(MemberRevisionList)

##### Declaration

```
public void AddRange(MemberRevisionList values)
```

##### Parameters

| Type                                                                | Name   | Description |
| ------------------------------------------------------------------- | ------ | ----------- |
| [MemberRevisionList](DesignData.SDS2.Setup.MemberRevisionList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5F%5F%5F)CopyTo(MemberRevision\[\])

##### Declaration

```
public void CopyTo(MemberRevision[] array)
```

##### Parameters

| Type                                                            | Name  | Description |
| --------------------------------------------------------------- | ----- | ----------- |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5F%5F%5FSystem%5FInt32%5F)CopyTo(MemberRevision\[\], int)

##### Declaration

```
public void CopyTo(MemberRevision[] array, int arrayIndex)
```

##### Parameters

| Type                                                            | Name       | Description |
| --------------------------------------------------------------- | ---------- | ----------- |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, MemberRevision\[\], int, int)

##### Declaration

```
public void CopyTo(int index, MemberRevision[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                            | Name       | Description |
| --------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | index      |             |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FFinalize)\~MemberRevisionList()

##### Declaration

```
protected ~MemberRevisionList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public MemberRevisionList.MemberRevisionListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                           | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [MemberRevisionList](DesignData.SDS2.Setup.MemberRevisionList.html).[MemberRevisionListEnumerator](DesignData.SDS2.Setup.MemberRevisionList.MemberRevisionListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public MemberRevisionList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [MemberRevisionList](DesignData.SDS2.Setup.MemberRevisionList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5F)Insert(int, MemberRevision)

##### Declaration

```
public void Insert(int index, MemberRevision x)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index |             |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html) | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FMemberRevisionList%5F)InsertRange(int, MemberRevisionList)

##### Declaration

```
public void InsertRange(int index, MemberRevisionList values)
```

##### Parameters

| Type                                                                | Name   | Description |
| ------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | index  |             |
| [MemberRevisionList](DesignData.SDS2.Setup.MemberRevisionList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5FSystem%5FInt32%5F)Repeat(MemberRevision, int)

##### Declaration

```
public static MemberRevisionList Repeat(MemberRevision value, int count)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | count |             |

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [MemberRevisionList](DesignData.SDS2.Setup.MemberRevisionList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FMemberRevisionList%5F)SetRange(int, MemberRevisionList)

##### Declaration

```
public void SetRange(int index, MemberRevisionList values)
```

##### Parameters

| Type                                                                | Name   | Description |
| ------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | index  |             |
| [MemberRevisionList](DesignData.SDS2.Setup.MemberRevisionList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevisionList%5FToArray)ToArray()

##### Declaration

```
public MemberRevision[] ToArray()
```

##### Returns

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)