# Class LockableShape 

A lockable value holding a reference to a Shape in the job

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Lockable](DesignData.SDS2.Model.Lockable.html)

LockableShape

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
public sealed class LockableShape : Lockable
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FLockableShape%5F%5Fctor)LockableShape()

A lockable value holding a reference to a Shape in the job

##### Declaration

```
public LockableShape()
```

#### [](#DesignData%5FSDS2%5FModel%5FLockableShape%5F%5Fctor%5FDesignData%5FSDS2%5FSetup%5FShape%5F)LockableShape(Shape)

Create a locked ViaMemberEdit LockableShape from a DesignData.SDS2.Setup.Shape

##### Declaration

```
public LockableShape(Shape value)
```

##### Parameters

| Type                                      | Name  | Description |
| ----------------------------------------- | ----- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockableShape%5FValue)Value

The underlying shape data

##### Declaration

```
public Shape Value { get; set; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockableShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A lockable value holding a reference to a Shape in the job

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

#### [](#DesignData%5FSDS2%5FModel%5FLockableShape%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FLockableShape%5F%5FDesignData%5FSDS2%5FSetup%5FShape)implicit operator Shape(LockableShape)

Implicit conversion to value type

##### Declaration

```
public static implicit operator Shape(LockableShape value)
```

##### Parameters

| Type                                                      | Name  | Description |
| --------------------------------------------------------- | ----- | ----------- |
| [LockableShape](DesignData.SDS2.Model.LockableShape.html) | value |             |

##### Returns

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FLockableShape%5Fop%5FImplicit%5FDesignData%5FSDS2%5FSetup%5FShape%5F%5FDesignData%5FSDS2%5FModel%5FLockableShape)implicit operator LockableShape(Shape)

Implicit conversion using the DesignData.SDS2.Setup.Shape constructor

##### Declaration

```
public static implicit operator LockableShape(Shape value)
```

##### Parameters

| Type                                      | Name  | Description |
| ----------------------------------------- | ----- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) | value |             |

##### Returns

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [LockableShape](DesignData.SDS2.Model.LockableShape.html) |             |