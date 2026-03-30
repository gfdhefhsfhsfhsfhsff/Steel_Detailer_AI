# Class BentPlateEndList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BentPlateEndList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html)\>

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
public class BentPlateEndList : IEnumerable<BentPlateEnd>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5F%5Fctor)BentPlateEndList()

##### Declaration

```
public BentPlateEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FBentPlateEndList%5F)BentPlateEndList(BentPlateEndList)

##### Declaration

```
public BentPlateEndList(BentPlateEndList other)
```

##### Parameters

| Type                                                            | Name  | Description |
| --------------------------------------------------------------- | ----- | ----------- |
| [BentPlateEndList](DesignData.SDS2.Model.BentPlateEndList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FBentPlateEnd%5F%5F)BentPlateEndList(IEnumerable<BentPlateEnd>)

##### Declaration

```
public BentPlateEndList(IEnumerable<BentPlateEnd> c)
```

##### Parameters

| Type                                                                                                                                                     | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)BentPlateEndList(IEnumerable)

##### Declaration

```
public BentPlateEndList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5F%5Fctor%5FSystem%5FInt32%5F)BentPlateEndList(int)

##### Declaration

```
public BentPlateEndList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public BentPlateEnd this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FAdd%5FDesignData%5FSDS2%5FModel%5FBentPlateEnd%5F)Add(BentPlateEnd)

##### Declaration

```
public void Add(BentPlateEnd x)
```

##### Parameters

| Type                                                    | Name | Description |
| ------------------------------------------------------- | ---- | ----------- |
| [BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FBentPlateEndList%5F)AddRange(BentPlateEndList)

##### Declaration

```
public void AddRange(BentPlateEndList values)
```

##### Parameters

| Type                                                            | Name   | Description |
| --------------------------------------------------------------- | ------ | ----------- |
| [BentPlateEndList](DesignData.SDS2.Model.BentPlateEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FBentPlateEnd%5F%5F%5F)CopyTo(BentPlateEnd\[\])

##### Declaration

```
public void CopyTo(BentPlateEnd[] array)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FBentPlateEnd%5F%5F%5FSystem%5FInt32%5F)CopyTo(BentPlateEnd\[\], int)

##### Declaration

```
public void CopyTo(BentPlateEnd[] array, int arrayIndex)
```

##### Parameters

| Type                                                        | Name       | Description |
| ----------------------------------------------------------- | ---------- | ----------- |
| [BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBentPlateEnd%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, BentPlateEnd\[\], int, int)

##### Declaration

```
public void CopyTo(int index, BentPlateEnd[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                        | Name       | Description |
| ----------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index      |             |
| [BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FFinalize)\~BentPlateEndList()

##### Declaration

```
protected ~BentPlateEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public BentPlateEndList.BentPlateEndListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                 | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [BentPlateEndList](DesignData.SDS2.Model.BentPlateEndList.html).[BentPlateEndListEnumerator](DesignData.SDS2.Model.BentPlateEndList.BentPlateEndListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public BentPlateEndList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [BentPlateEndList](DesignData.SDS2.Model.BentPlateEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBentPlateEnd%5F)Insert(int, BentPlateEnd)

##### Declaration

```
public void Insert(int index, BentPlateEnd x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html)    | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBentPlateEndList%5F)InsertRange(int, BentPlateEndList)

##### Declaration

```
public void InsertRange(int index, BentPlateEndList values)
```

##### Parameters

| Type                                                            | Name   | Description |
| --------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | index  |             |
| [BentPlateEndList](DesignData.SDS2.Model.BentPlateEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FBentPlateEnd%5FSystem%5FInt32%5F)Repeat(BentPlateEnd, int)

##### Declaration

```
public static BentPlateEndList Repeat(BentPlateEnd value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html)    | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [BentPlateEndList](DesignData.SDS2.Model.BentPlateEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBentPlateEndList%5F)SetRange(int, BentPlateEndList)

##### Declaration

```
public void SetRange(int index, BentPlateEndList values)
```

##### Parameters

| Type                                                            | Name   | Description |
| --------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | index  |             |
| [BentPlateEndList](DesignData.SDS2.Model.BentPlateEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateEndList%5FToArray)ToArray()

##### Declaration

```
public BentPlateEnd[] ToArray()
```

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)