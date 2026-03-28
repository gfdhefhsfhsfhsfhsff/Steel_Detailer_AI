# Class VerticalBraceEndList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

VerticalBraceEndList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html)\>

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
public class VerticalBraceEndList : IEnumerable<VerticalBraceEnd>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5F%5Fctor)VerticalBraceEndList()

##### Declaration

```
public VerticalBraceEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5F)VerticalBraceEndList(VerticalBraceEndList)

##### Declaration

```
public VerticalBraceEndList(VerticalBraceEndList other)
```

##### Parameters

| Type                                                                    | Name  | Description |
| ----------------------------------------------------------------------- | ----- | ----------- |
| [VerticalBraceEndList](DesignData.SDS2.Model.VerticalBraceEndList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEnd%5F%5F)VerticalBraceEndList(IEnumerable<VerticalBraceEnd>)

##### Declaration

```
public VerticalBraceEndList(IEnumerable<VerticalBraceEnd> c)
```

##### Parameters

| Type                                                                                                                                                             | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)VerticalBraceEndList(IEnumerable)

##### Declaration

```
public VerticalBraceEndList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5F%5Fctor%5FSystem%5FInt32%5F)VerticalBraceEndList(int)

##### Declaration

```
public VerticalBraceEndList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FItem%5FDesignData%5FSDS2%5FDatabase%5FMemberEnd%5F)this\[MemberEnd\]

##### Declaration

```
public VerticalBraceEnd this[MemberEnd end] { get; set; }
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [MemberEnd](DesignData.SDS2.Database.MemberEnd.html) | end  |             |

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public VerticalBraceEnd this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FAdd%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEnd%5F)Add(VerticalBraceEnd)

##### Declaration

```
public void Add(VerticalBraceEnd x)
```

##### Parameters

| Type                                                            | Name | Description |
| --------------------------------------------------------------- | ---- | ----------- |
| [VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5F)AddRange(VerticalBraceEndList)

##### Declaration

```
public void AddRange(VerticalBraceEndList values)
```

##### Parameters

| Type                                                                    | Name   | Description |
| ----------------------------------------------------------------------- | ------ | ----------- |
| [VerticalBraceEndList](DesignData.SDS2.Model.VerticalBraceEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEnd%5F%5F%5F)CopyTo(VerticalBraceEnd\[\])

##### Declaration

```
public void CopyTo(VerticalBraceEnd[] array)
```

##### Parameters

| Type                                                                | Name  | Description |
| ------------------------------------------------------------------- | ----- | ----------- |
| [VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEnd%5F%5F%5FSystem%5FInt32%5F)CopyTo(VerticalBraceEnd\[\], int)

##### Declaration

```
public void CopyTo(VerticalBraceEnd[] array, int arrayIndex)
```

##### Parameters

| Type                                                                | Name       | Description |
| ------------------------------------------------------------------- | ---------- | ----------- |
| [VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEnd%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, VerticalBraceEnd\[\], int, int)

##### Declaration

```
public void CopyTo(int index, VerticalBraceEnd[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                | Name       | Description |
| ------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | index      |             |
| [VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FFinalize)\~VerticalBraceEndList()

##### Declaration

```
protected ~VerticalBraceEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public VerticalBraceEndList.VerticalBraceEndListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                     | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [VerticalBraceEndList](DesignData.SDS2.Model.VerticalBraceEndList.html).[VerticalBraceEndListEnumerator](DesignData.SDS2.Model.VerticalBraceEndList.VerticalBraceEndListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public VerticalBraceEndList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [VerticalBraceEndList](DesignData.SDS2.Model.VerticalBraceEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEnd%5F)Insert(int, VerticalBraceEnd)

##### Declaration

```
public void Insert(int index, VerticalBraceEnd x)
```

##### Parameters

| Type                                                            | Name  | Description |
| --------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | index |             |
| [VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html) | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5F)InsertRange(int, VerticalBraceEndList)

##### Declaration

```
public void InsertRange(int index, VerticalBraceEndList values)
```

##### Parameters

| Type                                                                    | Name   | Description |
| ----------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)              | index  |             |
| [VerticalBraceEndList](DesignData.SDS2.Model.VerticalBraceEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEnd%5FSystem%5FInt32%5F)Repeat(VerticalBraceEnd, int)

##### Declaration

```
public static VerticalBraceEndList Repeat(VerticalBraceEnd value, int count)
```

##### Parameters

| Type                                                            | Name  | Description |
| --------------------------------------------------------------- | ----- | ----------- |
| [VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | count |             |

##### Returns

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [VerticalBraceEndList](DesignData.SDS2.Model.VerticalBraceEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5F)SetRange(int, VerticalBraceEndList)

##### Declaration

```
public void SetRange(int index, VerticalBraceEndList values)
```

##### Parameters

| Type                                                                    | Name   | Description |
| ----------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)              | index  |             |
| [VerticalBraceEndList](DesignData.SDS2.Model.VerticalBraceEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FVerticalBraceEndList%5FToArray)ToArray()

##### Declaration

```
public VerticalBraceEnd[] ToArray()
```

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)