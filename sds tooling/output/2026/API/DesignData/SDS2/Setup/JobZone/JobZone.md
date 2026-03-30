# Class JobZone 

A zone in a job is a named set of sequences

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

JobZone

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class JobZone
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FJobZone%5FIndex)Index

The zone index value, may be needed in some cases

##### Declaration

```
public int Index { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZone%5FName)Name

The name of this zone

##### Declaration

```
public string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZone%5FSequences)Sequences

The list of sequences in this zone

##### Declaration

```
public JobSequenceList Sequences { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [JobSequenceList](DesignData.SDS2.Setup.JobSequenceList.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FJobZone%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A zone in a job is a named set of sequences

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZone%5FEquals%5FSystem%5FObject%5F)Equals(object)

A zone in a job is a named set of sequences

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

#### [](#DesignData%5FSDS2%5FSetup%5FJobZone%5FFinalize)\~JobZone()

A zone in a job is a named set of sequences

##### Declaration

```
protected ~JobZone()
```

#### [](#DesignData%5FSDS2%5FSetup%5FJobZone%5FGetHashCode)GetHashCode()

A zone in a job is a named set of sequences

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

#### [](#DesignData%5FSDS2%5FSetup%5FJobZone%5Fop%5FEquality%5FDesignData%5FSDS2%5FSetup%5FJobZone%5FDesignData%5FSDS2%5FSetup%5FJobZone%5F)operator ==(JobZone, JobZone)

A zone in a job is a named set of sequences

##### Declaration

```
public static bool operator ==(JobZone a, JobZone b)
```

##### Parameters

| Type                                          | Name | Description |
| --------------------------------------------- | ---- | ----------- |
| [JobZone](DesignData.SDS2.Setup.JobZone.html) | a    |             |
| [JobZone](DesignData.SDS2.Setup.JobZone.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FJobZone%5Fop%5FInequality%5FDesignData%5FSDS2%5FSetup%5FJobZone%5FDesignData%5FSDS2%5FSetup%5FJobZone%5F)operator !=(JobZone, JobZone)

A zone in a job is a named set of sequences

##### Declaration

```
public static bool operator !=(JobZone a, JobZone b)
```

##### Parameters

| Type                                          | Name | Description |
| --------------------------------------------- | ---- | ----------- |
| [JobZone](DesignData.SDS2.Setup.JobZone.html) | a    |             |
| [JobZone](DesignData.SDS2.Setup.JobZone.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |