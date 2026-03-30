# Class StairStringer 

The left/right ns/fs stringer data for a stair

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

StairStringer

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
public class StairStringer
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FBoltToFloorClearanceAndCapSetback)BoltToFloorClearanceAndCapSetback

The distance to set the bottom of the stringer back from the floor, only applicable if EndCondition is BoltToFloor

##### Declaration

```
public double BoltToFloorClearanceAndCapSetback { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FCapPlateThickness)CapPlateThickness

The thickness of the cap plate or, if applicable, the top cap. A thickness of '0' (zero) results in no cap plate or top cap.

##### Declaration

```
public double CapPlateThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FCopeDepthBottom)CopeDepthBottom

The cope depth (vertical) required at the bottom of the return. A CopeDepthBottom distance needs to be specified for both the left- and the right-end NS stringers and for both the left- and the right-end FS stringers.

##### Declaration

```
public double CopeDepthBottom { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FCopeDepthTop)CopeDepthTop

The depth (vertical) of the L-shaped cut at the top of the return. This distance is measured parallel with the depth of the return material. A CopeDepthTop distance needs to be specified for both the left- and the right-end NS stringers and for both the left- and the right-end FS stringers.

##### Declaration

```
public double CopeDepthTop { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FCopeLengthBottom)CopeLengthBottom

The cope length (horizontal) required at the bottom of the return. A CopeLengthBottom distance needs to be specified for both the left- and the right-end NS stringers and for both the left- and the right-end FS stringers.

##### Declaration

```
public double CopeLengthBottom { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FCopeLengthTop)CopeLengthTop

The length (horizontal) of the L-shaped cut at the top of the return. This distance is measured parallel with the length of the return material. A CopeLengthTop distance needs to be specified for both the left- and the right-end NS stringers and for both the left- and the right-end FS stringers.

##### Declaration

```
public double CopeLengthTop { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FEndCondition)EndCondition

The end condition for this stringer end, see StairStringerEndCondition documentation for more information

##### Declaration

```
public StairStringerEndCondition EndCondition { get; set; }
```

##### Property Value

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [StairStringerEndCondition](DesignData.SDS2.Model.StairStringerEndCondition.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FSetbackFromWorkpoint)SetbackFromWorkpoint

Additional setback (if positive shifts further from support, if negative shifts toward it) from the workpoint to the stringer

##### Declaration

```
public double SetbackFromWorkpoint { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FSlabToTopReturn)SlabToTopReturn

The vertical distance between the top of the slab and the top of the return steel.

##### Declaration

```
public double SlabToTopReturn { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FSupportToWorkpoint)SupportToWorkpoint

The distance from the supporting member to the workpoint of the stair

##### Declaration

```
public double SupportToWorkpoint { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

The left/right ns/fs stringer data for a stair

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairStringer%5FFinalize)\~StairStringer()

The left/right ns/fs stringer data for a stair

##### Declaration

```
protected ~StairStringer()
```