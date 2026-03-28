# Class BaseCapPlateAdditionalHoleList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BaseCapPlateAdditionalHoleList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BaseCapPlateAdditionalHole](DesignData.SDS2.Setup.BaseCapPlateAdditionalHole.html)\>

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
public class BaseCapPlateAdditionalHoleList : IEnumerable<BaseCapPlateAdditionalHole>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5F%5Fctor)BaseCapPlateAdditionalHoleList()

##### Declaration

```
public BaseCapPlateAdditionalHoleList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5F)BaseCapPlateAdditionalHoleList(BaseCapPlateAdditionalHoleList)

##### Declaration

```
public BaseCapPlateAdditionalHoleList(BaseCapPlateAdditionalHoleList other)
```

##### Parameters

| Type                                                                                        | Name  | Description |
| ------------------------------------------------------------------------------------------- | ----- | ----------- |
| [BaseCapPlateAdditionalHoleList](DesignData.SDS2.Setup.BaseCapPlateAdditionalHoleList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHole%5F%5F)BaseCapPlateAdditionalHoleList(IEnumerable<BaseCapPlateAdditionalHole>)

##### Declaration

```
public BaseCapPlateAdditionalHoleList(IEnumerable<BaseCapPlateAdditionalHole> c)
```

##### Parameters

| Type                                                                                                                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BaseCapPlateAdditionalHole](DesignData.SDS2.Setup.BaseCapPlateAdditionalHole.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)BaseCapPlateAdditionalHoleList(IEnumerable)

##### Declaration

```
public BaseCapPlateAdditionalHoleList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5F%5Fctor%5FSystem%5FInt32%5F)BaseCapPlateAdditionalHoleList(int)

##### Declaration

```
public BaseCapPlateAdditionalHoleList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public BaseCapPlateAdditionalHole this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [BaseCapPlateAdditionalHole](DesignData.SDS2.Setup.BaseCapPlateAdditionalHole.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHole%5F)Add(BaseCapPlateAdditionalHole)

##### Declaration

```
public void Add(BaseCapPlateAdditionalHole x)
```

##### Parameters

| Type                                                                                | Name | Description |
| ----------------------------------------------------------------------------------- | ---- | ----------- |
| [BaseCapPlateAdditionalHole](DesignData.SDS2.Setup.BaseCapPlateAdditionalHole.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5F)AddRange(BaseCapPlateAdditionalHoleList)

##### Declaration

```
public void AddRange(BaseCapPlateAdditionalHoleList values)
```

##### Parameters

| Type                                                                                        | Name   | Description |
| ------------------------------------------------------------------------------------------- | ------ | ----------- |
| [BaseCapPlateAdditionalHoleList](DesignData.SDS2.Setup.BaseCapPlateAdditionalHoleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHole%5F%5F%5F)CopyTo(BaseCapPlateAdditionalHole\[\])

##### Declaration

```
public void CopyTo(BaseCapPlateAdditionalHole[] array)
```

##### Parameters

| Type                                                                                    | Name  | Description |
| --------------------------------------------------------------------------------------- | ----- | ----------- |
| [BaseCapPlateAdditionalHole](DesignData.SDS2.Setup.BaseCapPlateAdditionalHole.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHole%5F%5F%5FSystem%5FInt32%5F)CopyTo(BaseCapPlateAdditionalHole\[\], int)

##### Declaration

```
public void CopyTo(BaseCapPlateAdditionalHole[] array, int arrayIndex)
```

##### Parameters

| Type                                                                                    | Name       | Description |
| --------------------------------------------------------------------------------------- | ---------- | ----------- |
| [BaseCapPlateAdditionalHole](DesignData.SDS2.Setup.BaseCapPlateAdditionalHole.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                              | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHole%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, BaseCapPlateAdditionalHole\[\], int, int)

##### Declaration

```
public void CopyTo(int index, BaseCapPlateAdditionalHole[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                                    | Name       | Description |
| --------------------------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                              | index      |             |
| [BaseCapPlateAdditionalHole](DesignData.SDS2.Setup.BaseCapPlateAdditionalHole.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                              | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                              | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FFinalize)\~BaseCapPlateAdditionalHoleList()

##### Declaration

```
protected ~BaseCapPlateAdditionalHoleList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public BaseCapPlateAdditionalHoleList.BaseCapPlateAdditionalHoleListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                                                                       | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [BaseCapPlateAdditionalHoleList](DesignData.SDS2.Setup.BaseCapPlateAdditionalHoleList.html).[BaseCapPlateAdditionalHoleListEnumerator](DesignData.SDS2.Setup.BaseCapPlateAdditionalHoleList.BaseCapPlateAdditionalHoleListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public BaseCapPlateAdditionalHoleList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                                        | Description |
| ------------------------------------------------------------------------------------------- | ----------- |
| [BaseCapPlateAdditionalHoleList](DesignData.SDS2.Setup.BaseCapPlateAdditionalHoleList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHole%5F)Insert(int, BaseCapPlateAdditionalHole)

##### Declaration

```
public void Insert(int index, BaseCapPlateAdditionalHole x)
```

##### Parameters

| Type                                                                                | Name  | Description |
| ----------------------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                          | index |             |
| [BaseCapPlateAdditionalHole](DesignData.SDS2.Setup.BaseCapPlateAdditionalHole.html) | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5F)InsertRange(int, BaseCapPlateAdditionalHoleList)

##### Declaration

```
public void InsertRange(int index, BaseCapPlateAdditionalHoleList values)
```

##### Parameters

| Type                                                                                        | Name   | Description |
| ------------------------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                  | index  |             |
| [BaseCapPlateAdditionalHoleList](DesignData.SDS2.Setup.BaseCapPlateAdditionalHoleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHole%5FSystem%5FInt32%5F)Repeat(BaseCapPlateAdditionalHole, int)

##### Declaration

```
public static BaseCapPlateAdditionalHoleList Repeat(BaseCapPlateAdditionalHole value, int count)
```

##### Parameters

| Type                                                                                | Name  | Description |
| ----------------------------------------------------------------------------------- | ----- | ----------- |
| [BaseCapPlateAdditionalHole](DesignData.SDS2.Setup.BaseCapPlateAdditionalHole.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                          | count |             |

##### Returns

| Type                                                                                        | Description |
| ------------------------------------------------------------------------------------------- | ----------- |
| [BaseCapPlateAdditionalHoleList](DesignData.SDS2.Setup.BaseCapPlateAdditionalHoleList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5F)SetRange(int, BaseCapPlateAdditionalHoleList)

##### Declaration

```
public void SetRange(int index, BaseCapPlateAdditionalHoleList values)
```

##### Parameters

| Type                                                                                        | Name   | Description |
| ------------------------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                  | index  |             |
| [BaseCapPlateAdditionalHoleList](DesignData.SDS2.Setup.BaseCapPlateAdditionalHoleList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateAdditionalHoleList%5FToArray)ToArray()

##### Declaration

```
public BaseCapPlateAdditionalHole[] ToArray()
```

##### Returns

| Type                                                                                    | Description |
| --------------------------------------------------------------------------------------- | ----------- |
| [BaseCapPlateAdditionalHole](DesignData.SDS2.Setup.BaseCapPlateAdditionalHole.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)