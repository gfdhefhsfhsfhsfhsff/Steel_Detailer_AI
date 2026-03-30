# Class BoltTypeList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BoltTypeList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BoltType](DesignData.SDS2.Setup.BoltType.html)\>

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
public class BoltTypeList : IEnumerable<BoltType>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5F%5Fctor)BoltTypeList()

##### Declaration

```
public BoltTypeList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FBoltTypeList%5F)BoltTypeList(BoltTypeList)

##### Declaration

```
public BoltTypeList(BoltTypeList other)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [BoltTypeList](DesignData.SDS2.Setup.BoltTypeList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FBoltType%5F%5F)BoltTypeList(IEnumerable<BoltType>)

##### Declaration

```
public BoltTypeList(IEnumerable<BoltType> c)
```

##### Parameters

| Type                                                                                                                                             | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BoltType](DesignData.SDS2.Setup.BoltType.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)BoltTypeList(IEnumerable)

##### Declaration

```
public BoltTypeList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5F%5Fctor%5FSystem%5FInt32%5F)BoltTypeList(int)

##### Declaration

```
public BoltTypeList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public BoltType this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FBoltType%5F)Add(BoltType)

##### Declaration

```
public void Add(BoltType x)
```

##### Parameters

| Type                                            | Name | Description |
| ----------------------------------------------- | ---- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FBoltTypeList%5F)AddRange(BoltTypeList)

##### Declaration

```
public void AddRange(BoltTypeList values)
```

##### Parameters

| Type                                                    | Name   | Description |
| ------------------------------------------------------- | ------ | ----------- |
| [BoltTypeList](DesignData.SDS2.Setup.BoltTypeList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FBoltType%5F%5F%5F)CopyTo(BoltType\[\])

##### Declaration

```
public void CopyTo(BoltType[] array)
```

##### Parameters

| Type                                                | Name  | Description |
| --------------------------------------------------- | ----- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FBoltType%5F%5F%5FSystem%5FInt32%5F)CopyTo(BoltType\[\], int)

##### Declaration

```
public void CopyTo(BoltType[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html)\[\]        | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBoltType%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, BoltType\[\], int, int)

##### Declaration

```
public void CopyTo(int index, BoltType[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [BoltType](DesignData.SDS2.Setup.BoltType.html)\[\]        | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FFinalize)\~BoltTypeList()

##### Declaration

```
protected ~BoltTypeList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public BoltTypeList.BoltTypeListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                             | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [BoltTypeList](DesignData.SDS2.Setup.BoltTypeList.html).[BoltTypeListEnumerator](DesignData.SDS2.Setup.BoltTypeList.BoltTypeListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public BoltTypeList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [BoltTypeList](DesignData.SDS2.Setup.BoltTypeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBoltType%5F)Insert(int, BoltType)

##### Declaration

```
public void Insert(int index, BoltType x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [BoltType](DesignData.SDS2.Setup.BoltType.html)            | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBoltTypeList%5F)InsertRange(int, BoltTypeList)

##### Declaration

```
public void InsertRange(int index, BoltTypeList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [BoltTypeList](DesignData.SDS2.Setup.BoltTypeList.html)    | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FBoltType%5FSystem%5FInt32%5F)Repeat(BoltType, int)

##### Declaration

```
public static BoltTypeList Repeat(BoltType value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html)            | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [BoltTypeList](DesignData.SDS2.Setup.BoltTypeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBoltTypeList%5F)SetRange(int, BoltTypeList)

##### Declaration

```
public void SetRange(int index, BoltTypeList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [BoltTypeList](DesignData.SDS2.Setup.BoltTypeList.html)    | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeList%5FToArray)ToArray()

##### Declaration

```
public BoltType[] ToArray()
```

##### Returns

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)