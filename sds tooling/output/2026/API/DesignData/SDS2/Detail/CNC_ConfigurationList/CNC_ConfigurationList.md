# Class CNC\_ConfigurationList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CNC\_ConfigurationList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Detail](DesignData.SDS2.Detail.html)

###### **Assembly**: DesignData.SDS2.Detail.dll

##### Syntax

```
public class CNC_ConfigurationList : IEnumerable<CNC_Configuration>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5F%5Fctor)CNC\_ConfigurationList()

##### Declaration

```
public CNC_ConfigurationList()
```

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5F%5Fctor%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5F)CNC\_ConfigurationList(CNC\_ConfigurationList)

##### Declaration

```
public CNC_ConfigurationList(CNC_ConfigurationList other)
```

##### Parameters

| Type                                                                          | Name  | Description |
| ----------------------------------------------------------------------------- | ----- | ----------- |
| [CNC\_ConfigurationList](DesignData.SDS2.Detail.CNC%5FConfigurationList.html) | other |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5F%5F)CNC\_ConfigurationList(IEnumerable<CNC\_Configuration>)

##### Declaration

```
public CNC_ConfigurationList(IEnumerable<CNC_Configuration> c)
```

##### Parameters

| Type                                                                                                                                                                   | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)CNC\_ConfigurationList(IEnumerable)

##### Declaration

```
public CNC_ConfigurationList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5F%5Fctor%5FSystem%5FInt32%5F)CNC\_ConfigurationList(int)

##### Declaration

```
public CNC_ConfigurationList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public CNC_Configuration this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FAdd%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5F)Add(CNC\_Configuration)

##### Declaration

```
public void Add(CNC_Configuration x)
```

##### Parameters

| Type                                                                  | Name | Description |
| --------------------------------------------------------------------- | ---- | ----------- |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html) | x    |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FAddRange%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5F)AddRange(CNC\_ConfigurationList)

##### Declaration

```
public void AddRange(CNC_ConfigurationList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [CNC\_ConfigurationList](DesignData.SDS2.Detail.CNC%5FConfigurationList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FCopyTo%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5F%5F%5F)CopyTo(CNC\_Configuration\[\])

##### Declaration

```
public void CopyTo(CNC_Configuration[] array)
```

##### Parameters

| Type                                                                      | Name  | Description |
| ------------------------------------------------------------------------- | ----- | ----------- |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FCopyTo%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5F%5F%5FSystem%5FInt32%5F)CopyTo(CNC\_Configuration\[\], int)

##### Declaration

```
public void CopyTo(CNC_Configuration[] array, int arrayIndex)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, CNC\_Configuration\[\], int, int)

##### Declaration

```
public void CopyTo(int index, CNC_Configuration[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | index      |             |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html)\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                | count      |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FFinalize)\~CNC\_ConfigurationList()

##### Declaration

```
protected ~CNC_ConfigurationList()
```

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public CNC_ConfigurationList.CNC_ConfigurationListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                                                    | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [CNC\_ConfigurationList](DesignData.SDS2.Detail.CNC%5FConfigurationList.html).[CNC\_ConfigurationListEnumerator](DesignData.SDS2.Detail.CNC%5FConfigurationList.CNC%5FConfigurationListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public CNC_ConfigurationList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [CNC\_ConfigurationList](DesignData.SDS2.Detail.CNC%5FConfigurationList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5F)Insert(int, CNC\_Configuration)

##### Declaration

```
public void Insert(int index, CNC_Configuration x)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | index |             |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html) | x     |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5F)InsertRange(int, CNC\_ConfigurationList)

##### Declaration

```
public void InsertRange(int index, CNC_ConfigurationList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | index  |             |
| [CNC\_ConfigurationList](DesignData.SDS2.Detail.CNC%5FConfigurationList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FRepeat%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FSystem%5FInt32%5F)Repeat(CNC\_Configuration, int)

##### Declaration

```
public static CNC_ConfigurationList Repeat(CNC_Configuration value, int count)
```

##### Parameters

| Type                                                                  | Name  | Description |
| --------------------------------------------------------------------- | ----- | ----------- |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html) | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)            | count |             |

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [CNC\_ConfigurationList](DesignData.SDS2.Detail.CNC%5FConfigurationList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5F)SetRange(int, CNC\_ConfigurationList)

##### Declaration

```
public void SetRange(int index, CNC_ConfigurationList values)
```

##### Parameters

| Type                                                                          | Name   | Description |
| ----------------------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                    | index  |             |
| [CNC\_ConfigurationList](DesignData.SDS2.Detail.CNC%5FConfigurationList.html) | values |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FToArray)ToArray()

##### Declaration

```
public CNC_Configuration[] ToArray()
```

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)