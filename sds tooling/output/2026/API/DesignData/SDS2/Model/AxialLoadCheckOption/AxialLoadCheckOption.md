# Enum AxialLoadCheckOption 

Values for the AxialLoadCheck option on ShearTabSpecification

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum AxialLoadCheckOption
```

### [](#fields)Fields 

| Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ForSupportingBeam   | results in calculation 264 being a potential cause of connection failure in the design of the shear plate on this end of the supported beam (this beam) when that end has a "Tension load" applied to it and the shear plate welds to an HSS beam. Calculation 265 will not result in connection failure of a shear plate to an HSS column, though the calculation will still be done, and a for-information-only note reporting the results of the calculation will be provided, when applicable, in both design calculations reports.                |
| ForSupportingColumn | results in calculation 265 being a potential cause of connection failure in the design of the shear plate on this end of the supported beam (this beam) when that end has a "Tension load" applied to it and the shear plate welds to a supporting HSS column. Calculation 264 will not result in connection failure of a shear plate to an HSS beam, though the calculation will still be done, and a for-information-only note reporting the results of the calculation will be provided, when applicable, in both design calculations reports.      |
| IfRequired          | results in design calculations 265 and 264 being potential causes of connection failure when applicable. Design calculation 265 is applicable when the shear plate connection on this end of the supported beam has a "Tension load" applied to it and that shear plate welds to a supporting HSS column. Calculation 264 is applicable when the shear plate connection on this end of the supported beam (this beam) has a "Tension" load applied to it and the shear plate welds to a supporting HSS beam.                                           |
| Never               | results in calculations 265 and 264 still being performed, if applicable, but not ever causing the connection to fail. In the Connection Design Calculations or Expanded Connection Design Calculations, the results of the check will be reported with a parenthetical, for-information-only note such as "(Allowable local axial transverse force on the HSS wall: K1, (264) 8.7 kips )" for a beam. For a column, the parenthetical note will be something like "(Allowable local longitudinal axial force on the HSS wall: K1, (265) 21.1 kips )." |