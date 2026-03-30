# Class ShapeMaterialEnd 

Collection of information about a rolled material's end

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html)

ShapeMaterialEnd

##### Inherited Members

[CuttableMaterialEnd.Setback](DesignData.SDS2.Model.CuttableMaterialEnd.html#DesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5FSetback) 

[CuttableMaterialEnd.WebCutAngle](DesignData.SDS2.Model.CuttableMaterialEnd.html#DesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5FWebCutAngle) 

[CuttableMaterialEnd.FlangeCutAngle](DesignData.SDS2.Model.CuttableMaterialEnd.html#DesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5FFlangeCutAngle) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class ShapeMaterialEnd : CuttableMaterialEnd
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FShapeMaterialEnd%5FBottomFlangeCutOperation)BottomFlangeCutOperation

The bottom flange cut operations. If no operation is set, this will be null.

##### Declaration

```
public FlangeCutOperation BottomFlangeCutOperation { get; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShapeMaterialEnd%5FEndCutType)EndCutType

The type or method of cut to make on this end.

##### Declaration

```
public EndCutType EndCutType { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [EndCutType](DesignData.SDS2.Model.EndCutType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FShapeMaterialEnd%5FMomentConnectionWebSetback)MomentConnectionWebSetback

The distance that you want the web of this material setback

##### Declaration

```
public double MomentConnectionWebSetback { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Only applies if top and bottom are one of CopeFieldWeldN1FEMA, CopeShopWeldN1FEMA, SeismicCopeFieldWeld, SeismicCopeShopWeld, CopeFieldWeldN3, CopeShopWeldN3

#### [](#DesignData%5FSDS2%5FModel%5FShapeMaterialEnd%5FTopFlangeCutOperation)TopFlangeCutOperation

The top flange cut operations. If no operation is set, this will be null.

##### Declaration

```
public FlangeCutOperation TopFlangeCutOperation { get; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FShapeMaterialEnd%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Collection of information about a rolled material's end

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[CuttableMaterialEnd.Dispose(bool)](DesignData.SDS2.Model.CuttableMaterialEnd.html#DesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FModel%5FShapeMaterialEnd%5FSetBottomFlangeCutOperation%5FDesignData%5FSDS2%5FModel%5FFlangeCutOperation%5F)SetBottomFlangeCutOperation(FlangeCutOperation)

When setting the cut operation, we will copy the options you give into our own data. Your operation passed in will not be a reference to the underlying operation. To get a reference you'll need to look to the BottomFlangeCutOperation property after assigning this.

##### Declaration

```
public void SetBottomFlangeCutOperation(FlangeCutOperation cutOperation)
```

##### Parameters

| Type                                                                | Name         | Description |
| ------------------------------------------------------------------- | ------------ | ----------- |
| [FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html) | cutOperation |             |

#### [](#DesignData%5FSDS2%5FModel%5FShapeMaterialEnd%5FSetTopFlangeCutOperation%5FDesignData%5FSDS2%5FModel%5FFlangeCutOperation%5F)SetTopFlangeCutOperation(FlangeCutOperation)

When setting the cut operation, we will copy the options you give into our own data. Your operation passed in will not be a reference to the underlying operation. To get a reference you'll need to look to the TopFlangeCutOperation property after assigning this.

##### Declaration

```
public void SetTopFlangeCutOperation(FlangeCutOperation cutOperation)
```

##### Parameters

| Type                                                                | Name         | Description |
| ------------------------------------------------------------------- | ------------ | ----------- |
| [FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html) | cutOperation |             |