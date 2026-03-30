# Class PolygonList.PolygonListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

PolygonList.PolygonListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[Polygon](DesignData.SDS2.Primitives.Polygon.html)\>

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator)

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class PolygonList.PolygonListEnumerator : IEnumerator<Polygon>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FPolygonListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPolygonList%5F)PolygonListEnumerator(PolygonList)

##### Declaration

```
public PolygonListEnumerator(PolygonList collection)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [PolygonList](DesignData.SDS2.Primitives.PolygonList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FPolygonListEnumerator%5FCurrent)Current

##### Declaration

```
public Polygon Current { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Polygon](DesignData.SDS2.Primitives.Polygon.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FPolygonListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FPolygonListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPolygonList%5FPolygonListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)