# Class HorizontalBraceEndList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

HorizontalBraceEndList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html)\>

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
public class HorizontalBraceEndList : IEnumerable<HorizontalBraceEnd>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5F%5Fctor)HorizontalBraceEndList()

##### Declaration

```
public HorizontalBraceEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5F)HorizontalBraceEndList(HorizontalBraceEndList)

##### Declaration

```
public HorizontalBraceEndList(HorizontalBraceEndList other)
```

##### Parameters

| Type                                                                        | Name  | Description |
| --------------------------------------------------------------------------- | ----- | ----------- |
| [HorizontalBraceEndList](DesignData.SDS2.Model.HorizontalBraceEndList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEnd%5F%5F)HorizontalBraceEndList(IEnumerable<HorizontalBraceEnd>)

##### Declaration

```
public HorizontalBraceEndList(IEnumerable<HorizontalBraceEnd> c)
```

##### Parameters

| Type                                                                                                                                                                 | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)HorizontalBraceEndList(IEnumerable)

##### Declaration

```
public HorizontalBraceEndList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5F%5Fctor%5FSystem%5FInt32%5F)HorizontalBraceEndList(int)

##### Declaration

```
public HorizontalBraceEndList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FItem%5FDesignData%5FSDS2%5FDatabase%5FMemberEnd%5F)this\[MemberEnd\]

##### Declaration

```
public HorizontalBraceEnd this[MemberEnd end] { get; set; }
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [MemberEnd](DesignData.SDS2.Database.MemberEnd.html) | end  |             |

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public HorizontalBraceEnd this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FAdd%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEnd%5F)Add(HorizontalBraceEnd)

##### Declaration

```
public void Add(HorizontalBraceEnd x)
```

##### Parameters

| Type                                                                | Name | Description |
| ------------------------------------------------------------------- | ---- | ----------- |
| [HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5F)AddRange(HorizontalBraceEndList)

##### Declaration

```
public void AddRange(HorizontalBraceEndList values)
```

##### Parameters

| Type                                                                        | Name   | Description |
| --------------------------------------------------------------------------- | ------ | ----------- |
| [HorizontalBraceEndList](DesignData.SDS2.Model.HorizontalBraceEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEnd%5F%5F%5F)CopyTo(HorizontalBraceEnd\[\])

##### Declaration

```
public void CopyTo(HorizontalBraceEnd[] array)
```

##### Parameters

| Type                                                                    | Name  | Description |
| ----------------------------------------------------------------------- | ----- | ----------- |
| [HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEnd%5F%5F%5FSystem%5FInt32%5F)CopyTo(HorizontalBraceEnd\[\], int)

##### Declaration

```
public void CopyTo(HorizontalBraceEnd[] array, int arrayIndex)
```

##### Parameters

| Type                                                                    | Name       | Description |
| ----------------------------------------------------------------------- | ---------- | ----------- |
| [HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)              | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEnd%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, HorizontalBraceEnd\[\], int, int)

##### Declaration

```
public void CopyTo(int index, HorizontalBraceEnd[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                    | Name       | Description |
| ----------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)              | index      |             |
| [HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)              | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)              | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FFinalize)\~HorizontalBraceEndList()

##### Declaration

```
protected ~HorizontalBraceEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public HorizontalBraceEndList.HorizontalBraceEndListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                               | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [HorizontalBraceEndList](DesignData.SDS2.Model.HorizontalBraceEndList.html).[HorizontalBraceEndListEnumerator](DesignData.SDS2.Model.HorizontalBraceEndList.HorizontalBraceEndListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public HorizontalBraceEndList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [HorizontalBraceEndList](DesignData.SDS2.Model.HorizontalBraceEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEnd%5F)Insert(int, HorizontalBraceEnd)

##### Declaration

```
public void Insert(int index, HorizontalBraceEnd x)
```

##### Parameters

| Type                                                                | Name  | Description |
| ------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | index |             |
| [HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html) | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5F)InsertRange(int, HorizontalBraceEndList)

##### Declaration

```
public void InsertRange(int index, HorizontalBraceEndList values)
```

##### Parameters

| Type                                                                        | Name   | Description |
| --------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                  | index  |             |
| [HorizontalBraceEndList](DesignData.SDS2.Model.HorizontalBraceEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEnd%5FSystem%5FInt32%5F)Repeat(HorizontalBraceEnd, int)

##### Declaration

```
public static HorizontalBraceEndList Repeat(HorizontalBraceEnd value, int count)
```

##### Parameters

| Type                                                                | Name  | Description |
| ------------------------------------------------------------------- | ----- | ----------- |
| [HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | count |             |

##### Returns

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [HorizontalBraceEndList](DesignData.SDS2.Model.HorizontalBraceEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5F)SetRange(int, HorizontalBraceEndList)

##### Declaration

```
public void SetRange(int index, HorizontalBraceEndList values)
```

##### Parameters

| Type                                                                        | Name   | Description |
| --------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                  | index  |             |
| [HorizontalBraceEndList](DesignData.SDS2.Model.HorizontalBraceEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FHorizontalBraceEndList%5FToArray)ToArray()

##### Declaration

```
public HorizontalBraceEnd[] ToArray()
```

##### Returns

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)