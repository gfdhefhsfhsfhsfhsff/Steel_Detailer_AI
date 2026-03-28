# Class StairTread 

Base class for Stair Tread Schedule objects. There are 4 types of tread: Pan, Grating, Plate, and Continuous. This class is used primarily as a method of transport/storage of the various tread types, as well as containing basic functionalities shared across all the classes. It is recommended to cast StairTread to the relevant type based on GetTreadType before working with it.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

StairTread

[ContinuousTread](DesignData.SDS2.Setup.ContinuousTread.html)

[CustomContinuousTread](DesignData.SDS2.Setup.CustomContinuousTread.html)

[CustomGratingTread](DesignData.SDS2.Setup.CustomGratingTread.html)

[CustomPanTread](DesignData.SDS2.Setup.CustomPanTread.html)

[CustomPlateTread](DesignData.SDS2.Setup.CustomPlateTread.html)

[GratingTread](DesignData.SDS2.Setup.GratingTread.html)

[PanTread](DesignData.SDS2.Setup.PanTread.html)

[PlateTread](DesignData.SDS2.Setup.PlateTread.html)

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
public class StairTread
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FStairTread%5FName)Name

Returns a string containing the name associated with the specific tread schedule index.

##### Declaration

```
public virtual string Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTread%5FTreadType)TreadType

Returns type of tread associated with the specific tread schedule index. It is recommended to cast StairTread to the relevant type before working with it.

##### Declaration

```
public virtual StairTreadType TreadType { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [StairTreadType](DesignData.SDS2.Setup.StairTreadType.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FStairTread%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Base class for Stair Tread Schedule objects. There are 4 types of tread: Pan, Grating, Plate, and Continuous. This class is used primarily as a method of transport/storage of the various tread types, as well as containing basic functionalities shared across all the classes. It is recommended to cast StairTread to the relevant type based on GetTreadType before working with it.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FStairTread%5FFinalize)\~StairTread()

Base class for Stair Tread Schedule objects. There are 4 types of tread: Pan, Grating, Plate, and Continuous. This class is used primarily as a method of transport/storage of the various tread types, as well as containing basic functionalities shared across all the classes. It is recommended to cast StairTread to the relevant type based on GetTreadType before working with it.

##### Declaration

```
protected ~StairTread()
```