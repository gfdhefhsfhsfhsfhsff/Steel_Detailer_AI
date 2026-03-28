# Class IdentifierList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

IdentifierList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Identifier](DesignData.SDS2.Database.Identifier.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class IdentifierList : IEnumerable<Identifier>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5F%5Fctor)IdentifierList()

##### Declaration

```
public IdentifierList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FIdentifierList%5F)IdentifierList(IdentifierList)

##### Declaration

```
public IdentifierList(IdentifierList other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [IdentifierList](DesignData.SDS2.Database.IdentifierList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDatabase%5FIdentifier%5F%5F)IdentifierList(IEnumerable<Identifier>)

##### Declaration

```
public IdentifierList(IEnumerable<Identifier> c)
```

##### Parameters

| Type                                                                                                                                                    | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Identifier](DesignData.SDS2.Database.Identifier.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)IdentifierList(IEnumerable)

##### Declaration

```
public IdentifierList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5F%5Fctor%5FSystem%5FInt32%5F)IdentifierList(int)

##### Declaration

```
public IdentifierList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Identifier this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [Identifier](DesignData.SDS2.Database.Identifier.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FIdentifier%5F)Add(Identifier)

##### Declaration

```
public void Add(Identifier x)
```

##### Parameters

| Type                                                   | Name | Description |
| ------------------------------------------------------ | ---- | ----------- |
| [Identifier](DesignData.SDS2.Database.Identifier.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FAddRange%5FDesignData%5FSDS2%5FDatabase%5FIdentifierList%5F)AddRange(IdentifierList)

##### Declaration

```
public void AddRange(IdentifierList values)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [IdentifierList](DesignData.SDS2.Database.IdentifierList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FIdentifier%5F%5F%5F)CopyTo(Identifier\[\])

##### Declaration

```
public void CopyTo(Identifier[] array)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Identifier](DesignData.SDS2.Database.Identifier.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FCopyTo%5FDesignData%5FSDS2%5FDatabase%5FIdentifier%5F%5F%5FSystem%5FInt32%5F)CopyTo(Identifier\[\], int)

##### Declaration

```
public void CopyTo(Identifier[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Identifier](DesignData.SDS2.Database.Identifier.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FIdentifier%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Identifier\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Identifier[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Identifier](DesignData.SDS2.Database.Identifier.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FFinalize)\~IdentifierList()

##### Declaration

```
protected ~IdentifierList()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public IdentifierList.IdentifierListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                             | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [IdentifierList](DesignData.SDS2.Database.IdentifierList.html).[IdentifierListEnumerator](DesignData.SDS2.Database.IdentifierList.IdentifierListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public IdentifierList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [IdentifierList](DesignData.SDS2.Database.IdentifierList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FIdentifier%5F)Insert(int, Identifier)

##### Declaration

```
public void Insert(int index, Identifier x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Identifier](DesignData.SDS2.Database.Identifier.html)     | x     |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FIdentifierList%5F)InsertRange(int, IdentifierList)

##### Declaration

```
public void InsertRange(int index, IdentifierList values)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index  |             |
| [IdentifierList](DesignData.SDS2.Database.IdentifierList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FRepeat%5FDesignData%5FSDS2%5FDatabase%5FIdentifier%5FSystem%5FInt32%5F)Repeat(Identifier, int)

##### Declaration

```
public static IdentifierList Repeat(Identifier value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Identifier](DesignData.SDS2.Database.Identifier.html)     | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [IdentifierList](DesignData.SDS2.Database.IdentifierList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FIdentifierList%5F)SetRange(int, IdentifierList)

##### Declaration

```
public void SetRange(int index, IdentifierList values)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index  |             |
| [IdentifierList](DesignData.SDS2.Database.IdentifierList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FIdentifierList%5FToArray)ToArray()

##### Declaration

```
public Identifier[] ToArray()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [Identifier](DesignData.SDS2.Database.Identifier.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)