# Class DeformedBarAttachmentList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DeformedBarAttachmentList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[DeformedBarAttachment](DesignData.SDS2.Setup.DeformedBarAttachment.html)\>

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
public class DeformedBarAttachmentList : IEnumerable<DeformedBarAttachment>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5F%5Fctor)DeformedBarAttachmentList()

##### Declaration

```
public DeformedBarAttachmentList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5F)DeformedBarAttachmentList(DeformedBarAttachmentList)

##### Declaration

```
public DeformedBarAttachmentList(DeformedBarAttachmentList other)
```

##### Parameters

| Type                                                                              | Name  | Description |
| --------------------------------------------------------------------------------- | ----- | ----------- |
| [DeformedBarAttachmentList](DesignData.SDS2.Setup.DeformedBarAttachmentList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachment%5F%5F)DeformedBarAttachmentList(IEnumerable<DeformedBarAttachment>)

##### Declaration

```
public DeformedBarAttachmentList(IEnumerable<DeformedBarAttachment> c)
```

##### Parameters

| Type                                                                                                                                                                       | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[DeformedBarAttachment](DesignData.SDS2.Setup.DeformedBarAttachment.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)DeformedBarAttachmentList(IEnumerable)

##### Declaration

```
public DeformedBarAttachmentList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5F%5Fctor%5FSystem%5FInt32%5F)DeformedBarAttachmentList(int)

##### Declaration

```
public DeformedBarAttachmentList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public DeformedBarAttachment this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [DeformedBarAttachment](DesignData.SDS2.Setup.DeformedBarAttachment.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachment%5F)Add(DeformedBarAttachment)

##### Declaration

```
public void Add(DeformedBarAttachment x)
```

##### Parameters

| Type                                                                      | Name | Description |
| ------------------------------------------------------------------------- | ---- | ----------- |
| [DeformedBarAttachment](DesignData.SDS2.Setup.DeformedBarAttachment.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5F)AddRange(DeformedBarAttachmentList)

##### Declaration

```
public void AddRange(DeformedBarAttachmentList values)
```

##### Parameters

| Type                                                                              | Name   | Description |
| --------------------------------------------------------------------------------- | ------ | ----------- |
| [DeformedBarAttachmentList](DesignData.SDS2.Setup.DeformedBarAttachmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachment%5F%5F%5F)CopyTo(DeformedBarAttachment\[\])

##### Declaration

```
public void CopyTo(DeformedBarAttachment[] array)
```

##### Parameters

| Type                                                                          | Name  | Description |
| ----------------------------------------------------------------------------- | ----- | ----------- |
| [DeformedBarAttachment](DesignData.SDS2.Setup.DeformedBarAttachment.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachment%5F%5F%5FSystem%5FInt32%5F)CopyTo(DeformedBarAttachment\[\], int)

##### Declaration

```
public void CopyTo(DeformedBarAttachment[] array, int arrayIndex)
```

##### Parameters

| Type                                                                          | Name       | Description |
| ----------------------------------------------------------------------------- | ---------- | ----------- |
| [DeformedBarAttachment](DesignData.SDS2.Setup.DeformedBarAttachment.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachment%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, DeformedBarAttachment\[\], int, int)

##### Declaration

```
public void CopyTo(int index, DeformedBarAttachment[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                          | Name       | Description |
| ----------------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | index      |             |
| [DeformedBarAttachment](DesignData.SDS2.Setup.DeformedBarAttachment.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FFinalize)\~DeformedBarAttachmentList()

##### Declaration

```
protected ~DeformedBarAttachmentList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public DeformedBarAttachmentList.DeformedBarAttachmentListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                                              | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [DeformedBarAttachmentList](DesignData.SDS2.Setup.DeformedBarAttachmentList.html).[DeformedBarAttachmentListEnumerator](DesignData.SDS2.Setup.DeformedBarAttachmentList.DeformedBarAttachmentListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public DeformedBarAttachmentList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [DeformedBarAttachmentList](DesignData.SDS2.Setup.DeformedBarAttachmentList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachment%5F)Insert(int, DeformedBarAttachment)

##### Declaration

```
public void Insert(int index, DeformedBarAttachment x)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | index |             |
| [DeformedBarAttachment](DesignData.SDS2.Setup.DeformedBarAttachment.html) | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5F)InsertRange(int, DeformedBarAttachmentList)

##### Declaration

```
public void InsertRange(int index, DeformedBarAttachmentList values)
```

##### Parameters

| Type                                                                              | Name   | Description |
| --------------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                        | index  |             |
| [DeformedBarAttachmentList](DesignData.SDS2.Setup.DeformedBarAttachmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachment%5FSystem%5FInt32%5F)Repeat(DeformedBarAttachment, int)

##### Declaration

```
public static DeformedBarAttachmentList Repeat(DeformedBarAttachment value, int count)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [DeformedBarAttachment](DesignData.SDS2.Setup.DeformedBarAttachment.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | count |             |

##### Returns

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [DeformedBarAttachmentList](DesignData.SDS2.Setup.DeformedBarAttachmentList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5F)SetRange(int, DeformedBarAttachmentList)

##### Declaration

```
public void SetRange(int index, DeformedBarAttachmentList values)
```

##### Parameters

| Type                                                                              | Name   | Description |
| --------------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                        | index  |             |
| [DeformedBarAttachmentList](DesignData.SDS2.Setup.DeformedBarAttachmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDeformedBarAttachmentList%5FToArray)ToArray()

##### Declaration

```
public DeformedBarAttachment[] ToArray()
```

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [DeformedBarAttachment](DesignData.SDS2.Setup.DeformedBarAttachment.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)