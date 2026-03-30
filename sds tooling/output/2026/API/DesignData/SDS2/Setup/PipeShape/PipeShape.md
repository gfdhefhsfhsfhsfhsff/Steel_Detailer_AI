# Class PipeShape 

A Shape derived class.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

[RolledShape](DesignData.SDS2.Setup.RolledShape.html)

PipeShape

##### Inherited Members

[RolledShape.Depth](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FDepth) 

[RolledShape.NominalDepth](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FNominalDepth) 

[RolledShape.WeightPerUnitFoot](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FWeightPerUnitFoot) 

[Shape.GetHashCode()](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FGetHashCode) 

[Shape.Equals(object)](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FEquals%5FSystem%5FObject%5F) 

[Shape.SectionSize](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FSectionSize) 

[Shape.IsAvailable](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FIsAvailable) 

[Shape.SourceReference](DesignData.SDS2.Setup.Shape.html#DesignData%5FSDS2%5FSetup%5FShape%5FSourceReference) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class PipeShape : RolledShape
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FPipeShape%5F%5Fctor)PipeShape()

A Shape derived class.

##### Declaration

```
public PipeShape()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FPipeShape%5FThickness)Thickness

Wall thickness

##### Declaration

```
public double Thickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FPipeShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A Shape derived class.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[RolledShape.Dispose(bool)](DesignData.SDS2.Setup.RolledShape.html#DesignData%5FSDS2%5FSetup%5FRolledShape%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FSetup%5FPipeShape%5FGetStructuralProperties%5FDesignData%5FSDS2%5FSetup%5FSteelGrade%5F)GetStructuralProperties(SteelGrade)

Get the structural properties, from the production standard, for a specific grade. To get the default standard pass null for the grade

##### Declaration

```
public TubeStructuralProperties GetStructuralProperties(SteelGrade forGrade)
```

##### Parameters

| Type                                                | Name     | Description                                                                                                                                                                                                                      |
| --------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | forGrade | Production standards are under grade names for many types, so passing in the grade lets us lookup StructuralProperties for a specific production standard for this grade. There is also always a default, pass null to get this. |

##### Returns

| Type                                                                            | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [TubeStructuralProperties](DesignData.SDS2.Setup.TubeStructuralProperties.html) |             |