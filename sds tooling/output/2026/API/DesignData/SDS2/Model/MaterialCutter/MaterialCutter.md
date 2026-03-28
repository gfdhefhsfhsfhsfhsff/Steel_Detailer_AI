# Class MaterialCutter 

Snapshot of material used to cut another material

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialCutter

##### Inherited Members

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
public sealed class MaterialCutter
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutter%5F%5Fctor)MaterialCutter()

Snapshot of material used to cut another material

##### Declaration

```
public MaterialCutter()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutter%5FSurface)Surface

Snapshot of the material used to cut another material in the local coordinate system of the material being cut

##### Declaration

```
public Surface Surface { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutter%5FToCutterMaterialCoordinates)ToCutterMaterialCoordinates

The transformation to convert the cutting poly to its original local material coordinates

##### Declaration

```
public Matrix ToCutterMaterialCoordinates { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialCutter%5FFinalize)\~MaterialCutter()

Snapshot of material used to cut another material

##### Declaration

```
protected ~MaterialCutter()
```