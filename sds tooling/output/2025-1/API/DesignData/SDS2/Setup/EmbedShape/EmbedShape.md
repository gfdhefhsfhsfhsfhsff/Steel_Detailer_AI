# Class EmbedShape 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Embed](DesignData.SDS2.Setup.Embed.html)

EmbedShape

##### Inherited Members

[Embed.Piecemark](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FPiecemark) 

[Embed.Grade](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FGrade) 

[Embed.PlateFinish](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FPlateFinish) 

[Embed.StudFinish](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FStudFinish) 

[Embed.StudSurfaceFinish](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FStudSurfaceFinish) 

[Embed.PlateSurfaceFinish](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FPlateSurfaceFinish) 

[Embed.Location](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FLocation) 

[Embed.Length](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FLength) 

[Embed.HoleAttachments](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FHoleAttachments) 

[Embed.StudAttachments](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FStudAttachments) 

[Embed.DeformedBarAttachments](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FDeformedBarAttachments) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class EmbedShape : Embed
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedShape%5FEnds)Ends

Get the ends of the embed plate

##### Declaration

```
public EmbedEndList Ends { get; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [EmbedEndList](DesignData.SDS2.Setup.EmbedEndList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedShape%5FIsGalvanized)IsGalvanized

Sets the material's finish to galvanized

##### Declaration

```
public bool IsGalvanized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedShape%5FShape)Shape

Get the embedded shape description

##### Declaration

```
public Shape Shape { get; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[Embed.Dispose(bool)](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedShape%5FEquals%5FSystem%5FObject%5F)Equals(object)

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

[Embed.Equals(object)](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FEquals%5FSystem%5FObject%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FEmbedShape%5FGetHashCode)GetHashCode()

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[Embed.GetHashCode()](DesignData.SDS2.Setup.Embed.html#DesignData%5FSDS2%5FSetup%5FEmbed%5FGetHashCode)