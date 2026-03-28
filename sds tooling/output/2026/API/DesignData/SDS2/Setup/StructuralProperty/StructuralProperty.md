# Class StructuralProperty 

A single structural property value. These are similar to a value type, when you get one it is always a copy. So to commit any changes, you have to assign back your modified StructuralProperty from where you got it.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

StructuralProperty

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class StructuralProperty
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FStructuralProperty%5F%5Fctor)StructuralProperty()

An empty StructuralProperty, UserValue, FormulaValue, and UsedValue will all be null. FormulaValue will never be calculated, but UserValue can be set and then the property can be assigned to an existing one (this will not impact calculation of FormulaValue for subsequent retrievals of the property)

##### Declaration

```
public StructuralProperty()
```

#### [](#DesignData%5FSDS2%5FSetup%5FStructuralProperty%5F%5Fctor%5FSystem%5FNullable%5FSystem%5FDouble%5F%5F)StructuralProperty(double?)

Create a structural property with the user value set to this. Formula value will be inoperable

##### Declaration

```
public StructuralProperty(double? value)
```

##### Parameters

| Type                                                            | Name  | Description |
| --------------------------------------------------------------- | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double)? | value |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FStructuralProperty%5FFormulaValue)FormulaValue

The calculated formula value in the material file for this property. null if this Shape lacks formula values for this property

##### Declaration

```
public double? FormulaValue { get; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double)? |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStructuralProperty%5FUsedValue)UsedValue

The value the system will use (should be either UserValue or FormulaValue. The system prefers UserValue over FormulaValue when it is present. In some cases this could be null if there is no FormulaValue or UserValue.

##### Declaration

```
public double? UsedValue { get; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double)? |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStructuralProperty%5FUserValue)UserValue

The value manually entered into the material file for this property. null if no value was entered.

##### Declaration

```
public double? UserValue { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double)? |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FStructuralProperty%5FFinalize)\~StructuralProperty()

A single structural property value. These are similar to a value type, when you get one it is always a copy. So to commit any changes, you have to assign back your modified StructuralProperty from where you got it.

##### Declaration

```
protected ~StructuralProperty()
```

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FSetup%5FStructuralProperty%5Fop%5FImplicit%5FSystem%5FNullable%5FSystem%5FDouble%5F%5F%5FDesignData%5FSDS2%5FSetup%5FStructuralProperty)implicit operator StructuralProperty(double?)

Implicitly cast from double? to a StructuralProperty with the user value set to that double?

##### Declaration

```
public static implicit operator StructuralProperty(double? value)
```

##### Parameters

| Type                                                            | Name  | Description |
| --------------------------------------------------------------- | ----- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double)? | value |             |

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StructuralProperty](DesignData.SDS2.Setup.StructuralProperty.html) |             |