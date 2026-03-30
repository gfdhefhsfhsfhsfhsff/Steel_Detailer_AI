# Class MemberEndHandle 

A handle specifically for member ends. This can also be passed in place of a MemberHandle, in which case it will point at the member for this end.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[TableIndexHandle](DesignData.SDS2.Database.TableIndexHandle.html)

[MemberHandle](DesignData.SDS2.Database.MemberHandle.html)

MemberEndHandle

##### Inherited Members

[MemberHandle.CustomPropertyHandle](DesignData.SDS2.Database.MemberHandle.html#DesignData%5FSDS2%5FDatabase%5FMemberHandle%5FCustomPropertyHandle) 

[MemberHandle.CustomPropertyMapHandle](DesignData.SDS2.Database.MemberHandle.html#DesignData%5FSDS2%5FDatabase%5FMemberHandle%5FCustomPropertyMapHandle) 

[TableIndexHandle.ToString()](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FToString) 

[TableIndexHandle.Table](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FTable) 

[TableIndexHandle.Index](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FIndex) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class MemberEndHandle : MemberHandle
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberEndHandle%5F%5Fctor%5FSystem%5FInt32%5FDesignData%5FSDS2%5FDatabase%5FMemberEnd%5F)MemberEndHandle(int, MemberEnd)

Create a new member end handle from the member number and end

##### Declaration

```
public MemberEndHandle(int memberNumber, MemberEnd memberEnd)
```

##### Parameters

| Type                                                       | Name         | Description |
| ---------------------------------------------------------- | ------------ | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | memberNumber |             |
| [MemberEnd](DesignData.SDS2.Database.MemberEnd.html)       | memberEnd    |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberEndHandle%5FEnd)End

The enumeration value representing this end of a member

##### Declaration

```
public MemberEnd End { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [MemberEnd](DesignData.SDS2.Database.MemberEnd.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberEndHandle%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A handle specifically for member ends. This can also be passed in place of a MemberHandle, in which case it will point at the member for this end.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[MemberHandle.Dispose(bool)](DesignData.SDS2.Database.MemberHandle.html#DesignData%5FSDS2%5FDatabase%5FMemberHandle%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberEndHandle%5FEquals%5FSystem%5FObject%5F)Equals(object)

A handle specifically for member ends. This can also be passed in place of a MemberHandle, in which case it will point at the member for this end.

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

[TableIndexHandle.Equals(object)](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FEquals%5FSystem%5FObject%5F)

#### [](#DesignData%5FSDS2%5FDatabase%5FMemberEndHandle%5FGetHashCode)GetHashCode()

A handle specifically for member ends. This can also be passed in place of a MemberHandle, in which case it will point at the member for this end.

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[TableIndexHandle.GetHashCode()](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FGetHashCode)