# Class CruciformShape 

Base class for Cruciform Shape Material. Derived from the Shape class.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

CruciformShape

[PLCruciformShape](DesignData.SDS2.Setup.PLCruciformShape.html)

[PLWTCruciformShape](DesignData.SDS2.Setup.PLWTCruciformShape.html)

[WFPLCruciformShape](DesignData.SDS2.Setup.WFPLCruciformShape.html)

[WFWTCruciformShape](DesignData.SDS2.Setup.WFWTCruciformShape.html)

##### Inherited Members

[Shape.GetHashCode()](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FGetHashCode) 

[Shape.Equals(object)](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FEquals%5FSystem%5FObject%5F) 

[Shape.SectionSize](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FSectionSize) 

[Shape.IsAvailable](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FIsAvailable) 

[Shape.SourceReference](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FSourceReference) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class CruciformShape : Shape
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FCruciformShape%5FCruciformSubType)CruciformSubType

Identifies the specific subtype of the cruciform material. Uses CruciformSubType.

##### Declaration

```
public CruciformSubType CruciformSubType { get; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [CruciformSubType](DesignData.SDS2.Setup.CruciformSubType.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FCruciformShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base class for Cruciform Shape Material. Derived from the Shape class.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[Shape.Dispose(bool)](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FCruciformShape%5FGetStructuralProperties%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F)GetStructuralProperties(SteelGrade)

Get the structural properties, from the production standard, for a specific grade. To get the default standard pass null for the grade

##### Declaration

```
public ChannelTeeStructuralProperties GetStructuralProperties(SteelGrade forGrade)
```

##### Parameters

| Type                                                | Name     | Description                                                                                                                                                                                                                      |
| --------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | forGrade | Production standards are under grade names for many types, so passing in the grade lets us lookup StructuralProperties for a specific production standard for this grade. There is also always a default, pass null to get this. |

##### Returns

| Type                                                                                        | Description |
| ------------------------------------------------------------------------------------------- | ----------- |
| [ChannelTeeStructuralProperties](DesignData.SDS2.Setup.ChannelTeeStructuralProperties.html) |             |