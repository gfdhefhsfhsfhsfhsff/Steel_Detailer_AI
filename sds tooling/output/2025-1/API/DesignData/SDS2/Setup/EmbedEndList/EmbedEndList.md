# Class EmbedEndList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

EmbedEndList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[EmbedEnd](DesignData.SDS2.Setup.EmbedEnd.html)\>

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
public class EmbedEndList : IEnumerable<EmbedEnd>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5F%5Fctor)EmbedEndList()

##### Declaration

```
public EmbedEndList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FEmbedEndList%5F)EmbedEndList(EmbedEndList)

##### Declaration

```
public EmbedEndList(EmbedEndList other)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [EmbedEndList](DesignData.SDS2.Setup.EmbedEndList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FEmbedEnd%5F%5F)EmbedEndList(IEnumerable<EmbedEnd>)

##### Declaration

```
public EmbedEndList(IEnumerable<EmbedEnd> c)
```

##### Parameters

| Type                                                                                                                                             | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[EmbedEnd](DesignData.SDS2.Setup.EmbedEnd.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)EmbedEndList(IEnumerable)

##### Declaration

```
public EmbedEndList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5F%5Fctor%5FSystem%5FInt32%5F)EmbedEndList(int)

##### Declaration

```
public EmbedEndList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public EmbedEnd this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [EmbedEnd](DesignData.SDS2.Setup.EmbedEnd.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FEmbedEnd%5F)Add(EmbedEnd)

##### Declaration

```
public void Add(EmbedEnd x)
```

##### Parameters

| Type                                            | Name | Description |
| ----------------------------------------------- | ---- | ----------- |
| [EmbedEnd](DesignData.SDS2.Setup.EmbedEnd.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FEmbedEndList%5F)AddRange(EmbedEndList)

##### Declaration

```
public void AddRange(EmbedEndList values)
```

##### Parameters

| Type                                                    | Name   | Description |
| ------------------------------------------------------- | ------ | ----------- |
| [EmbedEndList](DesignData.SDS2.Setup.EmbedEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FEmbedEnd%5F%5F%5F)CopyTo(EmbedEnd\[\])

##### Declaration

```
public void CopyTo(EmbedEnd[] array)
```

##### Parameters

| Type                                                | Name  | Description |
| --------------------------------------------------- | ----- | ----------- |
| [EmbedEnd](DesignData.SDS2.Setup.EmbedEnd.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FEmbedEnd%5F%5F%5FSystem%5FInt32%5F)CopyTo(EmbedEnd\[\], int)

##### Declaration

```
public void CopyTo(EmbedEnd[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [EmbedEnd](DesignData.SDS2.Setup.EmbedEnd.html)\[\]        | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedEnd%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, EmbedEnd\[\], int, int)

##### Declaration

```
public void CopyTo(int index, EmbedEnd[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [EmbedEnd](DesignData.SDS2.Setup.EmbedEnd.html)\[\]        | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FFinalize)\~EmbedEndList()

##### Declaration

```
protected ~EmbedEndList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public EmbedEndList.EmbedEndListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                             | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [EmbedEndList](DesignData.SDS2.Setup.EmbedEndList.html).[EmbedEndListEnumerator](DesignData.SDS2.Setup.EmbedEndList.EmbedEndListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public EmbedEndList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [EmbedEndList](DesignData.SDS2.Setup.EmbedEndList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedEnd%5F)Insert(int, EmbedEnd)

##### Declaration

```
public void Insert(int index, EmbedEnd x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [EmbedEnd](DesignData.SDS2.Setup.EmbedEnd.html)            | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedEndList%5F)InsertRange(int, EmbedEndList)

##### Declaration

```
public void InsertRange(int index, EmbedEndList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [EmbedEndList](DesignData.SDS2.Setup.EmbedEndList.html)    | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FEmbedEnd%5FSystem%5FInt32%5F)Repeat(EmbedEnd, int)

##### Declaration

```
public static EmbedEndList Repeat(EmbedEnd value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [EmbedEnd](DesignData.SDS2.Setup.EmbedEnd.html)            | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [EmbedEndList](DesignData.SDS2.Setup.EmbedEndList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedEndList%5F)SetRange(int, EmbedEndList)

##### Declaration

```
public void SetRange(int index, EmbedEndList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [EmbedEndList](DesignData.SDS2.Setup.EmbedEndList.html)    | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedEndList%5FToArray)ToArray()

##### Declaration

```
public EmbedEnd[] ToArray()
```

##### Returns

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [EmbedEnd](DesignData.SDS2.Setup.EmbedEnd.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)