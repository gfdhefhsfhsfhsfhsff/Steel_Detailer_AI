# Enum ColumnPlateWeldPattern 

Weld pattern types for column base and cap plates

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum ColumnPlateWeldPattern
```

### [](#fields)Fields 

| Name             | Description                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AllAround        | specifies that the system shop weld all faces of the column, including the thickness edges and fillets of a wide flange and the round corners of an HSS rectangular (tube).                                                                                                                                                                                                              |
| AllFaces         | configures the system to shop weld all faces except thickness edges and fillets and HSS corners. For HSS rectangular sections, only the outside faces are welded. For wide flange, both inside and outside faces are welded.                                                                                                                                                             |
| AllFacesWithSeal | gives the same results as 'All faces,' except that thickness edges and fillets and HSS corners are seal welded. Job Setup > Weld Design Settings > "Seal weld size" sets the weld size for the seal welds. The tail text applied during Detail Membersf for seal welds on HSS/TS columns is '4 SIDES WITH SEAL.' For columuns other than HSS/TS, the tail text is 'ALL FACES WITH SEAL.' |
| Automatic        | specifies that the system apply a setup choice (Job Setup > Weld Design Settings > "On base plate" or "On cap plate").                                                                                                                                                                                                                                                                   |
| TwoFaces         | instructs the system to shop weld two opposite faces of the column to the user base/cap plate. For a wide flange, the outside face of one flange is welded, and the inside faces (NS and FS) of the other flange are welded.                                                                                                                                                             |