# Class BaseCapPlateList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BaseCapPlateList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html)\>

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
public class BaseCapPlateList : IEnumerable<BaseCapPlate>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5F%5Fctor)BaseCapPlateList()

##### Declaration

```
public BaseCapPlateList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5F)BaseCapPlateList(BaseCapPlateList)

##### Declaration

```
public BaseCapPlateList(BaseCapPlateList other)
```

##### Parameters

| Type                                                            | Name  | Description |
| --------------------------------------------------------------- | ----- | ----------- |
| [BaseCapPlateList](DesignData.SDS2.Setup.BaseCapPlateList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlate%5F%5F)BaseCapPlateList(IEnumerable<BaseCapPlate>)

##### Declaration

```
public BaseCapPlateList(IEnumerable<BaseCapPlate> c)
```

##### Parameters

| Type                                                                                                                                                     | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)BaseCapPlateList(IEnumerable)

##### Declaration

```
public BaseCapPlateList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5F%5Fctor%5FSystem%5FInt32%5F)BaseCapPlateList(int)

##### Declaration

```
public BaseCapPlateList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public BaseCapPlate this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlate%5F)Add(BaseCapPlate)

##### Declaration

```
public void Add(BaseCapPlate x)
```

##### Parameters

| Type                                                    | Name | Description |
| ------------------------------------------------------- | ---- | ----------- |
| [BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5F)AddRange(BaseCapPlateList)

##### Declaration

```
public void AddRange(BaseCapPlateList values)
```

##### Parameters

| Type                                                            | Name   | Description |
| --------------------------------------------------------------- | ------ | ----------- |
| [BaseCapPlateList](DesignData.SDS2.Setup.BaseCapPlateList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlate%5F%5F%5F)CopyTo(BaseCapPlate\[\])

##### Declaration

```
public void CopyTo(BaseCapPlate[] array)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlate%5F%5F%5FSystem%5FInt32%5F)CopyTo(BaseCapPlate\[\], int)

##### Declaration

```
public void CopyTo(BaseCapPlate[] array, int arrayIndex)
```

##### Parameters

| Type                                                        | Name       | Description |
| ----------------------------------------------------------- | ---------- | ----------- |
| [BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlate%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, BaseCapPlate\[\], int, int)

##### Declaration

```
public void CopyTo(int index, BaseCapPlate[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                        | Name       | Description |
| ----------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index      |             |
| [BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FFinalize)\~BaseCapPlateList()

##### Declaration

```
protected ~BaseCapPlateList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public BaseCapPlateList.BaseCapPlateListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                 | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [BaseCapPlateList](DesignData.SDS2.Setup.BaseCapPlateList.html).[BaseCapPlateListEnumerator](DesignData.SDS2.Setup.BaseCapPlateList.BaseCapPlateListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public BaseCapPlateList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [BaseCapPlateList](DesignData.SDS2.Setup.BaseCapPlateList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlate%5F)Insert(int, BaseCapPlate)

##### Declaration

```
public void Insert(int index, BaseCapPlate x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html)    | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5F)InsertRange(int, BaseCapPlateList)

##### Declaration

```
public void InsertRange(int index, BaseCapPlateList values)
```

##### Parameters

| Type                                                            | Name   | Description |
| --------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | index  |             |
| [BaseCapPlateList](DesignData.SDS2.Setup.BaseCapPlateList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlate%5FSystem%5FInt32%5F)Repeat(BaseCapPlate, int)

##### Declaration

```
public static BaseCapPlateList Repeat(BaseCapPlate value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html)    | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [BaseCapPlateList](DesignData.SDS2.Setup.BaseCapPlateList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5F)SetRange(int, BaseCapPlateList)

##### Declaration

```
public void SetRange(int index, BaseCapPlateList values)
```

##### Parameters

| Type                                                            | Name   | Description |
| --------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)      | index  |             |
| [BaseCapPlateList](DesignData.SDS2.Setup.BaseCapPlateList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateList%5FToArray)ToArray()

##### Declaration

```
public BaseCapPlate[] ToArray()
```

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)