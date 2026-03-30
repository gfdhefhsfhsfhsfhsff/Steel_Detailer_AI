# Class NoteComment 

Notes are for authoring and reviewing comments related the the model or to the project.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

NoteComment

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
public sealed class NoteComment
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FNoteComment%5F%5Fctor)NoteComment()

Notes are for authoring and reviewing comments related the the model or to the project.

##### Declaration

```
public NoteComment()
```

#### [](#DesignData%5FSDS2%5FModel%5FNoteComment%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FNoteComment%5F)NoteComment(NoteComment)

Notes are for authoring and reviewing comments related the the model or to the project.

##### Declaration

```
public NoteComment(NoteComment arg0)
```

##### Parameters

| Type                                                  | Name | Description |
| ----------------------------------------------------- | ---- | ----------- |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html) | arg0 |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FNoteComment%5FAuthor)Author

The author information associated with a comment

##### Declaration

```
public string Author { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteComment%5FComment)Comment

The comment information associated with a comment

##### Declaration

```
public string Comment { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteComment%5FDate)Date

The date information associated with a comment

##### Declaration

```
public string Date { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FNoteComment%5FFinalize)\~NoteComment()

Notes are for authoring and reviewing comments related the the model or to the project.

##### Declaration

```
protected ~NoteComment()
```

#### [](#DesignData%5FSDS2%5FModel%5FNoteComment%5FSetAuthorUser)SetAuthorUser()

Set the Author string to the user's name

##### Declaration

```
public void SetAuthorUser()
```

#### [](#DesignData%5FSDS2%5FModel%5FNoteComment%5FSetDateNow)SetDateNow()

Set the Date string to the formatted current local time

##### Declaration

```
public void SetDateNow()
```