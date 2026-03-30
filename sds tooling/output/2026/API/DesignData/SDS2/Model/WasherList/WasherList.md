# Class WasherList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

WasherList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Washer](DesignData.SDS2.Model.Washer.html)\>

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
public class WasherList : IEnumerable<Washer>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5F%5Fctor)WasherList()

##### Declaration

```
public WasherList()
```

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FWasherList%5F)WasherList(WasherList)

##### Declaration

```
public WasherList(WasherList other)
```

##### Parameters

| Type                                                | Name  | Description |
| --------------------------------------------------- | ----- | ----------- |
| [WasherList](DesignData.SDS2.Model.WasherList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FWasher%5F%5F)WasherList(IEnumerable<Washer>)

##### Declaration

```
public WasherList(IEnumerable<Washer> c)
```

##### Parameters

| Type                                                                                                                                         | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Washer](DesignData.SDS2.Model.Washer.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)WasherList(IEnumerable)

##### Declaration

```
public WasherList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5F%5Fctor%5FSystem%5FInt32%5F)WasherList(int)

##### Declaration

```
public WasherList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Washer this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FAdd%5FDesignData%5FSDS2%5FModel%5FWasher%5F)Add(Washer)

##### Declaration

```
public void Add(Washer x)
```

##### Parameters

| Type                                        | Name | Description |
| ------------------------------------------- | ---- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FWasherList%5F)AddRange(WasherList)

##### Declaration

```
public void AddRange(WasherList values)
```

##### Parameters

| Type                                                | Name   | Description |
| --------------------------------------------------- | ------ | ----------- |
| [WasherList](DesignData.SDS2.Model.WasherList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FWasher%5F%5F%5F)CopyTo(Washer\[\])

##### Declaration

```
public void CopyTo(Washer[] array)
```

##### Parameters

| Type                                            | Name  | Description |
| ----------------------------------------------- | ----- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FWasher%5F%5F%5FSystem%5FInt32%5F)CopyTo(Washer\[\], int)

##### Declaration

```
public void CopyTo(Washer[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html)\[\]            | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWasher%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Washer\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Washer[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Washer](DesignData.SDS2.Model.Washer.html)\[\]            | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FFinalize)\~WasherList()

##### Declaration

```
protected ~WasherList()
```

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public WasherList.WasherListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                   | Description |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [WasherList](DesignData.SDS2.Model.WasherList.html).[WasherListEnumerator](DesignData.SDS2.Model.WasherList.WasherListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public WasherList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [WasherList](DesignData.SDS2.Model.WasherList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWasher%5F)Insert(int, Washer)

##### Declaration

```
public void Insert(int index, Washer x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Washer](DesignData.SDS2.Model.Washer.html)                | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWasherList%5F)InsertRange(int, WasherList)

##### Declaration

```
public void InsertRange(int index, WasherList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [WasherList](DesignData.SDS2.Model.WasherList.html)        | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FWasher%5FSystem%5FInt32%5F)Repeat(Washer, int)

##### Declaration

```
public static WasherList Repeat(Washer value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html)                | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [WasherList](DesignData.SDS2.Model.WasherList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWasherList%5F)SetRange(int, WasherList)

##### Declaration

```
public void SetRange(int index, WasherList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [WasherList](DesignData.SDS2.Model.WasherList.html)        | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasherList%5FToArray)ToArray()

##### Declaration

```
public Washer[] ToArray()
```

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)