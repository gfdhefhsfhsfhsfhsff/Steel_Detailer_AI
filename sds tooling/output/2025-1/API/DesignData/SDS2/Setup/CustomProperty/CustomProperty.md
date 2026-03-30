# Class CustomProperty 

Schema entry for a single custom property

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CustomProperty

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
public sealed class CustomProperty
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FCustomProperty%5FIsErectionViewable)IsErectionViewable

Schema entry for a single custom property

##### Declaration

```
public bool IsErectionViewable { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomProperty%5FIsExported)IsExported

Schema entry for a single custom property

##### Declaration

```
public bool IsExported { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomProperty%5FIsHashable)IsHashable

If true, changing this property will separate piecemarks for material and members

##### Declaration

```
public bool IsHashable { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

For other types this has no effect

#### [](#DesignData%5FSDS2%5FSetup%5FCustomProperty%5FIsRemarkable)IsRemarkable

Schema entry for a single custom property

##### Declaration

```
public bool IsRemarkable { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomProperty%5FLabel)Label

The user visible label for this property

##### Declaration

```
public string Label { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomProperty%5FName)Name

The name for this property within the schema. This is the name used to look it up on a CustomPropertyMap in the model namespace

##### Declaration

```
public string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FCustomProperty%5FType)Type

The value type

##### Declaration

```
public CustomPropertyValueType Type { get; }
```

##### Property Value

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [CustomPropertyValueType](DesignData.SDS2.Setup.CustomPropertyValueType.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FCustomProperty%5FFinalize)\~CustomProperty()

Schema entry for a single custom property

##### Declaration

```
protected ~CustomProperty()
```