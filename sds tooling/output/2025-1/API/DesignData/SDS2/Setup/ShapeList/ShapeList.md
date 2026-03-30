# Class ShapeList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ShapeList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Shape](DesignData.SDS2.Setup.Shape.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class ShapeList : IEnumerable<Shape>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5F%5Fctor)ShapeList()

##### Declaration

```
public ShapeList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FShapeList%5F)ShapeList(ShapeList)

##### Declaration

```
public ShapeList(ShapeList other)
```

##### Parameters

| Type                                              | Name  | Description |
| ------------------------------------------------- | ----- | ----------- |
| [ShapeList](DesignData.SDS2.Setup.ShapeList.html) | other |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FSetup%5FShape%5F%5F)ShapeList(IEnumerable<Shape>)

##### Declaration

```
public ShapeList(IEnumerable<Shape> c)
```

##### Parameters

| Type                                                                                                                                       | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Shape](DesignData.SDS2.Setup.Shape.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)ShapeList(IEnumerable)

##### Declaration

```
public ShapeList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5F%5Fctor%5FSystem%5FInt32%5F)ShapeList(int)

##### Declaration

```
public ShapeList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Shape this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FAdd%5FDesignData%5FSDS2%5FSetup%5FShape%5F)Add(Shape)

##### Declaration

```
public void Add(Shape x)
```

##### Parameters

| Type                                      | Name | Description |
| ----------------------------------------- | ---- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) | x    |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FAddRange%5FDesignData%5FSDS2%5FSetup%5FShapeList%5F)AddRange(ShapeList)

##### Declaration

```
public void AddRange(ShapeList values)
```

##### Parameters

| Type                                              | Name   | Description |
| ------------------------------------------------- | ------ | ----------- |
| [ShapeList](DesignData.SDS2.Setup.ShapeList.html) | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FShape%5F%5F%5F)CopyTo(Shape\[\])

##### Declaration

```
public void CopyTo(Shape[] array)
```

##### Parameters

| Type                                          | Name  | Description |
| --------------------------------------------- | ----- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FCopyTo%5FDesignData%5FSDS2%5FSetup%5FShape%5F%5F%5FSystem%5FInt32%5F)CopyTo(Shape\[\], int)

##### Declaration

```
public void CopyTo(Shape[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html)\[\]              | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FShape%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Shape\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Shape[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Shape](DesignData.SDS2.Setup.Shape.html)\[\]              | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FFinalize)\~ShapeList()

##### Declaration

```
protected ~ShapeList()
```

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public ShapeList.ShapeListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                              | Description |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [ShapeList](DesignData.SDS2.Setup.ShapeList.html).[ShapeListEnumerator](DesignData.SDS2.Setup.ShapeList.ShapeListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public ShapeList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShapeList](DesignData.SDS2.Setup.ShapeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FShape%5F)Insert(int, Shape)

##### Declaration

```
public void Insert(int index, Shape x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Shape](DesignData.SDS2.Setup.Shape.html)                  | x     |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FShapeList%5F)InsertRange(int, ShapeList)

##### Declaration

```
public void InsertRange(int index, ShapeList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [ShapeList](DesignData.SDS2.Setup.ShapeList.html)          | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FRepeat%5FDesignData%5FSDS2%5FSetup%5FShape%5FSystem%5FInt32%5F)Repeat(Shape, int)

##### Declaration

```
public static ShapeList Repeat(Shape value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html)                  | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShapeList](DesignData.SDS2.Setup.ShapeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FSetup%5FShapeList%5F)SetRange(int, ShapeList)

##### Declaration

```
public void SetRange(int index, ShapeList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [ShapeList](DesignData.SDS2.Setup.ShapeList.html)          | values |             |

#### [](#DesignData%5FSDS2%5FSetup%5FShapeList%5FToArray)ToArray()

##### Declaration

```
public Shape[] ToArray()
```

##### Returns

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)