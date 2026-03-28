# Class GroupMemberHandleList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

GroupMemberHandleList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html)\>

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
public class GroupMemberHandleList : IEnumerable<GroupMemberHandle>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5F%5Fctor)GroupMemberHandleList()

##### Declaration

```
public GroupMemberHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5F)GroupMemberHandleList(GroupMemberHandleList)

##### Declaration

```
public GroupMemberHandleList(GroupMemberHandleList other)
```

##### Parameters

| Type                                                                         | Name  | Description |
| ---------------------------------------------------------------------------- | ----- | ----------- |
| [GroupMemberHandleList](DesignData.SDS2.Database.GroupMemberHandleList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandle%5F%5F)GroupMemberHandleList(IEnumerable<GroupMemberHandle>)

##### Declaration

```
public GroupMemberHandleList(IEnumerable<GroupMemberHandle> c)
```

##### Parameters

| Type                                                                                                                                                                  | Name | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)GroupMemberHandleList(IEnumerable)

##### Declaration

```
public GroupMemberHandleList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5F%5Fctor%5FSystem%5FInt32%5F)GroupMemberHandleList(int)

##### Declaration

```
public GroupMemberHandleList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public GroupMemberHandle this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandle%5F)Add(GroupMemberHandle)

##### Declaration

```
public void Add(GroupMemberHandle x)
```

##### Parameters

| Type                                                                 | Name | Description |
| -------------------------------------------------------------------- | ---- | ----------- |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FAddRange%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5F)AddRange(GroupMemberHandleList)

##### Declaration

```
public void AddRange(GroupMemberHandleList values)
```

##### Parameters

| Type                                                                         | Name   | Description |
| ---------------------------------------------------------------------------- | ------ | ----------- |
| [GroupMemberHandleList](DesignData.SDS2.Database.GroupMemberHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandle%5F%5F%5F)CopyTo(GroupMemberHandle\[\])

##### Declaration

```
public void CopyTo(GroupMemberHandle[] array)
```

##### Parameters

| Type                                                                     | Name  | Description |
| ------------------------------------------------------------------------ | ----- | ----------- |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandle%5F%5F%5FSystem%5FInt32%5F)CopyTo(GroupMemberHandle\[\], int)

##### Declaration

```
public void CopyTo(GroupMemberHandle[] array, int arrayIndex)
```

##### Parameters

| Type                                                                     | Name       | Description |
| ------------------------------------------------------------------------ | ---------- | ----------- |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)               | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandle%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, GroupMemberHandle\[\], int, int)

##### Declaration

```
public void CopyTo(int index, GroupMemberHandle[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                     | Name       | Description |
| ------------------------------------------------------------------------ | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)               | index      |             |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)               | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)               | count      |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FFinalize)\~GroupMemberHandleList()

##### Declaration

```
protected ~GroupMemberHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public GroupMemberHandleList.GroupMemberHandleListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                                | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [GroupMemberHandleList](DesignData.SDS2.Database.GroupMemberHandleList.html).[GroupMemberHandleListEnumerator](DesignData.SDS2.Database.GroupMemberHandleList.GroupMemberHandleListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public GroupMemberHandleList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                         | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [GroupMemberHandleList](DesignData.SDS2.Database.GroupMemberHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandle%5F)Insert(int, GroupMemberHandle)

##### Declaration

```
public void Insert(int index, GroupMemberHandle x)
```

##### Parameters

| Type                                                                 | Name  | Description |
| -------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)           | index |             |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html) | x     |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5F)InsertRange(int, GroupMemberHandleList)

##### Declaration

```
public void InsertRange(int index, GroupMemberHandleList values)
```

##### Parameters

| Type                                                                         | Name   | Description |
| ---------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                   | index  |             |
| [GroupMemberHandleList](DesignData.SDS2.Database.GroupMemberHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FRepeat%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandle%5FSystem%5FInt32%5F)Repeat(GroupMemberHandle, int)

##### Declaration

```
public static GroupMemberHandleList Repeat(GroupMemberHandle value, int count)
```

##### Parameters

| Type                                                                 | Name  | Description |
| -------------------------------------------------------------------- | ----- | ----------- |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)           | count |             |

##### Returns

| Type                                                                         | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [GroupMemberHandleList](DesignData.SDS2.Database.GroupMemberHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5F)SetRange(int, GroupMemberHandleList)

##### Declaration

```
public void SetRange(int index, GroupMemberHandleList values)
```

##### Parameters

| Type                                                                         | Name   | Description |
| ---------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                   | index  |             |
| [GroupMemberHandleList](DesignData.SDS2.Database.GroupMemberHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FGroupMemberHandleList%5FToArray)ToArray()

##### Declaration

```
public GroupMemberHandle[] ToArray()
```

##### Returns

| Type                                                                     | Description |
| ------------------------------------------------------------------------ | ----------- |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)