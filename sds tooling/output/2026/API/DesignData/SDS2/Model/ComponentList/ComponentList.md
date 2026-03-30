# Class ComponentList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ComponentList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Component](DesignData.SDS2.Model.Component.html)\>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class ComponentList : IEnumerable<Component>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5F%5Fctor)ComponentList()

##### Declaration

```
public ComponentList()
```

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FComponentList%5F)ComponentList(ComponentList)

##### Declaration

```
public ComponentList(ComponentList other)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [ComponentList](DesignData.SDS2.Model.ComponentList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FComponent%5F%5F)ComponentList(IEnumerable<Component>)

##### Declaration

```
public ComponentList(IEnumerable<Component> c)
```

##### Parameters

| Type                                                                                                                                               | Name | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Component](DesignData.SDS2.Model.Component.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)ComponentList(IEnumerable)

##### Declaration

```
public ComponentList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5F%5Fctor%5FSystem%5FInt32%5F)ComponentList(int)

##### Declaration

```
public ComponentList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public Component this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [Component](DesignData.SDS2.Model.Component.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FAdd%5FDesignData%5FSDS2%5FModel%5FComponent%5F)Add(Component)

##### Declaration

```
public void Add(Component x)
```

##### Parameters

| Type                                              | Name | Description |
| ------------------------------------------------- | ---- | ----------- |
| [Component](DesignData.SDS2.Model.Component.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FComponentList%5F)AddRange(ComponentList)

##### Declaration

```
public void AddRange(ComponentList values)
```

##### Parameters

| Type                                                      | Name   | Description |
| --------------------------------------------------------- | ------ | ----------- |
| [ComponentList](DesignData.SDS2.Model.ComponentList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FComponent%5F%5F%5F)CopyTo(Component\[\])

##### Declaration

```
public void CopyTo(Component[] array)
```

##### Parameters

| Type                                                  | Name  | Description |
| ----------------------------------------------------- | ----- | ----------- |
| [Component](DesignData.SDS2.Model.Component.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FComponent%5F%5F%5FSystem%5FInt32%5F)CopyTo(Component\[\], int)

##### Declaration

```
public void CopyTo(Component[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [Component](DesignData.SDS2.Model.Component.html)\[\]      | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FComponent%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, Component\[\], int, int)

##### Declaration

```
public void CopyTo(int index, Component[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [Component](DesignData.SDS2.Model.Component.html)\[\]      | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FFinalize)\~ComponentList()

##### Declaration

```
protected ~ComponentList()
```

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public ComponentList.ComponentListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [ComponentList](DesignData.SDS2.Model.ComponentList.html).[ComponentListEnumerator](DesignData.SDS2.Model.ComponentList.ComponentListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public ComponentList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ComponentList](DesignData.SDS2.Model.ComponentList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FComponent%5F)Insert(int, Component)

##### Declaration

```
public void Insert(int index, Component x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [Component](DesignData.SDS2.Model.Component.html)          | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FComponentList%5F)InsertRange(int, ComponentList)

##### Declaration

```
public void InsertRange(int index, ComponentList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [ComponentList](DesignData.SDS2.Model.ComponentList.html)  | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FComponent%5FSystem%5FInt32%5F)Repeat(Component, int)

##### Declaration

```
public static ComponentList Repeat(Component value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [Component](DesignData.SDS2.Model.Component.html)          | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [ComponentList](DesignData.SDS2.Model.ComponentList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FComponentList%5F)SetRange(int, ComponentList)

##### Declaration

```
public void SetRange(int index, ComponentList values)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index  |             |
| [ComponentList](DesignData.SDS2.Model.ComponentList.html)  | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FComponentList%5FToArray)ToArray()

##### Declaration

```
public Component[] ToArray()
```

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [Component](DesignData.SDS2.Model.Component.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)