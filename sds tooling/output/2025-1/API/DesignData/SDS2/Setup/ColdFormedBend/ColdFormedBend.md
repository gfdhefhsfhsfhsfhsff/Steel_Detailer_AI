# Class ColdFormedBend 

Base class for the different types of cold formed bends

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ColdFormedBend

[ColdFormedBendRadiused](DesignData.SDS2.Setup.ColdFormedBendRadiused.html)

[ColdFormedBendRegular](DesignData.SDS2.Setup.ColdFormedBendRegular.html)

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
public class ColdFormedBend
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBend%5FNode)Node

Base class for the different types of cold formed bends

##### Declaration

```
public ColdFormedBendNode Node { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [ColdFormedBendNode](DesignData.SDS2.Setup.ColdFormedBendNode.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBend%5FNodeDistance)NodeDistance

The distance in inches from the face's reference node to the bend reference point

##### Declaration

```
public double NodeDistance { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBend%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base class for the different types of cold formed bends

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBend%5FFinalize)\~ColdFormedBend()

Base class for the different types of cold formed bends

##### Declaration

```
protected ~ColdFormedBend()
```