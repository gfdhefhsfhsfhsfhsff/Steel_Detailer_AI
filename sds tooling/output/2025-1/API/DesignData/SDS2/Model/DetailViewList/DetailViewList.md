# Class DetailViewList 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DetailViewList

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[DetailView](DesignData.SDS2.Model.DetailView.html)\>

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
public class DetailViewList : IEnumerable<DetailView>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5F%5Fctor)DetailViewList()

##### Declaration

```
public DetailViewList()
```

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FDetailViewList%5F)DetailViewList(DetailViewList)

##### Declaration

```
public DetailViewList(DetailViewList other)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [DetailViewList](DesignData.SDS2.Model.DetailViewList.html) | other |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5F%5Fctor%5FSystem%5FCollections%5FGeneric%5FIEnumerable%5FDesignData%5FSDS2%5FModel%5FDetailView%5F%5F)DetailViewList(IEnumerable<DetailView>)

##### Declaration

```
public DetailViewList(IEnumerable<DetailView> c)
```

##### Parameters

| Type                                                                                                                                                 | Name | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[DetailView](DesignData.SDS2.Model.DetailView.html)\> | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5F%5Fctor%5FSystem%5FCollections%5FIEnumerable%5F)DetailViewList(IEnumerable)

##### Declaration

```
public DetailViewList(IEnumerable c)
```

##### Parameters

| Type                                                                                 | Name | Description |
| ------------------------------------------------------------------------------------ | ---- | ----------- |
| [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable) | c    |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5F%5Fctor%5FSystem%5FInt32%5F)DetailViewList(int)

##### Declaration

```
public DetailViewList(int capacity)
```

##### Parameters

| Type                                                       | Name     | Description |
| ---------------------------------------------------------- | -------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | capacity |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FCapacity)Capacity

##### Declaration

```
public int Capacity { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FIsFixedSize)IsFixedSize

##### Declaration

```
public bool IsFixedSize { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FIsSynchronized)IsSynchronized

##### Declaration

```
public bool IsSynchronized { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FItem%5FSystem%5FInt32%5F)this\[int\]

##### Declaration

```
public DetailView this[int index] { get; set; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [DetailView](DesignData.SDS2.Model.DetailView.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FAdd%5FDesignData%5FSDS2%5FModel%5FDetailView%5F)Add(DetailView)

##### Declaration

```
public void Add(DetailView x)
```

##### Parameters

| Type                                                | Name | Description |
| --------------------------------------------------- | ---- | ----------- |
| [DetailView](DesignData.SDS2.Model.DetailView.html) | x    |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FAddRange%5FDesignData%5FSDS2%5FModel%5FDetailViewList%5F)AddRange(DetailViewList)

##### Declaration

```
public void AddRange(DetailViewList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [DetailViewList](DesignData.SDS2.Model.DetailViewList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FDetailView%5F%5F%5F)CopyTo(DetailView\[\])

##### Declaration

```
public void CopyTo(DetailView[] array)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [DetailView](DesignData.SDS2.Model.DetailView.html)\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FCopyTo%5FDesignData%5FSDS2%5FModel%5FDetailView%5F%5F%5FSystem%5FInt32%5F)CopyTo(DetailView\[\], int)

##### Declaration

```
public void CopyTo(DetailView[] array, int arrayIndex)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [DetailView](DesignData.SDS2.Model.DetailView.html)\[\]    | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FCopyTo%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FDetailView%5F%5F%5FSystem%5FInt32%5FSystem%5FInt32%5F)CopyTo(int, DetailView\[\], int, int)

##### Declaration

```
public void CopyTo(int index, DetailView[] array, int arrayIndex, int count)
```

##### Parameters

| Type                                                       | Name       | Description |
| ---------------------------------------------------------- | ---------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index      |             |
| [DetailView](DesignData.SDS2.Model.DetailView.html)\[\]    | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | arrayIndex |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count      |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FFinalize)\~DetailViewList()

##### Declaration

```
protected ~DetailViewList()
```

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public DetailViewList.DetailViewListEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                       | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [DetailViewList](DesignData.SDS2.Model.DetailViewList.html).[DetailViewListEnumerator](DesignData.SDS2.Model.DetailViewList.DetailViewListEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FGetRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)GetRange(int, int)

##### Declaration

```
public DetailViewList GetRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [DetailViewList](DesignData.SDS2.Model.DetailViewList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FInsert%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FDetailView%5F)Insert(int, DetailView)

##### Declaration

```
public void Insert(int index, DetailView x)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [DetailView](DesignData.SDS2.Model.DetailView.html)        | x     |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FInsertRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FDetailViewList%5F)InsertRange(int, DetailViewList)

##### Declaration

```
public void InsertRange(int index, DetailViewList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index  |             |
| [DetailViewList](DesignData.SDS2.Model.DetailViewList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FRemoveAt%5FSystem%5FInt32%5F)RemoveAt(int)

##### Declaration

```
public void RemoveAt(int index)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FRemoveRange%5FSystem%5FInt32%5FSystem%5FInt32%5F)RemoveRange(int, int)

##### Declaration

```
public void RemoveRange(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FRepeat%5FDesignData%5FSDS2%5FModel%5FDetailView%5FSystem%5FInt32%5F)Repeat(DetailView, int)

##### Declaration

```
public static DetailViewList Repeat(DetailView value, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [DetailView](DesignData.SDS2.Model.DetailView.html)        | value |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [DetailViewList](DesignData.SDS2.Model.DetailViewList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FReverse)Reverse()

##### Declaration

```
public void Reverse()
```

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FReverse%5FSystem%5FInt32%5FSystem%5FInt32%5F)Reverse(int, int)

##### Declaration

```
public void Reverse(int index, int count)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | count |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FSetRange%5FSystem%5FInt32%5FDesignData%5FSDS2%5FModel%5FDetailViewList%5F)SetRange(int, DetailViewList)

##### Declaration

```
public void SetRange(int index, DetailViewList values)
```

##### Parameters

| Type                                                        | Name   | Description |
| ----------------------------------------------------------- | ------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | index  |             |
| [DetailViewList](DesignData.SDS2.Model.DetailViewList.html) | values |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailViewList%5FToArray)ToArray()

##### Declaration

```
public DetailView[] ToArray()
```

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [DetailView](DesignData.SDS2.Model.DetailView.html)\[\] |             |

### [](#implements)Implements

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)