# Class PythonComponent 

A component implemented in python

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Component](DesignData.SDS2.Model.Component.html)

PythonComponent

[StairConnection](DesignData.SDS2.Model.StairConnection.html)

##### Inherited Members

[Component.Handle](DesignData.SDS2.Model.Component.html#DesignData%5FSDS2%5FModel%5FComponent%5FHandle) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class PythonComponent : Component
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FPythonComponent%5FPythonObject)PythonObject

The underlying python object for this component. Use this object with the "dynamic" type in csharp.

##### Declaration

```
public dynamic PythonObject { get; }
```

##### Property Value

| Type    | Description |
| ------- | ----------- |
| dynamic |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FPythonComponent%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A component implemented in python

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[Component.Dispose(bool)](DesignData.SDS2.Model.Component.html#DesignData%5FSDS2%5FModel%5FComponent%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FModel%5FPythonComponent%5FFindCreatedMaterial)FindCreatedMaterial()

Returns an object containing three lists, Materials, Bolts, Welds that a connection created.

##### Declaration

```
public override CreatedConnectionMaterial FindCreatedMaterial()
```

##### Returns

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [CreatedConnectionMaterial](DesignData.SDS2.Model.CreatedConnectionMaterial.html) |             |

##### Overrides

[Component.FindCreatedMaterial()](DesignData.SDS2.Model.Component.html#DesignData%5FSDS2%5FModel%5FComponent%5FFindCreatedMaterial)