# Enum ClipAngleGage 

Gage settings specific to clip angle connections

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum ClipAngleGage
```

### [](#fields)Fields 

| Name   | Description                                                                                                                                                                                                                                                                                       |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Heavy  | specifies double clip angles that may be shop welded or shop bolted. Heavy gage clip angles may have two columns of bolts per leg. The inside and outside center-to-center hole spacing of a heavy gage double clip angle is defined under Standard Fabricator Connections > Clip Angle Settings. |
| Narrow | specifies that a narrow gage clip angle connection be designed per the distance entered to Fabricator Setup > Standard Fabricator Connections > Clip Angle Settings > "Center to center distance, Narrow gage." A narrow gage clip angle has a single column of bolts.                            |
| Wide   | instructs the system to create a wide gage clip angle per the distance entered to Fabricator Setup > Standard Fabricator Connections > Clip Angle Settings > "Center to center distance, Wide gage." A wide gage clip angle has a single column of bolts.                                         |