# Class NutList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

NutList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Nut](DesignData.SDS2.Model.Nut.html)\>

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
public class NutList : IEnumerable<Nut>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5F%5Fctor)NutList()

##### Declaration

```
public NutList()
```

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FNutList%5F)NutList(NutList)

##### Declaration

```
public NutList(NutList other)
```

##### Parameters

| Type                                          | Name  | Description |
| --------------------------------------------- | ----- | ----------- |
| [NutList](DesignData.SDS2.Model.NutList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FNut%5F%5F)NutList(IEnumerable<Nut>)

##### Declaration

```
public NutList(IEnumerable<Nut> c)
```

##### Parameters

| Type                                                                                                                                   | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Nut](DesignData.SDS2.Model.Nut.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)NutList(IEnumerable)

##### Declaration

```
public NutList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5F%5Fctor%5FSystem%5FInt32%5F)NutList(int)

##### Declaration

```
public NutList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Nut this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                  | Description |
| ------------------------------------- | ----------- |
| [Nut](DesignData.SDS2.Model.Nut.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FAdd%5FDesignData%5FSDS2%5FModel%5FNut%5F)Add(Nut)

##### Declaration

```
public void Add(Nut x)
```

##### Parameters

| Type                                  | Name | Description |
| ------------------------------------- | ---- | ----------- |
| [Nut](DesignData.SDS2.Model.Nut.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FNutList%5F)AddRange(NutList)

##### Declaration

```
public void AddRange(NutList values)
```

##### Parameters

| Type                                          | Name   | Description |
| --------------------------------------------- | ------ | ----------- |
| [NutList](DesignData.SDS2.Model.NutList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FNut%5F%5F%5F)CopyTo(Nut\[\])

##### Declaration

```
public void CopyTo(Nut[] array)
```

##### Parameters

| Type                                      | Name  | Description |
| ----------------------------------------- | ----- | ----------- |
| [Nut](DesignData.SDS2.Model.Nut.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FNut%5F%5F%5FSystem%5FInt32%5F)CopyTo(Nut\[\], int)

##### Declaration

```
public void CopyTo(Nut[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Nut](DesignData.SDS2.Model.Nut.html)\[\]                  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FNut%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Nut\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Nut[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Nut](DesignData.SDS2.Model.Nut.html)\[\]                  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FFinalize)\~NutList()

##### Declaration

```
protected ~NutList()
```

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public NutList.NutListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                    | Description |
| ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| [NutList](DesignData.SDS2.Model.NutList.html).[NutListEnumerator](DesignData.SDS2.Model.NutList.NutListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public NutList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [NutList](DesignData.SDS2.Model.NutList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FNut%5F)Insert(int, Nut)

##### Declaration

```
public void Insert(int index, Nut x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Nut](DesignData.SDS2.Model.Nut.html)                      | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FNutList%5F)InsertRange(int, NutList)

##### Declaration

```
public void InsertRange(int index, NutList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [NutList](DesignData.SDS2.Model.NutList.html)              | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FNut%5FSystem%5FInt32%5F)Repeat(Nut, int)

##### Declaration

```
public static NutList Repeat(Nut value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Nut](DesignData.SDS2.Model.Nut.html)                      | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [NutList](DesignData.SDS2.Model.NutList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FNutList%5F)SetRange(int, NutList)

##### Declaration

```
public void SetRange(int index, NutList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [NutList](DesignData.SDS2.Model.NutList.html)              | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FNutList%5FToArray)ToArray()

##### Declaration

```
public Nut[] ToArray()
```

##### Returns

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Nut](DesignData.SDS2.Model.Nut.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)