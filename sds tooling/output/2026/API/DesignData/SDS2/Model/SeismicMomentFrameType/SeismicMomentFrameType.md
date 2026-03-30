# Enum SeismicMomentFrameType 

The seismic moment frame type for a member's seismic moment design

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum SeismicMomentFrameType
```

### [](#fields)Fields 

| Name      | Description                                                                                                                                                                                              |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automatic | Choose between OMF, IMF, and SMF based on settings from setup                                                                                                                                            |
| IMF       | Intermediate Moment Frame connections are designed to be installed in moderate seismic regions.                                                                                                          |
| OMF       | Ordinary Moment Frame connections provide less resistance to lateral motion than IMF or SMF frames and are only recommended for non-seismic or low seismic regions.                                      |
| SMF       | Special Moment Frame connections are designed to resist flexural, axial, and shearing actions that result as a building sways through multiple inelastic displacement cycles due to a strong earthquake. |