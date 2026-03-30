# Enum StringerMark 

Enumeration denoting CNC marks to place on stair stringers.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum StringerMark
```

### [](#fields)Fields 

| Name    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| None    | Puts no CNC marks on the inside of stair stringers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Nosing  | Puts one CNC mark per stringer for each tread nosing. On pan treads, the CNC marks align with the 'abrasive setback'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Support | Puts two CNC marks per angle or plate or flat bar support in line with the corners of the support where the tread or riser rests on the support. The CNC marks are placed on the inside of bot the near and far side stringers. If the support is a bent plate, a single CNC mark is placed at the intersection of the riser with the next tread near the bend location. Pan and continuous treads can have dual or single supports. Plate treads are limited to a single support. Pan tread supports can be angle, plate, flat bar or bent plate. Continuous or plate tread supports can be angle, plate or flat bar. |