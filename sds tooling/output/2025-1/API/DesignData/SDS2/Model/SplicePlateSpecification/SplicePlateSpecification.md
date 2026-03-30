# Class SplicePlateSpecification 

A splice plate connection

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

SplicePlateSpecification

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
public sealed class SplicePlateSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5F%5Fctor)SplicePlateSpecification()

A splice plate connection

##### Declaration

```
public SplicePlateSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FColSpliceGap)ColSpliceGap

Specifies the gap between the lower and upper columns in a European column splice

##### Declaration

```
public double ColSpliceGap { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FColumnChannelWebLowerConnectionMethod)ColumnChannelWebLowerConnectionMethod

Attachment method of channel web connection. (columns only)

##### Declaration

```
public AttachmentMethod ColumnChannelWebLowerConnectionMethod { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [AttachmentMethod](DesignData.SDS2.Model.AttachmentMethod.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FColumnSpliceAttachmentMethod)ColumnSpliceAttachmentMethod

A splice plate connection

##### Declaration

```
public ColumnSpliceAttachmentMethod ColumnSpliceAttachmentMethod { get; set; }
```

##### Property Value

| Type                                                                                    | Description |
| --------------------------------------------------------------------------------------- | ----------- |
| [ColumnSpliceAttachmentMethod](DesignData.SDS2.Model.ColumnSpliceAttachmentMethod.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FFlangePlatesOn)FlangePlatesOn

Member end(s) that the flange plates ship with (beams only)

##### Declaration

```
public ConnectionSpecificationEndLeftRightBoth FlangePlatesOn { get; set; }
```

##### Property Value

| Type                                                                                                          | Description |
| ------------------------------------------------------------------------------------------------------------- | ----------- |
| [ConnectionSpecificationEndLeftRightBoth](DesignData.SDS2.Model.ConnectionSpecificationEndLeftRightBoth.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FGrade)Grade

The grade to set on the splice plate material for this connection. This value does not apply to a column channel web.

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

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FInnerFlangePlate)InnerFlangePlate

Applies to column splice connections with 'All-Bolted plates'. Each column section size must be a flanged shaped such as wide flange.

##### Declaration

```
public AutomaticYesNo InnerFlangePlate { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FIsAutoGrade)IsAutoGrade

If true, the system determines the splice plate grade. If false, the value specified in the Grade property will be used.

##### Declaration

```
public bool IsAutoGrade { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FIsColumnButtPlateAdded)IsColumnButtPlateAdded

True when a butt plate is specified. (columns only)

##### Declaration

```
public bool IsColumnButtPlateAdded { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FIsColumnChannelWebConnection)IsColumnChannelWebConnection

True when a channel web is specified. (columns only)

##### Declaration

```
public bool IsColumnChannelWebConnection { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FIsColumnWebPlateAdded)IsColumnWebPlateAdded

True when a web plate is specified. (columns only)

##### Declaration

```
public bool IsColumnWebPlateAdded { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FNonBearingSplice)NonBearingSplice

Specifies whether columns are in direct bearing in a European column splice

##### Declaration

```
public bool NonBearingSplice { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FSide)Side

Side(s) of the member that the web connection material is on

##### Declaration

```
public ClipAngleSide Side { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ClipAngleSide](DesignData.SDS2.Model.ClipAngleSide.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FWebPlatesOn)WebPlatesOn

Member end(s) that the web plates ship with

##### Declaration

```
public ConnectionSpecificationEndLeftRightBoth WebPlatesOn { get; set; }
```

##### Property Value

| Type                                                                                                          | Description |
| ------------------------------------------------------------------------------------------------------------- | ----------- |
| [ConnectionSpecificationEndLeftRightBoth](DesignData.SDS2.Model.ConnectionSpecificationEndLeftRightBoth.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FSplicePlateSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A splice plate connection

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