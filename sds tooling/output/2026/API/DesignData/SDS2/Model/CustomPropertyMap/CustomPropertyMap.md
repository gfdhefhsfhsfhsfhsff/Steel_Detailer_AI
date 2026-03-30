# Class CustomPropertyMap 

A set of custom properties for a member, material, bolt, weld, or other item with custom properties.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CustomPropertyMap

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
public class CustomPropertyMap
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A set of custom properties for a member, material, bolt, weld, or other item with custom properties.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FFinalize)\~CustomPropertyMap()

A set of custom properties for a member, material, bolt, weld, or other item with custom properties.

##### Declaration

```
protected ~CustomPropertyMap()
```

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FGet%5FDesignData%5FSDS2%5FDatabase%5FCustomPropertyMapHandle%5F)Get(CustomPropertyMapHandle)

Get a CustomPropertyMap object for the handle passed in.

##### Declaration

```
public static CustomPropertyMap Get(CustomPropertyMapHandle handle)
```

##### Parameters

| Type                                                                             | Name   | Description |
| -------------------------------------------------------------------------------- | ------ | ----------- |
| [CustomPropertyMapHandle](DesignData.SDS2.Database.CustomPropertyMapHandle.html) | handle |             |

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [CustomPropertyMap](DesignData.SDS2.Model.CustomPropertyMap.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FGet%5FSystem%5FString%5FSystem%5FBoolean%5F%5F)Get(string, ref bool)

Get the value for the custom property name on this member

##### Declaration

```
public bool Get(string name, ref bool value)
```

##### Parameters

| Type                                                           | Name  | Description                                           |
| -------------------------------------------------------------- | ----- | ----------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name  | Set to the value if it's found, and true is returned. |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | value |                                                       |

##### Returns

| Type                                                          | Description                                           |
| ------------------------------------------------------------- | ----------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | true if the value is found and is of the correct type |

##### Exceptions

| Type                                                                                                       | Condition                                                             |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| [CustomPropertyMissingException](DesignData.SDS2.Exceptions.CustomPropertyMissingException.html)           | If the custom property is not found in the schema                     |
| [CustomPropertyTypeMismatchException](DesignData.SDS2.Exceptions.CustomPropertyTypeMismatchException.html) | If the custom property is in the schema with a type other than double |

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FGet%5FSystem%5FString%5FSystem%5FDouble%5F%5F)Get(string, ref double)

Get the value for the custom property name on this member

##### Declaration

```
public bool Get(string name, ref double value)
```

##### Parameters

| Type                                                           | Name  | Description                                           |
| -------------------------------------------------------------- | ----- | ----------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name  | Set to the value if it's found, and true is returned. |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value |                                                       |

##### Returns

| Type                                                          | Description                                           |
| ------------------------------------------------------------- | ----------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | true if the value is found and is of the correct type |

##### Exceptions

| Type                                                                                                       | Condition                                                             |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| [CustomPropertyMissingException](DesignData.SDS2.Exceptions.CustomPropertyMissingException.html)           | If the custom property is not found in the schema                     |
| [CustomPropertyTypeMismatchException](DesignData.SDS2.Exceptions.CustomPropertyTypeMismatchException.html) | If the custom property is in the schema with a type other than double |

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FGet%5FSystem%5FString%5FSystem%5FNullable%5FSystem%5FDateTime%5F%5F%5F)Get(string, ref DateTime?)

Get the value for the custom property name on this member

##### Declaration

```
public bool Get(string name, ref DateTime? value)
```

##### Parameters

| Type                                                                | Name  | Description                                           |
| ------------------------------------------------------------------- | ----- | ----------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string)      | name  | Set to the value if it's found, and true is returned. |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | value |                                                       |

##### Returns

| Type                                                          | Description                                           |
| ------------------------------------------------------------- | ----------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | true if the value is found and is of the correct type |

##### Exceptions

| Type                                                                                                       | Condition                                                               |
| ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [CustomPropertyMissingException](DesignData.SDS2.Exceptions.CustomPropertyMissingException.html)           | If the custom property is not found in the schema                       |
| [CustomPropertyTypeMismatchException](DesignData.SDS2.Exceptions.CustomPropertyTypeMismatchException.html) | If the custom property is in the schema with a type other than DateTime |

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FGet%5FSystem%5FString%5FSystem%5FString%5F%5F)Get(string, ref string)

Lookup the value for the custom property name on this member

##### Declaration

```
public bool Get(string name, ref string value)
```

##### Parameters

