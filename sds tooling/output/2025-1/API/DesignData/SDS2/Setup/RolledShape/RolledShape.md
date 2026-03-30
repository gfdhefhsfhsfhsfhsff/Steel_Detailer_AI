# Class RolledShape 

A base class for shapes which are either rolled, or share common rolled properties such as depth, nominal depth, and weight per unit foot.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Shape](DesignData.SDS2.Setup.Shape.html)

RolledShape

[ColdFormedShape](DesignData.SDS2.Setup.ColdFormedShape.html)

[PipeShape](DesignData.SDS2.Setup.PipeShape.html)

[RolledWebFlangeShape](DesignData.SDS2.Setup.RolledWebFlangeShape.html)

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
public class RolledShape : Shape
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FRolledShape%5FDepth)Depth

Depth of the shape.

##### Declaration

```
public double Depth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRolledShape%5FNominalDepth)NominalDepth

The rounded depth value used in the typical section size string

##### Declaration

```
public double NominalDepth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FRolledShape%5FWeightPerUnitFoot)WeightPerUnitFoot

For extruded profile shapes, this is the weight for each foot of the shape. This will be 0.0 for some shapes where it does not apply.

##### Declaration

```
public double WeightPerUnitFoot { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FRolledShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A base class for shapes which are either rolled, or share common rolled properties such as depth, nominal depth, and weight per unit foot.

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