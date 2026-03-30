# Class CNC\_ConfigurationList.CNC\_ConfigurationListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CNC\_ConfigurationList.CNC\_ConfigurationListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html)\>

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator)

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Detail](DesignData.SDS2.Detail.html)

###### **Assembly**: DesignData.SDS2.Detail.dll

##### Syntax

```
public sealed class CNC_ConfigurationList.CNC_ConfigurationListEnumerator : IEnumerator<CNC_Configuration>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FCNC%5FConfigurationListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5F)CNC\_ConfigurationListEnumerator(CNC\_ConfigurationList)

##### Declaration

```
public CNC_ConfigurationListEnumerator(CNC_ConfigurationList collection)
```

##### Parameters

| Type                                                                          | Name       | Description |
| ----------------------------------------------------------------------------- | ---------- | ----------- |
| [CNC\_ConfigurationList](DesignData.SDS2.Detail.CNC%5FConfigurationList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FCNC%5FConfigurationListEnumerator%5FCurrent)Current

##### Declaration

```
public CNC_Configuration Current { get; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [CNC\_Configuration](DesignData.SDS2.Detail.CNC%5FConfiguration.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FCNC%5FConfigurationListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FCNC%5FConfigurationListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FCNC%5FConfigurationList%5FCNC%5FConfigurationListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)