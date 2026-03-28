# Enum EndPlateSafetyConnection 

The end plate safety connections that SDS2 can handle.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum EndPlateSafetyConnection
```

### [](#fields)Fields 

| Name         | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automatic    | specifies that the system apply the choice made to Fabricator Setup > Standard Fabricator Connections > End Plate Setup > "End plate safety connection."                                                                                                                                                                                                                                          |
| NonSafety    | specifies that the two end plates be designed to share all bolts.                                                                                                                                                                                                                                                                                                                                 |
| SafetyNotch  | instructs the system to create deeper end plates to accommodate an extra row of bolts and to perform a "Cope" on each plate so that each bolt in the top row of bolts is shared by the column and a different beam. The cut to the plate is on the far side of the beam with a left end end plate. The cut is on the near side of the other beam, which will have the end plate on its right end. |
| SafetyOffset | instructs the system to vertically offset the end plates with respect to one another so that one row of bolts is shared with the beam and column but not shared by the end plate of the opposing beam.                                                                                                                                                                                            |