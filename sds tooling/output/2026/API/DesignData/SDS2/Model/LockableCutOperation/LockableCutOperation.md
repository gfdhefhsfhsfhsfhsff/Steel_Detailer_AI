# Class LockableCutOperation 

Lockable value for CutOperation

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableCutOperation

##### Inherited Members

[Lockable.Unlock()](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FUnlock) 

[Lockable.GetIsLocked()](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FGetIsLocked) 

[Lockable.ToString()](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FToString) 

[Lockable.LockType](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FLockType) 

[Lockable.IsLocked](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FIsLocked) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public sealed class LockableCutOperation : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutOperation%5F%5Fctor)LockableCutOperation()

Lockable value for CutOperation

##### Declaration

```
public LockableCutOperation()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutOperation%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FCutOperation%5F)LockableCutOperation(CutOperation)

Create a locked ViaMemberEdit LockableCutOperation from a CutOperation

##### Declaration

```
public LockableCutOperation(CutOperation value)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [CutOperation](DesignData.SDS2.Model.CutOperation.html) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutOperation%5FValue)Value

The underlying value

##### Declaration

```
public CutOperation Value { get; set; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [CutOperation](DesignData.SDS2.Model.CutOperation.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutOperation%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Lockable value for CutOperation

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[Lockable.Dispose(bool)](DesignData.SDS2.Model.Lockable.html#DesignData%5FSDS2%5FModel%5FLockable%5FDispose%5FSystem%5FBoolean%5F)

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutOperation%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FCutOperation%5F%5FDesignData%5FSDS2%5FModel%5FLockableCutOperation)implicit operator LockableCutOperation(CutOperation)

Implicit conversion using the CutOperation constructor

##### Declaration

```
public static implicit operator LockableCutOperation(CutOperation value)
```

##### Parameters

| Type                                                    | Name  | Description |
| ------------------------------------------------------- | ----- | ----------- |
| [CutOperation](DesignData.SDS2.Model.CutOperation.html) | value |             |

##### Returns

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [LockableCutOperation](DesignData.SDS2.Model.LockableCutOperation.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableCutOperation%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockableCutOperation%5F%5FDesignData%5FSDS2%5FModel%5FCutOperation)implicit operator CutOperation(LockableCutOperation)

Implicit conversion to value type

##### Declaration

```
public static implicit operator CutOperation(LockableCutOperation value)
```

##### Parameters

| Type                                                                    | Name  | Description |
| ----------------------------------------------------------------------- | ----- | ----------- |
| [LockableCutOperation](DesignData.SDS2.Model.LockableCutOperation.html) | value |             |

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [CutOperation](DesignData.SDS2.Model.CutOperation.html) |             |