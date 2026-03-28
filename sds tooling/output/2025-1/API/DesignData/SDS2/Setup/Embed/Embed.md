# Class Embed 

One entry in the embed plate schedule

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Embed

[EmbedPlate](DesignData.SDS2.Setup.EmbedPlate.html)

[EmbedShape](DesignData.SDS2.Setup.EmbedShape.html)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class Embed
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FDeformedBarAttachments)DeformedBarAttachments

Get the deformed bar attachments

##### Declaration

```
public DeformedBarAttachmentList DeformedBarAttachments { get; }
```

##### Property Value

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [DeformedBarAttachmentList](DesignData.SDS2.Setup.DeformedBarAttachmentList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FGrade)Grade

One entry in the embed plate schedule

##### Declaration

```
public SteelGrade Grade { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FHoleAttachments)HoleAttachments

Get the hole attachments

##### Declaration

```
public EmbedHoleAttachmentList HoleAttachments { get; }
```

##### Property Value

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [EmbedHoleAttachmentList](DesignData.SDS2.Setup.EmbedHoleAttachmentList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FLength)Length

The length of the embed plate

##### Declaration

```
public double Length { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FLocation)Location

One entry in the embed plate schedule

##### Declaration

```
public EmbedLocation Location { get; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [EmbedLocation](DesignData.SDS2.Setup.EmbedLocation.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FPiecemark)Piecemark

One entry in the embed plate schedule

##### Declaration

```
public string Piecemark { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FPlateFinish)PlateFinish

The surface finish to use on the embed plate

##### Declaration

```
public SurfaceFinish PlateFinish { get; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [SurfaceFinish](DesignData.SDS2.Setup.SurfaceFinish.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FPlateSurfaceFinish)PlateSurfaceFinish

The surface finish to use on the embed plate

##### Declaration

```
[Obsolete("Setup.Embed.PlateSurfaceFinish return type enum is deprecated. Use the PlateFinish property for the new type Setup.SurfaceFinish", false)]
public MaterialSurfaceFinish PlateSurfaceFinish { get; }
```

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [MaterialSurfaceFinish](DesignData.SDS2.Setup.MaterialSurfaceFinish.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FStudAttachments)StudAttachments

Get the stud attachments

##### Declaration

```
public EmbedStudAttachmentList StudAttachments { get; }
```

##### Property Value

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [EmbedStudAttachmentList](DesignData.SDS2.Setup.EmbedStudAttachmentList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FStudFinish)StudFinish

The surface finish to use on the stud

##### Declaration

```
public SurfaceFinish StudFinish { get; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [SurfaceFinish](DesignData.SDS2.Setup.SurfaceFinish.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FStudSurfaceFinish)StudSurfaceFinish

The surface finish to use on the stud

##### Declaration

```
[Obsolete("Setup.Embed.StudSurfaceFinish return type enum is deprecated. Use the StudFinish property for the new type Setup.SurfaceFinish", false)]
public MaterialSurfaceFinish StudSurfaceFinish { get; }
```

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [MaterialSurfaceFinish](DesignData.SDS2.Setup.MaterialSurfaceFinish.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

One entry in the embed plate schedule

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FEquals%5FSystem%5FObject%5F)Equals(object)

One entry in the embed plate schedule

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

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FFinalize)\~Embed()

One entry in the embed plate schedule

##### Declaration

```
protected ~Embed()
```

#### [](#DesignData%5FSDS2%5FSetup%5FEmbed%5FGetHashCode)GetHashCode()

One entry in the embed plate schedule

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