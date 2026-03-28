# Enum WeldType 

Enumerated weld types

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public enum WeldType
```

### [](#fields)Fields 

| Name             | Description                                                                          |
| ---------------- | ------------------------------------------------------------------------------------ |
| BackingBar       | Backing bar weld                                                                     |
| BackingWeld      | Backing weld for the back side of bevel or V, J or U groove welds.                   |
| BevelGroove      | Bevel groove weld for general full penetration welding of material.                  |
| Fillet           | Fillet weld for general welding of material                                          |
| FlareBevelGroove | Flare bevel groove weld for a radiused surface to flat surface (e.g. tube to plate). |
| FlareVGroove     | Flare V groove weld for a radiused surface to radiused surface.                      |
| JGroove          | J groove weld for special full penetration welding of material.                      |
| NoWeldType       | No weld                                                                              |
| Plug             | Plug weld. Material must have plug weld holes for SDS2 to generate plug welds.       |
| SquareGroove     | Square groove weld for butt joints of material 3/8" thick or less                    |
| UGroove          | U groove weld for butt joints of thicker material.                                   |
| VGroove          | V groove weld for butt joints of thicker material.                                   |