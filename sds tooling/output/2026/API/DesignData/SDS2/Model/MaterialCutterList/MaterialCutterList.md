# Class MaterialCutterList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialCutterList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MaterialCutter](DesignData.SDS2.Model.MaterialCutter.html)\>

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
public class MaterialCutterList : IEnumerable<MaterialCutter>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5F%5Fctor)MaterialCutterList()

##### Declaration

```
public MaterialCutterList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FMaterialCutterList%5F)MaterialCutterList(MaterialCutterList)

##### Declaration

```
public MaterialCutterList(MaterialCutterList other)
```

##### Parameters

| Type                                                                | Name  | Description |
| ------------------------------------------------------------------- | ----- | ----------- |
| [MaterialCutterList](DesignData.SDS2.Model.MaterialCutterList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FMaterialCutter%5F%5F)MaterialCutterList(IEnumerable<MaterialCutter>)

##### Declaration

```
public MaterialCutterList(IEnumerable<MaterialCutter> c)
```

##### Parameters

| Type                                                                                                                                                         | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MaterialCutter](DesignData.SDS2.Model.MaterialCutter.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)MaterialCutterList(IEnumerable)

##### Declaration

```
public MaterialCutterList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5F%5Fctor%5FSystem%5FInt32%5F)MaterialCutterList(int)

##### Declaration

```
public MaterialCutterList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public MaterialCutter this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [MaterialCutter](DesignData.SDS2.Model.MaterialCutter.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FAdd%5FDesignData%5FSDS2%5FModel%5FMaterialCutter%5F)Add(MaterialCutter)

##### Declaration

```
public void Add(MaterialCutter x)
```

##### Parameters

| Type                                                        | Name | Description |
| ----------------------------------------------------------- | ---- | ----------- |
| [MaterialCutter](DesignData.SDS2.Model.MaterialCutter.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FMaterialCutterList%5F)AddRange(MaterialCutterList)

##### Declaration

```
public void AddRange(MaterialCutterList values)
```

##### Parameters

| Type                                                                | Name   | Description |
| ------------------------------------------------------------------- | ------ | ----------- |
| [MaterialCutterList](DesignData.SDS2.Model.MaterialCutterList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMaterialCutter%5F%5F%5F)CopyTo(MaterialCutter\[\])

##### Declaration

```
public void CopyTo(MaterialCutter[] array)
```

##### Parameters

| Type                                                            | Name  | Description |
| --------------------------------------------------------------- | ----- | ----------- |
| [MaterialCutter](DesignData.SDS2.Model.MaterialCutter.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FMaterialCutter%5F%5F%5FSystem%5FInt32%5F)CopyTo(MaterialCutter\[\], int)

##### Declaration

```
public void CopyTo(MaterialCutter[] array, int arrayIndex)
```

##### Parameters

| Type                                                            | Name       | Description |
| --------------------------------------------------------------- | ---------- | ----------- |
| [MaterialCutter](DesignData.SDS2.Model.MaterialCutter.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialCutter%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, MaterialCutter\[\], int, int)

##### Declaration

```
public void CopyTo(int index, MaterialCutter[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                            | Name       | Description |
| --------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | index      |             |
| [MaterialCutter](DesignData.SDS2.Model.MaterialCutter.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FFinalize)\~MaterialCutterList()

##### Declaration

```
protected ~MaterialCutterList()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public MaterialCutterList.MaterialCutterListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                           | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [MaterialCutterList](DesignData.SDS2.Model.MaterialCutterList.html).[MaterialCutterListEnumerator](DesignData.SDS2.Model.MaterialCutterList.MaterialCutterListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public MaterialCutterList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [MaterialCutterList](DesignData.SDS2.Model.MaterialCutterList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialCutter%5F)Insert(int, MaterialCutter)

##### Declaration

```
public void Insert(int index, MaterialCutter x)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index |             |
| [MaterialCutter](DesignData.SDS2.Model.MaterialCutter.html) | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialCutterList%5F)InsertRange(int, MaterialCutterList)

##### Declaration

```
public void InsertRange(int index, MaterialCutterList values)
```

##### Parameters

| Type                                                                | Name   | Description |
| ------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | index  |             |
| [MaterialCutterList](DesignData.SDS2.Model.MaterialCutterList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FMaterialCutter%5FSystem%5FInt32%5F)Repeat(MaterialCutter, int)

##### Declaration

```
public static MaterialCutterList Repeat(MaterialCutter value, int count)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [MaterialCutter](DesignData.SDS2.Model.MaterialCutter.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | count |             |

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [MaterialCutterList](DesignData.SDS2.Model.MaterialCutterList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FMaterialCutterList%5F)SetRange(int, MaterialCutterList)

##### Declaration

```
public void SetRange(int index, MaterialCutterList values)
```

##### Parameters

| Type                                                                | Name   | Description |
| ------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | index  |             |
| [MaterialCutterList](DesignData.SDS2.Model.MaterialCutterList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutterList%5FToArray)ToArray()

##### Declaration

```
public MaterialCutter[] ToArray()
```

##### Returns

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [MaterialCutter](DesignData.SDS2.Model.MaterialCutter.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)