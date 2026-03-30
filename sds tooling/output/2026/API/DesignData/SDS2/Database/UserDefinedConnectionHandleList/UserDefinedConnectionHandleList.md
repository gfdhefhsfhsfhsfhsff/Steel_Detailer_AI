# Class UserDefinedConnectionHandleList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

UserDefinedConnectionHandleList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html)\>

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
public class UserDefinedConnectionHandleList : IEnumerable<UserDefinedConnectionHandle>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5F%5Fctor)UserDefinedConnectionHandleList()

##### Declaration

```
public UserDefinedConnectionHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5F)UserDefinedConnectionHandleList(UserDefinedConnectionHandleList)

##### Declaration

```
public UserDefinedConnectionHandleList(UserDefinedConnectionHandleList other)
```

##### Parameters

| Type                                                                                             | Name  | Description |
| ------------------------------------------------------------------------------------------------ | ----- | ----------- |
| [UserDefinedConnectionHandleList](DesignData.SDS2.Database.UserDefinedConnectionHandleList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandle%5F%5F)UserDefinedConnectionHandleList(IEnumerable<UserDefinedConnectionHandle>)

##### Declaration

```
public UserDefinedConnectionHandleList(IEnumerable<UserDefinedConnectionHandle> c)
```

##### Parameters

| Type                                                                                                                                                                                      | Name | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)UserDefinedConnectionHandleList(IEnumerable)

##### Declaration

```
public UserDefinedConnectionHandleList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5F%5Fctor%5FSystem%5FInt32%5F)UserDefinedConnectionHandleList(int)

##### Declaration

```
public UserDefinedConnectionHandleList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public UserDefinedConnectionHandle this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                                     | Description |
| ---------------------------------------------------------------------------------------- | ----------- |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandle%5F)Add(UserDefinedConnectionHandle)

##### Declaration

```
public void Add(UserDefinedConnectionHandle x)
```

##### Parameters

| Type                                                                                     | Name | Description |
| ---------------------------------------------------------------------------------------- | ---- | ----------- |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FAddRange%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5F)AddRange(UserDefinedConnectionHandleList)

##### Declaration

```
public void AddRange(UserDefinedConnectionHandleList values)
```

##### Parameters

| Type                                                                                             | Name   | Description |
| ------------------------------------------------------------------------------------------------ | ------ | ----------- |
| [UserDefinedConnectionHandleList](DesignData.SDS2.Database.UserDefinedConnectionHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandle%5F%5F%5F)CopyTo(UserDefinedConnectionHandle\[\])

##### Declaration

```
public void CopyTo(UserDefinedConnectionHandle[] array)
```

##### Parameters

| Type                                                                                         | Name  | Description |
| -------------------------------------------------------------------------------------------- | ----- | ----------- |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandle%5F%5F%5FSystem%5FInt32%5F)CopyTo(UserDefinedConnectionHandle\[\], int)

##### Declaration

```
public void CopyTo(UserDefinedConnectionHandle[] array, int arrayIndex)
```

##### Parameters

| Type                                                                                         | Name       | Description |
| -------------------------------------------------------------------------------------------- | ---------- | ----------- |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                   | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandle%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, UserDefinedConnectionHandle\[\], int, int)

##### Declaration

```
public void CopyTo(int index, UserDefinedConnectionHandle[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                                         | Name       | Description |
| -------------------------------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                   | index      |             |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                   | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                   | count      |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FFinalize)\~UserDefinedConnectionHandleList()

##### Declaration

```
protected ~UserDefinedConnectionHandleList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public UserDefinedConnectionHandleList.UserDefinedConnectionHandleListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [UserDefinedConnectionHandleList](DesignData.SDS2.Database.UserDefinedConnectionHandleList.html).[UserDefinedConnectionHandleListEnumerator](DesignData.SDS2.Database.UserDefinedConnectionHandleList.UserDefinedConnectionHandleListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public UserDefinedConnectionHandleList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                                             | Description |
| ------------------------------------------------------------------------------------------------ | ----------- |
| [UserDefinedConnectionHandleList](DesignData.SDS2.Database.UserDefinedConnectionHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandle%5F)Insert(int, UserDefinedConnectionHandle)

##### Declaration

```
public void Insert(int index, UserDefinedConnectionHandle x)
```

##### Parameters

| Type                                                                                     | Name  | Description |
| ---------------------------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                               | index |             |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html) | x     |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5F)InsertRange(int, UserDefinedConnectionHandleList)

##### Declaration

```
public void InsertRange(int index, UserDefinedConnectionHandleList values)
```

##### Parameters

| Type                                                                                             | Name   | Description |
| ------------------------------------------------------------------------------------------------ | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                       | index  |             |
| [UserDefinedConnectionHandleList](DesignData.SDS2.Database.UserDefinedConnectionHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FRepeat%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandle%5FSystem%5FInt32%5F)Repeat(UserDefinedConnectionHandle, int)

##### Declaration

```
public static UserDefinedConnectionHandleList Repeat(UserDefinedConnectionHandle value, int count)
```

##### Parameters

| Type                                                                                     | Name  | Description |
| ---------------------------------------------------------------------------------------- | ----- | ----------- |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                               | count |             |

##### Returns

| Type                                                                                             | Description |
| ------------------------------------------------------------------------------------------------ | ----------- |
| [UserDefinedConnectionHandleList](DesignData.SDS2.Database.UserDefinedConnectionHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5F)SetRange(int, UserDefinedConnectionHandleList)

##### Declaration

```
public void SetRange(int index, UserDefinedConnectionHandleList values)
```

##### Parameters

| Type                                                                                             | Name   | Description |
| ------------------------------------------------------------------------------------------------ | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                       | index  |             |
| [UserDefinedConnectionHandleList](DesignData.SDS2.Database.UserDefinedConnectionHandleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FToArray)ToArray()

##### Declaration

```
public UserDefinedConnectionHandle[] ToArray()
```

##### Returns

| Type                                                                                         | Description |
| -------------------------------------------------------------------------------------------- | ----------- |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)