# Class VentDrainHolePattern 

Base class for vent drain hole patterns

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

VentDrainHolePattern

[VentDrainHolePatternPipe](DesignData.SDS2.Setup.VentDrainHolePatternPipe.html)

[VentDrainHolePatternTube](DesignData.SDS2.Setup.VentDrainHolePatternTube.html)

[VentDrainHolePatternWideFlange](DesignData.SDS2.Setup.VentDrainHolePatternWideFlange.html)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class VentDrainHolePattern
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FOffsetParallelToFlange)OffsetParallelToFlange

Base class for vent drain hole patterns

##### Declaration

```
public double OffsetParallelToFlange { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FOffsetParallelToWeb)OffsetParallelToWeb

Base class for vent drain hole patterns

##### Declaration

```
public double OffsetParallelToWeb { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FPlateRotation)PlateRotation

Base class for vent drain hole patterns

##### Declaration

```
public double PlateRotation { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base class for vent drain hole patterns

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FEquals%5FSystem%5FObject%5F)Equals(object)

Base class for vent drain hole patterns

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

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FFinalize)\~VentDrainHolePattern()

Base class for vent drain hole patterns

##### Declaration

```
protected ~VentDrainHolePattern()
```

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FGetHashCode)GetHashCode()

Base class for vent drain hole patterns

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

#### [](#DesignData%5FSDS2%5FSetup%5FVentDrainHolePattern%5FGetShape)GetShape()

Get the shape to base the vent drain hole pattern off for this base plate.

##### Declaration

```
public Shape GetShape()
```

##### Returns

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |