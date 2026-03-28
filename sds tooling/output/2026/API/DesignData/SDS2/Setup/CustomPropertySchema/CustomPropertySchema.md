# Class CustomPropertySchema 

A custom property schema. This is the definition for properties on a type of element/object in the model (member/material/bolt/weld/etc). It's essentially a list of the types of properties available.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CustomPropertySchema

##### Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

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
public sealed class CustomPropertySchema : IEnumerable
```

##### **Remarks**

This schema is editable, but it will be a copy, so changes are not stored in the database when they're made on this object.

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPropertySchema%5FCount)Count

Get count of spacings

##### Declaration

```
public int Count { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Remarks

This schema is editable, but it will be a copy, so changes are not stored in the database when they're made on this object.

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPropertySchema%5FItem%5FSystem%5FInt32%5F)this\[int\]

Get the nth spacing

##### Declaration

```
public CustomProperty this[int index] { get; }
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | index |             |

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [CustomProperty](DesignData.SDS2.Setup.CustomProperty.html) |             |

##### Remarks

This schema is editable, but it will be a copy, so changes are not stored in the database when they're made on this object.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPropertySchema%5FContains%5FSystem%5FString%5FDesignData%5FSDS2%5FSetup%5FCustomPropertyValueType%5FSystem%5FNullable%5FSystem%5FBoolean%5F%5FSystem%5FNullable%5FSystem%5FBoolean%5F%5FSystem%5FNullable%5FSystem%5FBoolean%5F%5FSystem%5FNullable%5FSystem%5FBoolean%5F%5F)Contains(string, CustomPropertyValueType, bool?, bool?, bool?, bool?)

Returns true if a matching property exists in this schema. You must give a name and a type to be checked, but all other properties (remarkable, hashable, erectionViewable, exported) are optional. If they're not specified then this will return a match regardless of those values on the property in the schema.

##### Declaration

```
public bool Contains(string name, CustomPropertyValueType type, bool? remarkable = null, bool? hashable = null, bool? erectionViewable = null, bool? exported = null)
```

##### Parameters

| Type                                                                          | Name             | Description                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string)                | name             | The Name field of a CustomProperty                                                                                                                                                                                           |
| [CustomPropertyValueType](DesignData.SDS2.Setup.CustomPropertyValueType.html) | type             | The Type field of a CustomProperty.                                                                                                                                                                                          |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)?                | remarkable       | The IsRemarkable field of a CustomProperty. If unset or null is passed in, then we won't check this property. If set to true or false then true is only returned if a property has remarkable set to that value.             |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)?                | hashable         | The IsHashable field of a CustomProperty. If unset or null is passed in, then we won't check this property. If set to true or false then true is only returned if a property has hashable set to that value.                 |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)?                | erectionViewable | The IsErectionViewable field of a CustomProperty. If unset or null is passed in, then we won't check this property. If set to true or false then true is only returned if a property has erectionViewable set to that value. |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)?                | exported         | The IsExported field of a CustomProperty. If unset or null is passed in, then we won't check this property. If set to true or false then true is only returned if a property has exported set to that value.                 |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

This schema is editable, but it will be a copy, so changes are not stored in the database when they're made on this object.

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPropertySchema%5FFinalize)\~CustomPropertySchema()

A custom property schema. This is the definition for properties on a type of element/object in the model (member/material/bolt/weld/etc). It's essentially a list of the types of properties available.

##### Declaration

```
protected ~CustomPropertySchema()
```

##### Remarks

This schema is editable, but it will be a copy, so changes are not stored in the database when they're made on this object.

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPropertySchema%5FGet%5FDesignData%5FSDS2%5FSetup%5FCustomPropertyItemType%5F)Get(CustomPropertyItemType)

Get a copy of the custom property schema for the given item type

##### Declaration

```
public static CustomPropertySchema Get(CustomPropertyItemType itemType)
```

##### Parameters

| Type                                                                        | Name     | Description                                                                                     |
| --------------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------- |
| [CustomPropertyItemType](DesignData.SDS2.Setup.CustomPropertyItemType.html) | itemType | There are different schemas for members, materials, etc, specify which you want the schema for. |

##### Returns

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [CustomPropertySchema](DesignData.SDS2.Setup.CustomPropertySchema.html) |             |

##### Remarks

This schema is editable, but it will be a copy, so changes are not stored in the database when they're made on this object.

#### [](#DesignData%5FSDS2%5FSetup%5FCustomPropertySchema%5FGetEnumerator)GetEnumerator()

Get the enumerator object

##### Declaration

```
public IEnumerator GetEnumerator()
```

##### Returns

| Type                                                                                 | Description |
| ------------------------------------------------------------------------------------ | ----------- |
| [IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator) |             |

##### Remarks

This schema is editable, but it will be a copy, so changes are not stored in the database when they're made on this object.

### [](#implements)Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)