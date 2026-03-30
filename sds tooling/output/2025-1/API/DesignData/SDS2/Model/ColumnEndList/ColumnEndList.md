# Class ColumnEndList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ColumnEndList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html)\>

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
public class ColumnEndList : IEnumerable<ColumnEnd>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5F%5Fctor)ColumnEndList()

##### Declaration

```
public ColumnEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FColumnEndList%5F)ColumnEndList(ColumnEndList)

##### Declaration

```
public ColumnEndList(ColumnEndList other)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [ColumnEndList](DesignData.SDS2.Model.ColumnEndList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FColumnEnd%5F%5F)ColumnEndList(IEnumerable<ColumnEnd>)

##### Declaration

```
public ColumnEndList(IEnumerable<ColumnEnd> c)
```

##### Parameters

| Type                                                                                                                                               | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)ColumnEndList(IEnumerable)

##### Declaration

```
public ColumnEndList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5F%5Fctor%5FSystem%5FInt32%5F)ColumnEndList(int)

##### Declaration

```
public ColumnEndList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FItem%5FDesignData%5FSDS2%5FDatabase%5FColumnEnd%5F)this\[ColumnEnd\]

##### Declaration

```
public ColumnEnd this[ColumnEnd end] { get; set; }
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [ColumnEnd](DesignData.SDS2.Database.ColumnEnd.html) | end  |             |

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public ColumnEnd this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FAdd%5FDesignData%5FSDS2%5FModel%5FColumnEnd%5F)Add(ColumnEnd)

##### Declaration

```
public void Add(ColumnEnd x)
```

##### Parameters

| Type                                              | Name | Description |
| ------------------------------------------------- | ---- | ----------- |
| [ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FColumnEndList%5F)AddRange(ColumnEndList)

##### Declaration

```
public void AddRange(ColumnEndList values)
```

##### Parameters

| Type                                                      | Name   | Description |
| --------------------------------------------------------- | ------ | ----------- |
| [ColumnEndList](DesignData.SDS2.Model.ColumnEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FColumnEnd%5F%5F%5F)CopyTo(ColumnEnd\[\])

##### Declaration

```
public void CopyTo(ColumnEnd[] array)
```

##### Parameters

| Type                                                  | Name  | Description |
| ----------------------------------------------------- | ----- | ----------- |
| [ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FColumnEnd%5F%5F%5FSystem%5FInt32%5F)CopyTo(ColumnEnd\[\], int)

##### Declaration

```
public void CopyTo(ColumnEnd[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html)\[\]      | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FColumnEnd%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, ColumnEnd\[\], int, int)

##### Declaration

```
public void CopyTo(int index, ColumnEnd[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html)\[\]      | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FFinalize)\~ColumnEndList()

##### Declaration

```
protected ~ColumnEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public ColumnEndList.ColumnEndListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [ColumnEndList](DesignData.SDS2.Model.ColumnEndList.html).[ColumnEndListEnumerator](DesignData.SDS2.Model.ColumnEndList.ColumnEndListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public ColumnEndList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ColumnEndList](DesignData.SDS2.Model.ColumnEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FColumnEnd%5F)Insert(int, ColumnEnd)

##### Declaration

```
public void Insert(int index, ColumnEnd x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html)          | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FColumnEndList%5F)InsertRange(int, ColumnEndList)

##### Declaration

```
public void InsertRange(int index, ColumnEndList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [ColumnEndList](DesignData.SDS2.Model.ColumnEndList.html)  | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FColumnEnd%5FSystem%5FInt32%5F)Repeat(ColumnEnd, int)

##### Declaration

```
public static ColumnEndList Repeat(ColumnEnd value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html)          | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ColumnEndList](DesignData.SDS2.Model.ColumnEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FColumnEndList%5F)SetRange(int, ColumnEndList)

##### Declaration

```
public void SetRange(int index, ColumnEndList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [ColumnEndList](DesignData.SDS2.Model.ColumnEndList.html)  | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnEndList%5FToArray)ToArray()

##### Declaration

```
public ColumnEnd[] ToArray()
```

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)