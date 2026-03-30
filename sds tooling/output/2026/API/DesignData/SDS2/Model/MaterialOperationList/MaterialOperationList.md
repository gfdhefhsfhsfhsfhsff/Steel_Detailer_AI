# Class MaterialOperationList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialOperationList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class MaterialOperationList : IEnumerable<MaterialOperation>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5F%5Fctor)MaterialOperationList()

##### Declaration

```
public MaterialOperationList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FMaterialOperationList%5F)MaterialOperationList(MaterialOperationList)

##### Declaration

```
public MaterialOperationList(MaterialOperationList other)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [MaterialOperationList](DesignData.SDS2.Model.MaterialOperationList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FMaterialOperation%5F%5F)MaterialOperationList(IEnumerable<MaterialOperation>)

##### Declaration

```
public MaterialOperationList(IEnumerable<MaterialOperation> c)
```

##### Parameters

| Type                                                                                                                                                               | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)MaterialOperationList(IEnumerable)

##### Declaration

```
public MaterialOperationList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5F%5Fctor%5FSystem%5FInt32%5F)MaterialOperationList(int)

##### Declaration

```
public MaterialOperationList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public MaterialOperation this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FAdd%5FDesignData%5FSDS2%5FModel%5FMaterialOperation%5F)Add(MaterialOperation)

##### Declaration

```
public void Add(MaterialOperation x)
```

##### Parameters

| Type                                                              | Name | Description |
| ----------------------------------------------------------------- | ---- | ----------- |
| [MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FMaterialOperationList%5F)AddRange(MaterialOperationList)

##### Declaration

```
public void AddRange(MaterialOperationList values)
```

##### Parameters

| Type                                                                      | Name   | Description |
| ------------------------------------------------------------------------- | ------ | ----------- |
| [MaterialOperationList](DesignData.SDS2.Model.MaterialOperationList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMaterialOperation%5F%5F%5F)CopyTo(MaterialOperation\[\])

##### Declaration

```
public void CopyTo(MaterialOperation[] array)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMaterialOperation%5F%5F%5FSystem%5FInt32%5F)CopyTo(MaterialOperation\[\], int)

##### Declaration

```
public void CopyTo(MaterialOperation[] array, int arrayIndex)
```

##### Parameters

| Type                                                                  | Name       | Description |
| --------------------------------------------------------------------- | ---------- | ----------- |
| [MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialOperation%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, MaterialOperation\[\], int, int)

##### Declaration

```
public void CopyTo(int index, MaterialOperation[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                  | Name       | Description |
| --------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | index      |             |
| [MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FFinalize)\~MaterialOperationList()

##### Declaration

```
protected ~MaterialOperationList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public MaterialOperationList.MaterialOperationListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                          | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [MaterialOperationList](DesignData.SDS2.Model.MaterialOperationList.html).[MaterialOperationListEnumerator](DesignData.SDS2.Model.MaterialOperationList.MaterialOperationListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public MaterialOperationList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [MaterialOperationList](DesignData.SDS2.Model.MaterialOperationList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialOperation%5F)Insert(int, MaterialOperation)

##### Declaration

```
public void Insert(int index, MaterialOperation x)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | index |             |
| [MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html) | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialOperationList%5F)InsertRange(int, MaterialOperationList)

##### Declaration

```
public void InsertRange(int index, MaterialOperationList values)
```

##### Parameters

| Type                                                                      | Name   | Description |
| ------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | index  |             |
| [MaterialOperationList](DesignData.SDS2.Model.MaterialOperationList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FMaterialOperation%5FSystem%5FInt32%5F)Repeat(MaterialOperation, int)

##### Declaration

```
public static MaterialOperationList Repeat(MaterialOperation value, int count)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | count |             |

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [MaterialOperationList](DesignData.SDS2.Model.MaterialOperationList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialOperationList%5F)SetRange(int, MaterialOperationList)

##### Declaration

```
public void SetRange(int index, MaterialOperationList values)
```

##### Parameters

| Type                                                                      | Name   | Description |
| ------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | index  |             |
| [MaterialOperationList](DesignData.SDS2.Model.MaterialOperationList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FToArray)ToArray()

##### Declaration

```
public MaterialOperation[] ToArray()
```

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)