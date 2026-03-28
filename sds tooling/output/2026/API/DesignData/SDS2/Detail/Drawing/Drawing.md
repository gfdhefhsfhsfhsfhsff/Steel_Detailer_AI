# Class Drawing 

Metadata for a drawing and access to a PDF rendering of the drawing

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Drawing

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Detail](DesignData.SDS2.Detail.html)

###### **Assembly**: DesignData.SDS2.Detail.dll

##### Syntax

```
public class Drawing
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FBillOfMaterial)BillOfMaterial

The bill of material associated with a drawing.

##### Declaration

```
public BillOfMaterial BillOfMaterial { get; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [BillOfMaterial](DesignData.SDS2.Detail.BillOfMaterial.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FDimensioningDefaults)DimensioningDefaults

Metadata for a drawing and access to a PDF rendering of the drawing

##### Declaration

```
public AnnotationDimensioningDefaults DimensioningDefaults { get; }
```

##### Property Value

| Type                                                                                        | Description |
| ------------------------------------------------------------------------------------------- | ----------- |
| [AnnotationDimensioningDefaults](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FDrawingType)DrawingType

the type of the drawing, detail, sheet, submaterial detail, etc

##### Declaration

```
public TableWithDrawings DrawingType { get; }
```

##### Property Value

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [TableWithDrawings](DesignData.SDS2.Database.TableWithDrawings.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FEvuDefaults)EvuDefaults

Metadata for a drawing and access to a PDF rendering of the drawing

##### Declaration

```
public ErectionViewDefaults EvuDefaults { get; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [ErectionViewDefaults](DesignData.SDS2.Setup.ErectionViewDefaults.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FHandle)Handle

The database handle for this drawing

##### Declaration

```
public DrawingHandle Handle { get; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FName)Name

the name of the drawing

##### Declaration

```
public string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FStatus)Status

Accessor object for drawing status information

##### Declaration

```
public DrawingStatus Status { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [DrawingStatus](DesignData.SDS2.Detail.DrawingStatus.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FCreatePDF)CreatePDF()

Get the PDF as a binary blob. This can be written to a file or stored elsewhere.

##### Declaration

```
public byte[] CreatePDF()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\] |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Metadata for a drawing and access to a PDF rendering of the drawing

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FFinalize)\~Drawing()

Metadata for a drawing and access to a PDF rendering of the drawing

##### Declaration

```
protected ~Drawing()
```

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FFind%5FDesignData%5FSDS2%5FDatabase%5FTableWithDrawings%5FSystem%5FString%5F)Find(TableWithDrawings, string)

Find a drawing, and anything referencing it, based on a database table and the name of the drawing

##### Declaration

```
public static DrawingList Find(TableWithDrawings table, string name)
```

##### Parameters

| Type                                                                 | Name  | Description |
| -------------------------------------------------------------------- | ----- | ----------- |
| [TableWithDrawings](DesignData.SDS2.Database.TableWithDrawings.html) | table |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string)       | name  |             |

##### Returns

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [DrawingList](DesignData.SDS2.Detail.DrawingList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FFind%5FDesignData%5FSDS2%5FDetail%5FPiecemarkType%5FSystem%5FString%5F)Find(PiecemarkType, string)

Find all drawings referencing the given piecemark. If a piecemark hasn't been detailed yet it will not have a drawing, so this list will be empty.

##### Declaration

```
public static DrawingList Find(PiecemarkType piecemarkType, string piecemark)
```

##### Parameters

| Type                                                           | Name          | Description                              |
| -------------------------------------------------------------- | ------------- | ---------------------------------------- |
| [PiecemarkType](DesignData.SDS2.Detail.PiecemarkType.html)     | piecemarkType | the type of mark, major or minor         |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | piecemark     | the name of the mark, such as B\_1 or p1 |

##### Returns

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [DrawingList](DesignData.SDS2.Detail.DrawingList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FGet%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F)Get(DrawingHandle)

Get a drawing based on its location in the database

##### Declaration

```
public static Drawing Get(DrawingHandle drawingHandle)
```

##### Parameters

| Type                                                         | Name          | Description |
| ------------------------------------------------------------ | ------------- | ----------- |
| [DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html) | drawingHandle |             |

##### Returns

| Type                                           | Description |
| ---------------------------------------------- | ----------- |
| [Drawing](DesignData.SDS2.Detail.Drawing.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FGet%5FDesignData%5FSDS2%5FDatabase%5FTableWithDrawings%5FSystem%5FString%5F)Get(TableWithDrawings, string)

Get a drawing based on a table and its name

##### Declaration

```
public static Drawing Get(TableWithDrawings table, string name)
```

##### Parameters

| Type                                                                 | Name  | Description |
| -------------------------------------------------------------------- | ----- | ----------- |
| [TableWithDrawings](DesignData.SDS2.Database.TableWithDrawings.html) | table |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string)       | name  |             |

##### Returns

| Type                                           | Description |
| ---------------------------------------------- | ----------- |
| [Drawing](DesignData.SDS2.Detail.Drawing.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawing%5FGet%5FDesignData%5FSDS2%5FDetail%5FPiecemarkType%5FSystem%5FString%5F)Get(PiecemarkType, string)

Get a drawing based on piecemark type and its name

##### Declaration

```
public static Drawing Get(PiecemarkType piecemarkType, string name)
```

##### Parameters

| Type                                                           | Name          | Description |
| -------------------------------------------------------------- | ------------- | ----------- |
| [PiecemarkType](DesignData.SDS2.Detail.PiecemarkType.html)     | piecemarkType |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name          |             |

##### Returns

| Type                                           | Description |
| ---------------------------------------------- | ----------- |
| [Drawing](DesignData.SDS2.Detail.Drawing.html) |             |