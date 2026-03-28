# Class RoutingDefinitionTableList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

RoutingDefinitionTableList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html)\>

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
public class RoutingDefinitionTableList : IEnumerable<RoutingDefinitionList>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5F%5Fctor)RoutingDefinitionTableList()

##### Declaration

```
public RoutingDefinitionTableList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5F)RoutingDefinitionTableList(RoutingDefinitionTableList)

##### Declaration

```
public RoutingDefinitionTableList(RoutingDefinitionTableList other)
```

##### Parameters

| Type                                                                                | Name  | Description |
| ----------------------------------------------------------------------------------- | ----- | ----------- |
| [RoutingDefinitionTableList](DesignData.SDS2.Setup.RoutingDefinitionTableList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F%5F)RoutingDefinitionTableList(IEnumerable<RoutingDefinitionList>)

##### Declaration

```
public RoutingDefinitionTableList(IEnumerable<RoutingDefinitionList> c)
```

##### Parameters

| Type                                                                                                                                                                       | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)RoutingDefinitionTableList(IEnumerable)

##### Declaration

```
public RoutingDefinitionTableList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5F%5Fctor%5FSystem%5FInt32%5F)RoutingDefinitionTableList(int)

##### Declaration

```
public RoutingDefinitionTableList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public RoutingDefinitionList this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F)Add(RoutingDefinitionList)

##### Declaration

```
public void Add(RoutingDefinitionList x)
```

##### Parameters

| Type                                                                      | Name | Description |
| ------------------------------------------------------------------------- | ---- | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5F)AddRange(RoutingDefinitionTableList)

##### Declaration

```
public void AddRange(RoutingDefinitionTableList values)
```

##### Parameters

| Type                                                                                | Name   | Description |
| ----------------------------------------------------------------------------------- | ------ | ----------- |
| [RoutingDefinitionTableList](DesignData.SDS2.Setup.RoutingDefinitionTableList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F%5F%5F)CopyTo(RoutingDefinitionList\[\])

##### Declaration

```
public void CopyTo(RoutingDefinitionList[] array)
```

##### Parameters

| Type                                                                          | Name  | Description |
| ----------------------------------------------------------------------------- | ----- | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F%5F%5FSystem%5FInt32%5F)CopyTo(RoutingDefinitionList\[\], int)

##### Declaration

```
public void CopyTo(RoutingDefinitionList[] array, int arrayIndex)
```

##### Parameters

| Type                                                                          | Name       | Description |
| ----------------------------------------------------------------------------- | ---------- | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, RoutingDefinitionList\[\], int, int)

##### Declaration

```
public void CopyTo(int index, RoutingDefinitionList[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                          | Name       | Description |
| ----------------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | index      |             |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FFinalize)\~RoutingDefinitionTableList()

##### Declaration

```
protected ~RoutingDefinitionTableList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public RoutingDefinitionTableList.RoutingDefinitionTableListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                                                   | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [RoutingDefinitionTableList](DesignData.SDS2.Setup.RoutingDefinitionTableList.html).[RoutingDefinitionTableListEnumerator](DesignData.SDS2.Setup.RoutingDefinitionTableList.RoutingDefinitionTableListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public RoutingDefinitionTableList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [RoutingDefinitionTableList](DesignData.SDS2.Setup.RoutingDefinitionTableList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F)Insert(int, RoutingDefinitionList)

##### Declaration

```
public void Insert(int index, RoutingDefinitionList x)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | index |             |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html) | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5F)InsertRange(int, RoutingDefinitionTableList)

##### Declaration

```
public void InsertRange(int index, RoutingDefinitionTableList values)
```

##### Parameters

| Type                                                                                | Name   | Description |
| ----------------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                          | index  |             |
| [RoutingDefinitionTableList](DesignData.SDS2.Setup.RoutingDefinitionTableList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FSystem%5FInt32%5F)Repeat(RoutingDefinitionList, int)

##### Declaration

```
public static RoutingDefinitionTableList Repeat(RoutingDefinitionList value, int count)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | count |             |

##### Returns

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [RoutingDefinitionTableList](DesignData.SDS2.Setup.RoutingDefinitionTableList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5F)SetRange(int, RoutingDefinitionTableList)

##### Declaration

```
public void SetRange(int index, RoutingDefinitionTableList values)
```

##### Parameters

| Type                                                                                | Name   | Description |
| ----------------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                          | index  |             |
| [RoutingDefinitionTableList](DesignData.SDS2.Setup.RoutingDefinitionTableList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionTableList%5FToArray)ToArray()

##### Declaration

```
public RoutingDefinitionList[] ToArray()
```

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)