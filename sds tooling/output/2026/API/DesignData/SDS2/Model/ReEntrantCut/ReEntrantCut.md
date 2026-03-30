# Enum ReEntrantCut 

The re-entrant cut method to use for a welded moment connection

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum ReEntrantCut
```

### [](#fields)Fields 

| Name       | Description                                                                                                                                                                                                                                                                                                                                                            |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alternate1 | configures the system to apply the values entered to the Weld Design Criteria window for "Alternate 1 re-entrant cut radius" and "Alternate 1 re-entrant cut length" and "Alternate 1 re-entrant cut depth" and "Alternate 1 flange flush length." The TopFlangeCutOperation and BottomFlangeCutOperation on this end of this beam will be set to CopeFieldWeldN1FEMA. |
| Alternate3 | instructs the system to use the "Re-entrant cut radius" that is entered in Weld Design Criteria. The TopFlangeCutOperation and BottomFlangeCutOperation on this end of this beam will be set to CopeFieldWeldN3Standard.                                                                                                                                               |
| Automatic  | Decides between Alternate3 and Alternate1 based on setup options                                                                                                                                                                                                                                                                                                       |