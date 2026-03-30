# Enum StringerLength 

Enumeration denoting the stringer length reported in the stair's BOM.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum StringerLength
```

### [](#fields)Fields 

| Name    | Description                                                                                                                                                                                                                                                      |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PostCut | Results in stringer length in the stair BOM being its part length. Corresponds to the final length in the CNC setup. This is the length of the stringer _after_its end was cut so that it could be bolted to the floor.                                          |
| PreCut  | Results in length reported for stringer in stair BOM to be the order length of the material. Corresponds to saw length in the CNC setup. This is the length of the stringer material _before_ cuts were made to its end so that it could be bolted to the floor. |