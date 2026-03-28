# Class BillSequenceList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BillSequenceList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BillOfMaterialSequence](DesignData.SDS2.Detail.BillOfMaterialSequence.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Detail](DesignData.SDS2.Detail.html)

###### **Assembly**: DesignData.SDS2.Detail.dll

##### Syntax

```
public class BillSequenceList : IEnumerable<BillOfMaterialSequence>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5F%5Fctor)BillSequenceList()

##### Declaration

```
public BillSequenceList()
```

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5F%5Fctor%5FDesignData%5FSDS2%5FDetail%5FBillSequenceList%5F)BillSequenceList(BillSequenceList)

##### Declaration

```
public BillSequenceList(BillSequenceList other)
```

##### Parameters

| Type                                                             | Name  | Description |
| ---------------------------------------------------------------- | ----- | ----------- |
| [BillSequenceList](DesignData.SDS2.Detail.BillSequenceList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialSequence%5F%5F)BillSequenceList(IEnumerable<BillOfMaterialSequence>)

##### Declaration

```
public BillSequenceList(IEnumerable<BillOfMaterialSequence> c)
```

##### Parameters

| Type                                                                                                                                                                          | Name | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BillOfMaterialSequence](DesignData.SDS2.Detail.BillOfMaterialSequence.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)BillSequenceList(IEnumerable)

##### Declaration

```
public BillSequenceList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5F%5Fctor%5FSystem%5FInt32%5F)BillSequenceList(int)

##### Declaration

```
public BillSequenceList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public BillOfMaterialSequence this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                         | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [BillOfMaterialSequence](DesignData.SDS2.Detail.BillOfMaterialSequence.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FAdd%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialSequence%5F)Add(BillOfMaterialSequence)

##### Declaration

```
public void Add(BillOfMaterialSequence x)
```

##### Parameters

| Type                                                                         | Name | Description |
| ---------------------------------------------------------------------------- | ---- | ----------- |
| [BillOfMaterialSequence](DesignData.SDS2.Detail.BillOfMaterialSequence.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FAddRange%5FDesignData%5FSDS2%5FDetail%5FBillSequenceList%5F)AddRange(BillSequenceList)

##### Declaration

```
public void AddRange(BillSequenceList values)
```

##### Parameters

| Type                                                             | Name   | Description |
| ---------------------------------------------------------------- | ------ | ----------- |
| [BillSequenceList](DesignData.SDS2.Detail.BillSequenceList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FCopyTo%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialSequence%5F%5F%5F)CopyTo(BillOfMaterialSequence\[\])

##### Declaration

```
public void CopyTo(BillOfMaterialSequence[] array)
```

##### Parameters

| Type                                                                             | Name  | Description |
| -------------------------------------------------------------------------------- | ----- | ----------- |
| [BillOfMaterialSequence](DesignData.SDS2.Detail.BillOfMaterialSequence.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FCopyTo%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialSequence%5F%5F%5FSystem%5FInt32%5F)CopyTo(BillOfMaterialSequence\[\], int)

##### Declaration

```
public void CopyTo(BillOfMaterialSequence[] array, int arrayIndex)
```

##### Parameters

| Type                                                                             | Name       | Description |
| -------------------------------------------------------------------------------- | ---------- | ----------- |
| [BillOfMaterialSequence](DesignData.SDS2.Detail.BillOfMaterialSequence.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                       | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialSequence%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, BillOfMaterialSequence\[\], int, int)

##### Declaration

```
public void CopyTo(int index, BillOfMaterialSequence[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                             | Name       | Description |
| -------------------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                       | index      |             |
| [BillOfMaterialSequence](DesignData.SDS2.Detail.BillOfMaterialSequence.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                       | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                       | count      |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FFinalize)\~BillSequenceList()

##### Declaration

```
protected ~BillSequenceList()
```

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public BillSequenceList.BillSequenceListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                   | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [BillSequenceList](DesignData.SDS2.Detail.BillSequenceList.html).[BillSequenceListEnumerator](DesignData.SDS2.Detail.BillSequenceList.BillSequenceListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public BillSequenceList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                             | Description |
| ---------------------------------------------------------------- | ----------- |
| [BillSequenceList](DesignData.SDS2.Detail.BillSequenceList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialSequence%5F)Insert(int, BillOfMaterialSequence)

##### Declaration

```
public void Insert(int index, BillOfMaterialSequence x)
```

##### Parameters

| Type                                                                         | Name  | Description |
| ---------------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                   | index |             |
| [BillOfMaterialSequence](DesignData.SDS2.Detail.BillOfMaterialSequence.html) | x     |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FBillSequenceList%5F)InsertRange(int, BillSequenceList)

##### Declaration

```
public void InsertRange(int index, BillSequenceList values)
```

##### Parameters

| Type                                                             | Name   | Description |
| ---------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)       | index  |             |
| [BillSequenceList](DesignData.SDS2.Detail.BillSequenceList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FRepeat%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialSequence%5FSystem%5FInt32%5F)Repeat(BillOfMaterialSequence, int)

##### Declaration

```
public static BillSequenceList Repeat(BillOfMaterialSequence value, int count)
```

##### Parameters

| Type                                                                         | Name  | Description |
| ---------------------------------------------------------------------------- | ----- | ----------- |
| [BillOfMaterialSequence](DesignData.SDS2.Detail.BillOfMaterialSequence.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                   | count |             |

##### Returns

| Type                                                             | Description |
| ---------------------------------------------------------------- | ----------- |
| [BillSequenceList](DesignData.SDS2.Detail.BillSequenceList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FBillSequenceList%5F)SetRange(int, BillSequenceList)

##### Declaration

```
public void SetRange(int index, BillSequenceList values)
```

##### Parameters

| Type                                                             | Name   | Description |
| ---------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)       | index  |             |
| [BillSequenceList](DesignData.SDS2.Detail.BillSequenceList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillSequenceList%5FToArray)ToArray()

##### Declaration

```
public BillOfMaterialSequence[] ToArray()
```

##### Returns

| Type                                                                             | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [BillOfMaterialSequence](DesignData.SDS2.Detail.BillOfMaterialSequence.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)