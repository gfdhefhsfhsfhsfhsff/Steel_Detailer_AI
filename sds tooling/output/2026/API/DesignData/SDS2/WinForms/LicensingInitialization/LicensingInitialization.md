# Class LicensingInitialization 

Helper functions for licensing, which sometimes has to be interactive since the user must login to their license account if no credentials are on file.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

LicensingInitialization

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[WinForms](DesignData.SDS2.WinForms.html)

###### **Assembly**: DesignData.SDS2.WinForms.dll

##### Syntax

```
public sealed class LicensingInitialization
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FWinForms%5FLicensingInitialization%5F%5Fctor)LicensingInitialization()

Helper functions for licensing, which sometimes has to be interactive since the user must login to their license account if no credentials are on file.

##### Declaration

```
public LicensingInitialization()
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FWinForms%5FLicensingInitialization%5FCheckout)Checkout()

If there are stored credentials, checkout a license right away. If not, prompt the user (with a winforms dialog) for credentials and then ckeckout a license. Those credentials will be stored for the next use.

This helper, or equivalent code, must be called before doing anything else with the SDS2 API.

Equivalent code:

```
if(!Licensing.HasStoredCredentials)
{
    Licensing.SetCredentials("a license username", "their password");
}
Licensing.Checkout();
```

##### Declaration

```
public static bool Checkout()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |