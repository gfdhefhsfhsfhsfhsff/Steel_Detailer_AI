# Class MaterialOperationList.MaterialOperationListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialOperationList.MaterialOperationListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html)\>

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator)

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

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
public sealed class MaterialOperationList.MaterialOperationListEnumerator : IEnumerator<MaterialOperation>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FMaterialOperationListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FMaterialOperationList%5F)MaterialOperationListEnumerator(MaterialOperationList)

##### Declaration

```
public MaterialOperationListEnumerator(MaterialOperationList collection)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [MaterialOperationList](DesignData.SDS2.Model.MaterialOperationList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FMaterialOperationListEnumerator%5FCurrent)Current

##### Declaration

```
public MaterialOperation Current { get; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [MaterialOperation](DesignData.SDS2.Model.MaterialOperation.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FMaterialOperationListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FMaterialOperationListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterialOperationList%5FMaterialOperationListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)