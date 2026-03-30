# Enum VerticalBracePlateType 

Specifies a framing situation for a vertical brace connection with a gusset plate.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum VerticalBracePlateType
```

### [](#fields)Fields 

| Name                   | Description                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| BeamAndColumn          | The gusset plate connects near the intersection of a beam and column and is welded to both |
| BeamOnly               | The gusset plate only connects to a beam                                                   |
| BraceIntersectionPlate | The plate connects through another brace, an 'X' brace situation                           |
| ColumnAndBaseCapPlate  | The gusset plate connects to a column and it's base or cap plate                           |
| ColumnOnly             | The gusset plate only connects to a column                                                 |
| SharedKConnection      | A shared gusset with 2 or more braces                                                      |
| ThreePointBrace        | Similar to BraceIntersectionPlate, but specifically a 3 point brace                        |