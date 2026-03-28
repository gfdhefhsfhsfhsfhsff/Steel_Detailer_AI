# Class IFC2x3 

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

IFC2x3

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
public class IFC2x3
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FIFC2x3%5FExport%5FDesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FDesignData%5FSDS2%5FModel%5FIFCOptions%5F)Export(MemberHandleList, IFCOptions)

##### Declaration

```
public static byte[] Export(MemberHandleList members, IFCOptions options)
```

##### Parameters

| Type                                                               | Name    | Description |
| ------------------------------------------------------------------ | ------- | ----------- |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html) | members |             |
| [IFCOptions](DesignData.SDS2.Model.IFCOptions.html)                | options |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\] |             |

#### [](#DesignData%5FSDS2%5FModel%5FIFC2x3%5FExport%5FDesignData%5FSDS2%5FDatabase%5FMemberHandleList%5FDesignData%5FSDS2%5FModel%5FModelViewDefinition%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FString%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FBoolean%5FSystem%5FDouble%5FSystem%5FBoolean%5FSystem%5FDouble%5FSystem%5FDouble%5FSystem%5FDouble%5FSystem%5FDouble%5F)Export(MemberHandleList, ModelViewDefinition, bool, bool, bool, bool, bool, bool, bool, bool, string, bool, bool, bool, bool, double, bool, double, double, double, double)

Export an IFC2x3 file, returned as a byte array

##### Declaration

```
public static byte[] Export(MemberHandleList members, ModelViewDefinition modelViewDefinition = ModelViewDefinition.CoordinationView2, bool withHoles = true, bool withBolts = true, bool withWelds = true, bool withWeldsAllProperties = true, bool revitFriendly = false, bool strumisFriendly = false, bool storiesByZoneAndSequence = false, bool exportScheduling = false, string schedulingXML = "", bool withCenterOfMassLocation = true, bool withCustomProperties = true, bool withLogs = true, bool withGrids = true, double gridDistance = 0, bool compress = false, double translateX = 0, double translateY = 0, double translateZ = 0, double rotateCCWAboutZAxis = 0)
```

##### Parameters

| Type                                                                  | Name                     | Description                                                                                                                                             |
| --------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [MemberHandleList](DesignData.SDS2.Database.MemberHandleList.html)    | members                  | The members to include in this IFC export                                                                                                               |
| [ModelViewDefinition](DesignData.SDS2.Model.ModelViewDefinition.html) | modelViewDefinition      | Can only be CoordinationView2 or EM11SteelFabrication                                                                                                   |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | withHoles                | true to include holes in the IFC                                                                                                                        |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | withBolts                | true to include bolts in the IFC                                                                                                                        |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | withWelds                | true to include welds in the IFC                                                                                                                        |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | withWeldsAllProperties   | true to include welds in the IFC                                                                                                                        |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | revitFriendly            | if true, make modifications to the IFC to aid in importing it with revit                                                                                |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | strumisFriendly          | if true, make modifications to the IFC to aid in importing into strumis                                                                                 |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | storiesByZoneAndSequence | Export stories by zone and sequence                                                                                                                     |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | exportScheduling         | if true, export scheduling info for Synchro. See the schedulingXML parameter to supply necessary information                                            |
| [string](https://learn.microsoft.com/dotnet/api/system.string)        | schedulingXML            | if exportScheduling:true, then give a Synchro XML file here                                                                                             |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | withCenterOfMassLocation | if true, export the center of mass location. This option is will dramatically increase the time to generate an export.                                  |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | withCustomProperties     | if true, export custom property information                                                                                                             |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | withLogs                 | if true, export logs found under custom properties                                                                                                      |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | withGrids                | if true, export grids                                                                                                                                   |
| [double](https://learn.microsoft.com/dotnet/api/system.double)        | gridDistance             | Grid lines, in SDS2, are infinite. This is the distance, outside of the model's bounding box, to cut off grid lines. Only applies if withGrids is true. |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)         | compress                 | if true, the IFC blob will be a compressed zip file with the IFC in it                                                                                  |
| [double](https://learn.microsoft.com/dotnet/api/system.double)        | translateX               | The global translation on X axis to apply to all elements                                                                                               |
| [double](https://learn.microsoft.com/dotnet/api/system.double)        | translateY               | The global translation on Y axis to apply to all elements                                                                                               |
| [double](https://learn.microsoft.com/dotnet/api/system.double)        | translateZ               | The global translation on Z axis to apply to all elements                                                                                               |
| [double](https://learn.microsoft.com/dotnet/api/system.double)        | rotateCCWAboutZAxis      | The rotation of CCW about the Z axis in radians                                                                                                         |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\] |             |

##### Remarks

This requires the ModelLink license feature.

This function will change the current working directory for the program temporarily. While it's being called the directory will change to SDS2's data directory and then it will be put back before it exits.

So be very careful calling this in a multi-threaded environment where you may also change the working directory.

This may print to standard error, this is due to the library SDS2 uses for outputting IFC and is outside of our control.

##### Exceptions

| Type                                                                         | Condition                                                                                                                                                         |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [NotLicensedException](DesignData.SDS2.Exceptions.NotLicensedException.html) | thrown when the ModelLink license is not available or the current platform does not support IFC export. (Note, all Microsoft Windows systems support IFC export). |
| [IFCException](DesignData.SDS2.Exceptions.IFCException.html)                 | Thrown when an incompatible ModelViewDefinition is specified in modelViewDefinition.                                                                              |

#### [](#DesignData%5FSDS2%5FModel%5FIFC2x3%5FFinalize)\~IFC2x3()

##### Declaration

```
protected ~IFC2x3()
```