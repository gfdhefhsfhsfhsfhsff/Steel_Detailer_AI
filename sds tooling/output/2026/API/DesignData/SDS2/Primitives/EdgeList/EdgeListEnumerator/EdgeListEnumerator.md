# Class EdgeList.EdgeListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

EdgeList.EdgeListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[Edge](DesignData.SDS2.Primitives.Edge.html)\>

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
public sealed class EdgeList.EdgeListEnumerator : IEnumerator<Edge>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FEdgeListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FEdgeList%5F)EdgeListEnumerator(EdgeList)

##### Declaration

```
public EdgeListEnumerator(EdgeList collection)
```

##### Parameters

| Type                                                 | Name       | Description |
| ---------------------------------------------------- | ---------- | ----------- |
| [EdgeList](DesignData.SDS2.Primitives.EdgeList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FEdgeListEnumerator%5FCurrent)Current

##### Declaration

```
public Edge Current { get; }
```

##### Property Value

| Type                                         | Description |
| -------------------------------------------- | ----------- |
| [Edge](DesignData.SDS2.Primitives.Edge.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FEdgeListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FEdgeListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FEdgeList%5FEdgeListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)