# Class EmbedStudAttachment 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

EmbedStudAttachment

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class EmbedStudAttachment
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5F%5Fctor)EmbedStudAttachment()

##### Declaration

```
public EmbedStudAttachment()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5FGrade)Grade

This is the grade of steel for all of the shear studs that are a part of this pattern. This applies to embed plates, angles and channels.

##### Declaration

```
public string Grade { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5FHeadDiameter)HeadDiameter

The diameter of the shear stud's head. Making this diameter the same as the stud "Diameter" results in shear studs without heads.

##### Declaration

```
public double HeadDiameter { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5FHeadThickness)HeadThickness

The thickness of the shear study's head.

##### Declaration

```
public double HeadThickness { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5FLength)Length

The distance between the two ends of the shear studs. The head is included in the length of a shear stud. This applies to embed plates, angles and channels.

##### Declaration

```
public double Length { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5FRelativeWebRotation)RelativeWebRotation

##### Declaration

```
public double RelativeWebRotation { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5FEquals%5FSystem%5FObject%5F)Equals(object)

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

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5FFinalize)\~EmbedStudAttachment()

##### Declaration

```
protected ~EmbedStudAttachment()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedStudAttachment%5FGetHashCode)GetHashCode()

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