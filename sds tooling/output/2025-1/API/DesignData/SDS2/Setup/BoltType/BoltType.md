# Class BoltType 

Base class for bolt type setup information

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BoltType

[BoltTypeAISC14](DesignData.SDS2.Setup.BoltTypeAISC14.html)

[BoltTypeAISC15](DesignData.SDS2.Setup.BoltTypeAISC15.html)

[BoltTypeASD9](DesignData.SDS2.Setup.BoltTypeASD9.html)

[BoltTypeAustralia](DesignData.SDS2.Setup.BoltTypeAustralia.html)

[BoltTypeCanada](DesignData.SDS2.Setup.BoltTypeCanada.html)

[BoltTypeChina](DesignData.SDS2.Setup.BoltTypeChina.html)

[BoltTypeEuro](DesignData.SDS2.Setup.BoltTypeEuro.html)

[BoltTypeIndia](DesignData.SDS2.Setup.BoltTypeIndia.html)

[BoltTypeLRFD13](DesignData.SDS2.Setup.BoltTypeLRFD13.html)

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
public class BoltType
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBoltType%5FDescription)Description

This string is now the bolt type is named in the user interface.

##### Declaration

```
public string Description { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltType%5FFrictionBearing)FrictionBearing

Base class for bolt type setup information

##### Declaration

```
public FrictionBearingType FrictionBearing { get; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [FrictionBearingType](DesignData.SDS2.Setup.FrictionBearingType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltType%5FMaterial)Material

The bolt material

##### Declaration

```
public string Material { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBoltType%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base class for bolt type setup information

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltType%5FFinalize)\~BoltType()

Base class for bolt type setup information

##### Declaration

```
protected ~BoltType()
```