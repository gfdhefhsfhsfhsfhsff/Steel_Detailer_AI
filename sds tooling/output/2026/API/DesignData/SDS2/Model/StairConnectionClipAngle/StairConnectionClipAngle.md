# Class StairConnectionClipAngle 

Clip angle connection between stair stringer and supporting material

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[StairConnectionSpecification](DesignData.SDS2.Model.StairConnectionSpecification.html)

StairConnectionClipAngle

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
public sealed class StairConnectionClipAngle : StairConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5F%5Fctor)StairConnectionClipAngle()

Clip angle connection between stair stringer and supporting material

##### Declaration

```
public StairConnectionClipAngle()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5FAttachToMember)AttachToMember

Specifies which member that the clip angle ships with.

##### Declaration

```
public AttachToMember AttachToMember { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AttachToMember](DesignData.SDS2.Model.AttachToMember.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5FAttachmentSupported)AttachmentSupported

Specifies how the clip angle connects to the stair stringer.

##### Declaration

```
public StairConnectionAttachmentSpecification AttachmentSupported { get; set; }
```

##### Property Value

| Type                                                                                                        | Description |
| ----------------------------------------------------------------------------------------------------------- | ----------- |
| [StairConnectionAttachmentSpecification](DesignData.SDS2.Model.StairConnectionAttachmentSpecification.html) |             |

##### Remarks

This data is a copy of the attachment

##### Exceptions

| Type                                                                           | Condition                    |
| ------------------------------------------------------------------------------ | ---------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown for null attachments. |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5FAttachmentSupporting)AttachmentSupporting

Specifies how the clip angle connects to the supporting material.

##### Declaration

```
public StairConnectionAttachmentBolted AttachmentSupporting { get; set; }
```

##### Property Value

| Type                                                                                          | Description |
| --------------------------------------------------------------------------------------------- | ----------- |
| [StairConnectionAttachmentBolted](DesignData.SDS2.Model.StairConnectionAttachmentBolted.html) |             |

##### Remarks

This data is a copy of the attachment

##### Exceptions

| Type                                                                           | Condition                    |
| ------------------------------------------------------------------------------ | ---------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown for null attachments. |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5FDimensionToStringerEdge)DimensionToStringerEdge

Specifies the vertical distance from the stringer edge to the clip angle.

##### Declaration

```
public double DimensionToStringerEdge { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5FGrade)Grade

Specifies the clip angle material grade.

##### Declaration

```
public SteelGrade Grade { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

##### Exceptions

| Type                                                                           | Condition                  |
| ------------------------------------------------------------------------------ | -------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown for invalid grades. |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5FLength)Length

Specifies the clip angle length.

##### Declaration

```
public double Length { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown for dimensions less than or equal to 0.0. |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5FLongLegTo)LongLegTo

Specifies which member the long leg of the clip angle touches.

##### Declaration

```
public StairConnectionLongLegTo LongLegTo { get; set; }
```

##### Property Value

| Type                                                                            | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [StairConnectionLongLegTo](DesignData.SDS2.Model.StairConnectionLongLegTo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5FShape)Shape

Specifies the clip angle shape.

##### Declaration

```
public AngleShape Shape { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [AngleShape](DesignData.SDS2.Setup.AngleShape.html) |             |

##### Exceptions

| Type                                                                           | Condition               |
| ------------------------------------------------------------------------------ | ----------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown for null shapes. |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5FStringerSide)StringerSide

Specifies the side of the stringer the clip angle touches.

##### Declaration

```
public StairConnectionStringerSide StringerSide { get; set; }
```

##### Property Value

| Type                                                                                  | Description |
| ------------------------------------------------------------------------------------- | ----------- |
| [StairConnectionStringerSide](DesignData.SDS2.Model.StairConnectionStringerSide.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionClipAngle%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Clip angle connection between stair stringer and supporting material

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[StairConnectionSpecification.Dispose(bool)](DesignData.SDS2.Model.StairConnectionSpecification.html#DesignData%5FSDS2%5FModel%5FStairConnectionSpecification%5FDispose%5FSystem%5FBoolean%5F)