# Class WeldPathSegment 

Represents the orientation and length of one segment of a WeldPathSpecification.Segments

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

WeldPathSegment

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
public sealed class WeldPathSegment
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegment%5F%5Fctor)WeldPathSegment()

Represents the orientation and length of one segment of a WeldPathSpecification.Segments

##### Declaration

```
public WeldPathSegment()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegment%5FLength)Length

The length of the weld segment

##### Declaration

```
public double Length { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegment%5FToFilletRoot)ToFilletRoot

Defines the direction of toe1 to the root for fillet welds

##### Declaration

```
public Vector3D ToFilletRoot { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html) |             |

##### Remarks

Fillet welds should use FromFilletLayout(), FromFilletSegment(), or WeldProfileFillet.GetWeldPathSegment() to set this value appropriately

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegment%5FToGlobalCoordinates)ToGlobalCoordinates

The segment's transformation matrix from local coordinates to global coordinates. The X axis of a weld segment is is the direction from one end of the segment to the other end. The Y axis is the direction from the first toe to the second toe. For bevel welds, the Z axis is the direction from the first toe towards the root. Fillet welds ignore the Z axis and instead use ToFilletRoot. The translation portion of the matrix represents a point on the face of the weld. For fillet and groove welds this is toe1\. For U and V groove welds this is the midpoint between toes on the face of the weld.

##### Declaration

```
public Matrix ToGlobalCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Remarks

See WeldProfileFillet for an alternative representation that may be more useful for fillet welds

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegment%5FFinalize)\~WeldPathSegment()

Represents the orientation and length of one segment of a WeldPathSpecification.Segments

##### Declaration

```
protected ~WeldPathSegment()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegment%5FFromFilletLayout%5FDesignData%5FSDS2%5FPrimitives%5FLayout3D%5FSystem%5FDouble%5F)FromFilletLayout(Layout3D, double)

Return a list of WeldPathSegment objects that represent the fillet weld layout

##### Declaration

```
public static WeldPathSegmentList FromFilletLayout(Layout3D layout, double weldSize)
```

##### Parameters

| Type                                                           | Name     | Description |
| -------------------------------------------------------------- | -------- | ----------- |
| [Layout3D](DesignData.SDS2.Primitives.Layout3D.html)           | layout   |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | weldSize |             |

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html) |             |

##### Remarks

This will create welds where the root runs along the layout nodes which is useful for fillet welds. It is less useful for butt welds when you want the toe to run along the layout nodes. See FromLayout for butt welds

##### Exceptions

| Type                                                                           | Condition                                                                                                                       |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown when the cross product of the vector between end points of any segment and the depth vector for those end points is zero |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegment%5FFromFilletSegment%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FDesignData%5FSDS2%5FPrimitives%5FPoint3D%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5FDesignData%5FSDS2%5FPrimitives%5FVector3D%5FSystem%5FDouble%5F)FromFilletSegment(Point3D, Point3D, Vector3D, Vector3D, double)

Return a WeldPathSegment given the segment end points and two normals of the the surfaces to fillet weld

##### Declaration

```
public static WeldPathSegment FromFilletSegment(Point3D segmentEndPoint1, Point3D segmentEndPoint2, Vector3D surfaceNormal1, Vector3D surfaceNormal2, double weldSize)
```

##### Parameters

| Type                                                           | Name             | Description |
| -------------------------------------------------------------- | ---------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)             | segmentEndPoint1 |             |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html)             | segmentEndPoint2 |             |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html)           | surfaceNormal1   |             |
| [Vector3D](DesignData.SDS2.Primitives.Vector3D.html)           | surfaceNormal2   |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | weldSize         |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                      |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown when the cross product of the profile toes is the zero. |

#### [](#DesignData%5FSDS2%5FModel%5FWeldPathSegment%5FFromLayout%5FDesignData%5FSDS2%5FPrimitives%5FLayout3D%5F)FromLayout(Layout3D)

Return a list of WeldPathSegment objects that represent the layout

##### Declaration

```
public static WeldPathSegmentList FromLayout(Layout3D layout)
```

##### Parameters

| Type                                                 | Name   | Description |
| ---------------------------------------------------- | ------ | ----------- |
| [Layout3D](DesignData.SDS2.Primitives.Layout3D.html) | layout |             |

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html) |             |

##### Remarks

This will create welds where the toe runs along the layout nodes which is useful for butt welds. It is not useful for fillet welds when you want the root to run along the layout nodes. See FromFilletLayout for a fillet weld layout

##### Exceptions

| Type                                                                           | Condition                                                                                                                       |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown when the cross product of the vector between end points of any segment and the depth vector for those end points is zero |