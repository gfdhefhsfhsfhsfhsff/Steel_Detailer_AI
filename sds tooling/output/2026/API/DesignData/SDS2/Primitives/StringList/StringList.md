# Class StringList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

StringList

##### Implements

[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public class StringList : IList<string>, ICollection<string>, IEnumerable<string>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5F%5Fctor)StringList()

##### Declaration

```
public StringList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FStringList%5F)StringList(StringList)

##### Declaration

```
public StringList(StringList other)
```

##### Parameters

| Type                                                     | Name  | Description |
| -------------------------------------------------------- | ----- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) | other |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FSystem%5FString%5F%5F)StringList(IEnumerable<string>)

##### Declaration

```
public StringList(IEnumerable<string> c)
```

##### Parameters

| Type                                                                                                                                                            | Name | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\> | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)StringList(IEnumerable)

##### Declaration

```
public StringList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5F%5Fctor%5FSystem%5FInt32%5F)StringList(int)

##### Declaration

```
public StringList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public string this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FAdd%5FSystem%5FString%5F)Add(string)

##### Declaration

```
public void Add(string x)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | x    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FAddRange%5FDesignData%5FSDS2%5FPrimitives%5FStringList%5F)AddRange(StringList)

##### Declaration

```
public void AddRange(StringList values)
```

##### Parameters

| Type                                                     | Name   | Description |
| -------------------------------------------------------- | ------ | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FContains%5FSystem%5FString%5F)Contains(string)

##### Declaration

```
public bool Contains(string value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | value |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FCopyTo%5FSystem%5FInt32%5FSystem%5FString%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, string\[\], int, int)

##### Declaration

```
public void CopyTo(int index, string[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                               | Name       | Description |
| ------------------------------------------------------------------ | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | index      |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | count      |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FCopyTo%5FSystem%5FString%5F%5F%5F)CopyTo(string\[\])

##### Declaration

```
public void CopyTo(string[] array)
```

##### Parameters

| Type                                                               | Name  | Description |
| ------------------------------------------------------------------ | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FCopyTo%5FSystem%5FString%5F%5F%5FSystem%5FInt32%5F)CopyTo(string\[\], int)

##### Declaration

```
public void CopyTo(string[] array, int arrayIndex)
```

##### Parameters

| Type                                                               | Name       | Description |
| ------------------------------------------------------------------ | ---------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FFinalize)\~StringList()

##### Declaration

```
protected ~StringList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public StringList.StringListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                             | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html).[StringListEnumerator](DesignData.SDS2.Primitives.StringList.StringListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public StringList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FIndexOf%5FSystem%5FString%5F)IndexOf(string)

##### Declaration

```
public int IndexOf(string value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | value |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FInsert%5FSystem%5FInt32%5FSystem%5FString%5F)Insert(int, string)

##### Declaration

```
public void Insert(int index, string x)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | x     |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FStringList%5F)InsertRange(int, StringList)

##### Declaration

```
public void InsertRange(int index, StringList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [StringList](DesignData.SDS2.Primitives.StringList.html)   | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FLastIndexOf%5FSystem%5FString%5F)LastIndexOf(string)

##### Declaration

```
public int LastIndexOf(string value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | value |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FRemove%5FSystem%5FString%5F)Remove(string)

##### Declaration

```
public bool Remove(string value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | value |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FRepeat%5FSystem%5FString%5FSystem%5FInt32%5F)Repeat(string, int)

##### Declaration

```
public static StringList Repeat(string value, int count)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | count |             |

##### Returns

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FStringList%5F)SetRange(int, StringList)

##### Declaration

```
public void SetRange(int index, StringList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [StringList](DesignData.SDS2.Primitives.StringList.html)   | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FStringList%5FToArray)ToArray()

##### Declaration

```
public string[] ToArray()
```

##### Returns

| Type                                                               | Description |
| ------------------------------------------------------------------ | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string)\[\] |             |

### [](#implements)Implements

[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1) 

[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1) 

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)