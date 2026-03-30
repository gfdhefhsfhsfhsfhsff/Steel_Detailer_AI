# Class CommonStructuralProperties 

Structural property values

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CommonStructuralProperties

[ChannelTeeStructuralProperties](DesignData.SDS2.Setup.ChannelTeeStructuralProperties.html)

[FullStructuralProperties](DesignData.SDS2.Setup.FullStructuralProperties.html)

[TubeStructuralProperties](DesignData.SDS2.Setup.TubeStructuralProperties.html)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class CommonStructuralProperties
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FArea)Area

Cross sectional area

##### Declaration

```
public StructuralProperty Area { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FCw)Cw

Warping constant

##### Declaration

```
public StructuralProperty Cw { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FIx)Ix

Moment of inertia (in inches^4)

##### Declaration

```
public StructuralProperty Ix { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FIy)Iy

Moment of inertia (in inches^4)

##### Declaration

```
public StructuralProperty Iy { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FJ)J

Polar inertia (in inches^4)

##### Declaration

```
public StructuralProperty J { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FReference)Reference

The name of the book this came from

##### Declaration

```
public string Reference { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FSx)Sx

Section modulus (in inches^3)

##### Declaration

```
public StructuralProperty Sx { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FSy)Sy

Secton modulus (in inches^3)

##### Declaration

```
public StructuralProperty Sy { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FZx)Zx

Plastic modulus (in inches^3)

##### Declaration

```
public StructuralProperty Zx { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FZy)Zy

Plastic modulus (in inches^3)

##### Declaration

```
public StructuralProperty Zy { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5Frx)rx

Radius of gyration about the x axis

##### Declaration

```
public StructuralProperty rx { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5Fry)ry

Radius of gyration about the y axis

##### Declaration

```
public StructuralProperty ry { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Structural property values

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCommonStructuralProperties%5FFinalize)\~CommonStructuralProperties()

Structural property values

##### Declaration

```
protected ~CommonStructuralProperties()
```