# Class FitMitre 

Fit mitre material operation

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)

FitMitre

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
public sealed class FitMitre : MaterialOperation
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FFitMitre%5FClearance)Clearance

The clearance used in the mitre operation

##### Declaration

```
public double Clearance { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FFitMitre%5FMitrers)Mitrers

All the materials involved in the operation

##### Declaration

```
public MaterialMitrerList Mitrers { get; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [MaterialMitrerList](DesignData.SDS2.Model.MaterialMitrerList.html) |             |