# Class UserSettings 

Access to user settings

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

UserSettings

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public class UserSettings
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FUserSettings%5FUserInterfaceAppearance)UserInterfaceAppearance

This user's current setting for light or dark mode. If you want your interface to match up with SDS2 this setting is useful to see what the current user's expectation is.

##### Declaration

```
public UIAppearance UserInterfaceAppearance { get; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [UIAppearance](DesignData.SDS2.Setup.UIAppearance.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FUserSettings%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Access to user settings

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FUserSettings%5FFinalize)\~UserSettings()

Access to user settings

##### Declaration

```
protected ~UserSettings()
```

#### [](#DesignData%5FSDS2%5FSetup%5FUserSettings%5FGet)Get()

Get the UserSettings object for the current user

##### Declaration

```
public static UserSettings Get()
```

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [UserSettings](DesignData.SDS2.Setup.UserSettings.html) |             |

##### Exceptions

| Type                                                                                   | Condition                                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | thrown if there is no DataDirectory open. You must call DataDirectory.Open() before checking node config |