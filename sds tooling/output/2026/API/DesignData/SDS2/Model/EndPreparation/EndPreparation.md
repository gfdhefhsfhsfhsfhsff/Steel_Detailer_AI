# Class EndPreparation 

End preparation lockables for most builtin members types (such as beams and braces). These are convenience methods for looking up lockables normally found on ConnectionComponent.GetLockable

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

EndPreparation

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
public class EndPreparation
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FEndPreparation%5FEndCutType)EndCutType

The end cut type for this end. This is a shortcut for getting the appropriate lockable from the connection component for this end.

##### Declaration

```
public LockableEndCutType EndCutType { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [LockableEndCutType](DesignData.SDS2.Model.LockableEndCutType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPreparation%5FFlangeCutAngle)FlangeCutAngle

The flange cut angle for this end. This is a shortcut for getting the appropriate lockable from the connection component for this end.

##### Declaration

```
public LockableDouble FlangeCutAngle { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPreparation%5FMomentConnectionWebSetback)MomentConnectionWebSetback

The moment web setback for this end. This is a shortcut for getting the appropriate lockable from the connection component for this end.

##### Declaration

```
public LockableDouble MomentConnectionWebSetback { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPreparation%5FWebCutAngle)WebCutAngle

The web cut angle for this end. This is a shortcut for getting the appropriate lockable from the connection component for this end.

##### Declaration

```
public LockableDouble WebCutAngle { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FEndPreparation%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

End preparation lockables for most builtin members types (such as beams and braces). These are convenience methods for looking up lockables normally found on ConnectionComponent.GetLockable

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FEndPreparation%5FFinalize)\~EndPreparation()

End preparation lockables for most builtin members types (such as beams and braces). These are convenience methods for looking up lockables normally found on ConnectionComponent.GetLockable

##### Declaration

```
protected ~EndPreparation()
```