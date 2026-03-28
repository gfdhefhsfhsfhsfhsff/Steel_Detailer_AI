# Class MaterialFit 

Base class for various fit operations

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)

MaterialFit

[FitCope](DesignData.SDS2.Model.FitCope.html)

[FitExact](DesignData.SDS2.Model.FitExact.html)

[FitNotch](DesignData.SDS2.Model.FitNotch.html)

##### Inherited Members

[MaterialOperation.Description](DesignData.SDS2.Model.MaterialOperation.html#DesignData%5FSDS2%5FModel%5FMaterialOperation%5FDescription) 

[MaterialOperation.RemovedSurfaces](DesignData.SDS2.Model.MaterialOperation.html#DesignData%5FSDS2%5FModel%5FMaterialOperation%5FRemovedSurfaces) 

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
public class MaterialFit : MaterialOperation
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialFit%5FClearance)Clearance

The clearance used in the fit operation

##### Declaration

```
public double Clearance { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialFit%5FCutters)Cutters

All the cutters involved in the operation

##### Declaration

```
public MaterialCutterList Cutters { get; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [MaterialCutterList](DesignData.SDS2.Model.MaterialCutterList.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialFit%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base class for various fit operations

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[MaterialOperation.Dispose(bool)](DesignData.SDS2.Model.MaterialOperation.html#DesignData%5FSDS2%5FModel%5FMaterialOperation%5FDispose%5FSystem%5FBoolean%5F)