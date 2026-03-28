# Class WeldSegment 

WeldSegment represents the position and orientation in the model of a logical segment of a weld. The segment may be stitched, so the weld between the two points of the segment may not be continuous.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

WeldSegment

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
public class WeldSegment
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegment%5Fp1)p1

End point of a logical weld segment.

##### Declaration

```
public Point3D p1 { get; set; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegment%5Fp2)p2

End point of a logical weld segment.

##### Declaration

```
public Point3D p2 { get; set; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegment%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

WeldSegment represents the position and orientation in the model of a logical segment of a weld. The segment may be stitched, so the weld between the two points of the segment may not be continuous.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldSegment%5FFinalize)\~WeldSegment()

WeldSegment represents the position and orientation in the model of a logical segment of a weld. The segment may be stitched, so the weld between the two points of the segment may not be continuous.

##### Declaration

```
protected ~WeldSegment()
```