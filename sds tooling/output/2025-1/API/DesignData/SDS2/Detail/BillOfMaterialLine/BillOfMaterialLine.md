# Class BillOfMaterialLine 

One line of a bill of material

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BillOfMaterialLine

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Detail](DesignData.SDS2.Detail.html)

###### **Assembly**: DesignData.SDS2.Detail.dll

##### Syntax

```
public class BillOfMaterialLine
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FAdvanceMill)AdvanceMill

The ABM page-line number (page-line) that is assigned to the piece of material listed on this line in the physical bill of material.

##### Declaration

```
public string AdvanceMill { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FDescription)Description

A description of the member or material. For a member, the description is the member type. For a submaterial, the description is the section size.

##### Declaration

```
public string Description { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FGrade)Grade

The steel grade of the material.

##### Declaration

```
public string Grade { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FIsLineHidden)IsLineHidden

Determines if the line is hidden in the bill of material.

##### Declaration

```
public bool IsLineHidden { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FLength)Length

The length of the material along its X material axis.

##### Declaration

```
public double Length { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FLineNumber)LineNumber

Line number

##### Declaration

```
public string LineNumber { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FMinorMark)MinorMark

The submaterial piecemark (material mark) of a material.

##### Declaration

```
public string MinorMark { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FPiecemark)Piecemark

The member piecemark of the shipping piece.

##### Declaration

```
public string Piecemark { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FRemarks)Remarks

User-entered comments and/or information automatically compiled from fields that are set to 'Merge'.

##### Declaration

```
public string Remarks { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FRevision)Revision

Revision

##### Declaration

```
public string Revision { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FRoute1)Route1

May be a definition from routing configuration #1 that was applied to a member or material, or it may be that a user has manually typed in infomation to the "Mult. Cutting #" column in the bill editor.

##### Declaration

```
public string Route1 { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FRoute2)Route2

May be a definition from routing configuration #2 that was applied to a member or material. Or it may be that a user has manually typed in information to the "Labor Code" column in the bill editor.

##### Declaration

```
public string Route2 { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FRoute3)Route3

May be a definition from routing configuration #3 that was applied to a member or material. Or it may be that a user has manually typed in information to the "Job Cost Code" column in the bill editor.

##### Declaration

```
public string Route3 { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FTotalQuantity)TotalQuantity

The count of submaterials required to fabricate the total number of shipping pieces (members).

##### Declaration

```
public int TotalQuantity { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FTotalWeight)TotalWeight

For a member, this is the total combined weight of the submaterials required to fabricate all shipping members that receive the same major mark. For a submaterial, this is the weight of all pieces of that submaterial.

##### Declaration

```
public double TotalWeight { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FUnitQuantity)UnitQuantity

The count of pieces of a particular submaterial that are required to fabricate one of the shipping pieces (members)

##### Declaration

```
public int UnitQuantity { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FUnitWeight)UnitWeight

For a member, this is the total combined weight of the submaterial pieces required to fabricate one shipping member. For a submaterial, this is the weight of one piece of submaterial.

##### Declaration

```
public double UnitWeight { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

One line of a bill of material

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterialLine%5FFinalize)\~BillOfMaterialLine()

One line of a bill of material

##### Declaration

```
protected ~BillOfMaterialLine()
```