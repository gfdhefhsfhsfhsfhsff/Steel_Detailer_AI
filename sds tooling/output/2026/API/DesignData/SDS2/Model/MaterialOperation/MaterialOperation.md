# Class MaterialOperation 

The abstract base class of all saved material operations. Points and vectors are specified in the material's local coordinate system unless otherwise noted

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialOperation

[ChamferEdge](DesignData.SDS2.Model.ChamferEdge.html)

[ChamferPointToPoint](DesignData.SDS2.Model.ChamferPointToPoint.html)

[CutLayout](DesignData.SDS2.Model.CutLayout.html)

[CutOnPlane](DesignData.SDS2.Model.CutOnPlane.html)

[FitMitre](DesignData.SDS2.Model.FitMitre.html)

[MaterialFit](DesignData.SDS2.Model.MaterialFit.html)

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
public class MaterialOperation
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperation%5FDescription)Description

A user facing description of the operation

##### Declaration

```
public string Description { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperation%5FRemovedSurfaces)RemovedSurfaces

The parts of the material that were removed due to the operation. These are typically displayed when the operation is selected

##### Declaration

```
public SurfaceList RemovedSurfaces { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [SurfaceList](DesignData.SDS2.Primitives.SurfaceList.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperation%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

The abstract base class of all saved material operations. Points and vectors are specified in the material's local coordinate system unless otherwise noted

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperation%5FFinalize)\~MaterialOperation()

The abstract base class of all saved material operations. Points and vectors are specified in the material's local coordinate system unless otherwise noted

##### Declaration

```
protected ~MaterialOperation()
```