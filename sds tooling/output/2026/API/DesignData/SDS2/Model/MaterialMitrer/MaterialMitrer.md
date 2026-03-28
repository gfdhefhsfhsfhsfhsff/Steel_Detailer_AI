# Class MaterialMitrer 

Snapshot of material used to mitre another material

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialMitrer

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
public sealed class MaterialMitrer
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialMitrer%5FLength)Length

The length of the material if it applies, e.g., plates.

##### Declaration

```
public double Length { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialMitrer%5FMaterialType)MaterialType

The material type of the material.

##### Declaration

```
public MaterialType MaterialType { get; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [MaterialType](DesignData.SDS2.Setup.MaterialType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialMitrer%5FOrigin)Origin

The origin of the material if it applies; see \* DesignData.SDS2.Model.ThicknessReferencePoint.

##### Declaration

```
public int Origin { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialMitrer%5FSurface)Surface

A polygon used to mitre a material. NOTE: this poly is not in the coordinate system of the material being mitred which is different from most data related to material operations. This poly is in the local coordinate of the cutting material

##### Declaration

```
public Surface Surface { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialMitrer%5FThickness)Thickness

The thickness of the material if it applies, e.g., plates.

##### Declaration

```
public double Thickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialMitrer%5FToGlobalCoordinates)ToGlobalCoordinates

The transformation matrix taking poly to global coordinates

##### Declaration

```
public Matrix ToGlobalCoordinates { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialMitrer%5FFinalize)\~MaterialMitrer()

Snapshot of material used to mitre another material

##### Declaration

```
protected ~MaterialMitrer()
```