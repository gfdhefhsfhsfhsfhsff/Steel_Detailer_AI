# Class EmbedHoleAttachmentList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

EmbedHoleAttachmentList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[EmbedHoleAttachment](DesignData.SDS2.Setup.EmbedHoleAttachment.html)\>

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
public class EmbedHoleAttachmentList : IEnumerable<EmbedHoleAttachment>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5F%5Fctor)EmbedHoleAttachmentList()

##### Declaration

```
public EmbedHoleAttachmentList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5F)EmbedHoleAttachmentList(EmbedHoleAttachmentList)

##### Declaration

```
public EmbedHoleAttachmentList(EmbedHoleAttachmentList other)
```

##### Parameters

| Type                                                                          | Name  | Description |
| ----------------------------------------------------------------------------- | ----- | ----------- |
| [EmbedHoleAttachmentList](DesignData.SDS2.Setup.EmbedHoleAttachmentList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachment%5F%5F)EmbedHoleAttachmentList(IEnumerable<EmbedHoleAttachment>)

##### Declaration

```
public EmbedHoleAttachmentList(IEnumerable<EmbedHoleAttachment> c)
```

##### Parameters

| Type                                                                                                                                                                   | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[EmbedHoleAttachment](DesignData.SDS2.Setup.EmbedHoleAttachment.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)EmbedHoleAttachmentList(IEnumerable)

##### Declaration

```
public EmbedHoleAttachmentList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5F%5Fctor%5FSystem%5FInt32%5F)EmbedHoleAttachmentList(int)

##### Declaration

```
public EmbedHoleAttachmentList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public EmbedHoleAttachment this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [EmbedHoleAttachment](DesignData.SDS2.Setup.EmbedHoleAttachment.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachment%5F)Add(EmbedHoleAttachment)

##### Declaration

```
public void Add(EmbedHoleAttachment x)
```

##### Parameters

| Type                                                                  | Name | Description |
| --------------------------------------------------------------------- | ---- | ----------- |
| [EmbedHoleAttachment](DesignData.SDS2.Setup.EmbedHoleAttachment.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5F)AddRange(EmbedHoleAttachmentList)

##### Declaration

```
public void AddRange(EmbedHoleAttachmentList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [EmbedHoleAttachmentList](DesignData.SDS2.Setup.EmbedHoleAttachmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachment%5F%5F%5F)CopyTo(EmbedHoleAttachment\[\])

##### Declaration

```
public void CopyTo(EmbedHoleAttachment[] array)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [EmbedHoleAttachment](DesignData.SDS2.Setup.EmbedHoleAttachment.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachment%5F%5F%5FSystem%5FInt32%5F)CopyTo(EmbedHoleAttachment\[\], int)

##### Declaration

```
public void CopyTo(EmbedHoleAttachment[] array, int arrayIndex)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [EmbedHoleAttachment](DesignData.SDS2.Setup.EmbedHoleAttachment.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachment%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, EmbedHoleAttachment\[\], int, int)

##### Declaration

```
public void CopyTo(int index, EmbedHoleAttachment[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | index      |             |
| [EmbedHoleAttachment](DesignData.SDS2.Setup.EmbedHoleAttachment.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FFinalize)\~EmbedHoleAttachmentList()

##### Declaration

```
protected ~EmbedHoleAttachmentList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public EmbedHoleAttachmentList.EmbedHoleAttachmentListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                                    | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [EmbedHoleAttachmentList](DesignData.SDS2.Setup.EmbedHoleAttachmentList.html).[EmbedHoleAttachmentListEnumerator](DesignData.SDS2.Setup.EmbedHoleAttachmentList.EmbedHoleAttachmentListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public EmbedHoleAttachmentList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [EmbedHoleAttachmentList](DesignData.SDS2.Setup.EmbedHoleAttachmentList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachment%5F)Insert(int, EmbedHoleAttachment)

##### Declaration

```
public void Insert(int index, EmbedHoleAttachment x)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | index |             |
| [EmbedHoleAttachment](DesignData.SDS2.Setup.EmbedHoleAttachment.html) | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5F)InsertRange(int, EmbedHoleAttachmentList)

##### Declaration

```
public void InsertRange(int index, EmbedHoleAttachmentList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | index  |             |
| [EmbedHoleAttachmentList](DesignData.SDS2.Setup.EmbedHoleAttachmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachment%5FSystem%5FInt32%5F)Repeat(EmbedHoleAttachment, int)

##### Declaration

```
public static EmbedHoleAttachmentList Repeat(EmbedHoleAttachment value, int count)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [EmbedHoleAttachment](DesignData.SDS2.Setup.EmbedHoleAttachment.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | count |             |

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [EmbedHoleAttachmentList](DesignData.SDS2.Setup.EmbedHoleAttachmentList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5F)SetRange(int, EmbedHoleAttachmentList)

##### Declaration

```
public void SetRange(int index, EmbedHoleAttachmentList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | index  |             |
| [EmbedHoleAttachmentList](DesignData.SDS2.Setup.EmbedHoleAttachmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedHoleAttachmentList%5FToArray)ToArray()

##### Declaration

```
public EmbedHoleAttachment[] ToArray()
```

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [EmbedHoleAttachment](DesignData.SDS2.Setup.EmbedHoleAttachment.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)