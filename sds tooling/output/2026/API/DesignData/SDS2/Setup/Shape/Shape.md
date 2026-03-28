# Class Shape 

Shape is the base class for all the shapes in the material file.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Shape

[AngleShape](DesignData.SDS2.Setup.AngleShape.html)

[BeadedFlatShape](DesignData.SDS2.Setup.BeadedFlatShape.html)

[ClevisShape](DesignData.SDS2.Setup.ClevisShape.html)

[CruciformShape](DesignData.SDS2.Setup.CruciformShape.html)

[JoistShape](DesignData.SDS2.Setup.JoistShape.html)

[RailShape](DesignData.SDS2.Setup.RailShape.html)

[RolledShape](DesignData.SDS2.Setup.RolledShape.html)

[RoundBarShape](DesignData.SDS2.Setup.RoundBarShape.html)

[TubeShape](DesignData.SDS2.Setup.TubeShape.html)

[TurnbuckleShape](DesignData.SDS2.Setup.TurnbuckleShape.html)

[WeldedBoxShape](DesignData.SDS2.Setup.WeldedBoxShape.html)

[WeldedWideFlangeShape](DesignData.SDS2.Setup.WeldedWideFlangeShape.html)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class Shape
```

##### **Remarks**

Shape objects are all essentially by value in that when you grab one from a material file you're getting a copy of that data. So making changes to it will not impact the material file. Modifying it, and then setting that modified shape to a material will not yield your modifications; because all shapes set to material must be in the material file.

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FShape%5FIsAvailable)IsAvailable

Specifies if the size is available from the mill

##### Declaration

```
public bool IsAvailable { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Shape objects are all essentially by value in that when you grab one from a material file you're getting a copy of that data. So making changes to it will not impact the material file. Modifying it, and then setting that modified shape to a material will not yield your modifications; because all shapes set to material must be in the material file.

#### [](#DesignData%5FSDS2%5FSetup%5FShape%5FSectionSize)SectionSize

The section size string of the shape.

##### Declaration

```
public string SectionSize { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

Shape objects are all essentially by value in that when you grab one from a material file you're getting a copy of that data. So making changes to it will not impact the material file. Modifying it, and then setting that modified shape to a material will not yield your modifications; because all shapes set to material must be in the material file.

#### [](#DesignData%5FSDS2%5FSetup%5FShape%5FSourceReference)SourceReference

The reference material this shape is pulled from

##### Declaration

```
public string SourceReference { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

Shape objects are all essentially by value in that when you grab one from a material file you're getting a copy of that data. So making changes to it will not impact the material file. Modifying it, and then setting that modified shape to a material will not yield your modifications; because all shapes set to material must be in the material file.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FShape%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Shape is the base class for all the shapes in the material file.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Remarks

Shape objects are all essentially by value in that when you grab one from a material file you're getting a copy of that data. So making changes to it will not impact the material file. Modifying it, and then setting that modified shape to a material will not yield your modifications; because all shapes set to material must be in the material file.

#### [](#DesignData%5FSDS2%5FSetup%5FShape%5FEquals%5FSystem%5FObject%5F)Equals(object)

Shape is the base class for all the shapes in the material file.

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

Shape objects are all essentially by value in that when you grab one from a material file you're getting a copy of that data. So making changes to it will not impact the material file. Modifying it, and then setting that modified shape to a material will not yield your modifications; because all shapes set to material must be in the material file.

#### [](#DesignData%5FSDS2%5FSetup%5FShape%5FFinalize)\~Shape()

Shape is the base class for all the shapes in the material file.

##### Declaration

```
protected ~Shape()
```

##### Remarks

Shape objects are all essentially by value in that when you grab one from a material file you're getting a copy of that data. So making changes to it will not impact the material file. Modifying it, and then setting that modified shape to a material will not yield your modifications; because all shapes set to material must be in the material file.

#### [](#DesignData%5FSDS2%5FSetup%5FShape%5FGetHashCode)GetHashCode()

Shape is the base class for all the shapes in the material file.

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

Shape objects are all essentially by value in that when you grab one from a material file you're getting a copy of that data. So making changes to it will not impact the material file. Modifying it, and then setting that modified shape to a material will not yield your modifications; because all shapes set to material must be in the material file.