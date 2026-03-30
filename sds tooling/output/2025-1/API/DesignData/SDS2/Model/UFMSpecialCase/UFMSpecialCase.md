# Enum UFMSpecialCase 

A specification for how the system spreads the load between the connection and supporting column and beams.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum UFMSpecialCase
```

##### **Remarks**

See SDS2's help on vertical brace connections for more information.

### [](#fields)Fields 

| Name      | Description                                                          |
| --------- | -------------------------------------------------------------------- |
| Automatic | Use the value defined in setup.                                      |
| Case2     | Distribute the vertical force to the connection instead of the beam. |
| Case3     | Design the connection to the beam and not the column.                |
| None      | Distribute the vertical force to the connection as well as the beam. |