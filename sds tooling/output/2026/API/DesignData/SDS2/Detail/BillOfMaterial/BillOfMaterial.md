# Class BillOfMaterial 

The bill of materials for a drawing

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BillOfMaterial

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
public class BillOfMaterial
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterial%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

The bill of materials for a drawing

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterial%5FFinalize)\~BillOfMaterial()

The bill of materials for a drawing

##### Declaration

```
protected ~BillOfMaterial()
```

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterial%5FGetLines)GetLines()

All the lines of bill of material.

##### Declaration

```
public BillLineList GetLines()
```

##### Returns

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [BillLineList](DesignData.SDS2.Detail.BillLineList.html) |             |

#### [](#DesignData%5FSDS2%5FDetail%5FBillOfMaterial%5FGetSequences)GetSequences()

Bill of material sequences.

##### Declaration

```
public BillSequenceList GetSequences()
```

##### Returns

| Type                                                             | Description |
| ---------------------------------------------------------------- | ----------- |
| [BillSequenceList](DesignData.SDS2.Detail.BillSequenceList.html) |             |