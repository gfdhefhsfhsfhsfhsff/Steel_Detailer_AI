# Class MaterialUseList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialUseList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MaterialUse](DesignData.SDS2.Model.MaterialUse.html)\>

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
public class MaterialUseList : IEnumerable<MaterialUse>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5F%5Fctor)MaterialUseList()

##### Declaration

```
public MaterialUseList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FMaterialUseList%5F)MaterialUseList(MaterialUseList)

##### Declaration

```
public MaterialUseList(MaterialUseList other)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [MaterialUseList](DesignData.SDS2.Model.MaterialUseList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FMaterialUse%5F%5F)MaterialUseList(IEnumerable<MaterialUse>)

##### Declaration

```
public MaterialUseList(IEnumerable<MaterialUse> c)
```

##### Parameters

| Type                                                                                                                                                   | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MaterialUse](DesignData.SDS2.Model.MaterialUse.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)MaterialUseList(IEnumerable)

##### Declaration

```
public MaterialUseList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5F%5Fctor%5FSystem%5FInt32%5F)MaterialUseList(int)

##### Declaration

```
public MaterialUseList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public MaterialUse this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [MaterialUse](DesignData.SDS2.Model.MaterialUse.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FAdd%5FDesignData%5FSDS2%5FModel%5FMaterialUse%5F)Add(MaterialUse)

##### Declaration

```
public void Add(MaterialUse x)
```

##### Parameters

| Type                                                  | Name | Description |
| ----------------------------------------------------- | ---- | ----------- |
| [MaterialUse](DesignData.SDS2.Model.MaterialUse.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FMaterialUseList%5F)AddRange(MaterialUseList)

##### Declaration

```
public void AddRange(MaterialUseList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [MaterialUseList](DesignData.SDS2.Model.MaterialUseList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMaterialUse%5F%5F%5F)CopyTo(MaterialUse\[\])

##### Declaration

```
public void CopyTo(MaterialUse[] array)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [MaterialUse](DesignData.SDS2.Model.MaterialUse.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMaterialUse%5F%5F%5FSystem%5FInt32%5F)CopyTo(MaterialUse\[\], int)

##### Declaration

```
public void CopyTo(MaterialUse[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [MaterialUse](DesignData.SDS2.Model.MaterialUse.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialUse%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, MaterialUse\[\], int, int)

##### Declaration

```
public void CopyTo(int index, MaterialUse[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [MaterialUse](DesignData.SDS2.Model.MaterialUse.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FFinalize)\~MaterialUseList()

##### Declaration

```
protected ~MaterialUseList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public MaterialUseList.MaterialUseListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                            | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [MaterialUseList](DesignData.SDS2.Model.MaterialUseList.html).[MaterialUseListEnumerator](DesignData.SDS2.Model.MaterialUseList.MaterialUseListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public MaterialUseList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [MaterialUseList](DesignData.SDS2.Model.MaterialUseList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialUse%5F)Insert(int, MaterialUse)

##### Declaration

```
public void Insert(int index, MaterialUse x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [MaterialUse](DesignData.SDS2.Model.MaterialUse.html)      | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialUseList%5F)InsertRange(int, MaterialUseList)

##### Declaration

```
public void InsertRange(int index, MaterialUseList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [MaterialUseList](DesignData.SDS2.Model.MaterialUseList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FMaterialUse%5FSystem%5FInt32%5F)Repeat(MaterialUse, int)

##### Declaration

```
public static MaterialUseList Repeat(MaterialUse value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [MaterialUse](DesignData.SDS2.Model.MaterialUse.html)      | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [MaterialUseList](DesignData.SDS2.Model.MaterialUseList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialUseList%5F)SetRange(int, MaterialUseList)

##### Declaration

```
public void SetRange(int index, MaterialUseList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [MaterialUseList](DesignData.SDS2.Model.MaterialUseList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialUseList%5FToArray)ToArray()

##### Declaration

```
public MaterialUse[] ToArray()
```

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [MaterialUse](DesignData.SDS2.Model.MaterialUse.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)