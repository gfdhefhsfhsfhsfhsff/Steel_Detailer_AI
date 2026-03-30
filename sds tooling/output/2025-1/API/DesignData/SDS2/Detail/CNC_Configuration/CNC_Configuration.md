# Class CNC\_Configuration 

CNC configuration information

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CNC\_Configuration

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Detail](DesignData.SDS2.Detail.html)

###### **Assembly**: DesignData.SDS2.Detail.dll

##### Syntax

```
public sealed class CNC_Configuration
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5F%5Fctor)CNC\_Configuration()

CNC configuration information

##### Declaration

```
public CNC_Configuration()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FName)Name

Return the name of the first CNC\_Configuration in the list.

##### Declaration

```
public string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FNames)Names

Return the name(s) of the CNC\_Configuration(s).

##### Declaration

```
public StringList Names { get; }
```

##### Property Value

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FAdd%5FDesignData%5FSDS2%5FPrimitives%5FStringList%5F)Add(StringList)

Add new CNC Configurations

##### Declaration

```
public void Add(StringList configurations)
```

##### Parameters

| Type                                                     | Name           | Description |
| -------------------------------------------------------- | -------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) | configurations |             |

##### Exceptions

| Type                                                                           | Condition                                                                          |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the name does not match any configuration. |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FDownloadMaterials%5FDesignData%5FSDS2%5FPrimitives%5FStringList%5FSystem%5FString%5F)DownloadMaterials(StringList, string)

Generate CNC files for the specified submaterial marks and save them to the specified destination path.

```
         The destination path should be a directory, if it does not exist
         we will attempt to create it.  The parent of the directory must
         already exist.

```

##### Declaration

```
public void DownloadMaterials(StringList material_marks, string destination_path)
```

##### Parameters

| Type                                                           | Name              | Description |
| -------------------------------------------------------------- | ----------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html)       | material\_marks   |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | destination\_path |             |

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html)         | InvalidValueException will be thrown the configuration is not active.                                                                                                                                                      |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | InvalidOperationException will be thrown if CNC is unlicensed or not permitted in the station. Or if the output path already exists as a file (not a directory), or if the directory doesn't exist and we can't create it. |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FDownloadMembers%5FDesignData%5FSDS2%5FPrimitives%5FStringList%5FSystem%5FString%5F)DownloadMembers(StringList, string)

Generate CNC files for the specified member marks and save them to the specified destination path.

```
         The destination path should be a directory, if it does not exist
         we will attempt to create it.  The parent of the directory must
         already exist.

```

##### Declaration

```
public void DownloadMembers(StringList member_marks, string destination_path)
```

##### Parameters

| Type                                                           | Name              | Description |
| -------------------------------------------------------------- | ----------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html)       | member\_marks     |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | destination\_path |             |

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html)         | InvalidValueException will be thrown the configuration is not active.                                                                                                                                                      |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | InvalidOperationException will be thrown if CNC is unlicensed or not permitted in the station. Or if the output path already exists as a file (not a directory), or if the directory doesn't exist and we can't create it. |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FFinalize)\~CNC\_Configuration()

CNC configuration information

##### Declaration

```
protected ~CNC_Configuration()
```

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FFind%5FDesignData%5FSDS2%5FPrimitives%5FStringList%5F)Find(StringList)

Return the configuration(s) with the specified name(s).

##### Declaration

```
public static CNC_Configuration Find(StringList configurations)
```

##### Parameters

| Type                                                     | Name           | Description |
| -------------------------------------------------------- | -------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) | configurations |             |

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                          |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the name does not match any configuration. |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FFind%5FSystem%5FString%5F)Find(string)

Return the configuration with the specified name.

##### Declaration

```
public static CNC_Configuration Find(string configurations)
```

##### Parameters

| Type                                                           | Name           | Description |
| -------------------------------------------------------------- | -------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | configurations |             |

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                          |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the name does not match any configuration. |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FGetConfigurations)GetConfigurations()

Return all the configurations defined in the job.

##### Declaration

```
public CNC_Configuration GetConfigurations()
```

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfiguration%5FRemove%5FDesignData%5FSDS2%5FPrimitives%5FStringList%5F)Remove(StringList)

Remove CNC Configurations

##### Declaration

```
public void Remove(StringList configurations)
```

##### Parameters

| Type                                                     | Name           | Description |
| -------------------------------------------------------- | -------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) | configurations |             |

##### Exceptions

| Type                                                                           | Condition                                                                          |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the name does not match any configuration. |