# Class VentDrainHolePatternPipeSlot 

Similar to a whole pattern, but leaves a slot of the base plate intact within the inner diameter of the pipe.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[VentDrainHolePattern](DesignData.SDS2.Setup.VentDrainHolePattern.html)

[VentDrainHolePatternPipe](DesignData.SDS2.Setup.VentDrainHolePatternPipe.html)

VentDrainHolePatternPipeSlot

##### Inherited Members

[VentDrainHolePatternPipe.PipeInnerDiameter](DesignData.SDS2.Setup.VentDrainHolePatternPipe.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipe%5FPipeInnerDiameter) 

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
public class VentDrainHolePatternPipeSlot : VentDrainHolePatternPipe
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipeSlot%5FPatternRotation)PatternRotation

The rotation of the slot. 0 is a slot along the Y axis of the base cap plate.

##### Declaration

```
public double PatternRotation { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipeSlot%5FSlotWidth)SlotWidth

The width of the slot

##### Declaration

```
public double SlotWidth { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipeSlot%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Similar to a whole pattern, but leaves a slot of the base plate intact within the inner diameter of the pipe.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[VentDrainHolePatternPipe.Dispose(bool)](DesignData.SDS2.Setup.VentDrainHolePatternPipe.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipe%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipeSlot%5FEquals%5FSystem%5FObject%5F)Equals(object)

Similar to a whole pattern, but leaves a slot of the base plate intact within the inner diameter of the pipe.

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

[VentDrainHolePatternPipe.Equals(object)](DesignData.SDS2.Setup.VentDrainHolePatternPipe.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipe%5FEquals%5FSystem%5FObject%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipeSlot%5FGetHashCode)GetHashCode()

Similar to a whole pattern, but leaves a slot of the base plate intact within the inner diameter of the pipe.

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[VentDrainHolePatternPipe.GetHashCode()](DesignData.SDS2.Setup.VentDrainHolePatternPipe.html#DesignData%5FSDS2%5FSetup%5FVentDrainHolePatternPipe%5FGetHashCode)