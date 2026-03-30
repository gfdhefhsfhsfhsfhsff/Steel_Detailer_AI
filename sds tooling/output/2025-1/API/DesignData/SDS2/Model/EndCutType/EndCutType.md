# Enum EndCutType 

The type or method of cut

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum EndCutType
```

### [](#fields)Fields 

| Name        | Description                                                                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| BevelCut    | A beveled cut: "BEV CUT" is added to the detail. When using BevelCut the WebCutAngle should be set to a value other than 0. |
| MillCut     | A milled cut: "MILL CUT" is added to the detail.                                                                            |
| SquareCut   | A square cut: "SQ CUT" is added to the detail/                                                                              |
| StandardCut | The default, standard cut method                                                                                            |