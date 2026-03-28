# Class DoubleList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DoubleList

##### Implements

[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

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
public class DoubleList : IList<double>, ICollection<double>, IEnumerable<double>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5F%5Fctor)DoubleList()

##### Declaration

```
public DoubleList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FDoubleList%5F)DoubleList(DoubleList)

##### Declaration

```
public DoubleList(DoubleList other)
```

##### Parameters

| Type                                                     | Name  | Description |
| -------------------------------------------------------- | ----- | ----------- |
| [DoubleList](DesignData.SDS2.Primitives.DoubleList.html) | other |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FSystem%5FDouble%5F%5F)DoubleList(IEnumerable<double>)

##### Declaration

```
public DoubleList(IEnumerable<double> c)
```

##### Parameters

| Type                                                                                                                                                            | Name | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\> | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)DoubleList(IEnumerable)

##### Declaration

```
public DoubleList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5F%5Fctor%5FSystem%5FInt32%5F)DoubleList(int)

##### Declaration

```
public DoubleList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public double this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FAdd%5FSystem%5FDouble%5F)Add(double)

##### Declaration

```
public void Add(double x)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | x    |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FAddRange%5FDesignData%5FSDS2%5FPrimitives%5FDoubleList%5F)AddRange(DoubleList)

##### Declaration

```
public void AddRange(DoubleList values)
```

##### Parameters

| Type                                                     | Name   | Description |
| -------------------------------------------------------- | ------ | ----------- |
| [DoubleList](DesignData.SDS2.Primitives.DoubleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FContains%5FSystem%5FDouble%5F)Contains(double)

##### Declaration

```
public bool Contains(double value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FCopyTo%5FSystem%5FDouble%5F%5F%5F)CopyTo(double\[\])

##### Declaration

```
public void CopyTo(double[] array)
```

##### Parameters

| Type                                                               | Name  | Description |
| ------------------------------------------------------------------ | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FCopyTo%5FSystem%5FDouble%5F%5F%5FSystem%5FInt32%5F)CopyTo(double\[\], int)

##### Declaration

```
public void CopyTo(double[] array, int arrayIndex)
```

##### Parameters

| Type                                                               | Name       | Description |
| ------------------------------------------------------------------ | ---------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FCopyTo%5FSystem%5FInt32%5FSystem%5FDouble%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, double\[\], int, int)

##### Declaration

```
public void CopyTo(int index, double[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                               | Name       | Description |
| ------------------------------------------------------------------ | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | index      |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)         | count      |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FFinalize)\~DoubleList()

##### Declaration

```
protected ~DoubleList()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public DoubleList.DoubleListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                             | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [DoubleList](DesignData.SDS2.Primitives.DoubleList.html).[DoubleListEnumerator](DesignData.SDS2.Primitives.DoubleList.DoubleListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public DoubleList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [DoubleList](DesignData.SDS2.Primitives.DoubleList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FIndexOf%5FSystem%5FDouble%5F)IndexOf(double)

##### Declaration

```
public int IndexOf(double value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FInsert%5FSystem%5FInt32%5FSystem%5FDouble%5F)Insert(int, double)

##### Declaration

```
public void Insert(int index, double x)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | x     |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FDoubleList%5F)InsertRange(int, DoubleList)

##### Declaration

```
public void InsertRange(int index, DoubleList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [DoubleList](DesignData.SDS2.Primitives.DoubleList.html)   | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FLastIndexOf%5FSystem%5FDouble%5F)LastIndexOf(double)

##### Declaration

```
public int LastIndexOf(double value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FRemove%5FSystem%5FDouble%5F)Remove(double)

##### Declaration

```
public bool Remove(double value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FRepeat%5FSystem%5FDouble%5FSystem%5FInt32%5F)Repeat(double, int)

##### Declaration

```
public static DoubleList Repeat(double value, int count)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | count |             |

##### Returns

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [DoubleList](DesignData.SDS2.Primitives.DoubleList.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FPrimitives%5FDoubleList%5F)SetRange(int, DoubleList)

##### Declaration

```
public void SetRange(int index, DoubleList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [DoubleList](DesignData.SDS2.Primitives.DoubleList.html)   | values |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FDoubleList%5FToArray)ToArray()

##### Declaration

```
public double[] ToArray()
```

##### Returns

| Type                                                               | Description |
| ------------------------------------------------------------------ | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double)\[\] |             |

### [](#implements)Implements

[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1) 

[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1) 

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)