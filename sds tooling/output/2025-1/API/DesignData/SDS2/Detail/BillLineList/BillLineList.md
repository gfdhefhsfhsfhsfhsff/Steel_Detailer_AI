# Class BillLineList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BillLineList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BillOfMaterialLine](DesignData.SDS2.Detail.BillOfMaterialLine.html)\>

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
public class BillLineList : IEnumerable<BillOfMaterialLine>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5F%5Fctor)BillLineList()

##### Declaration

```
public BillLineList()
```

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5F%5Fctor%5FDesignData%5FSDS2%5FDetail%5FBillLineList%5F)BillLineList(BillLineList)

##### Declaration

```
public BillLineList(BillLineList other)
```

##### Parameters

| Type                                                     | Name  | Description |
| -------------------------------------------------------- | ----- | ----------- |
| [BillLineList](DesignData.SDS2.Detail.BillLineList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5F%5F)BillLineList(IEnumerable<BillOfMaterialLine>)

##### Declaration

```
public BillLineList(IEnumerable<BillOfMaterialLine> c)
```

##### Parameters

| Type                                                                                                                                                                  | Name | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BillOfMaterialLine](DesignData.SDS2.Detail.BillOfMaterialLine.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)BillLineList(IEnumerable)

##### Declaration

```
public BillLineList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5F%5Fctor%5FSystem%5FInt32%5F)BillLineList(int)

##### Declaration

```
public BillLineList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public BillOfMaterialLine this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [BillOfMaterialLine](DesignData.SDS2.Detail.BillOfMaterialLine.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FAdd%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5F)Add(BillOfMaterialLine)

##### Declaration

```
public void Add(BillOfMaterialLine x)
```

##### Parameters

| Type                                                                 | Name | Description |
| -------------------------------------------------------------------- | ---- | ----------- |
| [BillOfMaterialLine](DesignData.SDS2.Detail.BillOfMaterialLine.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FAddRange%5FDesignData%5FSDS2%5FDetail%5FBillLineList%5F)AddRange(BillLineList)

##### Declaration

```
public void AddRange(BillLineList values)
```

##### Parameters

| Type                                                     | Name   | Description |
| -------------------------------------------------------- | ------ | ----------- |
| [BillLineList](DesignData.SDS2.Detail.BillLineList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FCopyTo%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5F%5F%5F)CopyTo(BillOfMaterialLine\[\])

##### Declaration

```
public void CopyTo(BillOfMaterialLine[] array)
```

##### Parameters

| Type                                                                     | Name  | Description |
| ------------------------------------------------------------------------ | ----- | ----------- |
| [BillOfMaterialLine](DesignData.SDS2.Detail.BillOfMaterialLine.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FCopyTo%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5F%5F%5FSystem%5FInt32%5F)CopyTo(BillOfMaterialLine\[\], int)

##### Declaration

```
public void CopyTo(BillOfMaterialLine[] array, int arrayIndex)
```

##### Parameters

| Type                                                                     | Name       | Description |
| ------------------------------------------------------------------------ | ---------- | ----------- |
| [BillOfMaterialLine](DesignData.SDS2.Detail.BillOfMaterialLine.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)               | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, BillOfMaterialLine\[\], int, int)

##### Declaration

```
public void CopyTo(int index, BillOfMaterialLine[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                     | Name       | Description |
| ------------------------------------------------------------------------ | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)               | index      |             |
| [BillOfMaterialLine](DesignData.SDS2.Detail.BillOfMaterialLine.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)               | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)               | count      |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FFinalize)\~BillLineList()

##### Declaration

```
protected ~BillLineList()
```

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public BillLineList.BillLineListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                               | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [BillLineList](DesignData.SDS2.Detail.BillLineList.html).[BillLineListEnumerator](DesignData.SDS2.Detail.BillLineList.BillLineListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public BillLineList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [BillLineList](DesignData.SDS2.Detail.BillLineList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5F)Insert(int, BillOfMaterialLine)

##### Declaration

```
public void Insert(int index, BillOfMaterialLine x)
```

##### Parameters

| Type                                                                 | Name  | Description |
| -------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)           | index |             |
| [BillOfMaterialLine](DesignData.SDS2.Detail.BillOfMaterialLine.html) | x     |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FBillLineList%5F)InsertRange(int, BillLineList)

##### Declaration

```
public void InsertRange(int index, BillLineList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [BillLineList](DesignData.SDS2.Detail.BillLineList.html)   | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FRepeat%5FDesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FSystem%5FInt32%5F)Repeat(BillOfMaterialLine, int)

##### Declaration

```
public static BillLineList Repeat(BillOfMaterialLine value, int count)
```

##### Parameters

| Type                                                                 | Name  | Description |
| -------------------------------------------------------------------- | ----- | ----------- |
| [BillOfMaterialLine](DesignData.SDS2.Detail.BillOfMaterialLine.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)           | count |             |

##### Returns

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [BillLineList](DesignData.SDS2.Detail.BillLineList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FBillLineList%5F)SetRange(int, BillLineList)

##### Declaration

```
public void SetRange(int index, BillLineList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [BillLineList](DesignData.SDS2.Detail.BillLineList.html)   | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillLineList%5FToArray)ToArray()

##### Declaration

```
public BillOfMaterialLine[] ToArray()
```

##### Returns

| Type                                                                     | Description |
| ------------------------------------------------------------------------ | ----------- |
| [BillOfMaterialLine](DesignData.SDS2.Detail.BillOfMaterialLine.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)