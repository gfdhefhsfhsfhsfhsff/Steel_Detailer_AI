# Class JobSequenceList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

JobSequenceList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[JobSequence](DesignData.SDS2.Setup.JobSequence.html)\>

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
public class JobSequenceList : IEnumerable<JobSequence>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5F%5Fctor)JobSequenceList()

##### Declaration

```
public JobSequenceList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FJobSequenceList%5F)JobSequenceList(JobSequenceList)

##### Declaration

```
public JobSequenceList(JobSequenceList other)
```

##### Parameters

| Type                                                          | Name  | Description |
| ------------------------------------------------------------- | ----- | ----------- |
| [JobSequenceList](DesignData.SDS2.Setup.JobSequenceList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5F%5F)JobSequenceList(IEnumerable<JobSequence>)

##### Declaration

```
public JobSequenceList(IEnumerable<JobSequence> c)
```

##### Parameters

| Type                                                                                                                                                   | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[JobSequence](DesignData.SDS2.Setup.JobSequence.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)JobSequenceList(IEnumerable)

##### Declaration

```
public JobSequenceList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5F%5Fctor%5FSystem%5FInt32%5F)JobSequenceList(int)

##### Declaration

```
public JobSequenceList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public JobSequence this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5F)Add(JobSequence)

##### Declaration

```
public void Add(JobSequence x)
```

##### Parameters

| Type                                                  | Name | Description |
| ----------------------------------------------------- | ---- | ----------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FJobSequenceList%5F)AddRange(JobSequenceList)

##### Declaration

```
public void AddRange(JobSequenceList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [JobSequenceList](DesignData.SDS2.Setup.JobSequenceList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5F%5F%5F)CopyTo(JobSequence\[\])

##### Declaration

```
public void CopyTo(JobSequence[] array)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5F%5F%5FSystem%5FInt32%5F)CopyTo(JobSequence\[\], int)

##### Declaration

```
public void CopyTo(JobSequence[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, JobSequence\[\], int, int)

##### Declaration

```
public void CopyTo(int index, JobSequence[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html)\[\]  | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FFinalize)\~JobSequenceList()

##### Declaration

```
protected ~JobSequenceList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public JobSequenceList.JobSequenceListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                            | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [JobSequenceList](DesignData.SDS2.Setup.JobSequenceList.html).[JobSequenceListEnumerator](DesignData.SDS2.Setup.JobSequenceList.JobSequenceListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public JobSequenceList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [JobSequenceList](DesignData.SDS2.Setup.JobSequenceList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5F)Insert(int, JobSequence)

##### Declaration

```
public void Insert(int index, JobSequence x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html)      | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FJobSequenceList%5F)InsertRange(int, JobSequenceList)

##### Declaration

```
public void InsertRange(int index, JobSequenceList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [JobSequenceList](DesignData.SDS2.Setup.JobSequenceList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5FSystem%5FInt32%5F)Repeat(JobSequence, int)

##### Declaration

```
public static JobSequenceList Repeat(JobSequence value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html)      | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [JobSequenceList](DesignData.SDS2.Setup.JobSequenceList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FJobSequenceList%5F)SetRange(int, JobSequenceList)

##### Declaration

```
public void SetRange(int index, JobSequenceList values)
```

##### Parameters

| Type                                                          | Name   | Description |
| ------------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)    | index  |             |
| [JobSequenceList](DesignData.SDS2.Setup.JobSequenceList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FToArray)ToArray()

##### Declaration

```
public JobSequence[] ToArray()
```

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)