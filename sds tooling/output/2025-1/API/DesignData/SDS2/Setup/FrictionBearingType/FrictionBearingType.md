# Enum FrictionBearingType 

Enumeration of valid values for the FrictionBearing attribute of BoltType.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public enum FrictionBearingType
```

##### **Remarks**

Values are used for bearing type bolts according to equation J3-1 on pg 16.1-108 of the AISC Steel Construction Manual, Thirteenth Edition. For slip-critical bolts, connection design calculates the strength limit state using equation J3-4 on pg 16.1-109.

### [](#fields)Fields 

| Name            | Description                                                                                                                                                                                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BearingExcluded | For bolts in slip-critical connections. For SlipCritical bolt types, SurfaceClass must also be set. Connection design uses the "Limit state for slip-critical bolt design" that is set in Bolt Settings when designing slip-critical bolts. |
| BearingIncluded | For a bearing-type connection with threads included in the shear plane.                                                                                                                                                                     |
| SlipCritical    | For a bearing-type connection with threads excluded from the shear plane.                                                                                                                                                                   |