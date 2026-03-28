# Class Fabricator 

Setup options for the job that relate directly to fabrication

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Fabricator

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class Fabricator
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FArePrimaryDimensionUnitsLocked)ArePrimaryDimensionUnitsLocked

Specifies if the primary dimension format is locked to the units implied by the PrimaryDimensionFormat.

##### Declaration

```
public bool ArePrimaryDimensionUnitsLocked { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FCategoryDefinitions)CategoryDefinitions

Get list of available category definitions for members.

##### Declaration

```
public CategoryDefinitionList CategoryDefinitions { get; }
```

##### Property Value

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [CategoryDefinitionList](DesignData.SDS2.Setup.CategoryDefinitionList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FCustomContinuousTread)CustomContinuousTread

Get a Custom Continuous Plate Tread based on the Continuous Plate Tread located in Fabricator Setup.

##### Declaration

```
public CustomContinuousTread CustomContinuousTread { get; }
```

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [CustomContinuousTread](DesignData.SDS2.Setup.CustomContinuousTread.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FCustomGratingTread)CustomGratingTread

Get a Custom Grating Tread based on the Grating Tread located in Fabricator Setup.

##### Declaration

```
public CustomGratingTread CustomGratingTread { get; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [CustomGratingTread](DesignData.SDS2.Setup.CustomGratingTread.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FCustomPanTread)CustomPanTread

Get a Custom Pan Tread based on the Pan Tread located in Fabricator Setup.

##### Declaration

```
public CustomPanTread CustomPanTread { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [CustomPanTread](DesignData.SDS2.Setup.CustomPanTread.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FCustomPlateTread)CustomPlateTread

Get a Custom Independent Plate Tread based on the Independent Plate Tread located in Fabricator Setup.

##### Declaration

```
public CustomPlateTread CustomPlateTread { get; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [CustomPlateTread](DesignData.SDS2.Setup.CustomPlateTread.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FEvuDefaults)EvuDefaults

Returns a ErectionViewDefaults object that can be used to read/write the Fabricator defaults settings for erection view drawings.

##### Declaration

```
public ErectionViewDefaults EvuDefaults { get; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [ErectionViewDefaults](DesignData.SDS2.Setup.ErectionViewDefaults.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FGroupMemberDimensioningDefaults)GroupMemberDimensioningDefaults

Returns a MemberAnnotationDimensioningDefaults object that can be used to read/write Fabricator annotation and dimensioning defaults for group members.

##### Declaration

```
public GroupMemberAnnotationDimensioningDefaults GroupMemberDimensioningDefaults { get; }
```

##### Property Value

| Type                                                                                                              | Description |
| ----------------------------------------------------------------------------------------------------------------- | ----------- |
| [GroupMemberAnnotationDimensioningDefaults](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FHandle)Handle

The handle for this fabricator

##### Declaration

```
public FabricatorHandle Handle { get; }
```

##### Property Value

| Type                                                               | Description |
| ------------------------------------------------------------------ | ----------- |
| [FabricatorHandle](DesignData.SDS2.Database.FabricatorHandle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FImperialDimensionPrecision)ImperialDimensionPrecision

Specifies the inch dimension precision during formatting. For example if precision is set to 1.0/16.0 in an imperial job with PrimaryDimensionFormat.FT\_IN\_FRAC a distance of (1.0/16.0 + .0001) will format to "1/16"

##### Declaration

```
public double ImperialDimensionPrecision { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FMaterialDescriptions)MaterialDescriptions

Default material descriptions, based on member type, from fabricator setup

##### Declaration

```
public MaterialDescriptions MaterialDescriptions { get; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [MaterialDescriptions](DesignData.SDS2.Setup.MaterialDescriptions.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FMemberDimensioningDefaults)MemberDimensioningDefaults

Returns a MemberAnnotationDimensioningDefaults object that can be used to read/write Fabricator annotation and dimensioning defaults for members.

##### Declaration

```
public MemberAnnotationDimensioningDefaults MemberDimensioningDefaults { get; }
```

##### Property Value

| Type                                                                                                    | Description |
| ------------------------------------------------------------------------------------------------------- | ----------- |
| [MemberAnnotationDimensioningDefaults](DesignData.SDS2.Setup.MemberAnnotationDimensioningDefaults.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FMetricDimensionPrecision)MetricDimensionPrecision

Specifies the millimeter dimension precision during formatting. For example if precision is set to 1.0/25.4 in a metric job with PrimaryDimensionFormat.MM a distance of 1.1mm will format to "1".

##### Declaration

```
public double MetricDimensionPrecision { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FPrimaryDimensionFormat)PrimaryDimensionFormat

The primary dimension format. The resulting DimensionFormat is restricted to the subset of values that are displayed in Fabricator Setup->Drawing Cosmetics->Primary Dimensions, i.e. MM, FT\_IN\_FRAC, IN\_SIX, IN\_FRAC, or IN\_DECIMAL

##### Declaration

```
public DimensionFormat PrimaryDimensionFormat { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [DimensionFormat](DesignData.SDS2.Setup.DimensionFormat.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FRoutingDefinitions)RoutingDefinitions

Get the table of routing definitions. The first index is the Route1 list, the second Route2, and so on.

##### Declaration

```
public RoutingDefinitionTableList RoutingDefinitions { get; }
```

##### Property Value

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [RoutingDefinitionTableList](DesignData.SDS2.Setup.RoutingDefinitionTableList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FStairTreads)StairTreads

Get the list of Stair Treads from Fabricator Setup.

##### Declaration

```
public StairTreadList StairTreads { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [StairTreadList](DesignData.SDS2.Setup.StairTreadList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FSubmaterialDimensioningDefaults)SubmaterialDimensioningDefaults

Returns a MemberAnnotationDimensioningDefaults object that can be used to read/write Fabricator annotation and dimensioning defaults for submaterials.

##### Declaration

```
public SubmaterialAnnotationDimensioningDefaults SubmaterialDimensioningDefaults { get; }
```

##### Property Value

| Type                                                                                                              | Description |
| ----------------------------------------------------------------------------------------------------------------- | ----------- |
| [SubmaterialAnnotationDimensioningDefaults](DesignData.SDS2.Setup.SubmaterialAnnotationDimensioningDefaults.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FAdd%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F)Add(CategoryDefinition)

Append a CategoryDefinition to the end of the list of definitions.

##### Declaration

```
public void Add(CategoryDefinition categoryDefinition)
```

##### Parameters

| Type                                                                | Name               | Description |
| ------------------------------------------------------------------- | ------------------ | ----------- |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html) | categoryDefinition |             |

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html)         | Thrown if null is passed into this method                                                                                                                                                         |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown if this is called outside of a transaction, or if the Fabricator has not been added to the transaction or locked, or if there are already too many CategoryDefinitions in this Fabricator. |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FAdd%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5F)Add(RoutingDefinition)

