# Class NamedColorList.NamedColorListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

NamedColorList.NamedColorListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[NamedColor](DesignData.SDS2.Setup.NamedColor.html)\>

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
public sealed class NamedColorList.NamedColorListEnumerator : IEnumerator<NamedColor>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FNamedColorListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FNamedColorList%5F)NamedColorListEnumerator(NamedColorList)

##### Declaration

```
public NamedColorListEnumerator(NamedColorList collection)
```

##### Parameters

| Type                                                        | Name       | Description |
| ----------------------------------------------------------- | ---------- | ----------- |
| [NamedColorList](DesignData.SDS2.Setup.NamedColorList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FNamedColorListEnumerator%5FCurrent)Current

##### Declaration

```
public NamedColor Current { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [NamedColor](DesignData.SDS2.Setup.NamedColor.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FNamedColorListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FNamedColorListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FNamedColorList%5FNamedColorListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)