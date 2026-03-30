# Class ColdFormedBendRegular 

One regular cold form bend, consisting of two bends with distinct angles and depths and a straight distance between the two.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ColdFormedBend](DesignData.SDS2.Setup.ColdFormedBend.html)

ColdFormedBendRegular

##### Inherited Members

[ColdFormedBend.Node](DesignData.SDS2.Setup.ColdFormedBend.html#DesignData%5FSDS2%5FSetup%5FColdFormedBend%5FNode) 

[ColdFormedBend.NodeDistance](DesignData.SDS2.Setup.ColdFormedBend.html#DesignData%5FSDS2%5FSetup%5FColdFormedBend%5FNodeDistance) 

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
public class ColdFormedBendRegular : ColdFormedBend
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendRegular%5FAngle1)Angle1

The angle in radians of the first bend

##### Declaration

```
public double Angle1 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendRegular%5FAngle2)Angle2

The angle in radians of the second bend

##### Declaration

```
public double Angle2 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendRegular%5FDepth1)Depth1

The depth in inches of the first bend

##### Declaration

```
public double Depth1 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendRegular%5FDepth2)Depth2

The depth in inches of the second bend

##### Declaration

```
public double Depth2 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendRegular%5FLength)Length

The length in inches between bends

##### Declaration

```
public double Length { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FColdFormedBendRegular%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

One regular cold form bend, consisting of two bends with distinct angles and depths and a straight distance between the two.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[ColdFormedBend.Dispose(bool)](DesignData.SDS2.Setup.ColdFormedBend.html#DesignData%5FSDS2%5FSetup%5FColdFormedBend%5FDispose%5FSystem%5FBoolean%5F)