# Class JobSequenceList.JobSequenceListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

JobSequenceList.JobSequenceListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[JobSequence](DesignData.SDS2.Setup.JobSequence.html)\>

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator)

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class JobSequenceList.JobSequenceListEnumerator : IEnumerator<JobSequence>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FJobSequenceListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FJobSequenceList%5F)JobSequenceListEnumerator(JobSequenceList)

##### Declaration

```
public JobSequenceListEnumerator(JobSequenceList collection)
```

##### Parameters

| Type                                                          | Name       | Description |
| ------------------------------------------------------------- | ---------- | ----------- |
| [JobSequenceList](DesignData.SDS2.Setup.JobSequenceList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FJobSequenceListEnumerator%5FCurrent)Current

##### Declaration

```
public JobSequence Current { get; }
```

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FJobSequenceListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FJobSequenceListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequenceList%5FJobSequenceListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)