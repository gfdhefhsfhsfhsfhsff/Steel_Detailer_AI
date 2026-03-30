# Enum MemberEndRotationType 

This determines how the end of a supported beam is rotated to match a supporting beam or column

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum MemberEndRotationType
```

### [](#fields)Fields 

| Name         | Description                                                                                                                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automatic    | In this case, connection design will choose the end rotation that's appropriate.                                                                                                                          |
| HipAndValley | Has no meaning for a supporting column. For a supporting beam: Rotates the end of the beam to keep the flange parallel with the member line of the supporting beam.                                       |
| WebNormal    | For supporting column: Rotates the end of the beam so its web aligns with the member line of the column. For supporting beam: Rotates the end of the beam so that the connection will fit a sloping beam. |
| WebVertical  | The web of the beam will be vertical in global coordinates                                                                                                                                                |