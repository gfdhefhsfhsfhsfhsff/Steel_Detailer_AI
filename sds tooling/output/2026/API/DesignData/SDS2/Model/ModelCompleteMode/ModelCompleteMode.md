# Enum ModelCompleteMode 

SDS2 has two distinct modes for model complete. A legacy mode that's not very strict and generally just warns users to not change a member. And a restrictive mode which actively prevents changes.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum ModelCompleteMode
```

### [](#fields)Fields 

| Name        | Description                                                                                                                                                  |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Automatic   | Look to a setup option to decide which mode is preferred                                                                                                     |
| Legacy      | Use the legacy mode, this allows changes to be made to members by APIs and user interfaces.                                                                  |
| Restrictive | Use the restrictive mode, this disallows changes in the user interface and causes APIs to throw exceptions when attempting to change model complete members. |