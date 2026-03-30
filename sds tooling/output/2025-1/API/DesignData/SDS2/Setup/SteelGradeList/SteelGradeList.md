# Class SteelGradeList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

SteelGradeList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[SteelGrade](DesignData.SDS2.Setup.SteelGrade.html)\>

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
public class SteelGradeList : IEnumerable<SteelGrade>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5F%5Fctor)SteelGradeList()

##### Declaration

```
public SteelGradeList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FSteelGradeList%5F)SteelGradeList(SteelGradeList)

##### Declaration

```
public SteelGradeList(SteelGradeList other)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F%5F)SteelGradeList(IEnumerable<SteelGrade>)

##### Declaration

```
public SteelGradeList(IEnumerable<SteelGrade> c)
```

##### Parameters

| Type                                                                                                                                                 | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[SteelGrade](DesignData.SDS2.Setup.SteelGrade.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)SteelGradeList(IEnumerable)

##### Declaration

```
public SteelGradeList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5F%5Fctor%5FSystem%5FInt32%5F)SteelGradeList(int)

##### Declaration

```
public SteelGradeList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public SteelGrade this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F)Add(SteelGrade)

##### Declaration

```
public void Add(SteelGrade x)
```

##### Parameters

| Type                                                | Name | Description |
| --------------------------------------------------- | ---- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FSteelGradeList%5F)AddRange(SteelGradeList)

##### Declaration

```
public void AddRange(SteelGradeList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F%5F%5F)CopyTo(SteelGrade\[\])

##### Declaration

```
public void CopyTo(SteelGrade[] array)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F%5F%5FSystem%5FInt32%5F)CopyTo(SteelGrade\[\], int)

##### Declaration

```
public void CopyTo(SteelGrade[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html)\[\]    | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, SteelGrade\[\], int, int)

##### Declaration

```
public void CopyTo(int index, SteelGrade[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html)\[\]    | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FFinalize)\~SteelGradeList()

##### Declaration

```
protected ~SteelGradeList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public SteelGradeList.SteelGradeListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                       | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html).[SteelGradeListEnumerator](DesignData.SDS2.Setup.SteelGradeList.SteelGradeListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public SteelGradeList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F)Insert(int, SteelGrade)

##### Declaration

```
public void Insert(int index, SteelGrade x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html)        | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FSteelGradeList%5F)InsertRange(int, SteelGradeList)

##### Declaration

```
public void InsertRange(int index, SteelGradeList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index  |             |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5FSystem%5FInt32%5F)Repeat(SteelGrade, int)

##### Declaration

```
public static SteelGradeList Repeat(SteelGrade value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html)        | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FSteelGradeList%5F)SetRange(int, SteelGradeList)

##### Declaration

```
public void SetRange(int index, SteelGradeList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index  |             |
| [SteelGradeList](DesignData.SDS2.Setup.SteelGradeList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGradeList%5FToArray)ToArray()

##### Declaration

```
public SteelGrade[] ToArray()
```

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)