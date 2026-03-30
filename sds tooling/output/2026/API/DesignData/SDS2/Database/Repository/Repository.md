# Class Repository 

A place where SDS2 jobs are stored. Jobs are accessed in this repository by name.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Repository

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public sealed class Repository
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FRepository%5F%5Fctor)Repository()

A place where SDS2 jobs are stored. Jobs are accessed in this repository by name.

##### Declaration

```
public Repository()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FRepository%5FDefault)Default

This gets the default job repository for the user running your software

##### Declaration

```
public static Repository Default { get; }
```

##### Property Value

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [Repository](DesignData.SDS2.Database.Repository.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepository%5FJobIdentifiers)JobIdentifiers

A list of all the jobs in this repository.

##### Declaration

```
public IdentifierList JobIdentifiers { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [IdentifierList](DesignData.SDS2.Database.IdentifierList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepository%5FName)Name

The name of the job repository

##### Declaration

```
public string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepository%5FShadowPath)ShadowPath

The URI for this repository.

##### Declaration

```
public string ShadowPath { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FRepository%5FURL)URL

The URI for this repository.

##### Declaration

```
public string URL { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FRepository%5FFinalize)\~Repository()

A place where SDS2 jobs are stored. Jobs are accessed in this repository by name.

##### Declaration

```
protected ~Repository()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FRepository%5FGetAllRepositories)GetAllRepositories()

Return a list of all job repositories on the system. Users can have multiple repositories on various database backends.

##### Declaration

```
public static RepositoryList GetAllRepositories()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [RepositoryList](DesignData.SDS2.Database.RepositoryList.html) |             |