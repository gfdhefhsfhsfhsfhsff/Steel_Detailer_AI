# Class MaterialUsage 

A usage description for material, based on material type.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialUsage

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
public sealed class MaterialUsage
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsage%5F%5Fctor%5FSystem%5FString%5FDesignData%5FSDS2%5FSetup%5FMaterialType%5F)MaterialUsage(string, MaterialType)

Create a new material usage description with a description and applicable material type

##### Declaration

```
public MaterialUsage(string description, MaterialType materialType)
```

##### Parameters

| Type                                                           | Name         | Description |
| -------------------------------------------------------------- | ------------ | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | description  |             |
| [MaterialType](DesignData.SDS2.Setup.MaterialType.html)        | materialType |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsage%5FDescription)Description

The description for this usage

##### Declaration

```
public string Description { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsage%5FMaterialType)MaterialType

The material type this usage is applicable to

##### Declaration

```
public MaterialType MaterialType { get; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [MaterialType](DesignData.SDS2.Setup.MaterialType.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsage%5FFinalize)\~MaterialUsage()

A usage description for material, based on material type.

##### Declaration

```
protected ~MaterialUsage()
```