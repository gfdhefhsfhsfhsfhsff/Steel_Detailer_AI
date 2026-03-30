# Class MaterialList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Material](DesignData.SDS2.Model.Material.html)\>

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
public class MaterialList : IEnumerable<Material>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5F%5Fctor)MaterialList()

##### Declaration

```
public MaterialList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FMaterialList%5F)MaterialList(MaterialList)

##### Declaration

```
public MaterialList(MaterialList other)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FMaterial%5F%5F)MaterialList(IEnumerable<Material>)

##### Declaration

```
public MaterialList(IEnumerable<Material> c)
```

##### Parameters

| Type                                                                                                                                             | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Material](DesignData.SDS2.Model.Material.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)MaterialList(IEnumerable)

##### Declaration

```
public MaterialList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5F%5Fctor%5FSystem%5FInt32%5F)MaterialList(int)

##### Declaration

```
public MaterialList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Material this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FAdd%5FDesignData%5FSDS2%5FModel%5FMaterial%5F)Add(Material)

##### Declaration

```
public void Add(Material x)
```

##### Parameters

| Type                                            | Name | Description |
| ----------------------------------------------- | ---- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FMaterialList%5F)AddRange(MaterialList)

##### Declaration

```
public void AddRange(MaterialList values)
```

##### Parameters

| Type                                                    | Name   | Description |
| ------------------------------------------------------- | ------ | ----------- |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMaterial%5F%5F%5F)CopyTo(Material\[\])

##### Declaration

```
public void CopyTo(Material[] array)
```

##### Parameters

| Type                                                | Name  | Description |
| --------------------------------------------------- | ----- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMaterial%5F%5F%5FSystem%5FInt32%5F)CopyTo(Material\[\], int)

##### Declaration

```
public void CopyTo(Material[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html)\[\]        | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterial%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Material\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Material[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Material](DesignData.SDS2.Model.Material.html)\[\]        | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FFinalize)\~MaterialList()

##### Declaration

```
protected ~MaterialList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public MaterialList.MaterialListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                             | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html).[MaterialListEnumerator](DesignData.SDS2.Model.MaterialList.MaterialListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public MaterialList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterial%5F)Insert(int, Material)

##### Declaration

```
public void Insert(int index, Material x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Material](DesignData.SDS2.Model.Material.html)            | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialList%5F)InsertRange(int, MaterialList)

##### Declaration

```
public void InsertRange(int index, MaterialList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html)    | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FMaterial%5FSystem%5FInt32%5F)Repeat(Material, int)

##### Declaration

```
public static MaterialList Repeat(Material value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html)            | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialList%5F)SetRange(int, MaterialList)

##### Declaration

```
public void SetRange(int index, MaterialList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html)    | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialList%5FToArray)ToArray()

##### Declaration

```
public Material[] ToArray()
```

##### Returns

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)