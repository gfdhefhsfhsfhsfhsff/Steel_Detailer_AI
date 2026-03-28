# Enum MomentBoltPattern 

The bolt pattern to use in a moment plate

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum MomentBoltPattern
```

### [](#fields)Fields 

| Name                     | Description                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| EightBolt                | applies only when ConnectionType is set to AISC\_Eurocode. The moment connection is designed with a stiffener. Adds 8 bolts around the flange of the beam.                                                                                                                                                                                                               |
| FourBolt                 | applies when ConnectionType is AISC\_Eurocode or MBMA. For a moment plate extended above the top flange, two bolts are above the flange, and two bolts below the flange. For a moment plate that is flush with the flange, the four bolts are below the flange.                                                                                                          |
| HalfUnstiffened          | applies when ConnectionType is MBMA. For a moment plate extended above the top flange, one bolt is above the flange on the near side of the web, and two bolts are below the flange on the near side of the web. A corresponding number of bolts are on the far side of the web.                                                                                         |
| PlateBelowTensionBolts   | applies when ConnectionType is MBMA. The plate is flush with both flanges. For PlateLocation set to TopOnly, two rectangular stiffener plates (one NS, one FS) are designed below the four tension bolts under the top flange. This arrangement is mirrored for the bottom flange when PlateLocation is TopAndBottom.                                                    |
| PlateBetweenTensionBolts | applies when ConnectionType is MBMA. The plate is flush with both flanges. For PlateLocation set to TopOnly, two rectangular stiffener plates (one NS, one FS) are designed between the four tension bolts under the top flange. This arrangement is mirrored for the bottom flange when PlateLocation is TopAndBottom.                                                  |
| ThirdStiffened           | applies when ConnectionType is MBMA. For a moment plate extended above the top flange, one bolt is above the flange on the near side, and three bolts are below the flange on the near side. A corresponding number of bolts are on the far side of the plate. A rectangular stiffener is designed between the two bolts that are in the extension above the top flange. |
| ThirdUnstiffened         | applies when ConnectionType is MBMA. For a moment plate extended above the top flange, one bolt is above the flange on the near side, and three bolts are below the flange on the near side. A corresponding number of bolts are on the far side of the plate. No stiffener plate is designed.                                                                           |
| TwoBolt                  | applies when ConnectionType is MBMA. The end plate is designed to be flush with both flanges. Two bolts directly beneath the top flange and two other bolts directly above the bottom flange fasten the plate to the column.                                                                                                                                             |