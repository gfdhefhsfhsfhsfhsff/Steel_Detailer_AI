# Enum HorizontalBracePlateType 

Specifies a framing situation for a horizontal brace connection with a gusset plate.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum HorizontalBracePlateType
```

### [](#fields)Fields 

| Name                       | Description                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------ |
| BeamFlange                 | A gusset plate connects to the flange of a beam                                      |
| BeamToBeamCorner           | A gusset plate connects to the web of two beams where one beam frames into the other |
| BeamToBeam\_Column         | A gusset plate connects to two beams, where they meet at a column                    |
| BeamWeb                    | The gusset plate connects to the web of a single beam                                |
| BraceIntersectionPlate     | A gusset plate connecting two braces through a third brace, an X connection.         |
| PerpendicularToBeam        | A gusset plate connects at a 90 degree angle to a beam                               |
| ThreePointSharedConnection | A 3 point brace connection                                                           |
| TwoPointSharedConnection   | A 2 point brace connection.                                                          |