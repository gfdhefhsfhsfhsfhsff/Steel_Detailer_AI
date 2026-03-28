# Class NotAddedException 

This is thrown when an attempt to set an object's data without first adding it to a transaction. It's necessary to add things to transactions so they can be locked and refreshed.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Exception](https://learn.microsoft.com/dotnet/api/system.exception)

[ApplicationException](https://learn.microsoft.com/dotnet/api/system.applicationexception)

NotAddedException

##### Implements

[ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)

##### Inherited Members

[Exception.GetBaseException()](https://learn.microsoft.com/dotnet/api/system.exception.getbaseexception) 

[Exception.ToString()](https://learn.microsoft.com/dotnet/api/system.exception.tostring) 

[Exception.GetType()](https://learn.microsoft.com/dotnet/api/system.exception.gettype) 

[Exception.TargetSite](https://learn.microsoft.com/dotnet/api/system.exception.targetsite) 

[Exception.Message](https://learn.microsoft.com/dotnet/api/system.exception.message) 

[Exception.Data](https://learn.microsoft.com/dotnet/api/system.exception.data) 

[Exception.InnerException](https://learn.microsoft.com/dotnet/api/system.exception.innerexception) 

[Exception.HelpLink](https://learn.microsoft.com/dotnet/api/system.exception.helplink) 

[Exception.Source](https://learn.microsoft.com/dotnet/api/system.exception.source) 

[Exception.HResult](https://learn.microsoft.com/dotnet/api/system.exception.hresult) 

[Exception.StackTrace](https://learn.microsoft.com/dotnet/api/system.exception.stacktrace) 

[Exception.SerializeObjectState](https://learn.microsoft.com/dotnet/api/system.exception.serializeobjectstate) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Exceptions](DesignData.SDS2.Exceptions.html)

###### **Assembly**: DesignData.SDS2.Exceptions.dll

##### Syntax

```
public class NotAddedException : ApplicationException, ISerializable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FExceptions%5FNotAddedException%5F%5Fctor%5FSystem%5FString%5F)NotAddedException(string)

This is thrown when an attempt to set an object's data without first adding it to a transaction. It's necessary to add things to transactions so they can be locked and refreshed.

##### Declaration

```
public NotAddedException(string message)
```

##### Parameters

| Type                                                           | Name    | Description |
| -------------------------------------------------------------- | ------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | message |             |

### [](#implements)Implements

[ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)