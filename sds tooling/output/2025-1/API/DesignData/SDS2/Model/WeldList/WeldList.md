# Class WeldList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

WeldList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Weld](DesignData.SDS2.Model.Weld.html)\>

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
public class WeldList : IEnumerable<Weld>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5F%5Fctor)WeldList()

##### Declaration

```
public WeldList()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FWeldList%5F)WeldList(WeldList)

##### Declaration

```
public WeldList(WeldList other)
```

##### Parameters

| Type                                            | Name  | Description |
| ----------------------------------------------- | ----- | ----------- |
| [WeldList](DesignData.SDS2.Model.WeldList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FWeld%5F%5F)WeldList(IEnumerable<Weld>)

##### Declaration

```
public WeldList(IEnumerable<Weld> c)
```

##### Parameters

| Type                                                                                                                                     | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Weld](DesignData.SDS2.Model.Weld.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)WeldList(IEnumerable)

##### Declaration

```
public WeldList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5F%5Fctor%5FSystem%5FInt32%5F)WeldList(int)

##### Declaration

```
public WeldList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Weld this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                    | Description |
| --------------------------------------- | ----------- |
| [Weld](DesignData.SDS2.Model.Weld.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FAdd%5FDesignData%5FSDS2%5FModel%5FWeld%5F)Add(Weld)

##### Declaration

```
public void Add(Weld x)
```

##### Parameters

| Type                                    | Name | Description |
| --------------------------------------- | ---- | ----------- |
| [Weld](DesignData.SDS2.Model.Weld.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FWeldList%5F)AddRange(WeldList)

##### Declaration

```
public void AddRange(WeldList values)
```

##### Parameters

| Type                                            | Name   | Description |
| ----------------------------------------------- | ------ | ----------- |
| [WeldList](DesignData.SDS2.Model.WeldList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FWeld%5F%5F%5F)CopyTo(Weld\[\])

##### Declaration

```
public void CopyTo(Weld[] array)
```

##### Parameters

| Type                                        | Name  | Description |
| ------------------------------------------- | ----- | ----------- |
| [Weld](DesignData.SDS2.Model.Weld.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FWeld%5F%5F%5FSystem%5FInt32%5F)CopyTo(Weld\[\], int)

##### Declaration

```
public void CopyTo(Weld[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Weld](DesignData.SDS2.Model.Weld.html)\[\]                | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeld%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Weld\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Weld[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Weld](DesignData.SDS2.Model.Weld.html)\[\]                | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FFinalize)\~WeldList()

##### Declaration

```
protected ~WeldList()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public WeldList.WeldListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                         | Description |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [WeldList](DesignData.SDS2.Model.WeldList.html).[WeldListEnumerator](DesignData.SDS2.Model.WeldList.WeldListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public WeldList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldList](DesignData.SDS2.Model.WeldList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeld%5F)Insert(int, Weld)

##### Declaration

```
public void Insert(int index, Weld x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Weld](DesignData.SDS2.Model.Weld.html)                    | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeldList%5F)InsertRange(int, WeldList)

##### Declaration

```
public void InsertRange(int index, WeldList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [WeldList](DesignData.SDS2.Model.WeldList.html)            | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FWeld%5FSystem%5FInt32%5F)Repeat(Weld, int)

##### Declaration

```
public static WeldList Repeat(Weld value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Weld](DesignData.SDS2.Model.Weld.html)                    | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldList](DesignData.SDS2.Model.WeldList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeldList%5F)SetRange(int, WeldList)

##### Declaration

```
public void SetRange(int index, WeldList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [WeldList](DesignData.SDS2.Model.WeldList.html)            | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FToArray)ToArray()

##### Declaration

```
public Weld[] ToArray()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Weld](DesignData.SDS2.Model.Weld.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)