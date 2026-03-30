# Enum LicenseReturnCode 

Codes indicating the state of licensing after a checkout attempt

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public enum LicenseReturnCode
```

### [](#fields)Fields 

| Name           | Description                                                                |
| -------------- | -------------------------------------------------------------------------- |
| BadCredentials | No license was given because the username or password did not match        |
| Canceled       | The user has canceled the operation                                        |
| Licensed       | Success, a license has been granted and used                               |
| NoLicense      | The user does not have this license, or does not have any left to checkout |