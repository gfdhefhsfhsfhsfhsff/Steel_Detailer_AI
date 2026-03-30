# Enum ModelViewDefinition 

The order of these model view definition values is critical, and MUST stay in sync with the MVD\_XXX defines in mdl\_link\_ext.h

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum ModelViewDefinition
```

### [](#fields)Fields 

| Name                        | Description                                                              |
| --------------------------- | ------------------------------------------------------------------------ |
| ACI131ConcreteReinforcement | IFC 4 ACI 131.2R-17 contains only concrete reinforcement materials       |
| CoordinationView2           | IFC 2x3 Coordination View 2.0 is the most common MVD used worldwide      |
| DesignTransferView          | IFC 4 Design Transfer View is the most common, general purpose IFC 4 MVD |
| EM11SteelFabrication        | IFC 2x3 EM11 is an AISC creation used only by steel fabricators          |
| ReferenceView               | IFC 4 Reference View provides little benefit and isn't supported yet     |
| Unknown                     | Using 'unknown' is an error condition                                    |