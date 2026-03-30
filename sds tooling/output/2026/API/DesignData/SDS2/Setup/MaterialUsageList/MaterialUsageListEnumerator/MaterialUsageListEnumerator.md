# Class MaterialUsageList.MaterialUsageListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialUsageList.MaterialUsageListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html)\>

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator)

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class MaterialUsageList.MaterialUsageListEnumerator : IEnumerator<MaterialUsage>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FMaterialUsageListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FMaterialUsageList%5F)MaterialUsageListEnumerator(MaterialUsageList)

##### Declaration

```
public MaterialUsageListEnumerator(MaterialUsageList collection)
```

##### Parameters

| Type                                                              | Name       | Description |
| ----------------------------------------------------------------- | ---------- | ----------- |
| [MaterialUsageList](DesignData.SDS2.Setup.MaterialUsageList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FMaterialUsageListEnumerator%5FCurrent)Current

##### Declaration

```
public MaterialUsage Current { get; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [MaterialUsage](DesignData.SDS2.Setup.MaterialUsage.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FMaterialUsageListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FMaterialUsageListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialUsageList%5FMaterialUsageListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)