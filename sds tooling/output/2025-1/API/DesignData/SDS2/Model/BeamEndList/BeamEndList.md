# Class BeamEndList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BeamEndList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BeamEnd](DesignData.SDS2.Model.BeamEnd.html)\>

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
public class BeamEndList : IEnumerable<BeamEnd>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5F%5Fctor)BeamEndList()

##### Declaration

```
public BeamEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FBeamEndList%5F)BeamEndList(BeamEndList)

##### Declaration

```
public BeamEndList(BeamEndList other)
```

##### Parameters

| Type                                                  | Name  | Description |
| ----------------------------------------------------- | ----- | ----------- |
| [BeamEndList](DesignData.SDS2.Model.BeamEndList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FBeamEnd%5F%5F)BeamEndList(IEnumerable<BeamEnd>)

##### Declaration

```
public BeamEndList(IEnumerable<BeamEnd> c)
```

##### Parameters

| Type                                                                                                                                           | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BeamEnd](DesignData.SDS2.Model.BeamEnd.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)BeamEndList(IEnumerable)

##### Declaration

```
public BeamEndList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5F%5Fctor%5FSystem%5FInt32%5F)BeamEndList(int)

##### Declaration

```
public BeamEndList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FItem%5FDesignData%5FSDS2%5FDatabase%5FMemberEnd%5F)this\[MemberEnd\]

##### Declaration

```
public BeamEnd this[MemberEnd end] { get; set; }
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [MemberEnd](DesignData.SDS2.Database.MemberEnd.html) | end  |             |

##### Property Value

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [BeamEnd](DesignData.SDS2.Model.BeamEnd.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public BeamEnd this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [BeamEnd](DesignData.SDS2.Model.BeamEnd.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FAdd%5FDesignData%5FSDS2%5FModel%5FBeamEnd%5F)Add(BeamEnd)

##### Declaration

```
public void Add(BeamEnd x)
```

##### Parameters

| Type                                          | Name | Description |
| --------------------------------------------- | ---- | ----------- |
| [BeamEnd](DesignData.SDS2.Model.BeamEnd.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FBeamEndList%5F)AddRange(BeamEndList)

##### Declaration

```
public void AddRange(BeamEndList values)
```

##### Parameters

| Type                                                  | Name   | Description |
| ----------------------------------------------------- | ------ | ----------- |
| [BeamEndList](DesignData.SDS2.Model.BeamEndList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FBeamEnd%5F%5F%5F)CopyTo(BeamEnd\[\])

##### Declaration

```
public void CopyTo(BeamEnd[] array)
```

##### Parameters

| Type                                              | Name  | Description |
| ------------------------------------------------- | ----- | ----------- |
| [BeamEnd](DesignData.SDS2.Model.BeamEnd.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FBeamEnd%5F%5F%5FSystem%5FInt32%5F)CopyTo(BeamEnd\[\], int)

##### Declaration

```
public void CopyTo(BeamEnd[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [BeamEnd](DesignData.SDS2.Model.BeamEnd.html)\[\]          | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBeamEnd%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, BeamEnd\[\], int, int)

##### Declaration

```
public void CopyTo(int index, BeamEnd[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [BeamEnd](DesignData.SDS2.Model.BeamEnd.html)\[\]          | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FFinalize)\~BeamEndList()

##### Declaration

```
protected ~BeamEndList()
```

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public BeamEndList.BeamEndListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                        | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [BeamEndList](DesignData.SDS2.Model.BeamEndList.html).[BeamEndListEnumerator](DesignData.SDS2.Model.BeamEndList.BeamEndListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public BeamEndList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [BeamEndList](DesignData.SDS2.Model.BeamEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBeamEnd%5F)Insert(int, BeamEnd)

##### Declaration

```
public void Insert(int index, BeamEnd x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [BeamEnd](DesignData.SDS2.Model.BeamEnd.html)              | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBeamEndList%5F)InsertRange(int, BeamEndList)

##### Declaration

```
public void InsertRange(int index, BeamEndList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [BeamEndList](DesignData.SDS2.Model.BeamEndList.html)      | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FBeamEnd%5FSystem%5FInt32%5F)Repeat(BeamEnd, int)

##### Declaration

```
public static BeamEndList Repeat(BeamEnd value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [BeamEnd](DesignData.SDS2.Model.BeamEnd.html)              | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [BeamEndList](DesignData.SDS2.Model.BeamEndList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FBeamEndList%5F)SetRange(int, BeamEndList)

##### Declaration

```
public void SetRange(int index, BeamEndList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [BeamEndList](DesignData.SDS2.Model.BeamEndList.html)      | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FBeamEndList%5FToArray)ToArray()

##### Declaration

```
public BeamEnd[] ToArray()
```

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [BeamEnd](DesignData.SDS2.Model.BeamEnd.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)