# Class LockableStiffClip 

Lockable value for stiffener clips

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableStiffClip

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
public sealed class LockableStiffClip : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableStiffClip%5F%5Fctor)LockableStiffClip()

Lockable value for stiffener clips

##### Declaration

```
public LockableStiffClip()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableStiffClip%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FStiffClip%5F)LockableStiffClip(StiffClip)

Create a locked ViaMemberEdit LockableStiffClip from a StiffClip

##### Declaration

```
public LockableStiffClip(StiffClip value)
```

##### Parameters

| Type                                              | Name  | Description |
| ------------------------------------------------- | ----- | ----------- |
| [StiffClip](DesignData.SDS2.Model.StiffClip.html) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableStiffClip%5FValue)Value

The underlying value

##### Declaration

```
public StiffClip Value { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [StiffClip](DesignData.SDS2.Model.StiffClip.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableStiffClip%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Lockable value for stiffener clips

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

#### [](#DesignData%5FSDS2%5FModel%5FLockableStiffClip%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockableStiffClip%5F%5FDesignData%5FSDS2%5FModel%5FStiffClip)implicit operator StiffClip(LockableStiffClip)

Implicit conversion to value type

##### Declaration

```
public static implicit operator StiffClip(LockableStiffClip value)
```

##### Parameters

| Type                                                              | Name  | Description |
| ----------------------------------------------------------------- | ----- | ----------- |
| [LockableStiffClip](DesignData.SDS2.Model.LockableStiffClip.html) | value |             |

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [StiffClip](DesignData.SDS2.Model.StiffClip.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableStiffClip%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FStiffClip%5F%5FDesignData%5FSDS2%5FModel%5FLockableStiffClip)implicit operator LockableStiffClip(StiffClip)

Implicit conversion using the StiffClip constructor

##### Declaration

```
public static implicit operator LockableStiffClip(StiffClip value)
```

##### Parameters

| Type                                              | Name  | Description |
| ------------------------------------------------- | ----- | ----------- |
| [StiffClip](DesignData.SDS2.Model.StiffClip.html) | value |             |

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [LockableStiffClip](DesignData.SDS2.Model.LockableStiffClip.html) |             |