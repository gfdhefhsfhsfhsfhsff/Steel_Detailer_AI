# Class Pdf 

A class representing a Pdf document

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Pdf

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
public sealed class Pdf
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDetail%5FPdf%5F%5Fctor)Pdf()

A class representing a Pdf document

##### Declaration

```
public Pdf()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FPdf%5FBytes)Bytes

A copy of the raw byte array representing the pdf.

##### Declaration

```
public byte[] Bytes { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\] |             |

##### Examples

```
Pdf pdf = new Pdf();
                      pdf.Bytes = System.IO.File.ReadAllBytes("document.pdf");
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FPdf%5FFinalize)\~Pdf()

A class representing a Pdf document

##### Declaration

```
protected ~Pdf()
```