| Type                                                           | Name  | Description                                           |
| -------------------------------------------------------------- | ----- | ----------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name  | Set to the value if it's found, and true is returned. |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | value |                                                       |

##### Returns

| Type                                                          | Description                                           |
| ------------------------------------------------------------- | ----------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | true if the value is found and is of the correct type |

##### Exceptions

| Type                                                                                                       | Condition                                                             |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| [CustomPropertyMissingException](DesignData.SDS2.Exceptions.CustomPropertyMissingException.html)           | If the custom property is not found in the schema                     |
| [CustomPropertyTypeMismatchException](DesignData.SDS2.Exceptions.CustomPropertyTypeMismatchException.html) | If the custom property is in the schema with a type other than string |

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FGetPropertyType%5FSystem%5FString%5F)GetPropertyType(string)

Get the type of a value. Which will be None if this does not exist

##### Declaration

```
public CustomPropertyValueType GetPropertyType(string name)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name |             |

##### Returns

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [CustomPropertyValueType](DesignData.SDS2.Setup.CustomPropertyValueType.html) |             |

##### Remarks

For Dimensions this returns Double to maintain compatibility, and reduce unnecessary code. To distinguish between doubles and dimensions look at Setup.CustomPropertySchema, that type will be dimension if it's a dimension.

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FSet%5FSystem%5FString%5FSystem%5FBoolean%5F)Set(string, bool)

Set the value for the custom property name on this member

##### Declaration

```
public bool Set(string name, bool value)
```

##### Parameters

| Type                                                           | Name  | Description                                           |
| -------------------------------------------------------------- | ----- | ----------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name  | Set to the value if it's found, and true is returned. |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)  | value |                                                       |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                                                       | Condition                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [CustomPropertyMissingException](DesignData.SDS2.Exceptions.CustomPropertyMissingException.html)           | If the custom property is not found in the schema                                                        |
| [CustomPropertyTypeMismatchException](DesignData.SDS2.Exceptions.CustomPropertyTypeMismatchException.html) | If the custom property is in the schema with a type other than bool                                      |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)                                     | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)                                   | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FSet%5FSystem%5FString%5FSystem%5FDouble%5F)Set(string, double)

Set the value for the custom property name on this member

##### Declaration

```
public bool Set(string name, double value)
```

##### Parameters

| Type                                                           | Name  | Description                                           |
| -------------------------------------------------------------- | ----- | ----------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name  | Set to the value if it's found, and true is returned. |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | value |                                                       |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                                                       | Condition                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [CustomPropertyMissingException](DesignData.SDS2.Exceptions.CustomPropertyMissingException.html)           | If the custom property is not found in the schema                                                        |
| [CustomPropertyTypeMismatchException](DesignData.SDS2.Exceptions.CustomPropertyTypeMismatchException.html) | If the custom property is in the schema with a type other than double                                    |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)                                     | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)                                   | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FSet%5FSystem%5FString%5FSystem%5FNullable%5FSystem%5FDateTime%5F%5F)Set(string, DateTime?)

Set the value for the custom property name on this member

##### Declaration

```
public bool Set(string name, DateTime? value)
```

##### Parameters

| Type                                                                | Name  | Description                                           |
| ------------------------------------------------------------------- | ----- | ----------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string)      | name  | Set to the value if it's found, and true is returned. |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? | value |                                                       |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                                                       | Condition                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [CustomPropertyMissingException](DesignData.SDS2.Exceptions.CustomPropertyMissingException.html)           | If the custom property is not found in the schema                                                        |
| [CustomPropertyTypeMismatchException](DesignData.SDS2.Exceptions.CustomPropertyTypeMismatchException.html) | If the custom property is in the schema with a type other than DateTime                                  |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)                                     | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)                                   | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FSet%5FSystem%5FString%5FSystem%5FString%5F)Set(string, string)

Set the value for the custom property name on this member

##### Declaration

```
public bool Set(string name, string value)
```

##### Parameters

| Type                                                           | Name  | Description                                           |
| -------------------------------------------------------------- | ----- | ----------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name  | Set to the value if it's found, and true is returned. |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | value |                                                       |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                                                       | Condition                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [CustomPropertyMissingException](DesignData.SDS2.Exceptions.CustomPropertyMissingException.html)           | If the custom property is not found in the schema                                                        |
| [CustomPropertyTypeMismatchException](DesignData.SDS2.Exceptions.CustomPropertyTypeMismatchException.html) | If the custom property is in the schema with a type other than string                                    |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)                                     | Thrown when setting data on the object without having added it to a transaction                          |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)                                   | Thrown when reading or writing the property of an object that was added to a transaction but is unlocked |