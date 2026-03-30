# Class BaseCapPlateWeldFullSpecification 

If you want different options for web, flange, and seal welds use this option.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[BaseCapPlateWelds](DesignData.SDS2.Setup.BaseCapPlateWelds.html)

BaseCapPlateWeldFullSpecification

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class BaseCapPlateWeldFullSpecification : BaseCapPlateWelds
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldFullSpecification%5FFlangeWeldSide)FlangeWeldSide

Weld side option for the flanges

##### Declaration

```
public WeldSide FlangeWeldSide { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldSide](DesignData.SDS2.Setup.WeldSide.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldFullSpecification%5FFlangeWeldSize)FlangeWeldSize

The size of the flange weld

##### Declaration

```
public double FlangeWeldSize { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldFullSpecification%5FFlangeWeldType)FlangeWeldType

Set the flange weld type. This can only be WeldType.Fillet, WeldType.SquareGroove, or WeldType.BevelGroove

##### Declaration

```
public WeldType FlangeWeldType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldType](DesignData.SDS2.Setup.WeldType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldFullSpecification%5FSealWeldSize)SealWeldSize

Size of the seal weld

##### Declaration

```
public double SealWeldSize { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldFullSpecification%5FUseSealWeld)UseSealWeld

Whether or not to add seal welds

##### Declaration

```
public bool UseSealWeld { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldFullSpecification%5FWebWeldSide)WebWeldSide

Weld side option for the web, this can only be None or BothSides

##### Declaration

```
public WeldSide WebWeldSide { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldSide](DesignData.SDS2.Setup.WeldSide.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldFullSpecification%5FWebWeldSize)WebWeldSize

The size of the web weld

##### Declaration

```
public double WebWeldSize { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldFullSpecification%5FWebWeldType)WebWeldType

Set the web weld type. This can only be WeldType.Fillet or WeldType.SquareGroove

##### Declaration

```
public WeldType WebWeldType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldType](DesignData.SDS2.Setup.WeldType.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldFullSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

If you want different options for web, flange, and seal welds use this option.

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[BaseCapPlateWelds.Dispose(bool)](DesignData.SDS2.Setup.BaseCapPlateWelds.html#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWelds%5FDispose%5FSystem%5FBoolean%5F)