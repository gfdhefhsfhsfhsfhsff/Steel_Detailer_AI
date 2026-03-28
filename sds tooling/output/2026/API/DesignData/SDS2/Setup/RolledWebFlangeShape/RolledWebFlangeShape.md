# Class RolledWebFlangeShape 

Base for shapes with I or H profiles, C profiles and T profiles. These shapes share all of these profile properties.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

[RolledShape](DesignData.SDS2.Setup.RolledShape.html)

RolledWebFlangeShape

[ChannelShape](DesignData.SDS2.Setup.ChannelShape.html)

[SFlangeShape](DesignData.SDS2.Setup.SFlangeShape.html)

[STeeShape](DesignData.SDS2.Setup.STeeShape.html)

[WTeeShape](DesignData.SDS2.Setup.WTeeShape.html)

[WideFlangeShape](DesignData.SDS2.Setup.WideFlangeShape.html)

##### Inherited Members

[RolledShape.Depth](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FDepth) 

[RolledShape.NominalDepth](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FNominalDepth) 

[RolledShape.WeightPerUnitFoot](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FWeightPerUnitFoot) 

[Shape.GetHashCode()](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FGetHashCode) 

[Shape.Equals(object)](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FEquals%5FSystem%5FObject%5F) 

[Shape.SectionSize](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FSectionSize) 

[Shape.IsAvailable](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FIsAvailable) 

[Shape.SourceReference](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FSourceReference) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class RolledWebFlangeShape : RolledShape
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FRolledWebFlangeShape%5FFlangeBevel)FlangeBevel

The bevel angle on the flange

##### Declaration

```
public double FlangeBevel { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRolledWebFlangeShape%5FFlangeGage)FlangeGage

The distance between the gage line on both flanges, half of this value would be the distance from the center of the web to either gage line.

##### Declaration

```
public double FlangeGage { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRolledWebFlangeShape%5FFlangeThickness)FlangeThickness

The thickness of the flange

##### Declaration

```
public double FlangeThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRolledWebFlangeShape%5FFlangeWidth)FlangeWidth

The width of the flange

##### Declaration

```
public double FlangeWidth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRolledWebFlangeShape%5FKDesign)KDesign

The width of the fillet measured from the outside of the flange to the edge of the fillet. This is a "design" value and reflects the minimum fillet size for worn rollers.

##### Declaration

```
public double KDesign { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRolledWebFlangeShape%5FKDetail)KDetail

The width of the fillet measured from the outside of the flange to the edge of the fillet. This is a "detail" value and reflects the maximum fillet size.

##### Declaration

```
public double KDetail { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRolledWebFlangeShape%5FRadius)Radius

The radius on the flange/web

##### Declaration

```
public double Radius { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRolledWebFlangeShape%5FWebThickness)WebThickness

The thickness of the web

##### Declaration

```
public double WebThickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FRolledWebFlangeShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base for shapes with I or H profiles, C profiles and T profiles. These shapes share all of these profile properties.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[RolledShape.Dispose(bool)](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FDispose%5FSystem%5FBoolean%5F)