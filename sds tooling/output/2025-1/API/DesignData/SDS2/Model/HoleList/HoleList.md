# Class HoleList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

HoleList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Hole](DesignData.SDS2.Model.Hole.html)\>

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
public class HoleList : IEnumerable<Hole>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5F%5Fctor)HoleList()

##### Declaration

```
public HoleList()
```

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FHoleList%5F)HoleList(HoleList)

##### Declaration

```
public HoleList(HoleList other)
```

##### Parameters

| Type                                            | Name  | Description |
| ----------------------------------------------- | ----- | ----------- |
| [HoleList](DesignData.SDS2.Model.HoleList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FHole%5F%5F)HoleList(IEnumerable<Hole>)

##### Declaration

```
public HoleList(IEnumerable<Hole> c)
```

##### Parameters

| Type                                                                                                                                     | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Hole](DesignData.SDS2.Model.Hole.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)HoleList(IEnumerable)

##### Declaration

```
public HoleList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5F%5Fctor%5FSystem%5FInt32%5F)HoleList(int)

##### Declaration

```
public HoleList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Hole this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                    | Description |
| --------------------------------------- | ----------- |
| [Hole](DesignData.SDS2.Model.Hole.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FAdd%5FDesignData%5FSDS2%5FModel%5FHole%5F)Add(Hole)

##### Declaration

```
public void Add(Hole x)
```

##### Parameters

| Type                                    | Name | Description |
| --------------------------------------- | ---- | ----------- |
| [Hole](DesignData.SDS2.Model.Hole.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FHoleList%5F)AddRange(HoleList)

##### Declaration

```
public void AddRange(HoleList values)
```

##### Parameters

| Type                                            | Name   | Description |
| ----------------------------------------------- | ------ | ----------- |
| [HoleList](DesignData.SDS2.Model.HoleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FHole%5F%5F%5F)CopyTo(Hole\[\])

##### Declaration

```
public void CopyTo(Hole[] array)
```

##### Parameters

| Type                                        | Name  | Description |
| ------------------------------------------- | ----- | ----------- |
| [Hole](DesignData.SDS2.Model.Hole.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FHole%5F%5F%5FSystem%5FInt32%5F)CopyTo(Hole\[\], int)

##### Declaration

```
public void CopyTo(Hole[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Hole](DesignData.SDS2.Model.Hole.html)\[\]                | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FHole%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Hole\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Hole[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Hole](DesignData.SDS2.Model.Hole.html)\[\]                | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FFinalize)\~HoleList()

##### Declaration

```
protected ~HoleList()
```

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public HoleList.HoleListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                         | Description |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [HoleList](DesignData.SDS2.Model.HoleList.html).[HoleListEnumerator](DesignData.SDS2.Model.HoleList.HoleListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public HoleList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [HoleList](DesignData.SDS2.Model.HoleList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FHole%5F)Insert(int, Hole)

##### Declaration

```
public void Insert(int index, Hole x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Hole](DesignData.SDS2.Model.Hole.html)                    | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FHoleList%5F)InsertRange(int, HoleList)

##### Declaration

```
public void InsertRange(int index, HoleList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [HoleList](DesignData.SDS2.Model.HoleList.html)            | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FHole%5FSystem%5FInt32%5F)Repeat(Hole, int)

##### Declaration

```
public static HoleList Repeat(Hole value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Hole](DesignData.SDS2.Model.Hole.html)                    | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [HoleList](DesignData.SDS2.Model.HoleList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FHoleList%5F)SetRange(int, HoleList)

##### Declaration

```
public void SetRange(int index, HoleList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [HoleList](DesignData.SDS2.Model.HoleList.html)            | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleList%5FToArray)ToArray()

##### Declaration

```
public Hole[] ToArray()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Hole](DesignData.SDS2.Model.Hole.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)