# Enum ShearThroughPlate 

Through plate options for shear tabs attaching to tubes

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum ShearThroughPlate
```

### [](#fields)Fields 

| Name    | Description                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------ |
| None    | Do not go through the tube                                                                       |
| Split   | Go through the tube, splitting the plate if it encounters another through plate intersecting it. |
| Through | Go through the tube with a single plate connecting to beams on both sides                        |