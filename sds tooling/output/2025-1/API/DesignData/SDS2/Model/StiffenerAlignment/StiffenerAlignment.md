# Enum StiffenerAlignment 

Stiffener alignment options, whether it should be aligned to the beam or column, or if it should look to setup for which to align to

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum StiffenerAlignment
```

### [](#fields)Fields 

| Name      | Description                                                                                                                                                                                          |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automatic | specifies that the system apply a setup choice (Fabricator Setup > Standard Fabricator Connections > Cap Plate Setup > "Align transverse stiffeners with").                                          |
| Beam      | configures the system to create transverse beam stiffeners that are perpendicular to the workline of the beam. The stiffeners are normal to the beam, regardless of the slope of the beam or column. |
| Column    | instructs the system to create transverse beam stiffeners that are parallel with the workline (stick form member line) of the column.                                                                |