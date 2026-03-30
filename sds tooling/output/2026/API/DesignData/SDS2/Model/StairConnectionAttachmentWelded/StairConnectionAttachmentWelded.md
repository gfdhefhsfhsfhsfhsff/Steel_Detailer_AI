# Class StairConnectionAttachmentWelded 

Welded StairConnection attachment

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[StairConnectionAttachmentSpecification](DesignData.SDS2.Model.StairConnectionAttachmentSpecification.html)

StairConnectionAttachmentWelded

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
public sealed class StairConnectionAttachmentWelded : StairConnectionAttachmentSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentWelded%5F%5Fctor)StairConnectionAttachmentWelded()

Welded StairConnection attachment

##### Declaration

```
public StairConnectionAttachmentWelded()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentWelded%5FSize)Size

Weld size

##### Declaration

```
public double Size { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                       |
| ------------------------------------------------------------------------------ | ------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown for negative weld sizes. |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnectionAttachmentWelded%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Welded StairConnection attachment

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