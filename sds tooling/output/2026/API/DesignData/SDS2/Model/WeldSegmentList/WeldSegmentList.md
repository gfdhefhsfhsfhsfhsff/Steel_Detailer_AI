# Class WeldSegmentList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

WeldSegmentList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[WeldSegment](DesignData.SDS2.Model.WeldSegment.html)\>

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
public class WeldSegmentList : IEnumerable<WeldSegment>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5F%5Fctor)WeldSegmentList()

##### Declaration

```
public WeldSegmentList()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FWeldSegmentList%5F)WeldSegmentList(WeldSegmentList)

##### Declaration

```
public WeldSegmentList(WeldSegmentList other)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [WeldSegmentList](DesignData.SDS2.Model.WeldSegmentList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FWeldSegment%5F%5F)WeldSegmentList(IEnumerable<WeldSegment>)

##### Declaration

```
public WeldSegmentList(IEnumerable<WeldSegment> c)
```

##### Parameters

| Type                                                                                                                                                   | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[WeldSegment](DesignData.SDS2.Model.WeldSegment.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)WeldSegmentList(IEnumerable)

##### Declaration

```
public WeldSegmentList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5F%5Fctor%5FSystem%5FInt32%5F)WeldSegmentList(int)

##### Declaration

```
public WeldSegmentList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public WeldSegment this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [WeldSegment](DesignData.SDS2.Model.WeldSegment.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FAdd%5FDesignData%5FSDS2%5FModel%5FWeldSegment%5F)Add(WeldSegment)

##### Declaration

```
public void Add(WeldSegment x)
```

##### Parameters

| Type                                                  | Name | Description |
| ----------------------------------------------------- | ---- | ----------- |
| [WeldSegment](DesignData.SDS2.Model.WeldSegment.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FWeldSegmentList%5F)AddRange(WeldSegmentList)

##### Declaration

```
public void AddRange(WeldSegmentList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [WeldSegmentList](DesignData.SDS2.Model.WeldSegmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FWeldSegment%5F%5F%5F)CopyTo(WeldSegment\[\])

##### Declaration

```
public void CopyTo(WeldSegment[] array)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [WeldSegment](DesignData.SDS2.Model.WeldSegment.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FWeldSegment%5F%5F%5FSystem%5FInt32%5F)CopyTo(WeldSegment\[\], int)

##### Declaration

```
public void CopyTo(WeldSegment[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [WeldSegment](DesignData.SDS2.Model.WeldSegment.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeldSegment%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, WeldSegment\[\], int, int)

##### Declaration

```
public void CopyTo(int index, WeldSegment[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [WeldSegment](DesignData.SDS2.Model.WeldSegment.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FFinalize)\~WeldSegmentList()

##### Declaration

```
protected ~WeldSegmentList()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public WeldSegmentList.WeldSegmentListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                            | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [WeldSegmentList](DesignData.SDS2.Model.WeldSegmentList.html).[WeldSegmentListEnumerator](DesignData.SDS2.Model.WeldSegmentList.WeldSegmentListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public WeldSegmentList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [WeldSegmentList](DesignData.SDS2.Model.WeldSegmentList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeldSegment%5F)Insert(int, WeldSegment)

##### Declaration

```
public void Insert(int index, WeldSegment x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [WeldSegment](DesignData.SDS2.Model.WeldSegment.html)      | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeldSegmentList%5F)InsertRange(int, WeldSegmentList)

##### Declaration

```
public void InsertRange(int index, WeldSegmentList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [WeldSegmentList](DesignData.SDS2.Model.WeldSegmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FWeldSegment%5FSystem%5FInt32%5F)Repeat(WeldSegment, int)

##### Declaration

```
public static WeldSegmentList Repeat(WeldSegment value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [WeldSegment](DesignData.SDS2.Model.WeldSegment.html)      | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [WeldSegmentList](DesignData.SDS2.Model.WeldSegmentList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeldSegmentList%5F)SetRange(int, WeldSegmentList)

##### Declaration

```
public void SetRange(int index, WeldSegmentList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [WeldSegmentList](DesignData.SDS2.Model.WeldSegmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegmentList%5FToArray)ToArray()

##### Declaration

```
public WeldSegment[] ToArray()
```

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [WeldSegment](DesignData.SDS2.Model.WeldSegment.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)