# Class ModelViewDescription 

This has been renamed ModelViewDefinition, please reference that class from now on.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ModelViewDescription

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
[Obsolete("This enum was renamed to ModelViewDefinition, please reference that.", false)]
public sealed class ModelViewDescription
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5F%5Fctor)ModelViewDescription()

This has been renamed ModelViewDefinition, please reference that class from now on.

##### Declaration

```
public ModelViewDescription()
```

### [](#fields)Fields 

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5FACI131ConcreteReinforcement)ACI131ConcreteReinforcement

IFC 4 ACI 131.2R-17 contains only concrete reinforcement materials

##### Declaration

```
[Obsolete("This enum was renamed to ModelViewDefinition. Please reference that.", false)]
public static ModelViewDefinition ACI131ConcreteReinforcement
```

##### Field Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [ModelViewDefinition](DesignData.SDS2.Model.ModelViewDefinition.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5FCoordinationView2)CoordinationView2

IFC 2x3 Coordination View 2.0 is the most common MVD used worldwide

##### Declaration

```
[Obsolete("This enum was renamed to ModelViewDefinition. Please reference that.", false)]
public static ModelViewDefinition CoordinationView2
```

##### Field Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [ModelViewDefinition](DesignData.SDS2.Model.ModelViewDefinition.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5FDesignTransferView)DesignTransferView

IFC 4 Design Transfer View is the most common, general purpose IFC 4 MVD

##### Declaration

```
[Obsolete("This enum was renamed to ModelViewDefinition. Please reference that.", false)]
public static ModelViewDefinition DesignTransferView
```

##### Field Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [ModelViewDefinition](DesignData.SDS2.Model.ModelViewDefinition.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5FEM11SteelFabrication)EM11SteelFabrication

IFC 2x3 EM11 is an AISC creation used only by steel fabricators

##### Declaration

```
[Obsolete("This enum was renamed to ModelViewDefinition. Please reference that.", false)]
public static ModelViewDefinition EM11SteelFabrication
```

##### Field Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [ModelViewDefinition](DesignData.SDS2.Model.ModelViewDefinition.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5FReferenceView)ReferenceView

IFC 4 Reference View provides little benefit and isn't supported yet

##### Declaration

```
[Obsolete("This enum was renamed to ModelViewDefinition. Please reference that.", false)]
public static ModelViewDefinition ReferenceView
```

##### Field Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [ModelViewDefinition](DesignData.SDS2.Model.ModelViewDefinition.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5FUnknown)Unknown

Using 'unknown' is an error condition

##### Declaration

```
[Obsolete("This enum was renamed to ModelViewDefinition. Please reference that.", false)]
public static ModelViewDefinition Unknown
```

##### Field Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [ModelViewDefinition](DesignData.SDS2.Model.ModelViewDefinition.html) |             |

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5Fop%5FExplicit%5FDesignData%5FSDS2%5FModel%5FModelViewDescription%5F%5FSystem%5FInt32)explicit operator int(ModelViewDescription)

Implicitly convert between new name and obsoleted name

##### Declaration

```
public static explicit operator int(ModelViewDescription mvd)
```

##### Parameters

| Type                                                                    | Name | Description |
| ----------------------------------------------------------------------- | ---- | ----------- |
| [ModelViewDescription](DesignData.SDS2.Model.ModelViewDescription.html) | mvd  |             |

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FModelViewDefinition%5F%5FDesignData%5FSDS2%5FModel%5FModelViewDescription)implicit operator ModelViewDescription(ModelViewDefinition)

Implicitly convert between new name and obsoleted name

##### Declaration

```
public static implicit operator ModelViewDescription(ModelViewDefinition mvd)
```

##### Parameters

| Type                                                                  | Name | Description |
| --------------------------------------------------------------------- | ---- | ----------- |
| [ModelViewDefinition](DesignData.SDS2.Model.ModelViewDefinition.html) | mvd  |             |

##### Returns

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [ModelViewDescription](DesignData.SDS2.Model.ModelViewDescription.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5Fop%5FImplicit%5FDesignData%5FSDS2%5FModel%5FModelViewDescription%5F%5FDesignData%5FSDS2%5FModel%5FModelViewDefinition)implicit operator ModelViewDefinition(ModelViewDescription)

Implicitly convert between new name and obsoleted name

##### Declaration

```
public static implicit operator ModelViewDefinition(ModelViewDescription mvd)
```

##### Parameters

| Type                                                                    | Name | Description |
| ----------------------------------------------------------------------- | ---- | ----------- |
| [ModelViewDescription](DesignData.SDS2.Model.ModelViewDescription.html) | mvd  |             |

##### Returns

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [ModelViewDefinition](DesignData.SDS2.Model.ModelViewDefinition.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FModelViewDescription%5Fop%5FImplicit%5FSystem%5FInt32%5F%5FDesignData%5FSDS2%5FModel%5FModelViewDescription)implicit operator ModelViewDescription(int)

Implicitly convert between new name and obsoleted name

##### Declaration

```
public static implicit operator ModelViewDescription(int v)
```

##### Parameters

| Type                                                       | Name | Description |
| ---------------------------------------------------------- | ---- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | v    |             |

##### Returns

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [ModelViewDescription](DesignData.SDS2.Model.ModelViewDescription.html) |             |