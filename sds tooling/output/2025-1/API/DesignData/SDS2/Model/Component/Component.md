# Class Component 

Base class for components on members

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Component

[ConnectionComponent](DesignData.SDS2.Model.ConnectionComponent.html)

[PythonComponent](DesignData.SDS2.Model.PythonComponent.html)

##### Inherited Members

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
public class Component
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FComponent%5FHandle)Handle

The handle for this component

##### Declaration

```
public ComponentHandle Handle { get; }
```

##### Property Value

| Type                                                             | Description |
| ---------------------------------------------------------------- | ----------- |
| [ComponentHandle](DesignData.SDS2.Database.ComponentHandle.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FComponent%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base class for components on members

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponent%5FFinalize)\~Component()

Base class for components on members

##### Declaration

```
protected ~Component()
```

#### [](#DesignData%5FSDS2%5FModel%5FComponent%5FFindCreatedMaterial)FindCreatedMaterial()

Returns an object containing three lists, Materials, Bolts, Welds that a connection created.  
This is the base virtual fucntion that returns an empty object.

##### Declaration

```
public virtual CreatedConnectionMaterial FindCreatedMaterial()
```

##### Returns

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [CreatedConnectionMaterial](DesignData.SDS2.Model.CreatedConnectionMaterial.html) |             |