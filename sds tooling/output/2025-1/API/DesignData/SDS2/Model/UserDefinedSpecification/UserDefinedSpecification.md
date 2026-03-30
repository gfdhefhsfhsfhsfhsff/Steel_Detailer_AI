# Class UserDefinedSpecification 

Defines the connection specification for a user defined connection. This is only ever an InputSpecification, the DesignedSpecification that results will match the kind of connection specified by the UDC chosen here, or possibly something different if applying that connection as an input would result in a change (for example, a shear tab because a clip angle was chosen on a non-perpindicular beam connection).

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

UserDefinedSpecification

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
public sealed class UserDefinedSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedSpecification%5F%5Fctor)UserDefinedSpecification()

A fresh UserDefinedSpecification. Don't forget to set the UserDefinedConnection property

##### Declaration

```
public UserDefinedSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedSpecification%5FUserDefinedConnection)UserDefinedConnection

The underlying definition selected for this user defined connection.

##### Declaration

```
public UserDefinedConnection UserDefinedConnection { get; set; }
```

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [UserDefinedConnection](DesignData.SDS2.Model.UserDefinedConnection.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if this UDC isn't found in the job (this should only occur if there's been some kind of corruption or job switching, users shouldn't need to worry about catching this). It will also be thrown if the set UserDefinedConnection is a null reference. |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Defines the connection specification for a user defined connection. This is only ever an InputSpecification, the DesignedSpecification that results will match the kind of connection specified by the UDC chosen here, or possibly something different if applying that connection as an input would result in a change (for example, a shear tab because a clip angle was chosen on a non-perpindicular beam connection).

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[ConnectionSpecification.Dispose(bool)](DesignData.SDS2.Model.ConnectionSpecification.html#DesignData%5FSDS2%5FModel%5FConnectionSpecification%5FDispose%5FSystem%5FBoolean%5F)