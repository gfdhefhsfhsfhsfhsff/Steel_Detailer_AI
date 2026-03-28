# Enum EndPlateEndOption 

Options for the ends of the end plates used

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum EndPlateEndOption
```

### [](#fields)Fields 

| Name                | Description                                                                                                                                                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| StiffenedExtended   | extends the end plate beyond the flange and designs a triangular stiffener between the two bolts that are beyond the flange. FourBolt and ThirdUnstiffened are BoltPattern options that control the number of bolts inside the flange for this configuration. |
| StiffenedFlush      | makes the edge of the end plate flush with the flange. Placement of the stiffener is the specified BoltPattern (PlateBelowTensionBolts and PlateBetweenTensionBolts are the two options).                                                                     |
| UnstiffenedExtended | extends the end plate beyond the flange, but without a stiffener. FourBolt and HalfUnstiffened and all "Third..." options are BoltPattern settings that control the number of bolts inside the flange for this configuration.                                 |
| UnstiffenedFlush    | makes the edge of the end plate flush with the flange. No stiffener are designed. TwoBolt and FourBolt are the two BoltPattern options.                                                                                                                       |