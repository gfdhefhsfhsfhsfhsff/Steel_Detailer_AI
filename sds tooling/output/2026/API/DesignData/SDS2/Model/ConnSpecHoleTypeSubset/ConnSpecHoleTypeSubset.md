# Enum ConnSpecHoleTypeSubset 

Set of connection specification values representing a subset of hole types appropriate for a connection

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum ConnSpecHoleTypeSubset
```

### [](#fields)Fields 

| Name          | Description                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------- |
| LongSlot      | Similar to a ShortSlot, but with a longer slot length (2.5" for a 1" diameter bolt)                 |
| Oversize      | A round hole, typically 3/16ths of an inch larger than the input bolt diameter.                     |
| ShortSlot     | An oblong shaped hole, diameter is typically 1/16th of an inch larger than the input bolt diameter. |
| StandardRound | A standard, perfectly round, hole.                                                                  |