# Class JobSequence 

Represents one fabrication sequence in the job.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

JobSequence

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class JobSequence
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequence%5F%5Fctor)JobSequence()

Create an undefined fabrication sequence. This will need to be added to the job to be useful.

##### Declaration

```
public JobSequence()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequence%5FName)Name

The user visible name of this sequence

##### Declaration

```
public string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Exceptions

| Type                                                                             | Condition                                                                                           |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [InvalidHandleException](DesignData.SDS2.Exceptions.InvalidHandleException.html) | If the sequence referenced is no longer valid. This generally means this object has become corrupt. |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequence%5FZone)Zone

The zone this sequence is in

##### Declaration

```
public JobZone Zone { get; }
```

##### Property Value

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [JobZone](DesignData.SDS2.Setup.JobZone.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequence%5FEquals%5FSystem%5FObject%5F)Equals(object)

Represents one fabrication sequence in the job.

##### Declaration

```
public override bool Equals(object other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | other |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequence%5FFinalize)\~JobSequence()

Represents one fabrication sequence in the job.

##### Declaration

```
protected ~JobSequence()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequence%5FGetHashCode)GetHashCode()

Represents one fabrication sequence in the job.

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequence%5Fop%5FEquality%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5F)operator ==(JobSequence, JobSequence)

Represents one fabrication sequence in the job.

##### Declaration

```
public static bool operator ==(JobSequence a, JobSequence b)
```

##### Parameters

| Type                                                  | Name | Description |
| ----------------------------------------------------- | ---- | ----------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html) | a    |             |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobSequence%5Fop%5FInequality%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5FDesignData%5FSDS2%5FSetup%5FJobSequence%5F)operator !=(JobSequence, JobSequence)

Represents one fabrication sequence in the job.

##### Declaration

```
public static bool operator !=(JobSequence a, JobSequence b)
```

##### Parameters

| Type                                                  | Name | Description |
| ----------------------------------------------------- | ---- | ----------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html) | a    |             |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |