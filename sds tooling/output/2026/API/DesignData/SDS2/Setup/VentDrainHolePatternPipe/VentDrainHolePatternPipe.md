# Class VentDrainHolePatternPipe 

Base class for all pipe vent drain hole patterns

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[VentDrainHolePattern](DesignData.SDS2.Setup.VentDrainHolePattern.html)

VentDrainHolePatternPipe

[VentDrainHolePatternPipeCrossSlot](DesignData.SDS2.Setup.VentDrainHolePatternPipeCrossSlot.html)

[VentDrainHolePatternPipeDualPie](DesignData.SDS2.Setup.VentDrainHolePatternPipeDualPie.html)

[VentDrainHolePatternPipeHalfCircles](DesignData.SDS2.Setup.VentDrainHolePatternPipeHalfCircles.html)

[VentDrainHolePatternPipeOvals](DesignData.SDS2.Setup.VentDrainHolePatternPipeOvals.html)

[VentDrainHolePatternPipePlain](DesignData.SDS2.Setup.VentDrainHolePatternPipePlain.html)

[VentDrainHolePatternPipeSlot](DesignData.SDS2.Setup.VentDrainHolePatternPipeSlot.html)

[VentDrainHolePatternPipeWhole](DesignData.SDS2.Setup.VentDrainHolePatternPipeWhole.html)

##### Inherited Members

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
public class VentDrainHolePatternPipe : VentDrainHolePattern
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipe%5FPipeInnerDiameter)PipeInnerDiameter

The inner diameter of the pipe to line up vent drain holes. This is generally pulled from the material file (Shape) information for the section size (Shape) used, but it can be varied by the user.

##### Declaration

```
public double PipeInnerDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipe%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base class for all pipe vent drain hole patterns

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[VentDrainHolePattern.Dispose(bool)](DesignData.SDS2.Setup.VentDrainHolePattern.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipe%5FEquals%5FSystem%5FObject%5F)Equals(object)

Base class for all pipe vent drain hole patterns

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

[VentDrainHolePattern.Equals(object)](DesignData.SDS2.Setup.VentDrainHolePattern.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FEquals%5FSystem%5FObject%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipe%5FGetHashCode)GetHashCode()

Base class for all pipe vent drain hole patterns

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[VentDrainHolePattern.GetHashCode()](DesignData.SDS2.Setup.VentDrainHolePattern.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FGetHashCode)