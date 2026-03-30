# Class StairTreadList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

StairTreadList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[StairTread](DesignData.SDS2.Setup.StairTread.html)\>

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
public class StairTreadList : IEnumerable<StairTread>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5F%5Fctor)StairTreadList()

##### Declaration

```
public StairTreadList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FStairTreadList%5F)StairTreadList(StairTreadList)

##### Declaration

```
public StairTreadList(StairTreadList other)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [StairTreadList](DesignData.SDS2.Setup.StairTreadList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FStairTread%5F%5F)StairTreadList(IEnumerable<StairTread>)

##### Declaration

```
public StairTreadList(IEnumerable<StairTread> c)
```

##### Parameters

| Type                                                                                                                                                 | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[StairTread](DesignData.SDS2.Setup.StairTread.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)StairTreadList(IEnumerable)

##### Declaration

```
public StairTreadList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5F%5Fctor%5FSystem%5FInt32%5F)StairTreadList(int)

##### Declaration

```
public StairTreadList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public StairTread this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [StairTread](DesignData.SDS2.Setup.StairTread.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FStairTread%5F)Add(StairTread)

##### Declaration

```
public void Add(StairTread x)
```

##### Parameters

| Type                                                | Name | Description |
| --------------------------------------------------- | ---- | ----------- |
| [StairTread](DesignData.SDS2.Setup.StairTread.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FStairTreadList%5F)AddRange(StairTreadList)

##### Declaration

```
public void AddRange(StairTreadList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [StairTreadList](DesignData.SDS2.Setup.StairTreadList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FStairTread%5F%5F%5F)CopyTo(StairTread\[\])

##### Declaration

```
public void CopyTo(StairTread[] array)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [StairTread](DesignData.SDS2.Setup.StairTread.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FStairTread%5F%5F%5FSystem%5FInt32%5F)CopyTo(StairTread\[\], int)

##### Declaration

```
public void CopyTo(StairTread[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [StairTread](DesignData.SDS2.Setup.StairTread.html)\[\]    | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FStairTread%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, StairTread\[\], int, int)

##### Declaration

```
public void CopyTo(int index, StairTread[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [StairTread](DesignData.SDS2.Setup.StairTread.html)\[\]    | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FFinalize)\~StairTreadList()

##### Declaration

```
protected ~StairTreadList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public StairTreadList.StairTreadListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                       | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [StairTreadList](DesignData.SDS2.Setup.StairTreadList.html).[StairTreadListEnumerator](DesignData.SDS2.Setup.StairTreadList.StairTreadListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public StairTreadList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [StairTreadList](DesignData.SDS2.Setup.StairTreadList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FStairTread%5F)Insert(int, StairTread)

##### Declaration

```
public void Insert(int index, StairTread x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [StairTread](DesignData.SDS2.Setup.StairTread.html)        | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FStairTreadList%5F)InsertRange(int, StairTreadList)

##### Declaration

```
public void InsertRange(int index, StairTreadList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index  |             |
| [StairTreadList](DesignData.SDS2.Setup.StairTreadList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FStairTread%5FSystem%5FInt32%5F)Repeat(StairTread, int)

##### Declaration

```
public static StairTreadList Repeat(StairTread value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [StairTread](DesignData.SDS2.Setup.StairTread.html)        | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [StairTreadList](DesignData.SDS2.Setup.StairTreadList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FStairTreadList%5F)SetRange(int, StairTreadList)

##### Declaration

```
public void SetRange(int index, StairTreadList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index  |             |
| [StairTreadList](DesignData.SDS2.Setup.StairTreadList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTreadList%5FToArray)ToArray()

##### Declaration

```
public StairTread[] ToArray()
```

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [StairTread](DesignData.SDS2.Setup.StairTread.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)