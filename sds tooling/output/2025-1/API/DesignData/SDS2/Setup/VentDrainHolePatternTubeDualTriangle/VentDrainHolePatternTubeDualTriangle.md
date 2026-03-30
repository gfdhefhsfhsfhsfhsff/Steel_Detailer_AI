# Class VentDrainHolePatternTubeDualTriangle 

Just like VentDrainHolePatternTubeQuadTriangle, except only two triangles are cut out. One on the top left and bottom right, unless FlipCorners and then it's the other two corners

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[VentDrainHolePattern](DesignData.SDS2.Setup.VentDrainHolePattern.html)

[VentDrainHolePatternTube](DesignData.SDS2.Setup.VentDrainHolePatternTube.html)

VentDrainHolePatternTubeDualTriangle

##### Inherited Members

[VentDrainHolePatternTube.TubeCornerRadius](DesignData.SDS2.Setup.VentDrainHolePatternTube.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTube%5FTubeCornerRadius) 

[VentDrainHolePatternTube.TubeInnerWidth](DesignData.SDS2.Setup.VentDrainHolePatternTube.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTube%5FTubeInnerWidth) 

[VentDrainHolePatternTube.TubeInnerLength](DesignData.SDS2.Setup.VentDrainHolePatternTube.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTube%5FTubeInnerLength) 

[VentDrainHolePattern.GetShape()](DesignData.SDS2.Setup.VentDrainHolePattern.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FGetShape) 

[VentDrainHolePattern.PlateRotation](DesignData.SDS2.Setup.VentDrainHolePattern.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FPlateRotation) 

[VentDrainHolePattern.OffsetParallelToWeb](DesignData.SDS2.Setup.VentDrainHolePattern.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FOffsetParallelToWeb) 

[VentDrainHolePattern.OffsetParallelToFlange](DesignData.SDS2.Setup.VentDrainHolePattern.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FOffsetParallelToFlange) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class VentDrainHolePatternTubeDualTriangle : VentDrainHolePatternTube
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTubeDualTriangle%5FFlipCorners)FlipCorners

Flips which corners are clipped

##### Declaration

```
public bool FlipCorners { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTubeDualTriangle%5FTriangleLegLength)TriangleLegLength

The leg length of these clipped triangles. The triangles are at least isosceles and sometimes equilateral. With sides always equal along the tube walls.

##### Declaration

```
public double TriangleLegLength { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTubeDualTriangle%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Just like VentDrainHolePatternTubeQuadTriangle, except only two triangles are cut out. One on the top left and bottom right, unless FlipCorners and then it's the other two corners

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[VentDrainHolePatternTube.Dispose(bool)](DesignData.SDS2.Setup.VentDrainHolePatternTube.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTube%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTubeDualTriangle%5FEquals%5FSystem%5FObject%5F)Equals(object)

Just like VentDrainHolePatternTubeQuadTriangle, except only two triangles are cut out. One on the top left and bottom right, unless FlipCorners and then it's the other two corners

##### Declaration

```
public override bool Equals(object other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | other |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[VentDrainHolePatternTube.Equals(object)](DesignData.SDS2.Setup.VentDrainHolePatternTube.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTube%5FEquals%5FSystem%5FObject%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTubeDualTriangle%5FGetHashCode)GetHashCode()

Just like VentDrainHolePatternTubeQuadTriangle, except only two triangles are cut out. One on the top left and bottom right, unless FlipCorners and then it's the other two corners

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[VentDrainHolePatternTube.GetHashCode()](DesignData.SDS2.Setup.VentDrainHolePatternTube.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternTube%5FGetHashCode)