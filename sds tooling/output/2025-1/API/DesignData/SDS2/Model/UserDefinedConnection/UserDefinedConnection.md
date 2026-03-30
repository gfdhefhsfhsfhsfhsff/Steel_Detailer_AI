# Class UserDefinedConnection 

This describes a user defined connection in this model. Every connection using this user defined connection shares this same data (there is one list, by name, of all UserDefinedConnections in each job).

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

UserDefinedConnection

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
public sealed class UserDefinedConnection
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5F%5Fctor%5FSystem%5FString%5F)UserDefinedConnection(string)

This describes a user defined connection in this model. Every connection using this user defined connection shares this same data (there is one list, by name, of all UserDefinedConnections in each job).

##### Declaration

```
public UserDefinedConnection(string name)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FCondition)Condition

The condition this user defined connection is intended to apply in.

##### Declaration

```
public UserDefinedConnectionCondition Condition { get; }
```

##### Property Value

| Type                                                                                        | Description |
| ------------------------------------------------------------------------------------------- | ----------- |
| [UserDefinedConnectionCondition](DesignData.SDS2.Model.UserDefinedConnectionCondition.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FHandle)Handle

The database handle for this object

##### Declaration

```
public UserDefinedConnectionHandle Handle { get; }
```

##### Property Value

| Type                                                                                     | Description |
| ---------------------------------------------------------------------------------------- | ----------- |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FName)Name

Get the name of this UserDefinedConnection object

##### Declaration

```
public string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FAdd%5FDesignData%5FSDS2%5FModel%5FUserDefinedConnection%5F)Add(UserDefinedConnection)

Add a new user defined connection to the current Transaction.

##### Declaration

```
public static void Add(UserDefinedConnection userDefinedConnection)
```

##### Parameters

| Type                                                                      | Name                  | Description |
| ------------------------------------------------------------------------- | --------------------- | ----------- |
| [UserDefinedConnection](DesignData.SDS2.Model.UserDefinedConnection.html) | userDefinedConnection |             |

##### Exceptions

| Type                                                                   | Condition                                                                        |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html) | If there is no Transaction or the Member has already been added to the database. |

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FFinalize)\~UserDefinedConnection()

This describes a user defined connection in this model. Every connection using this user defined connection shares this same data (there is one list, by name, of all UserDefinedConnections in each job).

##### Declaration

```
protected ~UserDefinedConnection()
```

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FFind%5FSystem%5FString%5F)Find(string)

Lookup a UserDefinedConnection class by name.

##### Declaration

```
public static UserDefinedConnection Find(string name)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name |             |

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [UserDefinedConnection](DesignData.SDS2.Model.UserDefinedConnection.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FGet%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandle%5F)Get(UserDefinedConnectionHandle)

Get a full UserDefinedConnection object from a UDC handle

##### Declaration

```
public static UserDefinedConnection Get(UserDefinedConnectionHandle udcHandle)
```

##### Parameters

| Type                                                                                     | Name      | Description |
| ---------------------------------------------------------------------------------------- | --------- | ----------- |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html) | udcHandle |             |

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [UserDefinedConnection](DesignData.SDS2.Model.UserDefinedConnection.html) |             |

##### Exceptions

| Type                                                                           | Condition                   |
| ------------------------------------------------------------------------------ | --------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | thrown if udcHandle is null |

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FGetInputSpecification)GetInputSpecification()

The input specification for this user defined connection, this is applied to the connection on a member end when this user defined connection is used

##### Declaration

```
public ConnectionSpecification GetInputSpecification()
```

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FGetLockable%5FSystem%5FString%5F)GetLockable(string)

Get a single lockable by name. Doing this with the map would work just as well, but this can be more efficient if you just need one.

##### Declaration

```
public Lockable GetLockable(string name)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [Lockable](DesignData.SDS2.Model.Lockable.html) |             |

##### Remarks

This will be a copy of the lockable. If you make changes to it, to see them reflected you will need to pass it to SetLockable

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FGetLockables)GetLockables()

The lockable map for this user defined connection, anything locked here will be locked and set on the member end this is applied to

##### Declaration

```
public LockableDictionary GetLockables()
```

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [LockableDictionary](DesignData.SDS2.Model.LockableDictionary.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FSetInputSpecification%5FDesignData%5FSDS2%5FModel%5FConnectionSpecification%5F)SetInputSpecification(ConnectionSpecification)

Overwrite this specification with a new one, this is only valid for new UserDefinedConnections that you haven't added to the job yet.

```
         We recommend that you set values in Condition before you set this.

```

##### Declaration

```
public void SetInputSpecification(ConnectionSpecification connSpec)
```

##### Parameters

| Type                                                                          | Name     | Description |
| ----------------------------------------------------------------------------- | -------- | ----------- |
| [ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html) | connSpec |             |

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | thrown if this UserDefinedConnection has already been added and committed to the job. The user defined connection list is append only for the API. Also sometimes thrown if the type of this specification does not match the MemberType and MaterialType set in Condition, so set that first. |

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FSetLockable%5FSystem%5FString%5FDesignData%5FSDS2%5FModel%5FLockable%5F)SetLockable(string, Lockable)

Apply a lockable value to this connection. You can only pass in names which would return a non-null lockable from GetLockable (so you can't add new lockable keys this way, you can just replace their value).

##### Declaration

```
public void SetLockable(string name, Lockable value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name  |             |
| [Lockable](DesignData.SDS2.Model.Lockable.html)                | value |             |

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown if this UserDefinedConnection has already been added and comitted to the job. The user defined connection list is append only for the API.                                                                                                                                            |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html)         | Thrown if value is null or if this connection does not have a lockable matching name.                                                                                                                                                                                                        |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown when attempting to override a locked lockable within process. Unless you are implementing an extension of SDS2 (such as a custom member) this does not apply.                                                                                                                         |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)                 | Thrown if this is called without adding both this Component object and the Member it is on to the Transaction. Or if there simply isn't a Transaction.                                                                                                                                       |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html)         | Thrown if the lockable given is not a valid value for this specific lockable. The Message on the InvalidValueException will include the message we'd give to a user if they typed that value on the screen, so it's usable to present directly to a user if your application is interactive. |