Append a routing definition so that it can be used on members and materials. If the routing definition already exists this will return false. If it does not it will add it and return true.

##### Declaration

```
public bool Add(RoutingDefinition routingDefinition)
```

##### Parameters

| Type                                                              | Name              | Description |
| ----------------------------------------------------------------- | ----------------- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) | routingDefinition |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Setup options for the job that relate directly to fabrication

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FFinalize)\~Fabricator()

Setup options for the job that relate directly to fabrication

##### Declaration

```
protected ~Fabricator()
```

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FGet)Get()

Get the fabricator object for the currently opened/active job.

##### Declaration

```
public static Fabricator Get()
```

##### Returns

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [Fabricator](DesignData.SDS2.Setup.Fabricator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FToDimension%5FSystem%5FDouble%5FDesignData%5FSDS2%5FSetup%5FDimensionFormat%5F)ToDimension(double, DimensionFormat)

Returns a dimension string with the specified format subject to the setup values for ImperialDimensionPrecision, MetricDimensionPrecision, and ArePrimaryDimensionUnitsLocked.

##### Declaration

```
public string ToDimension(double inches, DimensionFormat format = DimensionFormat.DIM)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | inches |             |
| [DimensionFormat](DesignData.SDS2.Setup.DimensionFormat.html)  | format |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FFabricator%5FToInches%5FSystem%5FString%5FDesignData%5FSDS2%5FSetup%5FDimensionFormat%5F)ToInches(string, DimensionFormat)

Returns the inches specified by the dimension string. The format determines the units when they are not explicitly noted in the dimension.

##### Declaration

```
public double ToInches(string dimension, DimensionFormat format = DimensionFormat.DIM)
```

##### Parameters

| Type                                                           | Name      | Description |
| -------------------------------------------------------------- | --------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | dimension |             |
| [DimensionFormat](DesignData.SDS2.Setup.DimensionFormat.html)  | format    |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                               |
| ------------------------------------------------------------------------------ | ------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown when the entire dimension string can't be parsed |