# Class ColdFormedBendList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ColdFormedBendList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html)\>

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
public class ColdFormedBendList : IEnumerable<ColdFormedBend>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5F%5Fctor)ColdFormedBendList()

##### Declaration

```
public ColdFormedBendList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FColdFormedBendList%5F)ColdFormedBendList(ColdFormedBendList)

##### Declaration

```
public ColdFormedBendList(ColdFormedBendList other)
```

##### Parameters

| Type                                                                | Name  | Description |
| ------------------------------------------------------------------- | ----- | ----------- |
| [ColdFormedBendList](DesignData.SDS2.Setup.ColdFormedBendList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FColdFormedBend%5F%5F)ColdFormedBendList(IEnumerable<ColdFormedBend>)

##### Declaration

```
public ColdFormedBendList(IEnumerable<ColdFormedBend> c)
```

##### Parameters

| Type                                                                                                                                                         | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)ColdFormedBendList(IEnumerable)

##### Declaration

```
public ColdFormedBendList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5F%5Fctor%5FSystem%5FInt32%5F)ColdFormedBendList(int)

##### Declaration

```
public ColdFormedBendList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public ColdFormedBend this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FColdFormedBend%5F)Add(ColdFormedBend)

##### Declaration

```
public void Add(ColdFormedBend x)
```

##### Parameters

| Type                                                        | Name | Description |
| ----------------------------------------------------------- | ---- | ----------- |
| [ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FColdFormedBendList%5F)AddRange(ColdFormedBendList)

##### Declaration

```
public void AddRange(ColdFormedBendList values)
```

##### Parameters

| Type                                                                | Name   | Description |
| ------------------------------------------------------------------- | ------ | ----------- |
| [ColdFormedBendList](DesignData.SDS2.Setup.ColdFormedBendList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FColdFormedBend%5F%5F%5F)CopyTo(ColdFormedBend\[\])

##### Declaration

```
public void CopyTo(ColdFormedBend[] array)
```

##### Parameters

| Type                                                            | Name  | Description |
| --------------------------------------------------------------- | ----- | ----------- |
| [ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FColdFormedBend%5F%5F%5FSystem%5FInt32%5F)CopyTo(ColdFormedBend\[\], int)

##### Declaration

```
public void CopyTo(ColdFormedBend[] array, int arrayIndex)
```

##### Parameters

| Type                                                            | Name       | Description |
| --------------------------------------------------------------- | ---------- | ----------- |
| [ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FColdFormedBend%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, ColdFormedBend\[\], int, int)

##### Declaration

```
public void CopyTo(int index, ColdFormedBend[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                            | Name       | Description |
| --------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | index      |             |
| [ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FFinalize)\~ColdFormedBendList()

##### Declaration

```
protected ~ColdFormedBendList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public ColdFormedBendList.ColdFormedBendListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                           | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [ColdFormedBendList](DesignData.SDS2.Setup.ColdFormedBendList.html).[ColdFormedBendListEnumerator](DesignData.SDS2.Setup.ColdFormedBendList.ColdFormedBendListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public ColdFormedBendList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [ColdFormedBendList](DesignData.SDS2.Setup.ColdFormedBendList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FColdFormedBend%5F)Insert(int, ColdFormedBend)

##### Declaration

```
public void Insert(int index, ColdFormedBend x)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index |             |
| [ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html) | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FColdFormedBendList%5F)InsertRange(int, ColdFormedBendList)

##### Declaration

```
public void InsertRange(int index, ColdFormedBendList values)
```

##### Parameters

| Type                                                                | Name   | Description |
| ------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | index  |             |
| [ColdFormedBendList](DesignData.SDS2.Setup.ColdFormedBendList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FColdFormedBend%5FSystem%5FInt32%5F)Repeat(ColdFormedBend, int)

##### Declaration

```
public static ColdFormedBendList Repeat(ColdFormedBend value, int count)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | count |             |

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [ColdFormedBendList](DesignData.SDS2.Setup.ColdFormedBendList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FColdFormedBendList%5F)SetRange(int, ColdFormedBendList)

##### Declaration

```
public void SetRange(int index, ColdFormedBendList values)
```

##### Parameters

| Type                                                                | Name   | Description |
| ------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)          | index  |             |
| [ColdFormedBendList](DesignData.SDS2.Setup.ColdFormedBendList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendList%5FToArray)ToArray()

##### Declaration

```
public ColdFormedBend[] ToArray()
```

##### Returns

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)