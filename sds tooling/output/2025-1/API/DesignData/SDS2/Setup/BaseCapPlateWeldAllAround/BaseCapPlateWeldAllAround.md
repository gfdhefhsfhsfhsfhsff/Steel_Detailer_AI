# Class BaseCapPlateWeldAllAround 

If you want the column welded all around to the base/cap plate use this set of options.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[BaseCapPlateWelds](DesignData.SDS2.Setup.BaseCapPlateWelds.html)

BaseCapPlateWeldAllAround

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
public class BaseCapPlateWeldAllAround : BaseCapPlateWelds
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldAllAround%5FWeldSize)WeldSize

The size of the weld

##### Declaration

```
public double WeldSize { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldAllAround%5FWeldType)WeldType

Set the weld type. This can only be WeldType.Fillet or WeldType.SquareGroove

##### Declaration

```
public WeldType WeldType { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldType](DesignData.SDS2.Setup.WeldType.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FBaseCapPlateWeldAllAround%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

If you want the column welded all around to the base/cap plate use this set of options.

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