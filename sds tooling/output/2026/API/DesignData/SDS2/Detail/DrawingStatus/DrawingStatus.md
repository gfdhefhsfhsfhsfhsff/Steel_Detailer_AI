# Class DrawingStatus 

Status information about a drawing.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DrawingStatus

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
public class DrawingStatus
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FActualShipDate)ActualShipDate

The date this was actually shipped out.

##### Declaration

```
public DateTime? ActualShipDate { get; set; }
```

##### Property Value

| Type                                                                | Description                                               |
| ------------------------------------------------------------------- | --------------------------------------------------------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | The shipped date. Returns null if it hasn't been shipped. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FApprovalStatus)ApprovalStatus

The approval status for this drawing

##### Declaration

```
public ApprovalStatus ApprovalStatus { get; set; }
```

##### Property Value

| Type                                                         | Description                           |
| ------------------------------------------------------------ | ------------------------------------- |
| [ApprovalStatus](DesignData.SDS2.Detail.ApprovalStatus.html) | The approval status for this drawing. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FDescription)Description

The drawing description.

##### Declaration

```
public string Description { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FDetailCompleteDate)DetailCompleteDate

The date this was set to detail complete.

##### Declaration

```
public DateTime? DetailCompleteDate { get; set; }
```

##### Property Value

| Type                                                                | Description                                                                  |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | The detail complete date of the drawing. Returns null if it hasn't been set. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FDetailFrozenDate)DetailFrozenDate

The date this was frozen, or null if the drawing is not frozen

##### Declaration

```
public DateTime? DetailFrozenDate { get; set; }
```

##### Property Value

| Type                                                                | Description                                                  |
| ------------------------------------------------------------------- | ------------------------------------------------------------ |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | The frozen date for this drawing, if a layer outline exists. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FDetailRotation)DetailRotation

The degrees of rotation of the member on the drawing.

##### Declaration

```
public double DetailRotation { get; set; }
```

##### Property Value

| Type                                                           | Description                                             |
| -------------------------------------------------------------- | ------------------------------------------------------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | Angle of rotation in radians. Range is \[-pi/2, pi/2\]. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FDrawingScale)DrawingScale

The scale of the drawing.

##### Declaration

```
public double DrawingScale { get; }
```

##### Property Value

| Type                                                           | Description                               |
| -------------------------------------------------------------- | ----------------------------------------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | The drawing scale, if the drawing exists. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FErectedDate)ErectedDate

Gets the date this was erected on site.

##### Declaration

```
public DateTime? ErectedDate { get; set; }
```

##### Property Value

| Type                                                                | Description                                                          |
| ------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | The erected date of the drawing. Returns null if it hasn't been set. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FFabricatedDate)FabricatedDate

The date this drawing went for fabrication.

##### Declaration

```
public DateTime? FabricatedDate { get; set; }
```

##### Property Value

| Type                                                                | Description                                                                         |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | The fabrication date of the drawing. Returns null if it hasn't gone to fabrication. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FHeight)Height

The height dimension of the drawing.

##### Declaration

```
public double Height { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FInShopDate)InShopDate

The date this drawing went to the shop.

##### Declaration

```
public DateTime? InShopDate { get; set; }
```

##### Property Value

| Type                                                                | Description                                                                             |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | The date the drawing went to the shop. Returns null if it hasn't been sent to the shop. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FIsDetailFromDrawingScale)IsDetailFromDrawingScale

Determines if the scale at which a member is detailed is regenerated next time detailing is run on the member. This applies only to member details.

##### Declaration

```
public bool IsDetailFromDrawingScale { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FIsMarkedForExport)IsMarkedForExport

Returns whether or not the member detail will be listed in a FabTrol export by "BOM" or "Model".

##### Declaration

```
public bool IsMarkedForExport { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FLastPlottedDate)LastPlottedDate

The last date this drawing was plotted.

##### Declaration

```
public DateTime? LastPlottedDate { get; set; }
```

##### Property Value

| Type                                                                | Description                                                               |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | The last plotted date of the drawing. Returns null if it hasn't been set. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FLength)Length

The length dimension of the drawing.

##### Declaration

```
public double Length { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FMaterial)Material

The section size of the member or submaterial.

##### Declaration

```
public string Material { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FMaterialLength)MaterialLength

The length of the material.

##### Declaration

```
public double MaterialLength { get; }
```

##### Property Value

| Type                                                           | Description                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | The length of the material, measured as the farthest point on its left end to the farthest point on the right end, as measured parallel with the workline of the material. Applies to member details and submaterial details. On member details, this is the total length of the member main material. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FMemberNumber)MemberNumber

The lowest member number of all members with the same piecemark as the drawing.

##### Declaration

```
public uint MemberNumber { get; }
```

##### Property Value

| Type                                                         | Description                                                                                                                                                                                               |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32) | If 0, then the drawing is not a member detail. If it is not 0, then the drawing is a member detail, and the number is the lowest member number of all members that have been assigned the same piecemark. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FMemberType)MemberType

The type of the member(Beam, Column, etc.).

##### Declaration

```
public MemberType MemberType { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [MemberType](DesignData.SDS2.Setup.MemberType.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FOverrideDrawingEditorModelConsistencyLocks)OverrideDrawingEditorModelConsistencyLocks

Returns whether or not restrictions from Dimension Settings that apply to submaterials and details are temporarily overwritten.

##### Declaration

```
public bool OverrideDrawingEditorModelConsistencyLocks { get; }
```

##### Property Value

| Type                                                          | Description                                        |
| ------------------------------------------------------------- | -------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | If true, restrictions are temporarily overwritten. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FQuantity)Quantity

The count of member or pieces of submaterial with this drawing's piecemark.

##### Declaration

```
public uint Quantity { get; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FReceivedForApprovalDate)ReceivedForApprovalDate

The date this was received for approval.

##### Declaration

```
public DateTime? ReceivedForApprovalDate { get; set; }
```

##### Property Value

| Type                                                                | Description                                                                             |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | The received for approval date of the drawing. Returns null if it hasn't been received. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FSentForApprovalDate)SentForApprovalDate

The date this was sent for approval.

##### Declaration

```
public DateTime? SentForApprovalDate { get; set; }
```

##### Property Value

| Type                                                                | Description                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | The sent for approval date of the drawing. Returns null if it hasn't been sent. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FSheet)Sheet

List of sheets the drawing appears on.

##### Declaration

```
public string Sheet { get; }
```

##### Property Value

| Type                                                           | Description                                              |
| -------------------------------------------------------------- | -------------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | A comma-separated list of sheets the drawing appears on. |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FSheetRevision)SheetRevision

Sheet revision information for this drawing, if any. If no information exists this will be null.

##### Declaration

```
public SheetRevision SheetRevision { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [SheetRevision](DesignData.SDS2.Detail.SheetRevision.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FVersion)Version

The version of SDS2 that the drawing was created with.

##### Declaration

```
public Version Version { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Version](DesignData.SDS2.Database.Version.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Status information about a drawing.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FFinalize)\~DrawingStatus()

Status information about a drawing.

##### Declaration

```
protected ~DrawingStatus()
```

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingStatus%5FGetFileDescription)GetFileDescription()

A user-defined description of the drawing.

##### Declaration

```
public string GetFileDescription()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |