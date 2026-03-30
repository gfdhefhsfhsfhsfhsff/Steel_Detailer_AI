# Class Point3DList.Point3DListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Point3DList.Point3DListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[Point3D](DesignData.SDS2.Primitives.Point3D.html)\>

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
public sealed class Point3DList.Point3DListEnumerator : IEnumerator<Point3D>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FPoint3DListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPoint3DList%5F)Point3DListEnumerator(Point3DList)

##### Declaration

```
public Point3DListEnumerator(Point3DList collection)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Point3DList](DesignData.SDS2.Primitives.Point3DList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FPoint3DListEnumerator%5FCurrent)Current

##### Declaration

```
public Point3D Current { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FPoint3DListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FPoint3DListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FPoint3DList%5FPoint3DListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)