# Class PythonException 

Thrown when there's an exception in a python call

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Exception](https://learn.microsoft.com/dotnet/api/system.exception)

[ApplicationException](https://learn.microsoft.com/dotnet/api/system.applicationexception)

PythonException

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
public class PythonException : ApplicationException, ISerializable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FExceptions%5FPythonException%5F%5Fctor%5FSystem%5FString%5FSystem%5FString%5FSystem%5FObject%5FSystem%5FObject%5F)PythonException(string, string, dynamic, dynamic)

Thrown when there's an exception in a python call

##### Declaration

```
public PythonException(string message, string traceback, dynamic pythonExceptionT, dynamic pythonExceptionO)
```

##### Parameters

| Type                                                           | Name             | Description |
| -------------------------------------------------------------- | ---------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | message          |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | traceback        |             |
| dynamic                                                        | pythonExceptionT |             |
| dynamic                                                        | pythonExceptionO |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FExceptions%5FPythonException%5FPythonExceptionInstance)PythonExceptionInstance

The underlying python exception that was thrown. This can be null if a python exception wasn't thrown, but this exception indicates an argument or return value could not be marshalled or an attempt was made to call a non-callable object.

##### Declaration

```
public dynamic PythonExceptionInstance { get; }
```

##### Property Value

| Type    | Description |
| ------- | ----------- |
| dynamic |             |

#### [](#DesignData%5FSDS2%5FExceptions%5FPythonException%5FPythonExceptionType)PythonExceptionType

The type of the underlying python exception (as a python object).

##### Declaration

```
public dynamic PythonExceptionType { get; }
```

##### Property Value

| Type    | Description |
| ------- | ----------- |
| dynamic |             |

#### [](#DesignData%5FSDS2%5FExceptions%5FPythonException%5FPythonTraceback)PythonTraceback

The python stack trace at the exception throw site

##### Declaration

```
public string PythonTraceback { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#implements)Implements

[ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)