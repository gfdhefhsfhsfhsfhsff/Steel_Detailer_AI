# Class GroupMemberAnnotationDimensioningDefaults 

Class for reading/writing annotation and dimensioning defaults for drawings. The Fabricator.GroupMemberAnnotationDimensioningDefaults returns an object that accesses the global settings for members. Group Member drawings return an instance of GroupMemberAnnotationDimensioningDefaults that accesses settings for that drawing.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[AnnotationDimensioningDefaults](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html)

GroupMemberAnnotationDimensioningDefaults

[MemberAnnotationDimensioningDefaults](DesignData.SDS2.Setup.MemberAnnotationDimensioningDefaults.html)

##### Inherited Members

[AnnotationDimensioningDefaults.DetailUsingTemplates](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FDetailUsingTemplates) 

[AnnotationDimensioningDefaults.RemoveSnaplines](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FRemoveSnaplines) 

[AnnotationDimensioningDefaults.VerboseProgressUpdates](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FVerboseProgressUpdates) 

[AnnotationDimensioningDefaults.ShowAppliedTemplates](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FShowAppliedTemplates) 

[AnnotationDimensioningDefaults.ShortenDrawing](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FShortenDrawing) 

[AnnotationDimensioningDefaults.DetailWithRevisions](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FDetailWithRevisions) 

[AnnotationDimensioningDefaults.GenerateNamedLocations](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FGenerateNamedLocations) 

[AnnotationDimensioningDefaults.RmHandrailHssLines](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FRmHandrailHssLines) 

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
public class GroupMemberAnnotationDimensioningDefaults : AnnotationDimensioningDefaults
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FDimensionHolesOnUserMaterial)DimensionHolesOnUserMaterial

Controls whether member detailing will dimension holes on user-created material.

##### Declaration

```
public bool DimensionHolesOnUserMaterial { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FDimensionUserMaterial)DimensionUserMaterial

Controls whether member detailing will generate dimensions on user-created material.

##### Declaration

```
public bool DimensionUserMaterial { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FPreserveExistingAnnotations)PreserveExistingAnnotations

Controls how changes to drawings are preserved if the drawing is regenerated.

##### Declaration

```
public AnnotationPreservationMode PreserveExistingAnnotations { get; set; }
```

##### Property Value

| Type                                                                                | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [AnnotationPreservationMode](DesignData.SDS2.Setup.AnnotationPreservationMode.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FPreserveUserModifiedBOM)PreserveUserModifiedBOM

Controls whether member detailing preserves user modified entries to member bills of material that are re-detailed unless those entries are shown.

##### Declaration

```
public bool PreserveUserModifiedBOM { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FUseGeneratedAnnotations)UseGeneratedAnnotations

Controls whether member detailing will automatically add annotations such as labels, pointers, bevel symbols and weld symbols.

##### Declaration

```
public bool UseGeneratedAnnotations { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FUseGeneratedDimensions)UseGeneratedDimensions

Controls whether member detailing will automatically dimension distances between holes, material edges and work points.

##### Declaration

```
public bool UseGeneratedDimensions { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FUseGeneratedWelds)UseGeneratedWelds

Controls whether member detailing draws weld symbols on details representing 3D welds that appear in modeling.

##### Declaration

```
public bool UseGeneratedWelds { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Class for reading/writing annotation and dimensioning defaults for drawings. The Fabricator.GroupMemberAnnotationDimensioningDefaults returns an object that accesses the global settings for members. Group Member drawings return an instance of GroupMemberAnnotationDimensioningDefaults that accesses settings for that drawing.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[AnnotationDimensioningDefaults.Dispose(bool)](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FDispose%5FSystem%5FBoolean%5F)