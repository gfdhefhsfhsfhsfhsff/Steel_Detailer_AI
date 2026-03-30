# Class ChamferList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ChamferList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Chamfer](DesignData.SDS2.Model.Chamfer.html)\>

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
public class ChamferList : IEnumerable<Chamfer>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5F%5Fctor)ChamferList()

##### Declaration

```
public ChamferList()
```

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FChamferList%5F)ChamferList(ChamferList)

##### Declaration

```
public ChamferList(ChamferList other)
```

##### Parameters

| Type                                                  | Name  | Description |
| ----------------------------------------------------- | ----- | ----------- |
| [ChamferList](DesignData.SDS2.Model.ChamferList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FChamfer%5F%5F)ChamferList(IEnumerable<Chamfer>)

##### Declaration

```
public ChamferList(IEnumerable<Chamfer> c)
```

##### Parameters

| Type                                                                                                                                           | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Chamfer](DesignData.SDS2.Model.Chamfer.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)ChamferList(IEnumerable)

##### Declaration

```
public ChamferList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5F%5Fctor%5FSystem%5FInt32%5F)ChamferList(int)

##### Declaration

```
public ChamferList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Chamfer this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [Chamfer](DesignData.SDS2.Model.Chamfer.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FAdd%5FDesignData%5FSDS2%5FModel%5FChamfer%5F)Add(Chamfer)

##### Declaration

```
public void Add(Chamfer x)
```

##### Parameters

| Type                                          | Name | Description |
| --------------------------------------------- | ---- | ----------- |
| [Chamfer](DesignData.SDS2.Model.Chamfer.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FChamferList%5F)AddRange(ChamferList)

##### Declaration

```
public void AddRange(ChamferList values)
```

##### Parameters

| Type                                                  | Name   | Description |
| ----------------------------------------------------- | ------ | ----------- |
| [ChamferList](DesignData.SDS2.Model.ChamferList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FChamfer%5F%5F%5F)CopyTo(Chamfer\[\])

##### Declaration

```
public void CopyTo(Chamfer[] array)
```

##### Parameters

| Type                                              | Name  | Description |
| ------------------------------------------------- | ----- | ----------- |
| [Chamfer](DesignData.SDS2.Model.Chamfer.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FChamfer%5F%5F%5FSystem%5FInt32%5F)CopyTo(Chamfer\[\], int)

##### Declaration

```
public void CopyTo(Chamfer[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Chamfer](DesignData.SDS2.Model.Chamfer.html)\[\]          | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FChamfer%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Chamfer\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Chamfer[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Chamfer](DesignData.SDS2.Model.Chamfer.html)\[\]          | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FFinalize)\~ChamferList()

##### Declaration

```
protected ~ChamferList()
```

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public ChamferList.ChamferListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                        | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [ChamferList](DesignData.SDS2.Model.ChamferList.html).[ChamferListEnumerator](DesignData.SDS2.Model.ChamferList.ChamferListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public ChamferList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [ChamferList](DesignData.SDS2.Model.ChamferList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FChamfer%5F)Insert(int, Chamfer)

##### Declaration

```
public void Insert(int index, Chamfer x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Chamfer](DesignData.SDS2.Model.Chamfer.html)              | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FChamferList%5F)InsertRange(int, ChamferList)

##### Declaration

```
public void InsertRange(int index, ChamferList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [ChamferList](DesignData.SDS2.Model.ChamferList.html)      | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FChamfer%5FSystem%5FInt32%5F)Repeat(Chamfer, int)

##### Declaration

```
public static ChamferList Repeat(Chamfer value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Chamfer](DesignData.SDS2.Model.Chamfer.html)              | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [ChamferList](DesignData.SDS2.Model.ChamferList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FChamferList%5F)SetRange(int, ChamferList)

##### Declaration

```
public void SetRange(int index, ChamferList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [ChamferList](DesignData.SDS2.Model.ChamferList.html)      | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FChamferList%5FToArray)ToArray()

##### Declaration

```
public Chamfer[] ToArray()
```

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [Chamfer](DesignData.SDS2.Model.Chamfer.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)