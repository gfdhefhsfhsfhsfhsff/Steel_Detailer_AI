# Class StairConnectionAttachmentBolted 

Bolted StairConnection attachment

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[StairConnectionAttachmentSpecification](DesignData.SDS2.Model.StairConnectionAttachmentSpecification.html)

StairConnectionAttachmentBolted

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
public sealed class StairConnectionAttachmentBolted : StairConnectionAttachmentSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5F%5Fctor)StairConnectionAttachmentBolted()

Bolted StairConnection attachment

##### Declaration

```
public StairConnectionAttachmentBolted()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FBoltDiameter)BoltDiameter

Bolt diameter for the hole group

##### Declaration

```
public double BoltDiameter { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                       |
| ------------------------------------------------------------------------------ | ----------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown for diameters less than or equal to 0.0. |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FBoltType)BoltType

Specifies the bolt type for the bolts involved in the connection.

##### Declaration

```
public BoltType BoltType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

##### Remarks

Due to how the underlying Python data is stored, assigning BoltType will always turn off IsAutoBoltType.

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FColumnSpacing)ColumnSpacing

Distance between columns of the hole group

##### Declaration

```
public double ColumnSpacing { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FColumns)Columns

Number of columns in the hole group

##### Declaration

```
public int Columns { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FGageOutstandingLeg)GageOutstandingLeg

Distance from the connection material edge, the heel for clip angles, to the first hole.

##### Declaration

```
public double GageOutstandingLeg { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

For shear plates this is the horizontal to first hole distance.

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FHoleType)HoleType

Type of holes for the hole group

##### Declaration

```
public ConnSpecHoleTypeSubset HoleType { get; set; }
```

##### Property Value

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [ConnSpecHoleTypeSubset](DesignData.SDS2.Model.ConnSpecHoleTypeSubset.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FIsAutoBoltType)IsAutoBoltType

Specifies if the bolt type for the bolts involved in the connection should use the default bolt type defined in setup.

##### Declaration

```
public bool IsAutoBoltType { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Due to how the underlying Python data is stored, assigning BoltType will always turn off IsAutoBoltType.

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FRowSpacing)RowSpacing

Distance between rows of the hole group

##### Declaration

```
public double RowSpacing { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FRows)Rows

Number of rows for the hole group

##### Declaration

```
public int Rows { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FSlotRotation)SlotRotation

Slot rotation, in radians, of the hole group

##### Declaration

```
public double SlotRotation { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FStringerEdgeToFirstHole)StringerEdgeToFirstHole

Distance from the stringer edge to the first hole

##### Declaration

```
public double StringerEdgeToFirstHole { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

This is a vertical distance for vertical connections and a horizontal distance for floor clips.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentBolted%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Bolted StairConnection attachment

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[StairConnectionAttachmentSpecification.Dispose(bool)](DesignData.SDS2.Model.StairConnectionAttachmentSpecification.html#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentSpecification%5FDispose%5FSystem%5FBoolean%5F)