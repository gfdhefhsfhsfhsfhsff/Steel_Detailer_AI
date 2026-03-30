# Class MemberHandleList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MemberHandleList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MemberHandle](DesignData.SDS2.Database.MemberHandle.html)\>

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
public class MemberHandleList : IEnumerable<MemberHandle>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5F%5Fctor)MemberHandleList()

##### Declaration

```
public MemberHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FMemberHandleList%5F)MemberHandleList(MemberHandleList)

##### Declaration

```
public MemberHandleList(MemberHandleList other)
```

##### Parameters

| Type                                                               | Name  | Description |
| ------------------------------------------------------------------ | ----- | ----------- |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F%5F)MemberHandleList(IEnumerable<MemberHandle>)

##### Declaration

```
public MemberHandleList(IEnumerable<MemberHandle> c)
```

##### Parameters

| Type                                                                                                                                                        | Name | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MemberHandle](DesignData.SDS2.Database.MemberHandle.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)MemberHandleList(IEnumerable)

##### Declaration

```
public MemberHandleList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5F%5Fctor%5FSystem%5FInt32%5F)MemberHandleList(int)

##### Declaration

```
public MemberHandleList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public MemberHandle this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F)Add(MemberHandle)

##### Declaration

```
public void Add(MemberHandle x)
```

##### Parameters

| Type                                                       | Name | Description |
| ---------------------------------------------------------- | ---- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FAddRange%5FDesignData%5FSDS2%5FDatabase%5FMemberHandleList%5F)AddRange(MemberHandleList)

##### Declaration

```
public void AddRange(MemberHandleList values)
```

##### Parameters

| Type                                                               | Name   | Description |
| ------------------------------------------------------------------ | ------ | ----------- |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F%5F%5F)CopyTo(MemberHandle\[\])

##### Declaration

```
public void CopyTo(MemberHandle[] array)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F%5F%5FSystem%5FInt32%5F)CopyTo(MemberHandle\[\], int)

##### Declaration

```
public void CopyTo(MemberHandle[] array, int arrayIndex)
```

##### Parameters

| Type                                                           | Name       | Description |
| -------------------------------------------------------------- | ---------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, MemberHandle\[\], int, int)

##### Declaration

```
public void CopyTo(int index, MemberHandle[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                           | Name       | Description |
| -------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index      |             |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | count      |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FFinalize)\~MemberHandleList()

##### Declaration

```
protected ~MemberHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public MemberHandleList.MemberHandleListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                       | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html).[MemberHandleListEnumerator](DesignData.SDS2.Database.MemberHandleList.MemberHandleListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public MemberHandleList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                               | Description |
| ------------------------------------------------------------------ | ----------- |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F)Insert(int, MemberHandle)

##### Declaration

```
public void Insert(int index, MemberHandle x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) | x     |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FMemberHandleList%5F)InsertRange(int, MemberHandleList)

##### Declaration

```
public void InsertRange(int index, MemberHandleList values)
```

##### Parameters

| Type                                                               | Name   | Description |
| ------------------------------------------------------------------ | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | index  |             |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FRepeat%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5FSystem%5FInt32%5F)Repeat(MemberHandle, int)

##### Declaration

```
public static MemberHandleList Repeat(MemberHandle value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                               | Description |
| ------------------------------------------------------------------ | ----------- |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FMemberHandleList%5F)SetRange(int, MemberHandleList)

##### Declaration

```
public void SetRange(int index, MemberHandleList values)
```

##### Parameters

| Type                                                               | Name   | Description |
| ------------------------------------------------------------------ | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | index  |             |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FToArray)ToArray()

##### Declaration

```
public MemberHandle[] ToArray()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)