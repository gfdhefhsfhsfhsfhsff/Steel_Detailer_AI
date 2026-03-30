# Class SurfaceFinish 

Surface finish information

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

SurfaceFinish

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class SurfaceFinish
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5F%5Fctor)SurfaceFinish()

Surface finish information

##### Declaration

```
public SurfaceFinish()
```

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FSurfaceFinish%5F)SurfaceFinish(SurfaceFinish)

Copy ctor

##### Declaration

```
public SurfaceFinish(SurfaceFinish src)
```

##### Parameters

| Type                                                      | Name | Description |
| --------------------------------------------------------- | ---- | ----------- |
| [SurfaceFinish](DesignData.SDS2.Setup.SurfaceFinish.html) | src  |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FAbbreviation)Abbreviation

The abbreviation used for the finish

##### Declaration

```
public string Abbreviation { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FAddToBOM)AddToBOM

Add surface finish to Bill of Material?

##### Declaration

```
public bool AddToBOM { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FDisplayName)DisplayName

The display name of the finish. All finishes in setup will have a unique display name

##### Declaration

```
public string DisplayName { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FHideEntry)HideEntry

Hide surface finish entry from menu pulldown-selection?

##### Declaration

```
public bool HideEntry { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FIsGalvanized)IsGalvanized

Is the specified surface finish a type of galvanizing finish?

##### Declaration

```
public bool IsGalvanized { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FMinorSuffix)MinorSuffix

Suffix used to distinguish minor/sub pcmks from standard marks when pcmks are split by surface finish

##### Declaration

```
public string MinorSuffix { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FPreparationProcess)PreparationProcess

Preparations and/or finish process description

##### Declaration

```
public string PreparationProcess { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FSetupIndex)SetupIndex

The index into the setup list of finishes, or -1 if the DisplayName is not in the setup list

##### Declaration

```
public int SetupIndex { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FSource)Source

Source of the finish. For example, a manufacture and/or catalog

##### Declaration

```
public string Source { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FSplitMajor)SplitMajor

Break major/member marks by surface finish?

##### Declaration

```
public bool SplitMajor { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FSplitMinor)SplitMinor

Break minor/material marks by surface finish?

##### Declaration

```
public bool SplitMinor { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FEquals%5FSystem%5FObject%5F)Equals(object)

Surface finish information

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

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FFinalize)\~SurfaceFinish()

Surface finish information

##### Declaration

```
protected ~SurfaceFinish()
```

#### [](#DesignData%5FSDS2%5FSetup%5FSurfaceFinish%5FGetHashCode)GetHashCode()

Surface finish information

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