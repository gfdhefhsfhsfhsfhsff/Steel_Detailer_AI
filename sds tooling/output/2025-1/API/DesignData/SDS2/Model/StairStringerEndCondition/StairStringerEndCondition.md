# Enum StairStringerEndCondition 

The options for stringer end conditions

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum StairStringerEndCondition
```

### [](#fields)Fields 

| Name        | Description                                                                                                                                                                                                                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BoltToFloor | cuts the bottom end of the stair stringer so that it is horizontal and can, therefore, lay flat on a floor. BoltToFloorCearance may be set. ClipWeb on the Rolled Section Material window can edit the cut that is made. For the top end, horizontal and vertical cuts are made to the stringer so that the top tread can be laid on the floor. |
| NoReturn    | cuts the stair stringer vertically. The cut is in vertical alignment with the stair workpoint when SupportToWorkpoint and SetbackFromWorkpoint are 0.0                                                                                                                                                                                          |
| Return      | adds a horizontal return, the length of which is based on the SupportToWorkpoint distance.                                                                                                                                                                                                                                                      |
| ReturnDown  | The options for stringer end conditions                                                                                                                                                                                                                                                                                                         |
| TopCap      | cuts the top of the stringer flat and adds a top cap plate when the CapPlateThickness is a value greater than 0\. The plate may be extended based on the SupportToWorkpoint.                                                                                                                                                                    |