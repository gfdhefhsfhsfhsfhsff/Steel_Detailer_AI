# Class SteelGrade 

Steel grade information

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

SteelGrade

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
public class SteelGrade
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FBetaW)BetaW

Euro code correlation factor

##### Declaration

```
public double BetaW { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FDensity)Density

Density value to determine weight

##### Declaration

```
public double Density { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

In lb/in^3

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FF)F

The tension, compression, and bending strength

##### Declaration

```
public double F { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

In ksi

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FFce)Fce

End bearing in Chinese design, planed and close fitted.

##### Declaration

```
public double Fce { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

In ksi

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FFu)Fu

The yield strength

##### Declaration

```
public double Fu { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

In ksi

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FFv)Fv

The shear strength

##### Declaration

```
public double Fv { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

In ksi

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FFy)Fy

The ultimate strength value

##### Declaration

```
public double Fy { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

In ksi

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FGradeType)GradeType

The type of grade, steel/Aluminum/Wood/etc.

##### Declaration

```
public string GradeType { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

This string returned may be internationalized

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FMaximumThickness)MaximumThickness

For AS 4100/China/India/Euro, the maximum thickness

##### Declaration

```
public double MaximumThickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FMinimumThickness)MinimumThickness

For AS 4100/China/India/Euro, the minimum thickness

##### Declaration

```
public double MinimumThickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FN)N

N value for CSA code

##### Declaration

```
public double N { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FName)Name

The name or steel specification for this grade

##### Declaration

```
public string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FNonStandardNote)NonStandardNote

Nonstandard, user, description of grade

##### Declaration

```
public string NonStandardNote { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FRt)Rt

Ratio of expected tensile strength to the specified minimum Fu

##### Declaration

```
public double Rt { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FRy)Ry

Ratio of expected yield stress to the specified minimum yield stress, Fy

##### Declaration

```
public double Ry { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Steel grade information

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FEquals%5FSystem%5FObject%5F)Equals(object)

Steel grade information

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

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FFinalize)\~SteelGrade()

Steel grade information

##### Declaration

```
protected ~SteelGrade()
```

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5FGetHashCode)GetHashCode()

Steel grade information

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

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5Fop%5FEquality%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F)operator ==(SteelGrade, SteelGrade)

Steel grade information

##### Declaration

```
public static bool operator ==(SteelGrade a, SteelGrade b)
```

##### Parameters

| Type                                                | Name | Description |
| --------------------------------------------------- | ---- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | a    |             |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSteelGrade%5Fop%5FInequality%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F)operator !=(SteelGrade, SteelGrade)

Steel grade information

##### Declaration

```
public static bool operator !=(SteelGrade a, SteelGrade b)
```

##### Parameters

| Type                                                | Name | Description |
| --------------------------------------------------- | ---- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | a    |             |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |