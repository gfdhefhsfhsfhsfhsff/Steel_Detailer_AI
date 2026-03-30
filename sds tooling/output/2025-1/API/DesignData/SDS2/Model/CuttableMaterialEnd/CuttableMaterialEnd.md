# Class CuttableMaterialEnd 

A material end which can be setback or have a simple web or flange cut applied. Some derived classes offer significantly more cutting options.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CuttableMaterialEnd

[RoundBarEnd](DesignData.SDS2.Model.RoundBarEnd.html)

[ShapeMaterialEnd](DesignData.SDS2.Model.ShapeMaterialEnd.html)

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
public class CuttableMaterialEnd
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5FFlangeCutAngle)FlangeCutAngle

Angle to cut across the end of the bar relative to the "Flange".

##### Declaration

```
public double FlangeCutAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5FSetback)Setback

The setback from the end where the plate material starts.

##### Declaration

```
public double Setback { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5FWebCutAngle)WebCutAngle

Angle to cut across the end of the bar relative to the "Web".

##### Declaration

```
public double WebCutAngle { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A material end which can be setback or have a simple web or flange cut applied. Some derived classes offer significantly more cutting options.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FCuttableMaterialEnd%5FFinalize)\~CuttableMaterialEnd()

A material end which can be setback or have a simple web or flange cut applied. Some derived classes offer significantly more cutting options.

##### Declaration

```
protected ~CuttableMaterialEnd()
```