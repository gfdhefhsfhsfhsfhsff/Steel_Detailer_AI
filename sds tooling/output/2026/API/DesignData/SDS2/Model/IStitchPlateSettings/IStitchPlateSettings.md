# Interface IStitchPlateSettings 

Interface for stitch plate settings (on brace main material)

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public interface IStitchPlateSettings
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FIStitchPlateSettings%5FIsAutoMaxStitchPlateSpacing)IsAutoMaxStitchPlateSpacing

If true, then MaxStitchPlateSpacing will be determined during process and should not be set here. If false, then it should be set here and it will be followed by process

##### Declaration

```
bool IsAutoMaxStitchPlateSpacing { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FIStitchPlateSettings%5FIsAutoNumberOfStitchPlates)IsAutoNumberOfStitchPlates

If true, then NumberOfStitchPlates will be set by the system during process. If false, then the user or API must set NumberOfStichPlates before process.

##### Declaration

```
bool IsAutoNumberOfStitchPlates { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FIStitchPlateSettings%5FIsAutoStitchPlateGap)IsAutoStitchPlateGap

If true, then StitchPlateGap will be determined by the system during process (not instantly). If false, then you can set StitchPlateGap and the system will follow that setting.

##### Declaration

```
bool IsAutoStitchPlateGap { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FIStitchPlateSettings%5FMaxStitchPlateSpacing)MaxStitchPlateSpacing

The center to center distance between stitch plates along the brace work line. This is the max distance, some may have to fall closer than this because the work line may not be simply divisible by this value

##### Declaration

```
double MaxStitchPlateSpacing { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

If AutoMaxStitchPlateSpacing is false, then this should be set by the user or API and will be used during process. If the auto field is true, then this will be set during process and you should not set it from the API.

#### [](#DesignData%5FSDS2%5FModel%5FIStitchPlateSettings%5FNumberOfStitchPlates)NumberOfStitchPlates

If AutoNumberOfStitchPlates is false, then set this and process will create this many stitch plates. If true, then during process the system will calculate the number of stitch plates and this will be set to that calculation

##### Declaration

```
double NumberOfStitchPlates { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FIStitchPlateSettings%5FStitchPlateGap)StitchPlateGap

The gap between two pieces of material for stitch plates to sit in. If AutoStitchPlateGap is true, then this field is calculated during process and should not be set by API users. If that field is false, then set this to cause the system to design with whatever gap you set.

##### Declaration

```
double StitchPlateGap { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |