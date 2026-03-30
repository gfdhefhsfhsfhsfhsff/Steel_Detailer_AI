# Class CutOnPlane 

A MaterialOperation that represents cutting a material by a plane

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)

CutOnPlane

##### Inherited Members

[MaterialOperation.Description](DesignData.SDS2.Model.MaterialOperation.html#DesignData%5FSDS2%5FModel%5FMaterialOperation%5FDescription) 

[MaterialOperation.RemovedSurfaces](DesignData.SDS2.Model.MaterialOperation.html#DesignData%5FSDS2%5FModel%5FMaterialOperation%5FRemovedSurfaces) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public sealed class CutOnPlane : MaterialOperation
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FCutOnPlane%5FPlaneNormalVector)PlaneNormalVector

a vector pointing towards the half space of the plane that is kept after the cut operation

##### Declaration

```
public Vector3D PlaneNormalVector { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCutOnPlane%5FPoint1)Point1

A point on the cut plane

##### Declaration

```
public Point3D Point1 { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |