# Class LockableDictionary.LockableDictionaryEnumerator 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

LockableDictionary.LockableDictionaryEnumerator

##### Implements

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [Lockable](DesignData.SDS2.Model.Lockable.html)\>>

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
public sealed class LockableDictionary.LockableDictionaryEnumerator : IEnumerator<KeyValuePair<string, Lockable>>, IEnumerator, IDisposable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FLockableDictionaryEnumerator%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FLockableDictionary%5F)LockableDictionaryEnumerator(LockableDictionary)

##### Declaration

```
public LockableDictionaryEnumerator(LockableDictionary collection)
```

##### Parameters

| Type                                                                | Name       | Description |
| ------------------------------------------------------------------- | ---------- | ----------- |
| [LockableDictionary](DesignData.SDS2.Model.LockableDictionary.html) | collection |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FLockableDictionaryEnumerator%5FCurrent)Current

##### Declaration

```
public KeyValuePair<string, Lockable> Current { get; }
```

##### Property Value

| Type                                                                                                                                                                                                               | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [Lockable](DesignData.SDS2.Model.Lockable.html)\> |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FLockableDictionaryEnumerator%5FDispose)Dispose()

##### Declaration

```
public void Dispose()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FLockableDictionaryEnumerator%5FMoveNext)MoveNext()

##### Declaration

```
public bool MoveNext()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableDictionary%5FLockableDictionaryEnumerator%5FReset)Reset()

##### Declaration

```
public void Reset()
```

### [](#implements)Implements

[IEnumerator<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) 

[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)