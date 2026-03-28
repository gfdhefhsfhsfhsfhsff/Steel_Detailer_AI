# Class Module 

Access to python modules

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Module

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Python](DesignData.SDS2.Python.html)

###### **Assembly**: DesignData.SDS2.Python.dll

##### Syntax

```
public sealed class Module
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPython%5FModule%5F%5Fctor)Module()

Access to python modules

##### Declaration

```
public Module()
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPython%5FModule%5FFinalize)\~Module()

Access to python modules

##### Declaration

```
protected ~Module()
```

#### [](#DesignData%5FSDS2%5FPython%5FModule%5FImport%5FSystem%5FString%5F)Import(string)

Import a python module and return that module. You can then reference classes inside the module:

##### Declaration

```
public static dynamic Import(string module)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | module |             |

##### Returns

| Type    | Description |
| ------- | ----------- |
| dynamic |             |

##### Examples

```
dynamic module = Python.Module.Import("my_module");
dynamic cls_instance = module.MyClass("an argument for the constructor");
```

##### Exceptions

| Type                                                               | Condition                                                                                                                 |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| [PythonException](DesignData.SDS2.Exceptions.PythonException.html) | If the module doesn't exist, or can't be imported, a python exception may occur and will be translated to PythonException |