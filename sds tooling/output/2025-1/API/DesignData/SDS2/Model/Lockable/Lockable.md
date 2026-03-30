# Class Lockable 

Base class for lockable values. Lockable values are values in SDS2 which can be locked to a user value, or unlocked and set by process to a system generated value.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Lockable

[LockableAttachToMember](DesignData.SDS2.Model.LockableAttachToMember.html)

[LockableBasePlateWeldInner](DesignData.SDS2.Model.LockableBasePlateWeldInner.html)

[LockableBasePlateWeldOuter](DesignData.SDS2.Model.LockableBasePlateWeldOuter.html)

[LockableBasePlateWeldWithGroove](DesignData.SDS2.Model.LockableBasePlateWeldWithGroove.html)

[LockableBasePlateWeldWithoutGroove](DesignData.SDS2.Model.LockableBasePlateWeldWithoutGroove.html)

[LockableBeamExtensionPlateWeldType](DesignData.SDS2.Model.LockableBeamExtensionPlateWeldType.html)

[LockableBool](DesignData.SDS2.Model.LockableBool.html)

[LockableBraceFillLocation](DesignData.SDS2.Model.LockableBraceFillLocation.html)

[LockableCutLocation](DesignData.SDS2.Model.LockableCutLocation.html)

[LockableCutOperation](DesignData.SDS2.Model.LockableCutOperation.html)

[LockableDouble](DesignData.SDS2.Model.LockableDouble.html)

[LockableEndCutType](DesignData.SDS2.Model.LockableEndCutType.html)

[LockableHoleType](DesignData.SDS2.Model.LockableHoleType.html)

[LockableInt](DesignData.SDS2.Model.LockableInt.html)

[LockablePlateSide](DesignData.SDS2.Model.LockablePlateSide.html)

[LockableShape](DesignData.SDS2.Model.LockableShape.html)

[LockableShearWeldType](DesignData.SDS2.Model.LockableShearWeldType.html)

[LockableSpacing](DesignData.SDS2.Model.LockableSpacing.html)

[LockableSteelGrade](DesignData.SDS2.Model.LockableSteelGrade.html)

[LockableStiffClip](DesignData.SDS2.Model.LockableStiffClip.html)

[LockableThreadDirection](DesignData.SDS2.Model.LockableThreadDirection.html)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class Lockable
```

##### **Remarks**

To get an actual value, you must cast this to its lockable type.

```
         Note that Lockable objects are always copies.  You can make changes to
         them, but for those changes to matter you must assign them back where you
         got them after making changes.

```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FLockable%5FIsLocked)IsLocked

True if this is locked to a user value

##### Declaration

```
public bool IsLocked { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

To get an actual value, you must cast this to its lockable type.

```
         Note that Lockable objects are always copies.  You can make changes to
         them, but for those changes to matter you must assign them back where you
         got them after making changes.

```

#### [](#DesignData%5FSDS2%5FModel%5FLockable%5FLockType)LockType

Base class for lockable values. Lockable values are values in SDS2 which can be locked to a user value, or unlocked and set by process to a system generated value.

##### Declaration

```
public LockType LockType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [LockType](DesignData.SDS2.Model.LockType.html) |             |

##### Remarks

To get an actual value, you must cast this to its lockable type.

```
         Note that Lockable objects are always copies.  You can make changes to
         them, but for those changes to matter you must assign them back where you
         got them after making changes.

```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FLockable%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base class for lockable values. Lockable values are values in SDS2 which can be locked to a user value, or unlocked and set by process to a system generated value.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Remarks

To get an actual value, you must cast this to its lockable type.

```
         Note that Lockable objects are always copies.  You can make changes to
         them, but for those changes to matter you must assign them back where you
         got them after making changes.

```

#### [](#DesignData%5FSDS2%5FModel%5FLockable%5FFinalize)\~Lockable()

Base class for lockable values. Lockable values are values in SDS2 which can be locked to a user value, or unlocked and set by process to a system generated value.

##### Declaration

```
protected ~Lockable()
```

##### Remarks

To get an actual value, you must cast this to its lockable type.

```
         Note that Lockable objects are always copies.  You can make changes to
         them, but for those changes to matter you must assign them back where you
         got them after making changes.

```

#### [](#DesignData%5FSDS2%5FModel%5FLockable%5FGetIsLocked)GetIsLocked()

True if this is locked to a user value

##### Declaration

```
public bool GetIsLocked()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

To get an actual value, you must cast this to its lockable type.

```
         Note that Lockable objects are always copies.  You can make changes to
         them, but for those changes to matter you must assign them back where you
         got them after making changes.

```

#### [](#DesignData%5FSDS2%5FModel%5FLockable%5FToString)ToString()

Base class for lockable values. Lockable values are values in SDS2 which can be locked to a user value, or unlocked and set by process to a system generated value.

##### Declaration

```
public override string ToString()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Overrides

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

##### Remarks

To get an actual value, you must cast this to its lockable type.

```
         Note that Lockable objects are always copies.  You can make changes to
         them, but for those changes to matter you must assign them back where you
         got them after making changes.

```

#### [](#DesignData%5FSDS2%5FModel%5FLockable%5FUnlock)Unlock()

Unlock this value, let it be set by the system during process

##### Declaration

```
public void Unlock()
```

##### Remarks

To get an actual value, you must cast this to its lockable type.

```
         Note that Lockable objects are always copies.  You can make changes to
         them, but for those changes to matter you must assign them back where you
         got them after making changes.

```