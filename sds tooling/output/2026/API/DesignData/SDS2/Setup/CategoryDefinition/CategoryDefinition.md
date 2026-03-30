# Class CategoryDefinition 

A fabricatory setup category

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CategoryDefinition

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class CategoryDefinition
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F%5Fctor)CategoryDefinition()

Create a standalone CategoryDefinition, which can be added to the fabricator.

##### Declaration

```
public CategoryDefinition()
```

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F%5Fctor%5FSystem%5FString%5F)CategoryDefinition(string)

Create a standalone CategoryDefinition, which can be added to the fabricator. The given name will be used.

##### Declaration

```
public CategoryDefinition(string name)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinition%5FName)Name

The description of this category

##### Declaration

```
public string Name { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

Can only be set on a standalone CategoryDefinition

##### Exceptions

| Type                                                                                   | Condition                                                                                                                         |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown if this is not a standalone CategoryDefinition, meaning it was retrieved from the fabricator and not created by user code. |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinition%5FEquals%5FSystem%5FObject%5F)Equals(object)

A fabricatory setup category

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

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinition%5FFinalize)\~CategoryDefinition()

A fabricatory setup category

##### Declaration

```
protected ~CategoryDefinition()
```

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinition%5FGetHashCode)GetHashCode()

A fabricatory setup category

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

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinition%5Fop%5FEquality%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F)operator ==(CategoryDefinition, CategoryDefinition)

A fabricatory setup category

##### Declaration

```
public static bool operator ==(CategoryDefinition a, CategoryDefinition b)
```

##### Parameters

| Type                                                                | Name | Description |
| ------------------------------------------------------------------- | ---- | ----------- |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html) | a    |             |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCategoryDefinition%5Fop%5FInequality%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5FDesignData%5FSDS2%5FSetup%5FCategoryDefinition%5F)operator !=(CategoryDefinition, CategoryDefinition)

A fabricatory setup category

##### Declaration

```
public static bool operator !=(CategoryDefinition a, CategoryDefinition b)
```

##### Parameters

| Type                                                                | Name | Description |
| ------------------------------------------------------------------- | ---- | ----------- |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html) | a    |             |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |