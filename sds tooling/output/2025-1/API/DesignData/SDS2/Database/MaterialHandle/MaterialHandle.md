# Class MaterialHandle 

A handle specifically for materials.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialHandle

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
public class MaterialHandle
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialHandle%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5FSystem%5FInt32%5FSystem%5FNullable%5FSystem%5FGuid%5F%5F)MaterialHandle(MemberHandle, int, Guid?)

Create a new material handle from a member handle, index of the material, and guid. Both the materialIndex and the guid must be correct.

##### Declaration

```
public MaterialHandle(MemberHandle memberHandle, int materialIndex, Guid? guid)
```

##### Parameters

| Type                                                        | Name          | Description |
| ----------------------------------------------------------- | ------------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html)  | memberHandle  |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)  | materialIndex |             |
| [Guid](https://learn.microsoft.com/dotnet/api/system.guid)? | guid          |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialHandle%5FGuid)Guid

The uuid or guid representing this material

##### Declaration

```
public Guid? Guid { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [Guid](https://learn.microsoft.com/dotnet/api/system.guid)? |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialHandle%5FMember)Member

The member this material is on

##### Declaration

```
public MemberHandle Member { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialHandle%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A handle specifically for materials.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialHandle%5FEquals%5FSystem%5FObject%5F)Equals(object)

A handle specifically for materials.

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

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialHandle%5FFinalize)\~MaterialHandle()

A handle specifically for materials.

##### Declaration

```
protected ~MaterialHandle()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialHandle%5FGetHashCode)GetHashCode()

A handle specifically for materials.

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