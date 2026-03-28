# Class BoltTypeASD9 

Bolt type setup information for an ASD9 bolt

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[BoltType](DesignData.SDS2.Setup.BoltType.html)

BoltTypeASD9

[BoltTypeLRFD3](DesignData.SDS2.Setup.BoltTypeLRFD3.html)

##### Inherited Members

[BoltType.Description](DesignData.SDS2.Setup.BoltType.html#DesignData%5FSDS2%5FSetup%5FBoltType%5FDescription) 

[BoltType.Material](DesignData.SDS2.Setup.BoltType.html#DesignData%5FSDS2%5FSetup%5FBoltType%5FMaterial) 

[BoltType.FrictionBearing](DesignData.SDS2.Setup.BoltType.html#DesignData%5FSDS2%5FSetup%5FBoltType%5FFrictionBearing) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class BoltTypeASD9 : BoltType
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeASD9%5FShearLongSlot)ShearLongSlot

The maximum allowable shear stress for the type of bolt being defined when it is used in a long slot.

##### Declaration

```
public double ShearLongSlot { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeASD9%5FShearOversized)ShearOversized

The maximum allowable shear stress for the type of bolt being defined when used in an oversized hole. An oversized hole is a round hole that is typically 1/8 inch larger than the bolt diameter.

##### Declaration

```
public double ShearOversized { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeASD9%5FShearShortSlot)ShearShortSlot

The maximum allowable shear stress for the type of bolt being defined when it is used in a short slot.

##### Declaration

```
public double ShearShortSlot { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeASD9%5FShearStandard)ShearStandard

The maximum allowable shear stress that the type of bolt being defined can withstand when used in a standard hole. A standard hole is a round hole that is typically 1/16 inch larger than the bolt diameter.

##### Declaration

```
public double ShearStandard { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeASD9%5FSurfaceClass)SurfaceClass

Only applies for slip critical bolts

##### Declaration

```
public SurfaceClassType SurfaceClass { get; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [SurfaceClassType](DesignData.SDS2.Setup.SurfaceClassType.html) |             |

##### Remarks

Can only be A, B, or C

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeASD9%5FTension)Tension

The nominal tension stress for this type of bolt

##### Declaration

```
public double Tension { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeASD9%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Bolt type setup information for an ASD9 bolt

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[BoltType.Dispose(bool)](DesignData.SDS2.Setup.BoltType.html#DesignData%5FSDS2%5FSetup%5FBoltType%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeASD9%5FEquals%5FSystem%5FObject%5F)Equals(object)

Bolt type setup information for an ASD9 bolt

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

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeASD9%5FGetHashCode)GetHashCode()

Bolt type setup information for an ASD9 bolt

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