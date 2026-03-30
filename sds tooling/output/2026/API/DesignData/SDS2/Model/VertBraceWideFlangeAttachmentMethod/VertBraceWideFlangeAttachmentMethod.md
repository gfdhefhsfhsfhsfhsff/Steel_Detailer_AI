# Enum VertBraceWideFlangeAttachmentMethod 

A specification for how the flanges of a vertical wide flange brace connects to the gusset plate.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum VertBraceWideFlangeAttachmentMethod
```

### [](#fields)Fields 

| Name         | Description                                                                                   |
| ------------ | --------------------------------------------------------------------------------------------- |
| Automatic    | Use setup to determine the connection                                                         |
| ClawAngles   | Connect with angles on both sides of the gusset connecting to the wide flange flanges         |
| None         | No wide flange flange connection                                                              |
| PaddlePlates | Connect with plates on the wide flange flanges with notches for the gusset plate to fit into. |