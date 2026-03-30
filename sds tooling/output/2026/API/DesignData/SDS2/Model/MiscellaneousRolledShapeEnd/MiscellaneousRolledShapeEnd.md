# Class MiscellaneousRolledShapeEnd 

End properties for a miscellaneous rolled shape/section, should be largely the same as to Model.ShapeMaterialEnd

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MiscellaneousRolledShapeEnd

##### Inherited Members

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
public class MiscellaneousRolledShapeEnd
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousRolledShapeEnd%5FBottomFlangeCutOperation)BottomFlangeCutOperation

The bottom flange cut operations. If no operation is set, this will be null.

##### Declaration

```
public FlangeCutOperation BottomFlangeCutOperation { get; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousRolledShapeEnd%5FFlangeCutAngle)FlangeCutAngle

Angle to cut across the end of the bar relative to the "Flange".

##### Declaration

```
public double FlangeCutAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousRolledShapeEnd%5FMaterialSetback)MaterialSetback

The setback from the end where the plate material starts.

##### Declaration

```
public double MaterialSetback { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousRolledShapeEnd%5FTopFlangeCutOperation)TopFlangeCutOperation

The top flange cut operations. If no operation is set, this will be null.

##### Declaration

```
public FlangeCutOperation TopFlangeCutOperation { get; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousRolledShapeEnd%5FWebCutAngle)WebCutAngle

Angle to cut across the end of the bar relative to the "Web".

##### Declaration

```
public double WebCutAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

These are in radians, but because SDS2 stores this particular angle in degrees you may see small changes after setting the value when you retrieve it, due to calculations

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousRolledShapeEnd%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

End properties for a miscellaneous rolled shape/section, should be largely the same as to Model.ShapeMaterialEnd

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousRolledShapeEnd%5FFinalize)\~MiscellaneousRolledShapeEnd()

End properties for a miscellaneous rolled shape/section, should be largely the same as to Model.ShapeMaterialEnd

##### Declaration

```
protected ~MiscellaneousRolledShapeEnd()
```

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousRolledShapeEnd%5FSetBottomFlangeCutOperation%5FDesignData%5FSDS2%5FModel%5FFlangeCutOperation%5F)SetBottomFlangeCutOperation(FlangeCutOperation)

When setting the cut operation, we will copy the options you give into our own data. Your operation passed in will not be a reference to the underlying operation. To get a reference you'll need to look to the BottomFlangeCutOperation property after assigning this.

##### Declaration

```
public void SetBottomFlangeCutOperation(FlangeCutOperation cutOperation)
```

##### Parameters

| Type                                                                | Name         | Description |
| ------------------------------------------------------------------- | ------------ | ----------- |
| [FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html) | cutOperation |             |

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousRolledShapeEnd%5FSetTopFlangeCutOperation%5FDesignData%5FSDS2%5FModel%5FFlangeCutOperation%5F)SetTopFlangeCutOperation(FlangeCutOperation)

When setting the cut operation, we will copy the options you give into our own data. Your operation passed in will not be a reference to the underlying operation. To get a reference you'll need to look to the TopFlangeCutOperation property after assigning this.

##### Declaration

```
public void SetTopFlangeCutOperation(FlangeCutOperation cutOperation)
```

##### Parameters

| Type                                                                | Name         | Description |
| ------------------------------------------------------------------- | ------------ | ----------- |
| [FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html) | cutOperation |             |