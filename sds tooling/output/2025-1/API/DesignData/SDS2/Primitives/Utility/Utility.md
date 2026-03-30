# Class Utility 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Utility

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public static class Utility
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FUtility%5FEpsilonEquals%5FSystem%5FDouble%5FSystem%5FDouble%5FSystem%5FDouble%5F)EpsilonEquals(double, double, double)

Test near-equality for floating point values.

##### Declaration

```
public static bool EpsilonEquals(double value1, double value2, double epsilon = 1.1920928955078125E-07)
```

##### Parameters

| Type                                                           | Name    | Description |
| -------------------------------------------------------------- | ------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value1  |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value2  |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | epsilon |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FUtility%5FToDegrees%5FSystem%5FDouble%5F)ToDegrees(double)

Convert from radians to degrees.

##### Declaration

```
public static double ToDegrees(double radians)
```

##### Parameters

| Type                                                           | Name    | Description |
| -------------------------------------------------------------- | ------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | radians |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FUtility%5FToRadians%5FSystem%5FDouble%5F)ToRadians(double)

Convert from degrees to radians.

##### Declaration

```
public static double ToRadians(double degrees)
```

##### Parameters

| Type                                                           | Name    | Description |
| -------------------------------------------------------------- | ------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | degrees |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |