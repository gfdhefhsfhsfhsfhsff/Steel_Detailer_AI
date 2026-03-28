# Class ColumnUserBaseCapPlateSpecification 

A user specified base or cap plate connection

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

ColumnUserBaseCapPlateSpecification

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
public sealed class ColumnUserBaseCapPlateSpecification : ConnectionSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FColumnUserBaseCapPlateSpecification%5F%5Fctor)ColumnUserBaseCapPlateSpecification()

A user specified base or cap plate connection

##### Declaration

```
public ColumnUserBaseCapPlateSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FColumnUserBaseCapPlateSpecification%5FAlignStiffenersWith)AlignStiffenersWith

Automatic specifies that the system apply a setup choice (Fabricator Setup > Standard Fabricator Connections > Cap Plate Setup > "Align transverse stiffeners with").

```
        Column instructs the system to create transverse beam stiffeners
        that are parallel with the workline (stick form member line) of
        the column.

        Beam configures the system to create transverse beam stiffeners
        that are perpendicular to the workline of the beam. The
        stiffeners are normal to the beam, regardless of the slope of the
        beam or column.

```

##### Declaration

```
public StiffenerAlignment AlignStiffenersWith { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [StiffenerAlignment](DesignData.SDS2.Model.StiffenerAlignment.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnUserBaseCapPlateSpecification%5FPlateDefinition)PlateDefinition

The base or cap plate to use for this connection. These can be found in the job setup object.

##### Declaration

```
public BaseCapPlate PlateDefinition { get; set; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [BaseCapPlate](DesignData.SDS2.Setup.BaseCapPlate.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnUserBaseCapPlateSpecification%5FPlateRotation)PlateRotation

The rotation of the plate around its center

##### Declaration

```
public double PlateRotation { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnUserBaseCapPlateSpecification%5FPlateYOffset)PlateYOffset

The horizontal offset of the center of the plate from the center of the column

##### Declaration

```
public double PlateYOffset { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnUserBaseCapPlateSpecification%5FPlateZOffset)PlateZOffset

The vertical offset of the center of the plate from the center of the column

##### Declaration

```
public double PlateZOffset { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnUserBaseCapPlateSpecification%5FUseExtendedStiffeners)UseExtendedStiffeners

Automatic specifies that the system look at the Fabricator Setup > Standard Fabricator Connections > Extended Flange Plate Setup > "Plate overhang tolerance" to determine whether or not to design a connection. If the setup value is less than or equal to the actual base/cap plate overhang in the model, then a connection will be designed. If the setup value is greater than the overhang, a connection is not designed.

```
        Yes instructs the system to attempt to design flange extension
        plates and stiffeners. If it is determined that such a connection
        should not be designed, for example, because of interference with
        another member, the system locks are populated with null values
        (e.g. distances of 0) in leaves named " Bottom extension plate"
        or " Top extension plate" and " Stiffener Plate."

        No results in no flange extension plates and beam stiffeners.

```

##### Declaration

```
public AutomaticYesNo UseExtendedStiffeners { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FColumnUserBaseCapPlateSpecification%5FUseTransverseBeamStiffener)UseTransverseBeamStiffener

Whether or not to use a transverse beam stiffener.

```
                Automatic specifies that the system apply a setup choice (Job
                Setup > Design Settings > "Always provide transverse beam
                stiffener").

                Yes instructs the system to create at least one pair of
                full-depth transverse beam stiffeners (one on the beam's near
                side, one far side) regardless of the "Load" on the column. Two
                pairs of stiffeners are created when the "Load" is sufficiently
                large. The two pairs of stiffeners align with the flanges of the
                column. A single pair of stiffeners is centered with respect to
                the column member line.

                No instructs the system to not create a pair of transverse
                beam stiffeners, even when the column's "Load" is large enough
                that the beam's web capacity is exceeded. If the system
                determines that the web capacity of the beam is exceeded, a
                connection is not designed, and you get the following end
                connection failure message: "Conn modified by framing situation,
                see Design Calcs."

```

##### Declaration

```
public AutomaticYesNo UseTransverseBeamStiffener { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FColumnUserBaseCapPlateSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A user specified base or cap plate connection

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[ConnectionSpecification.Dispose(bool)](DesignData.SDS2.Model.ConnectionSpecification.html#DesignData%5FSDS2%5FModel%5FConnectionSpecification%5FDispose%5FSystem%5FBoolean%5F)