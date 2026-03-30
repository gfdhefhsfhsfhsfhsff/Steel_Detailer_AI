# Class WeldProfileFillet 

WeldProfileFillet represents the profile of a fillet weld and can be used to generate the WeldPathSegment for a given weld size.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

WeldProfileFillet

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
public sealed class WeldProfileFillet
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FWeldProfileFillet%5F%5Fctor)WeldProfileFillet()

WeldProfileFillet represents the profile of a fillet weld and can be used to generate the WeldPathSegment for a given weld size.

##### Declaration

```
public WeldProfileFillet()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWeldProfileFillet%5FLengthDirection)LengthDirection

Direction of the length of the profile, i.e. ToToe2.Cross(ToToe1)

##### Declaration

```
public Vector3D LengthDirection { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldProfileFillet%5FRoot)Root

Location of the fillet weld root

##### Declaration

```
public Point3D Root { get; set; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldProfileFillet%5FSurfaceNormal1)SurfaceNormal1

The the normal direction of the surface where the first toe sits

##### Declaration

```
public Vector3D SurfaceNormal1 { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldProfileFillet%5FSurfaceNormal2)SurfaceNormal2

The the normal direction of the surface where the second toe sits

##### Declaration

```
public Vector3D SurfaceNormal2 { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldProfileFillet%5FToToe1)ToToe1

Direction from the root to the first toe

##### Declaration

```
public Vector3D ToToe1 { get; set; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldProfileFillet%5FToToe2)ToToe2

Direction from the root to the second toe

##### Declaration

```
public Vector3D ToToe2 { get; set; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWeldProfileFillet%5FFinalize)\~WeldProfileFillet()

WeldProfileFillet represents the profile of a fillet weld and can be used to generate the WeldPathSegment for a given weld size.

##### Declaration

```
protected ~WeldProfileFillet()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldProfileFillet%5FFromPlanes%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5F)FromPlanes(Point3D, Vector3D, Point3D, Vector3D)

Return a WeldProfileFillet for the intersection of two surface planes

##### Declaration

```
public static WeldProfileFillet FromPlanes(Point3D pointOnPlane1, Vector3D surfaceNormal1, Point3D pointOnPlane2, Vector3D surfaceNormal2)
```

##### Parameters

| Type                                                 | Name           | Description |
| ---------------------------------------------------- | -------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)   | pointOnPlane1  |             |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) | surfaceNormal1 |             |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)   | pointOnPlane2  |             |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) | surfaceNormal2 |             |

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [WeldProfileFillet](DesignData.SDS2.Model.WeldProfileFillet.html) |             |

##### Remarks

The surface planes should intersect in a line and the resulting WeldProfileFillet's Root will be a point on the line closest to pointOnPlane1\. If the planes do not intersect in a line then the resulting ToToe vectors will be zero vectors

#### [](#DesignData%5FSDS2%5FModel%5FWeldProfileFillet%5FGetWeldPathSegment%5FSystem%5FDouble%5FSystem%5FDouble%5F)GetWeldPathSegment(double, double)

Return a WeldPathSegment for corresponding to the profile and the given segmentLength and weldSize

##### Declaration

```
public WeldPathSegment GetWeldPathSegment(double segmentLength, double weldSize)
```

##### Parameters

| Type                                                           | Name          | Description |
| -------------------------------------------------------------- | ------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | segmentLength |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | weldSize      |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                           |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown if the cross product of the profile toes is the zero vector. |