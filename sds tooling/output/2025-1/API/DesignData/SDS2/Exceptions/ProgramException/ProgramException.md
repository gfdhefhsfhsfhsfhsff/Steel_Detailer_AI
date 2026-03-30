# Class ProgramException 

Thrown when there's an internal error in SDS/2's native implementation.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Exception](https://learn.microsoft.com/dotnet/api/system.exception)

[ApplicationException](https://learn.microsoft.com/dotnet/api/system.applicationexception)

ProgramException

##### Implements

[ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)

##### Inherited Members

[Exception.GetBaseException()](https://learn.microsoft.com/dotnet/api/system.exception.getbaseexception) 

[Exception.GetObjectData(SerializationInfo, StreamingContext)](https://learn.microsoft.com/dotnet/api/system.exception.getobjectdata) 

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
public class ProgramException : ApplicationException, ISerializable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FExceptions%5FProgramException%5F%5Fctor%5FSystem%5FString%5FSystem%5FString%5F)ProgramException(string, string)

Thrown when there's an internal error in SDS/2's native implementation.

##### Declaration

```
public ProgramException(string message, string backtrace)
```

##### Parameters

| Type                                                           | Name      | Description |
| -------------------------------------------------------------- | --------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | message   |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | backtrace |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FExceptions%5FProgramException%5FBacktrace)Backtrace

The native backtrace that led to this. This can be helpful when reporting this, so that SDS/2 programmers can see how we ran into this error.

##### Declaration

```
public string Backtrace { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#implements)Implements

[ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)