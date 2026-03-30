# Class WeldList.WeldListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

WeldList.WeldListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[Weld](DesignData.SDS2.Model.Weld.html)\>

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
public sealed class WeldList.WeldListEnumerator : IEnumerator<Weld>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FWeldListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FWeldList%5F)WeldListEnumerator(WeldList)

##### Declaration

```
public WeldListEnumerator(WeldList collection)
```

##### Parameters

| Type                                            | Name       | Description |
| ----------------------------------------------- | ---------- | ----------- |
| [WeldList](DesignData.SDS2.Model.WeldList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FWeldListEnumerator%5FCurrent)Current

##### Declaration

```
public Weld Current { get; }
```

##### Property Value

| Type                                    | Description |
| --------------------------------------- | ----------- |
| [Weld](DesignData.SDS2.Model.Weld.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FWeldListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FWeldListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWeldList%5FWeldListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)