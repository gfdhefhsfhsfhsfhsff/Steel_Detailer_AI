# Class CutLayout 

Cut layout material operation

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)

CutLayout

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
public sealed class CutLayout : MaterialOperation
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FCutLayout%5FLayout)Layout

A layout describing a planar area to be cut

##### Declaration

```
public Layout3D Layout { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Layout3D](DesignData.SDS2.Primitives.Layout3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCutLayout%5FToCuttingBottomFace)ToCuttingBottomFace

Cut layout material operation

##### Declaration

```
public Vector3D ToCuttingBottomFace { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCutLayout%5FToCuttingTopFace)ToCuttingTopFace

Cut layout material operation

##### Declaration

```
public Vector3D ToCuttingTopFace { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |