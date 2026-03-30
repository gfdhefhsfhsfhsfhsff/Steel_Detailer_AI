# Enum ElevationDisplayMode 

Enum for display modes set by ElevationDisplayOnMember property

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public enum ElevationDisplayMode
```

### [](#fields)Fields 

| Name      | Description                                                                                                                                                                                           |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Absolute  | The true elevation of members may be shown on erection view drawings of plan views, elevation views, and isometric views.                                                                             |
| No        | Elevation of member ends that are offset from the reference elevation are not reported on an already detailed erection view drawing.                                                                  |
| Reference | Members in an erection view drawing of a plan view may be marked with the amount of elevation offset when their exact points are at an elevation other than the reference elevation of the plan view. |