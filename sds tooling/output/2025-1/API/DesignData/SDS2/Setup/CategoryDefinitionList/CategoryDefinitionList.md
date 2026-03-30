# Class CategoryDefinitionList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CategoryDefinitionList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html)\>

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
public class CategoryDefinitionList : IEnumerable<CategoryDefinition>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5F%5Fctor)CategoryDefinitionList()

##### Declaration

```
public CategoryDefinitionList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5F)CategoryDefinitionList(CategoryDefinitionList)

##### Declaration

```
public CategoryDefinitionList(CategoryDefinitionList other)
```

##### Parameters

| Type                                                                        | Name  | Description |
| --------------------------------------------------------------------------- | ----- | ----------- |
| [CategoryDefinitionList](DesignData.SDS2.Setup.CategoryDefinitionList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F%5F)CategoryDefinitionList(IEnumerable<CategoryDefinition>)

##### Declaration

```
public CategoryDefinitionList(IEnumerable<CategoryDefinition> c)
```

##### Parameters

| Type                                                                                                                                                                 | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)CategoryDefinitionList(IEnumerable)

##### Declaration

```
public CategoryDefinitionList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5F%5Fctor%5FSystem%5FInt32%5F)CategoryDefinitionList(int)

##### Declaration

```
public CategoryDefinitionList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public CategoryDefinition this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F)Add(CategoryDefinition)

##### Declaration

```
public void Add(CategoryDefinition x)
```

##### Parameters

| Type                                                                | Name | Description |
| ------------------------------------------------------------------- | ---- | ----------- |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5F)AddRange(CategoryDefinitionList)

##### Declaration

```
public void AddRange(CategoryDefinitionList values)
```

##### Parameters

| Type                                                                        | Name   | Description |
| --------------------------------------------------------------------------- | ------ | ----------- |
| [CategoryDefinitionList](DesignData.SDS2.Setup.CategoryDefinitionList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F%5F%5F)CopyTo(CategoryDefinition\[\])

##### Declaration

```
public void CopyTo(CategoryDefinition[] array)
```

##### Parameters

| Type                                                                    | Name  | Description |
| ----------------------------------------------------------------------- | ----- | ----------- |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F%5F%5FSystem%5FInt32%5F)CopyTo(CategoryDefinition\[\], int)

##### Declaration

```
public void CopyTo(CategoryDefinition[] array, int arrayIndex)
```

##### Parameters

| Type                                                                    | Name       | Description |
| ----------------------------------------------------------------------- | ---------- | ----------- |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)              | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, CategoryDefinition\[\], int, int)

##### Declaration

```
public void CopyTo(int index, CategoryDefinition[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                    | Name       | Description |
| ----------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)              | index      |             |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)              | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)              | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FFinalize)\~CategoryDefinitionList()

##### Declaration

```
protected ~CategoryDefinitionList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public CategoryDefinitionList.CategoryDefinitionListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                               | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [CategoryDefinitionList](DesignData.SDS2.Setup.CategoryDefinitionList.html).[CategoryDefinitionListEnumerator](DesignData.SDS2.Setup.CategoryDefinitionList.CategoryDefinitionListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public CategoryDefinitionList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [CategoryDefinitionList](DesignData.SDS2.Setup.CategoryDefinitionList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F)Insert(int, CategoryDefinition)

##### Declaration

```
public void Insert(int index, CategoryDefinition x)
```

##### Parameters

| Type                                                                | Name  | Description |
| ------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | index |             |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html) | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5F)InsertRange(int, CategoryDefinitionList)

##### Declaration

```
public void InsertRange(int index, CategoryDefinitionList values)
```

##### Parameters

| Type                                                                        | Name   | Description |
| --------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                  | index  |             |
| [CategoryDefinitionList](DesignData.SDS2.Setup.CategoryDefinitionList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5FSystem%5FInt32%5F)Repeat(CategoryDefinition, int)

##### Declaration

```
public static CategoryDefinitionList Repeat(CategoryDefinition value, int count)
```

##### Parameters

| Type                                                                | Name  | Description |
| ------------------------------------------------------------------- | ----- | ----------- |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | count |             |

##### Returns

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [CategoryDefinitionList](DesignData.SDS2.Setup.CategoryDefinitionList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5F)SetRange(int, CategoryDefinitionList)

##### Declaration

```
public void SetRange(int index, CategoryDefinitionList values)
```

##### Parameters

| Type                                                                        | Name   | Description |
| --------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                  | index  |             |
| [CategoryDefinitionList](DesignData.SDS2.Setup.CategoryDefinitionList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinitionList%5FToArray)ToArray()

##### Declaration

```
public CategoryDefinition[] ToArray()
```

##### Returns

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)