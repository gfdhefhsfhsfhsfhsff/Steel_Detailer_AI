# Class LockableAttachToMember 

A lockable for the AttachToMember enum

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableAttachToMember

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
public sealed class LockableAttachToMember : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableAttachToMember%5F%5Fctor)LockableAttachToMember()

A lockable for the AttachToMember enum

##### Declaration

```
public LockableAttachToMember()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableAttachToMember%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FAttachToMember%5F)LockableAttachToMember(AttachToMember)

Create a locked ViaMemberEdit LockableAttachToMember from a AttachToMember

##### Declaration

```
public LockableAttachToMember(AttachToMember value)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [AttachToMember](DesignData.SDS2.Model.AttachToMember.html) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableAttachToMember%5FValue)Value

The underlying value

##### Declaration

```
public AttachToMember Value { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AttachToMember](DesignData.SDS2.Model.AttachToMember.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableAttachToMember%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A lockable for the AttachToMember enum

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

#### [](#DesignData%5FSDS2%5FModel%5FLockableAttachToMember%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FAttachToMember%5F%5FDesignData%5FSDS2%5FModel%5FLockableAttachToMember)implicit operator LockableAttachToMember(AttachToMember)

Implicit conversion using the AttachToMember constructor

##### Declaration

```
public static implicit operator LockableAttachToMember(AttachToMember value)
```

##### Parameters

| Type                                                        | Name  | Description |
| ----------------------------------------------------------- | ----- | ----------- |
| [AttachToMember](DesignData.SDS2.Model.AttachToMember.html) | value |             |

##### Returns

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [LockableAttachToMember](DesignData.SDS2.Model.LockableAttachToMember.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableAttachToMember%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockableAttachToMember%5F%5FDesignData%5FSDS2%5FModel%5FAttachToMember)implicit operator AttachToMember(LockableAttachToMember)

Implicit conversion to value type

##### Declaration

```
public static implicit operator AttachToMember(LockableAttachToMember value)
```

##### Parameters

| Type                                                                        | Name  | Description |
| --------------------------------------------------------------------------- | ----- | ----------- |
| [LockableAttachToMember](DesignData.SDS2.Model.LockableAttachToMember.html) | value |             |

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AttachToMember](DesignData.SDS2.Model.AttachToMember.html) |             |