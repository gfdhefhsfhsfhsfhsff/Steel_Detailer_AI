# Class DataDirectory 

Before jobs can be accessed or job repositories can be listed you must choose a data directory. It contains needed setup data for SDS2.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DataDirectory

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
public sealed class DataDirectory
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FDataDirectory%5F%5Fctor)DataDirectory()

Before jobs can be accessed or job repositories can be listed you must choose a data directory. It contains needed setup data for SDS2.

##### Declaration

```
public DataDirectory()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FDataDirectory%5FDefault)Default

The current default data directory, to be passed to DataDirectory.Open

##### Declaration

```
public static string Default { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

If no valid data directory can be found, this will return an empty string.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FDataDirectory%5FFinalize)\~DataDirectory()

Before jobs can be accessed or job repositories can be listed you must choose a data directory. It contains needed setup data for SDS2.

##### Declaration

```
protected ~DataDirectory()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FDataDirectory%5FOpen%5FSystem%5FString%5F)Open(string)

Make this the current data directory in this process. This must be done before you can list job repositories.

##### Declaration

```
public static bool Open(string directory)
```

##### Parameters

| Type                                                           | Name      | Description |
| -------------------------------------------------------------- | --------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | directory |             |

##### Returns

| Type                                                          | Description                                                       |
| ------------------------------------------------------------- | ----------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | true if the job is open, false if we were unable to open the job. |