# Class Job 

An SDS2 job, or project.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Job

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class Job
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FCustomPropertyMapHandle)CustomPropertyMapHandle

A handle to the custom properties for this job.

##### Declaration

```
public CustomPropertyMapHandle CustomPropertyMapHandle { get; }
```

##### Property Value

| Type                                                                             | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [CustomPropertyMapHandle](DesignData.SDS2.Database.CustomPropertyMapHandle.html) |             |

##### Exceptions

| Type                                                                       | Condition                                                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html) | If Open() hasn't been called on this job, or if that call returned false, or if another job has been Opened since this one was. |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FDefault)Default

The identifier for the currently selected job for the user running your software. This is the job they would see by just opening SDS2.

##### Declaration

```
public static Identifier Default { get; }
```

##### Property Value

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [Identifier](DesignData.SDS2.Database.Identifier.html) |             |

##### Remarks

You need to have opened a DataDirectory before calling this.

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FMajorVersion)MajorVersion

Returns the human readable major data version of the Job. This can be used to prevent opening an unconverted Job. It checks the Job's data version without needing to open the job.

##### Declaration

```
public int MajorVersion { get; }
```

##### Property Value

| Type                                                       | Description                        |
| ---------------------------------------------------------- | ---------------------------------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | The major data version of the job. |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FMembers)Members

Get a list of all members in the job.

##### Declaration

```
public MemberHandleList Members { get; }
```

##### Property Value

| Type                                                               | Description                                                           |
| ------------------------------------------------------------------ | --------------------------------------------------------------------- |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html) | A list of member objects representing every active member in the job. |

##### Remarks

This can be slow in large jobs, especially if it's called repeatedly.

##### Exceptions

| Type                                                                       | Condition                                                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html) | If Open() hasn't been called on this job, or if that call returned false, or if another job has been Opened since this one was. |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FMinorVersion)MinorVersion

Returns the human readable minor data version of the Job. This can be used to prevent opening an unconverted Job. It checks the Job's data version without needing to open the job.

##### Declaration

```
public int MinorVersion { get; }
```

##### Property Value

| Type                                                       | Description                        |
| ---------------------------------------------------------- | ---------------------------------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | The minor data version of the job. |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FUserDefinedConnections)UserDefinedConnections

Get a list of all UDC (user defined connection) handles in this job.

You can get real DesignData.SDS2.Model.UserDefinedConnection objects by using the static Get method on that object, passing one UserDefinedConnectionHandle to it.

##### Declaration

```
public UserDefinedConnectionHandleList UserDefinedConnections { get; }
```

##### Property Value

| Type                                                                                             | Description |
| ------------------------------------------------------------------------------------------------ | ----------- |
| [UserDefinedConnectionHandleList](DesignData.SDS2.Database.UserDefinedConnectionHandleList.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

An SDS2 job, or project.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FFinalize)\~Job()

An SDS2 job, or project.

##### Declaration

```
protected ~Job()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FFindJob%5FDesignData%5FSDS2%5FDatabase%5FIdentifier%5F)FindJob(Identifier)

Find a job on the system based on a job identifier.

##### Declaration

```
public static Job FindJob(Identifier id)
```

##### Parameters

| Type                                                   | Name | Description                                                                                                                            |
| ------------------------------------------------------ | ---- | -------------------------------------------------------------------------------------------------------------------------------------- |
| [Identifier](DesignData.SDS2.Database.Identifier.html) | id   | The job identifier used to find a job on the system. This includes the name of the job and the repository this job should be found in. |

##### Returns

| Type                                     | Description |
| ---------------------------------------- | ----------- |
| [Job](DesignData.SDS2.Database.Job.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FGetDrawingHandles%5FDesignData%5FSDS2%5FDatabase%5FTableWithDrawings%5F)GetDrawingHandles(TableWithDrawings)

Get all drawing handles for a particular table

##### Declaration

```
public DrawingHandleList GetDrawingHandles(TableWithDrawings table)
```

##### Parameters

| Type                                                                 | Name  | Description |
| -------------------------------------------------------------------- | ----- | ----------- |
| [TableWithDrawings](DesignData.SDS2.Database.TableWithDrawings.html) | table |             |

##### Returns

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [DrawingHandleList](DesignData.SDS2.Database.DrawingHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FGetGridLineHandles)GetGridLineHandles()

Get a list of all grid lines in the job.

##### Declaration

```
public GridLineHandleList GetGridLineHandles()
```

##### Returns

| Type                                                                   | Description                                                                 |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [GridLineHandleList](DesignData.SDS2.Database.GridLineHandleList.html) | A list of grid line handles representing every active grid line in the job. |

##### Exceptions

| Type                                                                       | Condition                                                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html) | If Open() hasn't been called on this job, or if that call returned false, or if another job has been Opened since this one was. |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FGetGroupMemberHandles)GetGroupMemberHandles()

Get a list of all group members in the job.

##### Declaration

```
public GroupMemberHandleList GetGroupMemberHandles()
```

##### Returns

| Type                                                                         | Description                                                                       |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [GroupMemberHandleList](DesignData.SDS2.Database.GroupMemberHandleList.html) | A list of group member handles representing every active group member in the job. |

##### Exceptions

| Type                                                                       | Condition                                                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html) | If Open() hasn't been called on this job, or if that call returned false, or if another job has been Opened since this one was. |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FGetNoteHandles)GetNoteHandles()

Get a list of all note handles in the job.

##### Declaration

```
public NoteHandleList GetNoteHandles()
```

##### Returns

| Type                                                           | Description                                                       |
| -------------------------------------------------------------- | ----------------------------------------------------------------- |
| [NoteHandleList](DesignData.SDS2.Database.NoteHandleList.html) | A list of note handles representing every active note in the job. |

##### Exceptions

| Type                                                                       | Condition                                                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html) | If Open() hasn't been called on this job, or if that call returned false, or if another job has been Opened since this one was. |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FGroupsForMember%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F)GroupsForMember(MemberHandle)

All the GroupMemberHandles where a member is a submember

##### Declaration

```
public GroupMemberHandleList GroupsForMember(MemberHandle arg0)
```

##### Parameters

| Type                                                       | Name | Description |
| ---------------------------------------------------------- | ---- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) | arg0 |             |

##### Returns

| Type                                                                         | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [GroupMemberHandleList](DesignData.SDS2.Database.GroupMemberHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FJob%5FOpen)Open()

Open this job and make it the current Job. This is required before you can begin accessing data inside this job. SDS2 can only have one job open at a time, so calling this on one job necessarily closed any already opened job. There is no need to explicitly close the job later.

##### Declaration

```
public bool Open()
```

##### Returns

| Type                                                          | Description                                                                                                                                 |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | true if the job has been successfully opened and is ready for access, or false if something went wrong and the job is not ready for access. |