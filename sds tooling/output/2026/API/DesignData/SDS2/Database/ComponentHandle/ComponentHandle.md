# Class ComponentHandle 

A handle for a member component

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ComponentHandle

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class ComponentHandle
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FComponentHandle%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A handle for a member component

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FComponentHandle%5FEquals%5FSystem%5FObject%5F)Equals(object)

A handle for a member component

##### Declaration

```
public override bool Equals(object other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | other |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

#### [](#DesignData%5FSDS2%5FDatabase%5FComponentHandle%5FFinalize)\~ComponentHandle()

A handle for a member component

##### Declaration

```
protected ~ComponentHandle()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FComponentHandle%5FGetGuid)GetGuid()

A globally unique identifier for this component

##### Declaration

```
public Guid? GetGuid()
```

##### Returns

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [Guid](https://learn.microsoft.com/dotnet/api/system.guid)? |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FComponentHandle%5FGetHashCode)GetHashCode()

A handle for a member component

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

#### [](#DesignData%5FSDS2%5FDatabase%5FComponentHandle%5FGetMemberHandle)GetMemberHandle()

The handle for the member that this component is attached to.

##### Declaration

```
public MemberHandle GetMemberHandle()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) |             |