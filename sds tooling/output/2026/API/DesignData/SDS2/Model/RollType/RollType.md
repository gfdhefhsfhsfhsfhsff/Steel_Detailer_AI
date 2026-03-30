# Enum RollType 

The type of roll made along the length of a material.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum RollType
```

### [](#fields)Fields 

| Name         | Description                                                                       |
| ------------ | --------------------------------------------------------------------------------- |
| Camber       | A parabolic bend along the strong axis, annotation only no change to SDS2 solids. |
| CamberBoth   | A parabolic bend along the strong axis represented in solids and annotated.       |
| CamberSolids | A parabolic bend along the strong axis represented in solids.                     |
| None         | No roll, this is a straight piece of material                                     |
| StrongAxis   | A circular bend along the strong axis                                             |
| WeakAxis     | A circular bend along the weak axis                                               |