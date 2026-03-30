# Class Note 

Notes are for authoring and reviewing comments related the the model or to the project.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Note

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public sealed class Note
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FNote%5F%5Fctor)Note()

Notes are for authoring and reviewing comments related the the model or to the project.

##### Declaration

```
public Note()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FColor)Color

The color of the note

##### Declaration

```
public Color Color { get; set; }
```

##### Property Value

| Type                                           | Description |
| ---------------------------------------------- | ----------- |
| [Color](DesignData.SDS2.Primitives.Color.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FComments)Comments

A deep copy of the comments assocated with the note

##### Declaration

```
public NoteCommentList Comments { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [NoteCommentList](DesignData.SDS2.Model.NoteCommentList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FCreateTime)CreateTime

Seconds between when this note was created and the unix epoch, January 1, 1970.

##### Declaration

```
public int CreateTime { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FCreateUser)CreateUser

Name of the user who created the note

##### Declaration

```
public string CreateUser { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FCustomTags)CustomTags

A deep copy of the custom tags assocated with the note. Beware, the user can change actual name of the Custom category. The actual name of this category can be read from the returned object.

##### Declaration

```
public StringList CustomTags { get; set; }
```

##### Property Value

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FDisciplineTags)DisciplineTags

A deep copy of the discipline tags associated with the note. Beware, the user can change actual name of the Discipline category. The actual name of this category can be read from the returned object.

##### Declaration

```
public StringList DisciplineTags { get; set; }
```

##### Property Value

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FIsShownInModel)IsShownInModel

Specifies whether the note has graphics displayed in the model

##### Declaration

```
public bool IsShownInModel { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FLastModifyTime)LastModifyTime

Seconds between when this note was last edited and the unix epoch, January 1, 1970.

##### Declaration

```
public int LastModifyTime { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FLastModifyUser)LastModifyUser

Name of the user who last modified the note

##### Declaration

```
public string LastModifyUser { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FLocation)Location

Location of the note in global coordinates. If the note is associated with a member, then the note's global location moves as the member is moved. However, the location relative to the member remains fixed.

##### Declaration

```
public Point3D Location { get; set; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FMemberHandle)MemberHandle

A handle to the member the note is linked to

##### Declaration

```
public MemberHandle MemberHandle { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FStatusTags)StatusTags

A deep copy of the status tags associated with the note. Beware, the user can change actual name of the Status category. The actual name of this category can be read from the returned object.

##### Declaration

```
public StringList StatusTags { get; set; }
```

##### Property Value

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FSubject)Subject

Subject of the note

##### Declaration

```
public string Subject { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FView)View

The view associated with a note. SDS2 will change to this view when the user clicks on the note the note viewer tool.

##### Declaration

```
public View View { get; set; }
```

##### Property Value

| Type                                    | Description |
| --------------------------------------- | ----------- |
| [View](DesignData.SDS2.Model.View.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FAdd%5FDesignData%5FSDS2%5FModel%5FNote%5F)Add(Note)

Add the view to the current transaction

##### Declaration

```
public static void Add(Note note)
```

##### Parameters

| Type                                    | Name | Description |
| --------------------------------------- | ---- | ----------- |
| [Note](DesignData.SDS2.Model.Note.html) | note |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FAppendComment%5FDesignData%5FSDS2%5FModel%5FNoteComment%5F)AppendComment(NoteComment)

Append the specified comment to the list of comments

##### Declaration

```
public void AppendComment(NoteComment comment)
```

##### Parameters

| Type                                                  | Name    | Description |
| ----------------------------------------------------- | ------- | ----------- |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html) | comment |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FFinalize)\~Note()

Notes are for authoring and reviewing comments related the the model or to the project.

##### Declaration

```
protected ~Note()
```

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FGet%5FDesignData%5FSDS2%5FDatabase%5FNoteHandle%5F)Get(NoteHandle)

Get a Note object for the NoteHandle passed in.

##### Declaration

```
public static Note Get(NoteHandle handle)
```

##### Parameters

| Type                                                   | Name   | Description |
| ------------------------------------------------------ | ------ | ----------- |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html) | handle |             |

##### Returns

| Type                                    | Description |
| --------------------------------------- | ----------- |
| [Note](DesignData.SDS2.Model.Note.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FGetHandle)GetHandle()

A handle for this note. Notes that have not been added to the model will have null handles.

##### Declaration

```
public NoteHandle GetHandle()
```

##### Returns

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [NoteHandle](DesignData.SDS2.Database.NoteHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNote%5FRefreshDatabaseTable)RefreshDatabaseTable()

Refresh the the primary table for objects of this type.

##### Declaration

```
public static void RefreshDatabaseTable()
```