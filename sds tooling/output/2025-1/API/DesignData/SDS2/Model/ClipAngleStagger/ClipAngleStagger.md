# Enum ClipAngleStagger 

Specifies where to stagger the bolts when clip angles share the same bolts.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum ClipAngleStagger
```

### [](#fields)Fields 

| Name       | Description                                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Neither    | instructs the system to create a clip angle with identical vertical hole spacing in both legs of the angle.                                 |
| Supported  | specifies normal vertical hole spacing in the leg to the supporting member and a staggered hole pattern in the leg to the supported member. |
| Supporting | specifies normal vertical hole spacing in the leg to the supported member and a staggered hole pattern in the leg to the supporting member. |