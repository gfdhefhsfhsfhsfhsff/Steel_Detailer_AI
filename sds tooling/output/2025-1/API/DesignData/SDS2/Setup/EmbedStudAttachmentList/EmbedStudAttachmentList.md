# Class EmbedStudAttachmentList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

EmbedStudAttachmentList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[EmbedStudAttachment](DesignData.SDS2.Setup.EmbedStudAttachment.html)\>

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
public class EmbedStudAttachmentList : IEnumerable<EmbedStudAttachment>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5F%5Fctor)EmbedStudAttachmentList()

##### Declaration

```
public EmbedStudAttachmentList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5F)EmbedStudAttachmentList(EmbedStudAttachmentList)

##### Declaration

```
public EmbedStudAttachmentList(EmbedStudAttachmentList other)
```

##### Parameters

| Type                                                                          | Name  | Description |
| ----------------------------------------------------------------------------- | ----- | ----------- |
| [EmbedStudAttachmentList](DesignData.SDS2.Setup.EmbedStudAttachmentList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5F%5F)EmbedStudAttachmentList(IEnumerable<EmbedStudAttachment>)

##### Declaration

```
public EmbedStudAttachmentList(IEnumerable<EmbedStudAttachment> c)
```

##### Parameters

| Type                                                                                                                                                                   | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[EmbedStudAttachment](DesignData.SDS2.Setup.EmbedStudAttachment.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)EmbedStudAttachmentList(IEnumerable)

##### Declaration

```
public EmbedStudAttachmentList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5F%5Fctor%5FSystem%5FInt32%5F)EmbedStudAttachmentList(int)

##### Declaration

```
public EmbedStudAttachmentList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public EmbedStudAttachment this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [EmbedStudAttachment](DesignData.SDS2.Setup.EmbedStudAttachment.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5F)Add(EmbedStudAttachment)

##### Declaration

```
public void Add(EmbedStudAttachment x)
```

##### Parameters

| Type                                                                  | Name | Description |
| --------------------------------------------------------------------- | ---- | ----------- |
| [EmbedStudAttachment](DesignData.SDS2.Setup.EmbedStudAttachment.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5F)AddRange(EmbedStudAttachmentList)

##### Declaration

```
public void AddRange(EmbedStudAttachmentList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [EmbedStudAttachmentList](DesignData.SDS2.Setup.EmbedStudAttachmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5F%5F%5F)CopyTo(EmbedStudAttachment\[\])

##### Declaration

```
public void CopyTo(EmbedStudAttachment[] array)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [EmbedStudAttachment](DesignData.SDS2.Setup.EmbedStudAttachment.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5F%5F%5FSystem%5FInt32%5F)CopyTo(EmbedStudAttachment\[\], int)

##### Declaration

```
public void CopyTo(EmbedStudAttachment[] array, int arrayIndex)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [EmbedStudAttachment](DesignData.SDS2.Setup.EmbedStudAttachment.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, EmbedStudAttachment\[\], int, int)

##### Declaration

```
public void CopyTo(int index, EmbedStudAttachment[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | index      |             |
| [EmbedStudAttachment](DesignData.SDS2.Setup.EmbedStudAttachment.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FFinalize)\~EmbedStudAttachmentList()

##### Declaration

```
protected ~EmbedStudAttachmentList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public EmbedStudAttachmentList.EmbedStudAttachmentListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                                    | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [EmbedStudAttachmentList](DesignData.SDS2.Setup.EmbedStudAttachmentList.html).[EmbedStudAttachmentListEnumerator](DesignData.SDS2.Setup.EmbedStudAttachmentList.EmbedStudAttachmentListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public EmbedStudAttachmentList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [EmbedStudAttachmentList](DesignData.SDS2.Setup.EmbedStudAttachmentList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5F)Insert(int, EmbedStudAttachment)

##### Declaration

```
public void Insert(int index, EmbedStudAttachment x)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | index |             |
| [EmbedStudAttachment](DesignData.SDS2.Setup.EmbedStudAttachment.html) | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5F)InsertRange(int, EmbedStudAttachmentList)

##### Declaration

```
public void InsertRange(int index, EmbedStudAttachmentList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | index  |             |
| [EmbedStudAttachmentList](DesignData.SDS2.Setup.EmbedStudAttachmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5FSystem%5FInt32%5F)Repeat(EmbedStudAttachment, int)

##### Declaration

```
public static EmbedStudAttachmentList Repeat(EmbedStudAttachment value, int count)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [EmbedStudAttachment](DesignData.SDS2.Setup.EmbedStudAttachment.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | count |             |

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [EmbedStudAttachmentList](DesignData.SDS2.Setup.EmbedStudAttachmentList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5F)SetRange(int, EmbedStudAttachmentList)

##### Declaration

```
public void SetRange(int index, EmbedStudAttachmentList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | index  |             |
| [EmbedStudAttachmentList](DesignData.SDS2.Setup.EmbedStudAttachmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachmentList%5FToArray)ToArray()

##### Declaration

```
public EmbedStudAttachment[] ToArray()
```

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [EmbedStudAttachment](DesignData.SDS2.Setup.EmbedStudAttachment.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)