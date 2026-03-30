# Class JobZoneList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

JobZoneList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[JobZone](DesignData.SDS2.Setup.JobZone.html)\>

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
public class JobZoneList : IEnumerable<JobZone>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5F%5Fctor)JobZoneList()

##### Declaration

```
public JobZoneList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FJobZoneList%5F)JobZoneList(JobZoneList)

##### Declaration

```
public JobZoneList(JobZoneList other)
```

##### Parameters

| Type                                                  | Name  | Description |
| ----------------------------------------------------- | ----- | ----------- |
| [JobZoneList](DesignData.SDS2.Setup.JobZoneList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FJobZone%5F%5F)JobZoneList(IEnumerable<JobZone>)

##### Declaration

```
public JobZoneList(IEnumerable<JobZone> c)
```

##### Parameters

| Type                                                                                                                                           | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[JobZone](DesignData.SDS2.Setup.JobZone.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)JobZoneList(IEnumerable)

##### Declaration

```
public JobZoneList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5F%5Fctor%5FSystem%5FInt32%5F)JobZoneList(int)

##### Declaration

```
public JobZoneList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public JobZone this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [JobZone](DesignData.SDS2.Setup.JobZone.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FJobZone%5F)Add(JobZone)

##### Declaration

```
public void Add(JobZone x)
```

##### Parameters

| Type                                          | Name | Description |
| --------------------------------------------- | ---- | ----------- |
| [JobZone](DesignData.SDS2.Setup.JobZone.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FJobZoneList%5F)AddRange(JobZoneList)

##### Declaration

```
public void AddRange(JobZoneList values)
```

##### Parameters

| Type                                                  | Name   | Description |
| ----------------------------------------------------- | ------ | ----------- |
| [JobZoneList](DesignData.SDS2.Setup.JobZoneList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FJobZone%5F%5F%5F)CopyTo(JobZone\[\])

##### Declaration

```
public void CopyTo(JobZone[] array)
```

##### Parameters

| Type                                              | Name  | Description |
| ------------------------------------------------- | ----- | ----------- |
| [JobZone](DesignData.SDS2.Setup.JobZone.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FJobZone%5F%5F%5FSystem%5FInt32%5F)CopyTo(JobZone\[\], int)

##### Declaration

```
public void CopyTo(JobZone[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [JobZone](DesignData.SDS2.Setup.JobZone.html)\[\]          | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FJobZone%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, JobZone\[\], int, int)

##### Declaration

```
public void CopyTo(int index, JobZone[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [JobZone](DesignData.SDS2.Setup.JobZone.html)\[\]          | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FFinalize)\~JobZoneList()

##### Declaration

```
protected ~JobZoneList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public JobZoneList.JobZoneListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                        | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [JobZoneList](DesignData.SDS2.Setup.JobZoneList.html).[JobZoneListEnumerator](DesignData.SDS2.Setup.JobZoneList.JobZoneListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public JobZoneList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [JobZoneList](DesignData.SDS2.Setup.JobZoneList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FJobZone%5F)Insert(int, JobZone)

##### Declaration

```
public void Insert(int index, JobZone x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [JobZone](DesignData.SDS2.Setup.JobZone.html)              | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FJobZoneList%5F)InsertRange(int, JobZoneList)

##### Declaration

```
public void InsertRange(int index, JobZoneList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [JobZoneList](DesignData.SDS2.Setup.JobZoneList.html)      | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FJobZone%5FSystem%5FInt32%5F)Repeat(JobZone, int)

##### Declaration

```
public static JobZoneList Repeat(JobZone value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [JobZone](DesignData.SDS2.Setup.JobZone.html)              | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [JobZoneList](DesignData.SDS2.Setup.JobZoneList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FJobZoneList%5F)SetRange(int, JobZoneList)

##### Declaration

```
public void SetRange(int index, JobZoneList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [JobZoneList](DesignData.SDS2.Setup.JobZoneList.html)      | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZoneList%5FToArray)ToArray()

##### Declaration

```
public JobZone[] ToArray()
```

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [JobZone](DesignData.SDS2.Setup.JobZone.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)