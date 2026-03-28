# Class MemberRevision 

Member revision

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MemberRevision

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class MemberRevision
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevision%5F%5Fctor%5FSystem%5FString%5FSystem%5FString%5F)MemberRevision(string, string)

Member revision

##### Declaration

```
public MemberRevision(string shortDescription, string longDescription)
```

##### Parameters

| Type                                                           | Name             | Description |
| -------------------------------------------------------------- | ---------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | shortDescription |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | longDescription  |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevision%5FLine)Line

The index of this revision in the list of revisions

##### Declaration

```
public int Line { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevision%5FLongDescription)LongDescription

The long description of the revision. Up to 255 characters

##### Declaration

```
public string LongDescription { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevision%5FShortDescription)ShortDescription

The short description (this is the one selected in member edit). Up to 31 characters/

##### Declaration

```
public string ShortDescription { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevision%5FEquals%5FSystem%5FObject%5F)Equals(object)

Member revision

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

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevision%5FFinalize)\~MemberRevision()

Member revision

##### Declaration

```
protected ~MemberRevision()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevision%5FGetHashCode)GetHashCode()

Member revision

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

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevision%5Fop%5FEquality%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5F)operator ==(MemberRevision, MemberRevision)

Member revision

##### Declaration

```
public static bool operator ==(MemberRevision a, MemberRevision b)
```

##### Parameters

| Type                                                        | Name | Description |
| ----------------------------------------------------------- | ---- | ----------- |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html) | a    |             |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMemberRevision%5Fop%5FInequality%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5FDesignData%5FSDS2%5FSetup%5FMemberRevision%5F)operator !=(MemberRevision, MemberRevision)

Member revision

##### Declaration

```
public static bool operator !=(MemberRevision a, MemberRevision b)
```

##### Parameters

| Type                                                        | Name | Description |
| ----------------------------------------------------------- | ---- | ----------- |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html) | a    |             |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |