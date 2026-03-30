# Class BoltTypeAISC15 

Bolt type setup information for an AISC15 bolt

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[BoltType](DesignData.SDS2.Setup.BoltType.html)

BoltTypeAISC15

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
public class BoltTypeAISC15 : BoltType
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeAISC15%5FShear)Shear

The nominal shear stress for this type of bolt

##### Declaration

```
public double Shear { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeAISC15%5FSurfaceClass)SurfaceClass

Bolt type setup information for an AISC15 bolt

##### Declaration

```
public SurfaceClassType SurfaceClass { get; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [SurfaceClassType](DesignData.SDS2.Setup.SurfaceClassType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeAISC15%5FTension)Tension

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

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeAISC15%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Bolt type setup information for an AISC15 bolt

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

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeAISC15%5FEquals%5FSystem%5FObject%5F)Equals(object)

Bolt type setup information for an AISC15 bolt

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

#### [](#DesignData%5FSDS2%5FSetup%5FBoltTypeAISC15%5FGetHashCode)GetHashCode()

Bolt type setup information for an AISC15 bolt

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