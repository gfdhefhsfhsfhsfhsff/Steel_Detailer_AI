# Class MaterialUsageList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialUsageList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html)\>

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
public class MaterialUsageList : IEnumerable<MaterialUsage>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5F%5Fctor)MaterialUsageList()

##### Declaration

```
public MaterialUsageList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FMaterialUsageList%5F)MaterialUsageList(MaterialUsageList)

##### Declaration

```
public MaterialUsageList(MaterialUsageList other)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [MaterialUsageList](DesignData.SDS2.Setup.MaterialUsageList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FMaterialUsage%5F%5F)MaterialUsageList(IEnumerable<MaterialUsage>)

##### Declaration

```
public MaterialUsageList(IEnumerable<MaterialUsage> c)
```

##### Parameters

| Type                                                                                                                                                       | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)MaterialUsageList(IEnumerable)

##### Declaration

```
public MaterialUsageList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5F%5Fctor%5FSystem%5FInt32%5F)MaterialUsageList(int)

##### Declaration

```
public MaterialUsageList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public MaterialUsage this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FMaterialUsage%5F)Add(MaterialUsage)

##### Declaration

```
public void Add(MaterialUsage x)
```

##### Parameters

| Type                                                      | Name | Description |
| --------------------------------------------------------- | ---- | ----------- |
| [MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FMaterialUsageList%5F)AddRange(MaterialUsageList)

##### Declaration

```
public void AddRange(MaterialUsageList values)
```

##### Parameters

| Type                                                              | Name   | Description |
| ----------------------------------------------------------------- | ------ | ----------- |
| [MaterialUsageList](DesignData.SDS2.Setup.MaterialUsageList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FMaterialUsage%5F%5F%5F)CopyTo(MaterialUsage\[\])

##### Declaration

```
public void CopyTo(MaterialUsage[] array)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FMaterialUsage%5F%5F%5FSystem%5FInt32%5F)CopyTo(MaterialUsage\[\], int)

##### Declaration

```
public void CopyTo(MaterialUsage[] array, int arrayIndex)
```

##### Parameters

| Type                                                          | Name       | Description |
| ------------------------------------------------------------- | ---------- | ----------- |
| [MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FMaterialUsage%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, MaterialUsage\[\], int, int)

##### Declaration

```
public void CopyTo(int index, MaterialUsage[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                          | Name       | Description |
| ------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index      |             |
| [MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FFinalize)\~MaterialUsageList()

##### Declaration

```
protected ~MaterialUsageList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public MaterialUsageList.MaterialUsageListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                      | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [MaterialUsageList](DesignData.SDS2.Setup.MaterialUsageList.html).[MaterialUsageListEnumerator](DesignData.SDS2.Setup.MaterialUsageList.MaterialUsageListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public MaterialUsageList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [MaterialUsageList](DesignData.SDS2.Setup.MaterialUsageList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FMaterialUsage%5F)Insert(int, MaterialUsage)

##### Declaration

```
public void Insert(int index, MaterialUsage x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html)  | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FMaterialUsageList%5F)InsertRange(int, MaterialUsageList)

##### Declaration

```
public void InsertRange(int index, MaterialUsageList values)
```

##### Parameters

| Type                                                              | Name   | Description |
| ----------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | index  |             |
| [MaterialUsageList](DesignData.SDS2.Setup.MaterialUsageList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FMaterialUsage%5FSystem%5FInt32%5F)Repeat(MaterialUsage, int)

##### Declaration

```
public static MaterialUsageList Repeat(MaterialUsage value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html)  | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [MaterialUsageList](DesignData.SDS2.Setup.MaterialUsageList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FMaterialUsageList%5F)SetRange(int, MaterialUsageList)

##### Declaration

```
public void SetRange(int index, MaterialUsageList values)
```

##### Parameters

| Type                                                              | Name   | Description |
| ----------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | index  |             |
| [MaterialUsageList](DesignData.SDS2.Setup.MaterialUsageList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FToArray)ToArray()

##### Declaration

```
public MaterialUsage[] ToArray()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)