# Class Transmittal 

Items combined together into a single package that is to be sent off for approval

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Transmittal

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
public sealed class Transmittal
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5F%5Fctor)Transmittal()

Start a new transmittal

##### Declaration

```
public Transmittal()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FAddressOne)AddressOne

The first address line for this transmittal

##### Declaration

```
public string AddressOne { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FAddressTwo)AddressTwo

The second address line for this transmittal

##### Declaration

```
public string AddressTwo { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FCity)City

The city this transmittal is being sent from

##### Declaration

```
public string City { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FDue)Due

The date this transmittal is due back

##### Declaration

```
public DateTime? Due { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FFrom)From

Contact information for the sender of the transmittal.

##### Declaration

```
public TransmittalContact From { get; set; }
```

##### Property Value

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [TransmittalContact](DesignData.SDS2.Detail.TransmittalContact.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FLogo)Logo

A copy of the raw byte array representing the logo image. This image is placed in the top right corner of the cover page. If necessary the image is scaled to fit inside a 193x100 rectangle. Loadable images include .jpg, .gif, .tif, and .png files.

##### Declaration

```
public byte[] Logo { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\] |             |

##### Examples

```
Transmittal transmittal = new Transmittal();
                      transmittal.Logo = System.IO.File.ReadAllBytes("logo193x100.jpg");
```

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FProjectName)ProjectName

The name of the project this transmittal pertains to

##### Declaration

```
public string ProjectName { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FProjectNumber)ProjectNumber

The number of the project this transmittal pertains to

##### Declaration

```
public string ProjectNumber { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FRemarks)Remarks

Remarks included on the transmittal cover page

##### Declaration

```
public string Remarks { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FSent)Sent

The date this transmittal will be sent

##### Declaration

```
public DateTime? Sent { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FState)State

The state this transmittal is being sent from

##### Declaration

```
public string State { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FTo)To

Contact information for the main recipient of the transmittal.

##### Declaration

```
public TransmittalContact To { get; set; }
```

##### Property Value

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [TransmittalContact](DesignData.SDS2.Detail.TransmittalContact.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FTransmittalNumber)TransmittalNumber

The number of this transmittal

##### Declaration

```
public string TransmittalNumber { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FZipCode)ZipCode

The zip code this transmittal is being sent from

##### Declaration

```
public string ZipCode { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FAdd%5FDesignData%5FSDS2%5FDetail%5FTransmittalCC%5F)Add(TransmittalCC)

Add a cc for a transmittal package

##### Declaration

```
public void Add(TransmittalCC cc)
```

##### Parameters

| Type                                                       | Name | Description |
| ---------------------------------------------------------- | ---- | ----------- |
| [TransmittalCC](DesignData.SDS2.Detail.TransmittalCC.html) | cc   |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FAdd%5FDesignData%5FSDS2%5FDetail%5FTransmittalItem%5F)Add(TransmittalItem)

Add an item to a transmittal package

##### Declaration

```
public void Add(TransmittalItem transmittal)
```

##### Parameters

| Type                                                           | Name        | Description |
| -------------------------------------------------------------- | ----------- | ----------- |
| [TransmittalItem](DesignData.SDS2.Detail.TransmittalItem.html) | transmittal |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FFinalize)\~Transmittal()

Items combined together into a single package that is to be sent off for approval

##### Declaration

```
protected ~Transmittal()
```

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FGeneratePDF)GeneratePDF()

Create the PDF for this transmittal and return it as a byte array, to be written diretly to a .pdf file

##### Declaration

```
public byte[] GeneratePDF()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\] |             |

#### [](#DesignData%5FSDS2%5FDetail%5FTransmittal%5FGeneratePDFs)GeneratePDFs()

Create a series of PDFs, one per drawing, returned as a map from the intended PDF filename to a byte array for the PDF.

```
         For the links to work, these must be written to files with the exact
         name used as the key of this map.  Any other name will break the
         links between drawings.

```

##### Declaration

```
public Dictionary<string, byte[]> GeneratePDFs()
```

##### Returns

| Type                                                                                                                                                                                                                         | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]> |             |