# Class UserDefinedConnectionHandleList.UserDefinedConnectionHandleListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

UserDefinedConnectionHandleList.UserDefinedConnectionHandleListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html)\>

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator)

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public sealed class UserDefinedConnectionHandleList.UserDefinedConnectionHandleListEnumerator : IEnumerator<UserDefinedConnectionHandle>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FUserDefinedConnectionHandleListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5F)UserDefinedConnectionHandleListEnumerator(UserDefinedConnectionHandleList)

##### Declaration

```
public UserDefinedConnectionHandleListEnumerator(UserDefinedConnectionHandleList collection)
```

##### Parameters

| Type                                                                                             | Name       | Description |
| ------------------------------------------------------------------------------------------------ | ---------- | ----------- |
| [UserDefinedConnectionHandleList](DesignData.SDS2.Database.UserDefinedConnectionHandleList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FUserDefinedConnectionHandleListEnumerator%5FCurrent)Current

##### Declaration

```
public UserDefinedConnectionHandle Current { get; }
```

##### Property Value

| Type                                                                                     | Description |
| ---------------------------------------------------------------------------------------- | ----------- |
| [UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FUserDefinedConnectionHandleListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FUserDefinedConnectionHandleListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FUserDefinedConnectionHandleList%5FUserDefinedConnectionHandleListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)