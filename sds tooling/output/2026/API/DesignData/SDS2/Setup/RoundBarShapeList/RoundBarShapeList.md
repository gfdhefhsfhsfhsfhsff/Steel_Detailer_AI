# Class RoundBarShapeList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

RoundBarShapeList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html)\>

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
public class RoundBarShapeList : IEnumerable<RoundBarShape>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5F%5Fctor)RoundBarShapeList()

##### Declaration

```
public RoundBarShapeList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5F)RoundBarShapeList(RoundBarShapeList)

##### Declaration

```
public RoundBarShapeList(RoundBarShapeList other)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [RoundBarShapeList](DesignData.SDS2.Setup.RoundBarShapeList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FRoundBarShape%5F%5F)RoundBarShapeList(IEnumerable<RoundBarShape>)

##### Declaration

```
public RoundBarShapeList(IEnumerable<RoundBarShape> c)
```

##### Parameters

| Type                                                                                                                                                       | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)RoundBarShapeList(IEnumerable)

##### Declaration

```
public RoundBarShapeList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5F%5Fctor%5FSystem%5FInt32%5F)RoundBarShapeList(int)

##### Declaration

```
public RoundBarShapeList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public RoundBarShape this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FRoundBarShape%5F)Add(RoundBarShape)

##### Declaration

```
public void Add(RoundBarShape x)
```

##### Parameters

| Type                                                      | Name | Description |
| --------------------------------------------------------- | ---- | ----------- |
| [RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5F)AddRange(RoundBarShapeList)

##### Declaration

```
public void AddRange(RoundBarShapeList values)
```

##### Parameters

| Type                                                              | Name   | Description |
| ----------------------------------------------------------------- | ------ | ----------- |
| [RoundBarShapeList](DesignData.SDS2.Setup.RoundBarShapeList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FRoundBarShape%5F%5F%5F)CopyTo(RoundBarShape\[\])

##### Declaration

```
public void CopyTo(RoundBarShape[] array)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FRoundBarShape%5F%5F%5FSystem%5FInt32%5F)CopyTo(RoundBarShape\[\], int)

##### Declaration

```
public void CopyTo(RoundBarShape[] array, int arrayIndex)
```

##### Parameters

| Type                                                          | Name       | Description |
| ------------------------------------------------------------- | ---------- | ----------- |
| [RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoundBarShape%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, RoundBarShape\[\], int, int)

##### Declaration

```
public void CopyTo(int index, RoundBarShape[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                          | Name       | Description |
| ------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index      |             |
| [RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FFinalize)\~RoundBarShapeList()

##### Declaration

```
protected ~RoundBarShapeList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public RoundBarShapeList.RoundBarShapeListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                      | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [RoundBarShapeList](DesignData.SDS2.Setup.RoundBarShapeList.html).[RoundBarShapeListEnumerator](DesignData.SDS2.Setup.RoundBarShapeList.RoundBarShapeListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public RoundBarShapeList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [RoundBarShapeList](DesignData.SDS2.Setup.RoundBarShapeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoundBarShape%5F)Insert(int, RoundBarShape)

##### Declaration

```
public void Insert(int index, RoundBarShape x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html)  | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5F)InsertRange(int, RoundBarShapeList)

##### Declaration

```
public void InsertRange(int index, RoundBarShapeList values)
```

##### Parameters

| Type                                                              | Name   | Description |
| ----------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | index  |             |
| [RoundBarShapeList](DesignData.SDS2.Setup.RoundBarShapeList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FRoundBarShape%5FSystem%5FInt32%5F)Repeat(RoundBarShape, int)

##### Declaration

```
public static RoundBarShapeList Repeat(RoundBarShape value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html)  | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [RoundBarShapeList](DesignData.SDS2.Setup.RoundBarShapeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5F)SetRange(int, RoundBarShapeList)

##### Declaration

```
public void SetRange(int index, RoundBarShapeList values)
```

##### Parameters

| Type                                                              | Name   | Description |
| ----------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)        | index  |             |
| [RoundBarShapeList](DesignData.SDS2.Setup.RoundBarShapeList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRoundBarShapeList%5FToArray)ToArray()

##### Declaration

```
public RoundBarShape[] ToArray()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)