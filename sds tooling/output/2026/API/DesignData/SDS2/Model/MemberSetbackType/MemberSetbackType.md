# Enum MemberSetbackType 

Determines the meaning of the MemberSetbackValue on the end of a member.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum MemberSetbackType
```

### [](#fields)Fields 

| Name                    | Description                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AutomaticMinusDimension | A system-calculated distance from the beam's work point to the face of the designed connection on this end of the beam.                                                                                                                                                                                                                                        |
| FieldClearance          | distance from the face of the designed connection to the face of the supporting member.                                                                                                                                                                                                                                                                        |
| InputMinusDimension     | positive or negative distance measured parallel with the workline of the beam from the beam's work point to the face of the designed connection on the end of the beam. A positive distance shortens the beam by that amount. A negative distance makes the beam longer. If the beam is sloping, the actual sloped minus dimension must be calculated and set. |