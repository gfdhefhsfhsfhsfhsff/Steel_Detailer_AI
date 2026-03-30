# Class GroupMember 

A GroupMember associates submembers that will be detailed as a single member with one piecemark.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

GroupMember

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class GroupMember
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FCustomPropertyMapHandle)CustomPropertyMapHandle

A handle to the custom properties for this group member.

##### Declaration

```
public CustomPropertyMapHandle CustomPropertyMapHandle { get; }
```

##### Property Value

| Type                                                                             | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [CustomPropertyMapHandle](DesignData.SDS2.Database.CustomPropertyMapHandle.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FDescription)Description

Description in the bill of material

##### Declaration

```
public string Description { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                                      |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when setting description with a string that is too long or if the group member handle is invalid. |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the group member without having added it to a transaction                                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked                       |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FGuid)Guid

The uuid or guid representing this group member

##### Declaration

```
public Guid? Guid { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [Guid](https://learn.microsoft.com/dotnet/api/system.guid)? |             |

##### Exceptions

| Type                                                                           | Condition                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FHandle)Handle

A handle for this group member

##### Declaration

```
public GroupMemberHandle Handle { get; }
```

##### Property Value

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FIsGalvanized)IsGalvanized

True iff the group members is marked as galvanized

##### Declaration

```
public bool IsGalvanized { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FIsMainViewLockedToMainMember)IsMainViewLockedToMainMember

True iff the group's main member view should be used as the group's main view

##### Declaration

```
public bool IsMainViewLockedToMainMember { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid.                                    |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the group member without having added it to a transaction                    |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FIsMarkedForDetailing)IsMarkedForDetailing

True iff the group member is marked for detailing. This can always be set to true, but in some cases setting it to false will fail. The underlying flag will be set, but since it would still appear on the list of groups to detail this flag will still show as true.

##### Declaration

```
public bool IsMarkedForDetailing { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid.                                    |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the group member without having added it to a transaction                    |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FMainMemberHandle)MainMemberHandle

A handle to the main member of this group member

##### Declaration

```
public MemberHandle MainMemberHandle { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                                                                               |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown when setting the main member to a member that is not currently in the group's submembers or if the group member handle is invalid. |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the group member without having added it to a transaction                                                                                   |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked                                                                |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FPiecemark)Piecemark

The piecemark of the group member.

##### Declaration

```
public string Piecemark { get; }
```

##### Property Value

| Type                                                           | Description             |
| -------------------------------------------------------------- | ----------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | A UTF-8 encoded string. |

##### Exceptions

| Type                                                                           | Condition                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FPiecemarkMemberHandle)PiecemarkMemberHandle

A handle to the member that displays the piecemark in erection views for this group member

##### Declaration

```
public MemberHandle PiecemarkMemberHandle { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                                                                               |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown when setting the main member to a member that is not currently in the group's submembers or if the group member handle is invalid. |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the group member without having added it to a transaction                                                                                   |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked                                                                |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FShouldMaterialMarksBeOnDetail)ShouldMaterialMarksBeOnDetail

True iff all material marks should be shown on the detail

##### Declaration

```
public bool ShouldMaterialMarksBeOnDetail { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid.                                    |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the group member without having added it to a transaction                    |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FShouldOrganizeBOMBySubmember)ShouldOrganizeBOMBySubmember

True iff the bill of material should be organized by submember, with submaterials, shop bolts, and field bolts listed together with their associated submember.

##### Declaration

```
public bool ShouldOrganizeBOMBySubmember { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid.                                    |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the group member without having added it to a transaction                    |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FShouldSectionSizesBeOnDetail)ShouldSectionSizesBeOnDetail

True iff all section sizes should be shown on the detail

##### Declaration

```
public bool ShouldSectionSizesBeOnDetail { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid.                                    |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the group member without having added it to a transaction                    |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FShouldSubmemberMarksBeOnDetail)ShouldSubmemberMarksBeOnDetail

True iff submember marks should be shown on the detail

##### Declaration

```
public bool ShouldSubmemberMarksBeOnDetail { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid.                                    |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown when setting data on the group member without having added it to a transaction                    |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A GroupMember associates submembers that will be detailed as a single member with one piecemark.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FEquals%5FSystem%5FObject%5F)Equals(object)

A GroupMember associates submembers that will be detailed as a single member with one piecemark.

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

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FFinalize)\~GroupMember()

A GroupMember associates submembers that will be detailed as a single member with one piecemark.

##### Declaration

```
protected ~GroupMember()
```

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FGet%5FDesignData%5FSDS2%5FDatabase%5FGroupMemberHandle%5F)Get(GroupMemberHandle)

Get a GroupMember object for the GroupMemberHandle passed in.

##### Declaration

```
public static GroupMember Get(GroupMemberHandle handle)
```

##### Parameters

| Type                                                                 | Name   | Description |
| -------------------------------------------------------------------- | ------ | ----------- |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html) | handle |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [GroupMember](DesignData.SDS2.Model.GroupMember.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FGetHashCode)GetHashCode()

A GroupMember associates submembers that will be detailed as a single member with one piecemark.

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

##### Remarks

This hash (and Equals) does not include submembers. It does include the piecemark and all other group member properties.

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FGetSubmemberHandles)GetSubmemberHandles()

Handles to all the submembers of the group member

##### Declaration

```
public MemberHandleList GetSubmemberHandles()
```

##### Returns

| Type                                                               | Description |
| ------------------------------------------------------------------ | ----------- |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FIsSubmember%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F)IsSubmember(MemberHandle)

True iff the member is a submember of the group

##### Declaration

```
public bool IsSubmember(MemberHandle arg0)
```

##### Parameters

| Type                                                       | Name | Description |
| ---------------------------------------------------------- | ---- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) | arg0 |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the group member handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FRefreshDatabaseTable)RefreshDatabaseTable()

Refresh the the primary table for objects of this type.

##### Declaration

```
public static void RefreshDatabaseTable()
```

#### [](#DesignData%5FSDS2%5FModel%5FGroupMember%5FSetPiecemark%5FSystem%5FString%5F)SetPiecemark(string)

Set a user piecemark to override the system generated piecemark for this group. If other groups shared this system mark, this will split them apart. To recombine them, the same user mark has to be set on those groups.

```
         By setting a user piecemark you opt this group out of
         system piecemarking and piecemark matching/batching.

```

##### Declaration

```
public void SetPiecemark(string userPiecemark)
```

##### Parameters

| Type                                                           | Name          | Description |
| -------------------------------------------------------------- | ------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | userPiecemark |             |