# Class RepositoryList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

RepositoryList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Repository](DesignData.SDS2.Database.Repository.html)\>

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
public class RepositoryList : IEnumerable<Repository>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5F%5Fctor)RepositoryList()

##### Declaration

```
public RepositoryList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FRepositoryList%5F)RepositoryList(RepositoryList)

##### Declaration

```
public RepositoryList(RepositoryList other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [RepositoryList](DesignData.SDS2.Database.RepositoryList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDatabase%5FRepository%5F%5F)RepositoryList(IEnumerable<Repository>)

##### Declaration

```
public RepositoryList(IEnumerable<Repository> c)
```

##### Parameters

| Type                                                                                                                                                    | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Repository](DesignData.SDS2.Database.Repository.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)RepositoryList(IEnumerable)

##### Declaration

```
public RepositoryList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5F%5Fctor%5FSystem%5FInt32%5F)RepositoryList(int)

##### Declaration

```
public RepositoryList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Repository this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [Repository](DesignData.SDS2.Database.Repository.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FRepository%5F)Add(Repository)

##### Declaration

```
public void Add(Repository x)
```

##### Parameters

| Type                                                   | Name | Description |
| ------------------------------------------------------ | ---- | ----------- |
| [Repository](DesignData.SDS2.Database.Repository.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FAddRange%5FDesignData%5FSDS2%5FDatabase%5FRepositoryList%5F)AddRange(RepositoryList)

##### Declaration

```
public void AddRange(RepositoryList values)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [RepositoryList](DesignData.SDS2.Database.RepositoryList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FRepository%5F%5F%5F)CopyTo(Repository\[\])

##### Declaration

```
public void CopyTo(Repository[] array)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Repository](DesignData.SDS2.Database.Repository.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FRepository%5F%5F%5FSystem%5FInt32%5F)CopyTo(Repository\[\], int)

##### Declaration

```
public void CopyTo(Repository[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Repository](DesignData.SDS2.Database.Repository.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FRepository%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Repository\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Repository[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Repository](DesignData.SDS2.Database.Repository.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FFinalize)\~RepositoryList()

##### Declaration

```
protected ~RepositoryList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public RepositoryList.RepositoryListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                             | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [RepositoryList](DesignData.SDS2.Database.RepositoryList.html).[RepositoryListEnumerator](DesignData.SDS2.Database.RepositoryList.RepositoryListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public RepositoryList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [RepositoryList](DesignData.SDS2.Database.RepositoryList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FRepository%5F)Insert(int, Repository)

##### Declaration

```
public void Insert(int index, Repository x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Repository](DesignData.SDS2.Database.Repository.html)     | x     |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FRepositoryList%5F)InsertRange(int, RepositoryList)

##### Declaration

```
public void InsertRange(int index, RepositoryList values)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index  |             |
| [RepositoryList](DesignData.SDS2.Database.RepositoryList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FRepeat%5FDesignData%5FSDS2%5FDatabase%5FRepository%5FSystem%5FInt32%5F)Repeat(Repository, int)

##### Declaration

```
public static RepositoryList Repeat(Repository value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Repository](DesignData.SDS2.Database.Repository.html)     | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [RepositoryList](DesignData.SDS2.Database.RepositoryList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FRepositoryList%5F)SetRange(int, RepositoryList)

##### Declaration

```
public void SetRange(int index, RepositoryList values)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index  |             |
| [RepositoryList](DesignData.SDS2.Database.RepositoryList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepositoryList%5FToArray)ToArray()

##### Declaration

```
public Repository[] ToArray()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [Repository](DesignData.SDS2.Database.Repository.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)