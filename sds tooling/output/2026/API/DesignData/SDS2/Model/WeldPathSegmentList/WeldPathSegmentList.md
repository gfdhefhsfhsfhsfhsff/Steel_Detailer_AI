# Class WeldPathSegmentList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

WeldPathSegmentList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html)\>

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
public class WeldPathSegmentList : IEnumerable<WeldPathSegment>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5F%5Fctor)WeldPathSegmentList()

##### Declaration

```
public WeldPathSegmentList()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5F)WeldPathSegmentList(WeldPathSegmentList)

##### Declaration

```
public WeldPathSegmentList(WeldPathSegmentList other)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FWeldPathSegment%5F%5F)WeldPathSegmentList(IEnumerable<WeldPathSegment>)

##### Declaration

```
public WeldPathSegmentList(IEnumerable<WeldPathSegment> c)
```

##### Parameters

| Type                                                                                                                                                           | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)WeldPathSegmentList(IEnumerable)

##### Declaration

```
public WeldPathSegmentList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5F%5Fctor%5FSystem%5FInt32%5F)WeldPathSegmentList(int)

##### Declaration

```
public WeldPathSegmentList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public WeldPathSegment this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FAdd%5FDesignData%5FSDS2%5FModel%5FWeldPathSegment%5F)Add(WeldPathSegment)

##### Declaration

```
public void Add(WeldPathSegment x)
```

##### Parameters

| Type                                                          | Name | Description |
| ------------------------------------------------------------- | ---- | ----------- |
| [WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5F)AddRange(WeldPathSegmentList)

##### Declaration

```
public void AddRange(WeldPathSegmentList values)
```

##### Parameters

| Type                                                                  | Name   | Description |
| --------------------------------------------------------------------- | ------ | ----------- |
| [WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FWeldPathSegment%5F%5F%5F)CopyTo(WeldPathSegment\[\])

##### Declaration

```
public void CopyTo(WeldPathSegment[] array)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FWeldPathSegment%5F%5F%5FSystem%5FInt32%5F)CopyTo(WeldPathSegment\[\], int)

##### Declaration

```
public void CopyTo(WeldPathSegment[] array, int arrayIndex)
```

##### Parameters

| Type                                                              | Name       | Description |
| ----------------------------------------------------------------- | ---------- | ----------- |
| [WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeldPathSegment%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, WeldPathSegment\[\], int, int)

##### Declaration

```
public void CopyTo(int index, WeldPathSegment[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                              | Name       | Description |
| ----------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | index      |             |
| [WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FFinalize)\~WeldPathSegmentList()

##### Declaration

```
protected ~WeldPathSegmentList()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public WeldPathSegmentList.WeldPathSegmentListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html).[WeldPathSegmentListEnumerator](DesignData.SDS2.Model.WeldPathSegmentList.WeldPathSegmentListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public WeldPathSegmentList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeldPathSegment%5F)Insert(int, WeldPathSegment)

##### Declaration

```
public void Insert(int index, WeldPathSegment x)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index |             |
| [WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html) | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5F)InsertRange(int, WeldPathSegmentList)

##### Declaration

```
public void InsertRange(int index, WeldPathSegmentList values)
```

##### Parameters

| Type                                                                  | Name   | Description |
| --------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | index  |             |
| [WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FWeldPathSegment%5FSystem%5FInt32%5F)Repeat(WeldPathSegment, int)

##### Declaration

```
public static WeldPathSegmentList Repeat(WeldPathSegment value, int count)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | count |             |

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5F)SetRange(int, WeldPathSegmentList)

##### Declaration

```
public void SetRange(int index, WeldPathSegmentList values)
```

##### Parameters

| Type                                                                  | Name   | Description |
| --------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | index  |             |
| [WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegmentList%5FToArray)ToArray()

##### Declaration

```
public WeldPathSegment[] ToArray()
```

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)