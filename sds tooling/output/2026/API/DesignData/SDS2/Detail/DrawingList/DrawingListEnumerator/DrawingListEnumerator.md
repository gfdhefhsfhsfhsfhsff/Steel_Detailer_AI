# Class DrawingList.DrawingListEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DrawingList.DrawingListEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[Drawing](DesignData.SDS2.Detail.Drawing.html)\>

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
public sealed class DrawingList.DrawingListEnumerator : IEnumerator<Drawing>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FDrawingListEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FDetail%5FDrawingList%5F)DrawingListEnumerator(DrawingList)

##### Declaration

```
public DrawingListEnumerator(DrawingList collection)
```

##### Parameters

| Type                                                   | Name       | Description |
| ------------------------------------------------------ | ---------- | ----------- |
| [DrawingList](DesignData.SDS2.Detail.DrawingList.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FDrawingListEnumerator%5FCurrent)Current

##### Declaration

```
public Drawing Current { get; }
```

##### Property Value

| Type                                           | Description |
| ---------------------------------------------- | ----------- |
| [Drawing](DesignData.SDS2.Detail.Drawing.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FDrawingListEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FDrawingListEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FDrawingList%5FDrawingListEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)