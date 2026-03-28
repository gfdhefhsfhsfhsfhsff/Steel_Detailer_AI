# Class NoteCommentList.NoteCommentListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

NoteCommentList.NoteCommentListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[NoteComment](DesignData.SDS2.Model.NoteComment.html)\>

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator)

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

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
public sealed class NoteCommentList.NoteCommentListEnumerator : IEnumerator<NoteComment>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FNoteCommentListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FNoteCommentList%5F)NoteCommentListEnumerator(NoteCommentList)

##### Declaration

```
public NoteCommentListEnumerator(NoteCommentList collection)
```

##### Parameters

| Type                                                          | Name       | Description |
| ------------------------------------------------------------- | ---------- | ----------- |
| [NoteCommentList](DesignData.SDS2.Model.NoteCommentList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FNoteCommentListEnumerator%5FCurrent)Current

##### Declaration

```
public NoteComment Current { get; }
```

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [NoteComment](DesignData.SDS2.Model.NoteComment.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FNoteCommentListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FNoteCommentListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FNoteCommentList%5FNoteCommentListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)