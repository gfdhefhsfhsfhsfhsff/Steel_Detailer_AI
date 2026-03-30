# Class NamedColorList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

NamedColorList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[NamedColor](DesignData.SDS2.Setup.NamedColor.html)\>

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
public class NamedColorList : IEnumerable<NamedColor>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5F%5Fctor)NamedColorList()

##### Declaration

```
public NamedColorList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FNamedColorList%5F)NamedColorList(NamedColorList)

##### Declaration

```
public NamedColorList(NamedColorList other)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [NamedColorList](DesignData.SDS2.Setup.NamedColorList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FNamedColor%5F%5F)NamedColorList(IEnumerable<NamedColor>)

##### Declaration

```
public NamedColorList(IEnumerable<NamedColor> c)
```

##### Parameters

| Type                                                                                                                                                 | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[NamedColor](DesignData.SDS2.Setup.NamedColor.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)NamedColorList(IEnumerable)

##### Declaration

```
public NamedColorList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5F%5Fctor%5FSystem%5FInt32%5F)NamedColorList(int)

##### Declaration

```
public NamedColorList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public NamedColor this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [NamedColor](DesignData.SDS2.Setup.NamedColor.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FNamedColor%5F)Add(NamedColor)

##### Declaration

```
public void Add(NamedColor x)
```

##### Parameters

| Type                                                | Name | Description |
| --------------------------------------------------- | ---- | ----------- |
| [NamedColor](DesignData.SDS2.Setup.NamedColor.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FNamedColorList%5F)AddRange(NamedColorList)

##### Declaration

```
public void AddRange(NamedColorList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [NamedColorList](DesignData.SDS2.Setup.NamedColorList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FNamedColor%5F%5F%5F)CopyTo(NamedColor\[\])

##### Declaration

```
public void CopyTo(NamedColor[] array)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [NamedColor](DesignData.SDS2.Setup.NamedColor.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FNamedColor%5F%5F%5FSystem%5FInt32%5F)CopyTo(NamedColor\[\], int)

##### Declaration

```
public void CopyTo(NamedColor[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [NamedColor](DesignData.SDS2.Setup.NamedColor.html)\[\]    | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FNamedColor%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, NamedColor\[\], int, int)

##### Declaration

```
public void CopyTo(int index, NamedColor[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [NamedColor](DesignData.SDS2.Setup.NamedColor.html)\[\]    | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FFinalize)\~NamedColorList()

##### Declaration

```
protected ~NamedColorList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public NamedColorList.NamedColorListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                       | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [NamedColorList](DesignData.SDS2.Setup.NamedColorList.html).[NamedColorListEnumerator](DesignData.SDS2.Setup.NamedColorList.NamedColorListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public NamedColorList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [NamedColorList](DesignData.SDS2.Setup.NamedColorList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FNamedColor%5F)Insert(int, NamedColor)

##### Declaration

```
public void Insert(int index, NamedColor x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [NamedColor](DesignData.SDS2.Setup.NamedColor.html)        | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FNamedColorList%5F)InsertRange(int, NamedColorList)

##### Declaration

```
public void InsertRange(int index, NamedColorList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index  |             |
| [NamedColorList](DesignData.SDS2.Setup.NamedColorList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FNamedColor%5FSystem%5FInt32%5F)Repeat(NamedColor, int)

##### Declaration

```
public static NamedColorList Repeat(NamedColor value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [NamedColor](DesignData.SDS2.Setup.NamedColor.html)        | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [NamedColorList](DesignData.SDS2.Setup.NamedColorList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FNamedColorList%5F)SetRange(int, NamedColorList)

##### Declaration

```
public void SetRange(int index, NamedColorList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index  |             |
| [NamedColorList](DesignData.SDS2.Setup.NamedColorList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FToArray)ToArray()

##### Declaration

```
public NamedColor[] ToArray()
```

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [NamedColor](DesignData.SDS2.Setup.NamedColor.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)