# Class Licensing 

A place for functions related to SDS2 licensing.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Licensing

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class Licensing
```

##### **Remarks**

The normal program start procedure looks like:

```
if(!Licensing.HasStoredCredentials)
{
    string userName = .. prompt for user name;
    string password = .. prompt for password;
    Licensing.SetCredentials(userName, password);
}
Licensing.Checkout();
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FLicensing%5FHasStoredCredentials)HasStoredCredentials

Check if SDS2 already has working stored credentials to use, if it does you do not need to prompt and get credentials

##### Declaration

```
public static bool HasStoredCredentials { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

The normal program start procedure looks like:

```
if(!Licensing.HasStoredCredentials)
{
    string userName = .. prompt for user name;
    string password = .. prompt for password;
    Licensing.SetCredentials(userName, password);
}
Licensing.Checkout();
```

#### [](#DesignData%5FSDS2%5FDatabase%5FLicensing%5FIsLicensed)IsLicensed

Returns true if the user has a valid license to run the API

##### Declaration

```
public static bool IsLicensed { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

The normal program start procedure looks like:

```
if(!Licensing.HasStoredCredentials)
{
    string userName = .. prompt for user name;
    string password = .. prompt for password;
    Licensing.SetCredentials(userName, password);
}
Licensing.Checkout();
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FLicensing%5FCheckout)Checkout()

Checkout your license for the full run of your program.

##### Declaration

```
public static LicenseReturnCode Checkout()
```

##### Returns

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [LicenseReturnCode](DesignData.SDS2.Database.LicenseReturnCode.html) |             |

##### Remarks

There is no checkin, this call is just needed to give you time to prompt for credentials if needed

#### [](#DesignData%5FSDS2%5FDatabase%5FLicensing%5FFinalize)\~Licensing()

A place for functions related to SDS2 licensing.

##### Declaration

```
protected ~Licensing()
```

##### Remarks

The normal program start procedure looks like:

```
if(!Licensing.HasStoredCredentials)
{
    string userName = .. prompt for user name;
    string password = .. prompt for password;
    Licensing.SetCredentials(userName, password);
}
Licensing.Checkout();
```

#### [](#DesignData%5FSDS2%5FDatabase%5FLicensing%5FGetIsLicensed)GetIsLicensed()

Returns true if the user has a valid license to run the API

##### Declaration

```
public static bool GetIsLicensed()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

The normal program start procedure looks like:

```
if(!Licensing.HasStoredCredentials)
{
    string userName = .. prompt for user name;
    string password = .. prompt for password;
    Licensing.SetCredentials(userName, password);
}
Licensing.Checkout();
```

#### [](#DesignData%5FSDS2%5FDatabase%5FLicensing%5FHasFeature%5FDesignData%5FSDS2%5FDatabase%5FLicenseFeatures%5F)HasFeature(LicenseFeatures)

Returns true if the user has a valid license to run the given API feature

##### Declaration

```
public static bool HasFeature(LicenseFeatures feature)
```

##### Parameters

| Type                                                             | Name    | Description |
| ---------------------------------------------------------------- | ------- | ----------- |
| [LicenseFeatures](DesignData.SDS2.Database.LicenseFeatures.html) | feature |             |

##### Returns

| Type                                                          | Description                    |
| ------------------------------------------------------------- | ------------------------------ |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | The API feature to be checked. |

##### Remarks

The normal program start procedure looks like:

```
if(!Licensing.HasStoredCredentials)
{
    string userName = .. prompt for user name;
    string password = .. prompt for password;
    Licensing.SetCredentials(userName, password);
}
Licensing.Checkout();
```

#### [](#DesignData%5FSDS2%5FDatabase%5FLicensing%5FSetCredentials%5FSystem%5FString%5FSystem%5FString%5F)SetCredentials(string, string)

If SDS2 didn't have stored credentials, and you've prompted the user for their license login, you can then pass these credentials to SDS2 and it will use them to checkout a license

##### Declaration

```
public static void SetCredentials(string userName, string password)
```

##### Parameters

| Type                                                           | Name     | Description |
| -------------------------------------------------------------- | -------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | userName |             |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | password |             |

##### Remarks

The normal program start procedure looks like:

```
if(!Licensing.HasStoredCredentials)
{
    string userName = .. prompt for user name;
    string password = .. prompt for password;
    Licensing.SetCredentials(userName, password);
}
Licensing.Checkout();
```