# Class AnnotationDimensioningDefaults 

Base class for reading/writing annotation and dimensioning defaults for drawings.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

AnnotationDimensioningDefaults

[GroupMemberAnnotationDimensioningDefaults](DesignData.SDS2.Setup.GroupMemberAnnotationDimensioningDefaults.html)

[SubmaterialAnnotationDimensioningDefaults](DesignData.SDS2.Setup.SubmaterialAnnotationDimensioningDefaults.html)

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
public class AnnotationDimensioningDefaults
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FDetailUsingTemplates)DetailUsingTemplates

Controls whether member detailing will apply templates stored in the fabs folder.

##### Declaration

```
public bool DetailUsingTemplates { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FDetailWithRevisions)DetailWithRevisions

Controls whether member detailing clouds change on the affected detail per "Method to be used for clouding changes on details".

##### Declaration

```
public bool DetailWithRevisions { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FGenerateNamedLocations)GenerateNamedLocations

Controls whether each resulting member detail will include named locations.

##### Declaration

```
public bool GenerateNamedLocations { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FRemoveSnaplines)RemoveSnaplines

Controls whether snaplines are removed before the drawing is shortened.

##### Declaration

```
public bool RemoveSnaplines { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FRmHandrailHssLines)RmHandrailHssLines

Controls whether member detailing automatically removes hidden lines from HSS materials on custom handrail members.

##### Declaration

```
public bool RmHandrailHssLines { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FShortenDrawing)ShortenDrawing

Controls whether member detailing automatically shortens the details of the members.

##### Declaration

```
public bool ShortenDrawing { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FShowAppliedTemplates)ShowAppliedTemplates

Controls whether member detailing will generate a label which names the templates that have been applied to the drawing.

##### Declaration

```
public bool ShowAppliedTemplates { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FVerboseProgressUpdates)VerboseProgressUpdates

Controls whether the progress bar window will display the name of each template as it is applied.

##### Declaration

```
public bool VerboseProgressUpdates { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base class for reading/writing annotation and dimensioning defaults for drawings.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FAnnotationDimensioningDefaults%5FFinalize)\~AnnotationDimensioningDefaults()

Base class for reading/writing annotation and dimensioning defaults for drawings.

##### Declaration

```
protected ~AnnotationDimensioningDefaults()
```