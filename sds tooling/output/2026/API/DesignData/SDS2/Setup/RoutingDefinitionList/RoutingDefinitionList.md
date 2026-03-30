# Class RoutingDefinitionList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

RoutingDefinitionList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html)\>

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
public class RoutingDefinitionList : IEnumerable<RoutingDefinition>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F%5Fctor)RoutingDefinitionList()

##### Declaration

```
public RoutingDefinitionList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F)RoutingDefinitionList(RoutingDefinitionList)

##### Declaration

```
public RoutingDefinitionList(RoutingDefinitionList other)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5F%5F)RoutingDefinitionList(IEnumerable<RoutingDefinition>)

##### Declaration

```
public RoutingDefinitionList(IEnumerable<RoutingDefinition> c)
```

##### Parameters

| Type                                                                                                                                                               | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)RoutingDefinitionList(IEnumerable)

##### Declaration

```
public RoutingDefinitionList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F%5Fctor%5FSystem%5FInt32%5F)RoutingDefinitionList(int)

##### Declaration

```
public RoutingDefinitionList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public RoutingDefinition this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5F)Add(RoutingDefinition)

##### Declaration

```
public void Add(RoutingDefinition x)
```

##### Parameters

| Type                                                              | Name | Description |
| ----------------------------------------------------------------- | ---- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F)AddRange(RoutingDefinitionList)

##### Declaration

```
public void AddRange(RoutingDefinitionList values)
```

##### Parameters

| Type                                                                      | Name   | Description |
| ------------------------------------------------------------------------- | ------ | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5F%5F%5F)CopyTo(RoutingDefinition\[\])

##### Declaration

```
public void CopyTo(RoutingDefinition[] array)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5F%5F%5FSystem%5FInt32%5F)CopyTo(RoutingDefinition\[\], int)

##### Declaration

```
public void CopyTo(RoutingDefinition[] array, int arrayIndex)
```

##### Parameters

| Type                                                                  | Name       | Description |
| --------------------------------------------------------------------- | ---------- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, RoutingDefinition\[\], int, int)

##### Declaration

```
public void CopyTo(int index, RoutingDefinition[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                  | Name       | Description |
| --------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | index      |             |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FFinalize)\~RoutingDefinitionList()

##### Declaration

```
protected ~RoutingDefinitionList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public RoutingDefinitionList.RoutingDefinitionListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                          | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html).[RoutingDefinitionListEnumerator](DesignData.SDS2.Setup.RoutingDefinitionList.RoutingDefinitionListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public RoutingDefinitionList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5F)Insert(int, RoutingDefinition)

##### Declaration

```
public void Insert(int index, RoutingDefinition x)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | index |             |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F)InsertRange(int, RoutingDefinitionList)

##### Declaration

```
public void InsertRange(int index, RoutingDefinitionList values)
```

##### Parameters

| Type                                                                      | Name   | Description |
| ------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | index  |             |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5FSystem%5FInt32%5F)Repeat(RoutingDefinition, int)

##### Declaration

```
public static RoutingDefinitionList Repeat(RoutingDefinition value, int count)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | count |             |

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5F)SetRange(int, RoutingDefinitionList)

##### Declaration

```
public void SetRange(int index, RoutingDefinitionList values)
```

##### Parameters

| Type                                                                      | Name   | Description |
| ------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | index  |             |
| [RoutingDefinitionList](DesignData.SDS2.Setup.RoutingDefinitionList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinitionList%5FToArray)ToArray()

##### Declaration

```
public RoutingDefinition[] ToArray()
```

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)