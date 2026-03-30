# Class RoutingDefinition 

A member or material routing definition

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

RoutingDefinition

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class RoutingDefinition
```

##### **Remarks**

This really points to an entry in the user routing table, and this definition knows which routing list it's from.

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinition%5F%5Fctor%5FSystem%5FString%5FSystem%5FString%5F)RoutingDefinition(string, string)

Create a new, standalone, route. This cannot be assigned until it's been added to a fabricator

##### Declaration

```
public RoutingDefinition(string routeType, string description)
```

##### Parameters

| Type                                                           | Name        | Description |
| -------------------------------------------------------------- | ----------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | routeType   |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | description |             |

##### Remarks

This really points to an entry in the user routing table, and this definition knows which routing list it's from.

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinition%5FRouteDescription)RouteDescription

The description of this individual routing

##### Declaration

```
public string RouteDescription { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

This really points to an entry in the user routing table, and this definition knows which routing list it's from.

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinition%5FRouteType)RouteType

The descriptive type of routing

##### Declaration

```
public string RouteType { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

This really points to an entry in the user routing table, and this definition knows which routing list it's from.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinition%5FEquals%5FSystem%5FObject%5F)Equals(object)

A member or material routing definition

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

##### Remarks

This really points to an entry in the user routing table, and this definition knows which routing list it's from.

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinition%5FFinalize)\~RoutingDefinition()

A member or material routing definition

##### Declaration

```
protected ~RoutingDefinition()
```

##### Remarks

This really points to an entry in the user routing table, and this definition knows which routing list it's from.

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinition%5FGetHashCode)GetHashCode()

A member or material routing definition

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

##### Remarks

This really points to an entry in the user routing table, and this definition knows which routing list it's from.

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinition%5Fop%5FEquality%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5F)operator ==(RoutingDefinition, RoutingDefinition)

A member or material routing definition

##### Declaration

```
public static bool operator ==(RoutingDefinition a, RoutingDefinition b)
```

##### Parameters

| Type                                                              | Name | Description |
| ----------------------------------------------------------------- | ---- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) | a    |             |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

This really points to an entry in the user routing table, and this definition knows which routing list it's from.

#### [](#DesignData%5FSDS2%5FSetup%5FRoutingDefinition%5Fop%5FInequality%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5FDesignData%5FSDS2%5FSetup%5FRoutingDefinition%5F)operator !=(RoutingDefinition, RoutingDefinition)

A member or material routing definition

##### Declaration

```
public static bool operator !=(RoutingDefinition a, RoutingDefinition b)
```

##### Parameters

| Type                                                              | Name | Description |
| ----------------------------------------------------------------- | ---- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) | a    |             |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

This really points to an entry in the user routing table, and this definition knows which routing list it's from.