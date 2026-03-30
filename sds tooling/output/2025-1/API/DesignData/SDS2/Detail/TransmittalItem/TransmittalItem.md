# Class TransmittalItem 

A line on the cover sheet of a transmittal

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

TransmittalItem

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Detail](DesignData.SDS2.Detail.html)

###### **Assembly**: DesignData.SDS2.Detail.dll

##### Syntax

```
public sealed class TransmittalItem
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittalItem%5F%5Fctor)TransmittalItem()

A line on the cover sheet of a transmittal

##### Declaration

```
public TransmittalItem()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittalItem%5FCopies)Copies

The number of copies

##### Declaration

```
public int Copies { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittalItem%5FDescription)Description

The description field of the line

##### Declaration

```
public string Description { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittalItem%5FRevision)Revision

The revision field of the line

##### Declaration

```
public string Revision { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittalItem%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F)Add(DrawingHandle)

Add a single drawing to a transmittal

##### Declaration

```
public void Add(DrawingHandle drawing)
```

##### Parameters

| Type                                                         | Name    | Description |
| ------------------------------------------------------------ | ------- | ----------- |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html) | drawing |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittalItem%5FAdd%5FDesignData%5FSDS2%5FDetail%5FPdf%5F)Add(Pdf)

Add a pdf to a transmittal

##### Declaration

```
public void Add(Pdf pdf)
```

##### Parameters

| Type                                   | Name | Description |
| -------------------------------------- | ---- | ----------- |
| [Pdf](DesignData.SDS2.Detail.Pdf.html) | pdf  |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittalItem%5FFinalize)\~TransmittalItem()

A line on the cover sheet of a transmittal

##### Declaration

```
protected ~TransmittalItem()
```