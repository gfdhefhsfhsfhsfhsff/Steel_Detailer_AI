# Class NamedColor 

A named color available to use for materials in the model. These colors are chosen by users by Description, but result in the HexColor.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

NamedColor

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
public class NamedColor
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColor%5FDescription)Description

Returns a string containing the description(name) for each associated color.

##### Declaration

```
public string Description { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColor%5FHexColor)HexColor

Returns a string containing the hex value of a color.

##### Declaration

```
public string HexColor { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColor%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A named color available to use for materials in the model. These colors are chosen by users by Description, but result in the HexColor.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColor%5FFinalize)\~NamedColor()

A named color available to use for materials in the model. These colors are chosen by users by Description, but result in the HexColor.

##### Declaration

```
protected ~NamedColor()
```