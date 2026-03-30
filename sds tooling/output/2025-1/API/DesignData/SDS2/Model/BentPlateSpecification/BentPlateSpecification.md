# Class BentPlateSpecification 

A bent plate connection

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

BentPlateSpecification

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
public sealed class BentPlateSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5F%5Fctor)BentPlateSpecification()

A bent plate connection

##### Declaration

```
public BentPlateSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5FAttachToMember)AttachToMember

How to attach the connection to the supporting member

##### Declaration

```
public AttachToMember AttachToMember { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AttachToMember](DesignData.SDS2.Model.AttachToMember.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5FAttachmentMethodToSupported)AttachmentMethodToSupported

How to attach the connection to the beam being supported

##### Declaration

```
public AttachmentMethod AttachmentMethodToSupported { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [AttachmentMethod](DesignData.SDS2.Model.AttachmentMethod.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5FAttachmentMethodToSupporting)AttachmentMethodToSupporting

How to attach the connection to the supporting member

##### Declaration

```
public AttachmentMethod AttachmentMethodToSupporting { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [AttachmentMethod](DesignData.SDS2.Model.AttachmentMethod.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5FGage)Gage

Specify whether this is a heavy, wide, or narrow gage clip

##### Declaration

```
public ClipAngleGage Gage { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ClipAngleGage](DesignData.SDS2.Model.ClipAngleGage.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5FGrade)Grade

The grade to set on the new bent plate material for this connection.

##### Declaration

```
public SteelGrade Grade { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

##### Remarks

Setting this fill flip AutoGrade to false

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5FIsAutoGrade)IsAutoGrade

If true, this has the system determine the plate grade for the bent plate. If false, whatever value is set to Grade will be used.

##### Declaration

```
public bool IsAutoGrade { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5FIsFullDepthTee)IsFullDepthTee

If true, the system creates a built-up tee that is the full depth of the supporting beam.

```
         If false, the built-up tee is designed to the depth of the
         connection if the top and bottom flanges of the supported beam
         (this beam) are entirely below or entirely above the half-depth
         of the supporting beam. If the depth of the supported beam is
         greater than half the depth of the supporting beam, the built-up
         tee is designed to the full depth of the supporting beam.

```

##### Declaration

```
public bool IsFullDepthTee { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5FSide)Side

Which side of the supported member to put clip angles on, or both.

##### Declaration

```
public ClipAngleSide Side { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ClipAngleSide](DesignData.SDS2.Model.ClipAngleSide.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5FStagger)Stagger

See documentation on the returned ClipAngleStagger enumeration

##### Declaration

```
public ClipAngleStagger Stagger { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [ClipAngleStagger](DesignData.SDS2.Model.ClipAngleStagger.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FBentPlateSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A bent plate connection

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[ConnectionSpecification.Dispose(bool)](DesignData.SDS2.Model.ConnectionSpecification.html#DesignData%5FSDS2%5FModel%5FConnectionSpecification%5FDispose%5FSystem%5FBoolean%5F)