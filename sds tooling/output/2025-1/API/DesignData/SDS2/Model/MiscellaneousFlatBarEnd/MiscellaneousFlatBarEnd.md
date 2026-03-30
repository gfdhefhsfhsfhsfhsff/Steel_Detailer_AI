# Class MiscellaneousFlatBarEnd 

End properties for a miscellaneous bent plate, should be largely the same as to Model.FlatBarEnd

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MiscellaneousFlatBarEnd

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
public class MiscellaneousFlatBarEnd
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousFlatBarEnd%5FMaterialSetback)MaterialSetback

The setback from the end where the plate material starts.

##### Declaration

```
public double MaterialSetback { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousFlatBarEnd%5FWebCutAngle)WebCutAngle

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

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousFlatBarEnd%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

End properties for a miscellaneous bent plate, should be largely the same as to Model.FlatBarEnd

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FMiscellaneousFlatBarEnd%5FFinalize)\~MiscellaneousFlatBarEnd()

End properties for a miscellaneous bent plate, should be largely the same as to Model.FlatBarEnd

##### Declaration

```
protected ~MiscellaneousFlatBarEnd()
```