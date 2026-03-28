# Class BoltList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BoltList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Bolt](DesignData.SDS2.Model.Bolt.html)\>

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
public class BoltList : IEnumerable<Bolt>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5F%5Fctor)BoltList()

##### Declaration

```
public BoltList()
```

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FBoltList%5F)BoltList(BoltList)

##### Declaration

```
public BoltList(BoltList other)
```

##### Parameters

| Type                                            | Name  | Description |
| ----------------------------------------------- | ----- | ----------- |
| [BoltList](DesignData.SDS2.Model.BoltList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FBolt%5F%5F)BoltList(IEnumerable<Bolt>)

##### Declaration

```
public BoltList(IEnumerable<Bolt> c)
```

##### Parameters

| Type                                                                                                                                     | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Bolt](DesignData.SDS2.Model.Bolt.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)BoltList(IEnumerable)

##### Declaration

```
public BoltList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5F%5Fctor%5FSystem%5FInt32%5F)BoltList(int)

##### Declaration

```
public BoltList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Bolt this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                    | Description |
| --------------------------------------- | ----------- |
| [Bolt](DesignData.SDS2.Model.Bolt.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FAdd%5FDesignData%5FSDS2%5FModel%5FBolt%5F)Add(Bolt)

##### Declaration

```
public void Add(Bolt x)
```

##### Parameters

| Type                                    | Name | Description |
| --------------------------------------- | ---- | ----------- |
| [Bolt](DesignData.SDS2.Model.Bolt.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FBoltList%5F)AddRange(BoltList)

##### Declaration

```
public void AddRange(BoltList values)
```

##### Parameters

| Type                                            | Name   | Description |
| ----------------------------------------------- | ------ | ----------- |
| [BoltList](DesignData.SDS2.Model.BoltList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FBolt%5F%5F%5F)CopyTo(Bolt\[\])

##### Declaration

```
public void CopyTo(Bolt[] array)
```

##### Parameters

| Type                                        | Name  | Description |
| ------------------------------------------- | ----- | ----------- |
| [Bolt](DesignData.SDS2.Model.Bolt.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FBolt%5F%5F%5FSystem%5FInt32%5F)CopyTo(Bolt\[\], int)

##### Declaration

```
public void CopyTo(Bolt[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Bolt](DesignData.SDS2.Model.Bolt.html)\[\]                | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBolt%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Bolt\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Bolt[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Bolt](DesignData.SDS2.Model.Bolt.html)\[\]                | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FFinalize)\~BoltList()

##### Declaration

```
protected ~BoltList()
```

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public BoltList.BoltListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                         | Description |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [BoltList](DesignData.SDS2.Model.BoltList.html).[BoltListEnumerator](DesignData.SDS2.Model.BoltList.BoltListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public BoltList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltList](DesignData.SDS2.Model.BoltList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBolt%5F)Insert(int, Bolt)

##### Declaration

```
public void Insert(int index, Bolt x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Bolt](DesignData.SDS2.Model.Bolt.html)                    | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBoltList%5F)InsertRange(int, BoltList)

##### Declaration

```
public void InsertRange(int index, BoltList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [BoltList](DesignData.SDS2.Model.BoltList.html)            | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FBolt%5FSystem%5FInt32%5F)Repeat(Bolt, int)

##### Declaration

```
public static BoltList Repeat(Bolt value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Bolt](DesignData.SDS2.Model.Bolt.html)                    | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltList](DesignData.SDS2.Model.BoltList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBoltList%5F)SetRange(int, BoltList)

##### Declaration

```
public void SetRange(int index, BoltList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [BoltList](DesignData.SDS2.Model.BoltList.html)            | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltList%5FToArray)ToArray()

##### Declaration

```
public Bolt[] ToArray()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Bolt](DesignData.SDS2.Model.Bolt.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)