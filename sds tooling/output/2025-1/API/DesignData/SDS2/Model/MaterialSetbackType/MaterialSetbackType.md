# Enum MaterialSetbackType 

Determines the meaning of the MaterialSetbackValue on the end of the main material.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum MaterialSetbackType
```

### [](#fields)Fields 

| Name                     | Description                                                                                                                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AutomaticMaterialSetback | distance measured parallel with the workline of the beam from the work point at this end of the beam to the end of the beam's main material. When this option is used, the system calculates the material setback distance for you. |
| ConnectionSetback        | distance from the face of the designed clip angle or bent plate to this end of this beam (the supported beam).                                                                                                                      |
| InputMaterialSetback     | distance measured parallel with the workline of the beam from the work point for this end of the beam to the beam's main material.                                                                                                  |