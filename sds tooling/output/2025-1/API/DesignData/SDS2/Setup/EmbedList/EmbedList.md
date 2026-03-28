# Class EmbedList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

EmbedList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Embed](DesignData.SDS2.Setup.Embed.html)\>

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
public class EmbedList : IEnumerable<Embed>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5F%5Fctor)EmbedList()

##### Declaration

```
public EmbedList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FEmbedList%5F)EmbedList(EmbedList)

##### Declaration

```
public EmbedList(EmbedList other)
```

##### Parameters

| Type                                              | Name  | Description |
| ------------------------------------------------- | ----- | ----------- |
| [EmbedList](DesignData.SDS2.Setup.EmbedList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FEmbed%5F%5F)EmbedList(IEnumerable<Embed>)

##### Declaration

```
public EmbedList(IEnumerable<Embed> c)
```

##### Parameters

| Type                                                                                                                                       | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Embed](DesignData.SDS2.Setup.Embed.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)EmbedList(IEnumerable)

##### Declaration

```
public EmbedList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5F%5Fctor%5FSystem%5FInt32%5F)EmbedList(int)

##### Declaration

```
public EmbedList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Embed this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FEmbed%5F)Add(Embed)

##### Declaration

```
public void Add(Embed x)
```

##### Parameters

| Type                                      | Name | Description |
| ----------------------------------------- | ---- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FEmbedList%5F)AddRange(EmbedList)

##### Declaration

```
public void AddRange(EmbedList values)
```

##### Parameters

| Type                                              | Name   | Description |
| ------------------------------------------------- | ------ | ----------- |
| [EmbedList](DesignData.SDS2.Setup.EmbedList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FEmbed%5F%5F%5F)CopyTo(Embed\[\])

##### Declaration

```
public void CopyTo(Embed[] array)
```

##### Parameters

| Type                                          | Name  | Description |
| --------------------------------------------- | ----- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FEmbed%5F%5F%5FSystem%5FInt32%5F)CopyTo(Embed\[\], int)

##### Declaration

```
public void CopyTo(Embed[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html)\[\]              | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbed%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Embed\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Embed[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Embed](DesignData.SDS2.Setup.Embed.html)\[\]              | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FFinalize)\~EmbedList()

##### Declaration

```
protected ~EmbedList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public EmbedList.EmbedListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                              | Description |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [EmbedList](DesignData.SDS2.Setup.EmbedList.html).[EmbedListEnumerator](DesignData.SDS2.Setup.EmbedList.EmbedListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public EmbedList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [EmbedList](DesignData.SDS2.Setup.EmbedList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbed%5F)Insert(int, Embed)

##### Declaration

```
public void Insert(int index, Embed x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Embed](DesignData.SDS2.Setup.Embed.html)                  | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedList%5F)InsertRange(int, EmbedList)

##### Declaration

```
public void InsertRange(int index, EmbedList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [EmbedList](DesignData.SDS2.Setup.EmbedList.html)          | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FEmbed%5FSystem%5FInt32%5F)Repeat(Embed, int)

##### Declaration

```
public static EmbedList Repeat(Embed value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html)                  | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [EmbedList](DesignData.SDS2.Setup.EmbedList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedList%5F)SetRange(int, EmbedList)

##### Declaration

```
public void SetRange(int index, EmbedList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [EmbedList](DesignData.SDS2.Setup.EmbedList.html)          | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedList%5FToArray)ToArray()

##### Declaration

```
public Embed[] ToArray()
```

##### Returns

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)