# Class MaterialDescriptions 

Default material descriptions, based on member type, from fabricator setup

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialDescriptions

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
public class MaterialDescriptions
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FBeam)Beam

Default description for a beam

##### Declaration

```
public string Beam { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FColumn)Column

Default description for a column

##### Declaration

```
public string Column { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FGirt)Girt

Default description for a girt

##### Declaration

```
public string Girt { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FGroupMember)GroupMember

Default description for a group member

##### Declaration

```
public string GroupMember { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FHorizontalBrace)HorizontalBrace

Default description for a horizontal brace

##### Declaration

```
public string HorizontalBrace { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FMiscellaneous)Miscellaneous

Available default descriptions for miscellaneous members.

##### Declaration

```
public StringList Miscellaneous { get; }
```

##### Property Value

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FPurlin)Purlin

Default description for a purlin

##### Declaration

```
public string Purlin { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FStair)Stair

Default description for a stair

##### Declaration

```
public string Stair { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FVerticalBrace)VerticalBrace

Default description for a vertical brace

##### Declaration

```
public string VerticalBrace { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FAddMiscellaneous%5FSystem%5FString%5F)AddMiscellaneous(string)

Add a new miscellaneous description to the list returned by the Miscellaneous property

##### Declaration

```
public void AddMiscellaneous(string description)
```

##### Parameters

| Type                                                           | Name        | Description |
| -------------------------------------------------------------- | ----------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | description |             |

##### Remarks

You will need to have added the fabricator to the transaction to do this

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Default material descriptions, based on member type, from fabricator setup

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialDescriptions%5FFinalize)\~MaterialDescriptions()

Default material descriptions, based on member type, from fabricator setup

##### Declaration

```
protected ~MaterialDescriptions()
```