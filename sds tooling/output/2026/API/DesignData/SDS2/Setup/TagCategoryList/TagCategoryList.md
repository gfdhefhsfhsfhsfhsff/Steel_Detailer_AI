# Class TagCategoryList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

TagCategoryList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[TagCategory](DesignData.SDS2.Setup.TagCategory.html)\>

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
public class TagCategoryList : IEnumerable<TagCategory>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5F%5Fctor)TagCategoryList()

##### Declaration

```
public TagCategoryList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FTagCategoryList%5F)TagCategoryList(TagCategoryList)

##### Declaration

```
public TagCategoryList(TagCategoryList other)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [TagCategoryList](DesignData.SDS2.Setup.TagCategoryList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FTagCategory%5F%5F)TagCategoryList(IEnumerable<TagCategory>)

##### Declaration

```
public TagCategoryList(IEnumerable<TagCategory> c)
```

##### Parameters

| Type                                                                                                                                                   | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[TagCategory](DesignData.SDS2.Setup.TagCategory.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)TagCategoryList(IEnumerable)

##### Declaration

```
public TagCategoryList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5F%5Fctor%5FSystem%5FInt32%5F)TagCategoryList(int)

##### Declaration

```
public TagCategoryList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public TagCategory this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [TagCategory](DesignData.SDS2.Setup.TagCategory.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FTagCategory%5F)Add(TagCategory)

##### Declaration

```
public void Add(TagCategory x)
```

##### Parameters

| Type                                                  | Name | Description |
| ----------------------------------------------------- | ---- | ----------- |
| [TagCategory](DesignData.SDS2.Setup.TagCategory.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FTagCategoryList%5F)AddRange(TagCategoryList)

##### Declaration

```
public void AddRange(TagCategoryList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [TagCategoryList](DesignData.SDS2.Setup.TagCategoryList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FTagCategory%5F%5F%5F)CopyTo(TagCategory\[\])

##### Declaration

```
public void CopyTo(TagCategory[] array)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [TagCategory](DesignData.SDS2.Setup.TagCategory.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FTagCategory%5F%5F%5FSystem%5FInt32%5F)CopyTo(TagCategory\[\], int)

##### Declaration

```
public void CopyTo(TagCategory[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [TagCategory](DesignData.SDS2.Setup.TagCategory.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FTagCategory%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, TagCategory\[\], int, int)

##### Declaration

```
public void CopyTo(int index, TagCategory[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [TagCategory](DesignData.SDS2.Setup.TagCategory.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FFinalize)\~TagCategoryList()

##### Declaration

```
protected ~TagCategoryList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public TagCategoryList.TagCategoryListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                            | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [TagCategoryList](DesignData.SDS2.Setup.TagCategoryList.html).[TagCategoryListEnumerator](DesignData.SDS2.Setup.TagCategoryList.TagCategoryListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public TagCategoryList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [TagCategoryList](DesignData.SDS2.Setup.TagCategoryList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FTagCategory%5F)Insert(int, TagCategory)

##### Declaration

```
public void Insert(int index, TagCategory x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [TagCategory](DesignData.SDS2.Setup.TagCategory.html)      | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FTagCategoryList%5F)InsertRange(int, TagCategoryList)

##### Declaration

```
public void InsertRange(int index, TagCategoryList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [TagCategoryList](DesignData.SDS2.Setup.TagCategoryList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FTagCategory%5FSystem%5FInt32%5F)Repeat(TagCategory, int)

##### Declaration

```
public static TagCategoryList Repeat(TagCategory value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [TagCategory](DesignData.SDS2.Setup.TagCategory.html)      | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [TagCategoryList](DesignData.SDS2.Setup.TagCategoryList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FTagCategoryList%5F)SetRange(int, TagCategoryList)

##### Declaration

```
public void SetRange(int index, TagCategoryList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [TagCategoryList](DesignData.SDS2.Setup.TagCategoryList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategoryList%5FToArray)ToArray()

##### Declaration

```
public TagCategory[] ToArray()
```

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [TagCategory](DesignData.SDS2.Setup.TagCategory.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)