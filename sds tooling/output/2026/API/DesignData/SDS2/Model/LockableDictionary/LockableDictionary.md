# Class LockableDictionary 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

LockableDictionary

##### Implements

[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [Lockable](DesignData.SDS2.Model.Lockable.html)\>

[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [Lockable](DesignData.SDS2.Model.Lockable.html)\>>

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [Lockable](DesignData.SDS2.Model.Lockable.html)\>>

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
public class LockableDictionary : IDictionary<string, Lockable>, ICollection<KeyValuePair<string, Lockable>>, IEnumerable<KeyValuePair<string, Lockable>>, IEnumerable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5F%5Fctor)LockableDictionary()

##### Declaration

```
public LockableDictionary()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FLockableDictionary%5F)LockableDictionary(LockableDictionary)

##### Declaration

```
public LockableDictionary(LockableDictionary other)
```

##### Parameters

| Type                                                                | Name  | Description |
| ------------------------------------------------------------------- | ----- | ----------- |
| [LockableDictionary](DesignData.SDS2.Model.LockableDictionary.html) | other |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FCount)Count

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FIsReadOnly)IsReadOnly

##### Declaration

```
public bool IsReadOnly { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FItem%5FSystem%5FString%5F)this\[string\]

##### Declaration

```
public Lockable this[string key] { get; set; }
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | key  |             |

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [Lockable](DesignData.SDS2.Model.Lockable.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FKeys)Keys

##### Declaration

```
public ICollection<string> Keys { get; }
```

##### Property Value

| Type                                                                                                                                                            | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\> |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FValues)Values

##### Declaration

```
public ICollection<Lockable> Values { get; }
```

##### Property Value

| Type                                                                                                                                             | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[Lockable](DesignData.SDS2.Model.Lockable.html)\> |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FAdd%5FSystem%5FCollections%5FGeneric%5FKeyValuePair%5FSystem%5FString%5FDesignData%5FSDS2%5FModel%5FLockable%5F%5F)Add(KeyValuePair<string, Lockable>)

##### Declaration

```
public void Add(KeyValuePair<string, Lockable> item)
```

##### Parameters

| Type                                                                                                                                                                                                               | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [Lockable](DesignData.SDS2.Model.Lockable.html)\> | item |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FAdd%5FSystem%5FString%5FDesignData%5FSDS2%5FModel%5FLockable%5F)Add(string, Lockable)

##### Declaration

```
public void Add(string key, Lockable value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | key   |             |
| [Lockable](DesignData.SDS2.Model.Lockable.html)                | value |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FClear)Clear()

##### Declaration

```
public void Clear()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FContains%5FSystem%5FCollections%5FGeneric%5FKeyValuePair%5FSystem%5FString%5FDesignData%5FSDS2%5FModel%5FLockable%5F%5F)Contains(KeyValuePair<string, Lockable>)

##### Declaration

```
public bool Contains(KeyValuePair<string, Lockable> item)
```

##### Parameters

| Type                                                                                                                                                                                                               | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [Lockable](DesignData.SDS2.Model.Lockable.html)\> | item |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FContainsKey%5FSystem%5FString%5F)ContainsKey(string)

##### Declaration

```
public bool ContainsKey(string key)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | key  |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FCopyTo%5FSystem%5FCollections%5FGeneric%5FKeyValuePair%5FSystem%5FString%5FDesignData%5FSDS2%5FModel%5FLockable%5F%5F%5F%5F)CopyTo(KeyValuePair<string, Lockable>\[\])

##### Declaration

```
public void CopyTo(KeyValuePair<string, Lockable>[] array)
```

##### Parameters

| Type                                                                                                                                                                                                                   | Name  | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ----------- |
| [KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [Lockable](DesignData.SDS2.Model.Lockable.html)\>\[\] | array |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FCopyTo%5FSystem%5FCollections%5FGeneric%5FKeyValuePair%5FSystem%5FString%5FDesignData%5FSDS2%5FModel%5FLockable%5F%5F%5F%5FSystem%5FInt32%5F)CopyTo(KeyValuePair<string, Lockable>\[\], int)

##### Declaration

```
public void CopyTo(KeyValuePair<string, Lockable>[] array, int arrayIndex)
```

##### Parameters

| Type                                                                                                                                                                                                                   | Name       | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----------- |
| [KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [Lockable](DesignData.SDS2.Model.Lockable.html)\>\[\] | array      |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)                                                                                                                                                             | arrayIndex |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FFinalize)\~LockableDictionary()

##### Declaration

```
protected ~LockableDictionary()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FGetEnumerator)GetEnumerator()

##### Declaration

```
public LockableDictionary.LockableDictionaryEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                                                                                                           | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [LockableDictionary](DesignData.SDS2.Model.LockableDictionary.html).[LockableDictionaryEnumerator](DesignData.SDS2.Model.LockableDictionary.LockableDictionaryEnumerator.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FRemove%5FSystem%5FCollections%5FGeneric%5FKeyValuePair%5FSystem%5FString%5FDesignData%5FSDS2%5FModel%5FLockable%5F%5F)Remove(KeyValuePair<string, Lockable>)

##### Declaration

```
public bool Remove(KeyValuePair<string, Lockable> item)
```

##### Parameters

| Type                                                                                                                                                                                                               | Name | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----------- |
| [KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [Lockable](DesignData.SDS2.Model.Lockable.html)\> | item |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FRemove%5FSystem%5FString%5F)Remove(string)

##### Declaration

```
public bool Remove(string key)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | key  |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FTryGetValue%5FSystem%5FString%5FDesignData%5FSDS2%5FModel%5FLockable%5F%5F)TryGetValue(string, out Lockable)

##### Declaration

```
public bool TryGetValue(string key, out Lockable value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | key   |             |
| [Lockable](DesignData.SDS2.Model.Lockable.html)                | value |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5Fempty)empty()

##### Declaration

```
public bool empty()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

### [](#implements)Implements

[IDictionary<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2) 

[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1) 

[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) 

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)