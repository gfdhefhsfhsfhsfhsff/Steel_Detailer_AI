# Class MemberAnnotationDimensioningDefaults 

Class for reading/writing annotation and dimensioning defaults for drawings. The Fabricator.MemberAnnotationDimensioningDefaults returns an object that accesses the global settings for members. Member drawings return an instance of MemberAnnotationDimensioningDefaults that accesses settings for that drawing.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[AnnotationDimensioningDefaults](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html)

[GroupMemberAnnotationDimensioningDefaults](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html)

MemberAnnotationDimensioningDefaults

##### Inherited Members

[GroupMemberAnnotationDimensioningDefaults.PreserveExistingAnnotations](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FPreserveExistingAnnotations) 

[GroupMemberAnnotationDimensioningDefaults.DimensionUserMaterial](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FDimensionUserMaterial) 

[GroupMemberAnnotationDimensioningDefaults.DimensionHolesOnUserMaterial](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FDimensionHolesOnUserMaterial) 

[GroupMemberAnnotationDimensioningDefaults.UseGeneratedDimensions](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FUseGeneratedDimensions) 

[GroupMemberAnnotationDimensioningDefaults.UseGeneratedAnnotations](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FUseGeneratedAnnotations) 

[GroupMemberAnnotationDimensioningDefaults.UseGeneratedWelds](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FUseGeneratedWelds) 

[GroupMemberAnnotationDimensioningDefaults.PreserveUserModifiedBOM](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FPreserveUserModifiedBOM) 

[AnnotationDimensioningDefaults.DetailUsingTemplates](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FDetailUsingTemplates) 

[AnnotationDimensioningDefaults.RemoveSnaplines](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FRemoveSnaplines) 

[AnnotationDimensioningDefaults.VerboseProgressUpdates](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FVerboseProgressUpdates) 

[AnnotationDimensioningDefaults.ShowAppliedTemplates](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FShowAppliedTemplates) 

[AnnotationDimensioningDefaults.ShortenDrawing](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FShortenDrawing) 

[AnnotationDimensioningDefaults.DetailWithRevisions](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FDetailWithRevisions) 

[AnnotationDimensioningDefaults.GenerateNamedLocations](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FGenerateNamedLocations) 

[AnnotationDimensioningDefaults.RmHandrailHssLines](DesignData.SDS2.Setup.AnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FRmHandrailHssLines) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class MemberAnnotationDimensioningDefaults : GroupMemberAnnotationDimensioningDefaults
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FMemberAnnotationDimensioningDefaults%5FPreserveSystemSetDetailFlags)PreserveSystemSetDetailFlags

When enabled, piecemarks deselected will be automatically re-selected the next time Detail Members is performed.

##### Declaration

```
public bool PreserveSystemSetDetailFlags { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberAnnotationDimensioningDefaults%5FShowNonAnnotatedSystemViews)ShowNonAnnotatedSystemViews

Applies only to system views. Controls whether member detailing includes all system views in the final drawing.

##### Declaration

```
public bool ShowNonAnnotatedSystemViews { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FMemberAnnotationDimensioningDefaults%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Class for reading/writing annotation and dimensioning defaults for drawings. The Fabricator.MemberAnnotationDimensioningDefaults returns an object that accesses the global settings for members. Member drawings return an instance of MemberAnnotationDimensioningDefaults that accesses settings for that drawing.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[GroupMemberAnnotationDimensioningDefaults.Dispose(bool)](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html#DesignData%5FSDS2%5FSetup%5FGroupMemberAnnotationDimensioningDefaults%5FDispose%5FSystem%5FBoolean%5F)