# Class CuttableMaterialEndList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CuttableMaterialEndList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html)\>

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
public class CuttableMaterialEndList : IEnumerable<CuttableMaterialEnd>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5F%5Fctor)CuttableMaterialEndList()

##### Declaration

```
public CuttableMaterialEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5F)CuttableMaterialEndList(CuttableMaterialEndList)

##### Declaration

```
public CuttableMaterialEndList(CuttableMaterialEndList other)
```

##### Parameters

| Type                                                                          | Name  | Description |
| ----------------------------------------------------------------------------- | ----- | ----------- |
| [CuttableMaterialEndList](DesignData.SDS2.Model.CuttableMaterialEndList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5F%5F)CuttableMaterialEndList(IEnumerable<CuttableMaterialEnd>)

##### Declaration

```
public CuttableMaterialEndList(IEnumerable<CuttableMaterialEnd> c)
```

##### Parameters

| Type                                                                                                                                                                   | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)CuttableMaterialEndList(IEnumerable)

##### Declaration

```
public CuttableMaterialEndList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5F%5Fctor%5FSystem%5FInt32%5F)CuttableMaterialEndList(int)

##### Declaration

```
public CuttableMaterialEndList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public CuttableMaterialEnd this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FAdd%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5F)Add(CuttableMaterialEnd)

##### Declaration

```
public void Add(CuttableMaterialEnd x)
```

##### Parameters

| Type                                                                  | Name | Description |
| --------------------------------------------------------------------- | ---- | ----------- |
| [CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5F)AddRange(CuttableMaterialEndList)

##### Declaration

```
public void AddRange(CuttableMaterialEndList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [CuttableMaterialEndList](DesignData.SDS2.Model.CuttableMaterialEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5F%5F%5F)CopyTo(CuttableMaterialEnd\[\])

##### Declaration

```
public void CopyTo(CuttableMaterialEnd[] array)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5F%5F%5FSystem%5FInt32%5F)CopyTo(CuttableMaterialEnd\[\], int)

##### Declaration

```
public void CopyTo(CuttableMaterialEnd[] array, int arrayIndex)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, CuttableMaterialEnd\[\], int, int)

##### Declaration

```
public void CopyTo(int index, CuttableMaterialEnd[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | index      |             |
| [CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FFinalize)\~CuttableMaterialEndList()

##### Declaration

```
protected ~CuttableMaterialEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public CuttableMaterialEndList.CuttableMaterialEndListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                                    | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [CuttableMaterialEndList](DesignData.SDS2.Model.CuttableMaterialEndList.html).[CuttableMaterialEndListEnumerator](DesignData.SDS2.Model.CuttableMaterialEndList.CuttableMaterialEndListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public CuttableMaterialEndList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [CuttableMaterialEndList](DesignData.SDS2.Model.CuttableMaterialEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5F)Insert(int, CuttableMaterialEnd)

##### Declaration

```
public void Insert(int index, CuttableMaterialEnd x)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | index |             |
| [CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html) | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5F)InsertRange(int, CuttableMaterialEndList)

##### Declaration

```
public void InsertRange(int index, CuttableMaterialEndList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | index  |             |
| [CuttableMaterialEndList](DesignData.SDS2.Model.CuttableMaterialEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5FSystem%5FInt32%5F)Repeat(CuttableMaterialEnd, int)

##### Declaration

```
public static CuttableMaterialEndList Repeat(CuttableMaterialEnd value, int count)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | count |             |

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [CuttableMaterialEndList](DesignData.SDS2.Model.CuttableMaterialEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5F)SetRange(int, CuttableMaterialEndList)

##### Declaration

```
public void SetRange(int index, CuttableMaterialEndList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | index  |             |
| [CuttableMaterialEndList](DesignData.SDS2.Model.CuttableMaterialEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEndList%5FToArray)ToArray()

##### Declaration

```
public CuttableMaterialEnd[] ToArray()
```

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)