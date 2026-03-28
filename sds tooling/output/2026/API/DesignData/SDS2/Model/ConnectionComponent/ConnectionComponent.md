# Class ConnectionComponent 

A builtin connection component

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Component](DesignData.SDS2.Model.Component.html)

ConnectionComponent

##### Inherited Members

[Component.Handle](DesignData.SDS2.Model.Component.html#DesignData%5FSDS2%5FModel%5FComponent%5FHandle) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class ConnectionComponent : Component
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FConnectionChangedMessage)ConnectionChangedMessage

The changed connection message that shows up in the edit screen when SDS2 designs a connection that is different from the input connection specification

##### Declaration

```
public string ConnectionChangedMessage { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

This will return a changed message even when there is also a ConnectionFailureMessage. This is in contrast to the member edit screen which will only show a failure message, when there is a change and a failure.

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FConnectionFailureMessage)ConnectionFailureMessage

The connection failure message that shows up in the edit screen when SDS2 is unable to create a connection for the framing situation

##### Declaration

```
public string ConnectionFailureMessage { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FDesignedSpecification)DesignedSpecification

The connection specification the system used to design the current connection. This can vary from the requested when the system determines that the requested specification is invalid. Or if the requested spec is auto standard, this will be filled in with the actual connection specification that auto standard applied.

##### Declaration

```
public ConnectionSpecification DesignedSpecification { get; }
```

##### Property Value

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html) |             |

##### Remarks

This should be considered readonly. Changes you make here will not modify the designed connection.

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FInputSpecification)InputSpecification

The requested connection specification input by the user. This can be modified in place, or a new specification can be made and assigned to this.

##### Declaration

```
public ConnectionSpecification InputSpecification { get; set; }
```

##### Property Value

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                                                              |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown if the input specification isn't valid for this member type.                                                                                    |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)         | Thrown if this is called without adding both this Component object and the Member it is on to the Transaction. Or if there simply isn't a Transaction. |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxCompression)MaxCompression

The highest the compression value can be without failing.

##### Declaration

```
public double MaxCompression { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxCompressionUnity)MaxCompressionUnity

The highest the compression unity can be without failing.

##### Declaration

```
public double MaxCompressionUnity { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxMoment)MaxMoment

The highest the moment value can be without failing.

##### Declaration

```
public double MaxMoment { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxMomentUnity)MaxMomentUnity

The highest the moment unity value can be without failing.

##### Declaration

```
public double MaxMomentUnity { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxPanelMoment)MaxPanelMoment

The highest the panel moment value can be without failing.

##### Declaration

```
public double MaxPanelMoment { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxPanelMomentUnity)MaxPanelMomentUnity

The highest the panel moment unity value can be without failing.

##### Declaration

```
public double MaxPanelMomentUnity { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxShear)MaxShear

The highest the shear value can be without failing.

##### Declaration

```
public double MaxShear { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxShearUnity)MaxShearUnity

The highest the shear unity value can be without failing.

##### Declaration

```
public double MaxShearUnity { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxTension)MaxTension

The highest the tension value can be without failing.

##### Declaration

```
public double MaxTension { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxTensionUnity)MaxTensionUnity

The highest the tension unity value can be without failing.

##### Declaration

```
public double MaxTensionUnity { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxTyingResistance)MaxTyingResistance

The highest the tying resistance value can be without failing.

##### Declaration

```
public double MaxTyingResistance { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FMaxTyingResistanceUnity)MaxTyingResistanceUnity

The highest the tying resistance unity value can be without failing.

##### Declaration

```
public double MaxTyingResistanceUnity { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A builtin connection component

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[Component.Dispose(bool)](DesignData.SDS2.Model.Component.html#DesignData%5FSDS2%5FModel%5FComponent%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FFindCreatedMaterial)FindCreatedMaterial()

Returns an object containing three lists, Materials, Bolts, Welds that a connection created.

##### Declaration

```
public override CreatedConnectionMaterial FindCreatedMaterial()
```

##### Returns

| Type                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [CreatedConnectionMaterial](DesignData.SDS2.Model.CreatedConnectionMaterial.html) |             |

##### Overrides

[Component.FindCreatedMaterial()](DesignData.SDS2.Model.Component.html#DesignData%5FSDS2%5FModel%5FComponent%5FFindCreatedMaterial)

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FGetImageLabelForLockableName%5FSystem%5FString%5F)GetImageLabelForLockableName(string)

Use this method to get the corresponding image label for the Lockable, if it has a label.

If there is no image label, an empty string is returned.

##### Declaration

```
public string GetImageLabelForLockableName(string name)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

Your final code should not include use of this method, this is for debugging purposes.

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FGetLabelForLockableName%5FSystem%5FString%5F)GetLabelForLockableName(string)

Use this method to translate names in the map returned by GetLockables into the labels visible on the edit screen. This is useful to help figure out what name you should use in your code to map to a name you see on the screen.

```
         The returned name will be translated into the user's local language.

         If this returns an empty string, then the name was not found.

```

##### Declaration

```
public string GetLabelForLockableName(string name)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

Your final code should not include use of this method, this is for debugging purposes.

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FGetLockable%5FSystem%5FString%5F)GetLockable(string)

Get a single lockable by name. Doing this with the map would work just as well, but this can be more efficient if you just need one.

##### Declaration

```
public Lockable GetLockable(string name)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [Lockable](DesignData.SDS2.Model.Lockable.html) |             |

##### Remarks

This will be a copy of the lockable. If you make changes to it, to see them reflected you will need to pass it to SetLockable

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FGetLockables)GetLockables()

Get a map of all lockables on this connection

##### Declaration

```
public LockableDictionary GetLockables()
```

##### Returns

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [LockableDictionary](DesignData.SDS2.Model.LockableDictionary.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FGetPromptGroupForLockableName%5FSystem%5FString%5F)GetPromptGroupForLockableName(string)

Use this method to get the prompt group for the Lockable.

##### Declaration

```
public string GetPromptGroupForLockableName(string name)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

Your final code should not include use of this method, this is for debugging purposes.

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FGetPromptTabForLockableName%5FSystem%5FString%5F)GetPromptTabForLockableName(string)

Use this method to get the prompt tab for the Lockable.

##### Declaration

```
public string GetPromptTabForLockableName(string name)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

Your final code should not include use of this method, this is for debugging purposes.

#### [](#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FSetLockable%5FSystem%5FString%5FDesignData%5FSDS2%5FModel%5FLockable%5F)SetLockable(string, Lockable)

Apply a lockable value to this connection. You can only pass in names which would return a non-null lockable from GetLockable (so you can't add new lockable keys this way, you can just replace their value).

##### Declaration

```
public void SetLockable(string name, Lockable value)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | name  |             |
| [Lockable](DesignData.SDS2.Model.Lockable.html)                | value |             |

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown when attempting to override a locked lockable within process. Unless you are implementing an extension of SDS2 (such as a custom member) this does not apply.                                                                                                                         |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)                 | Thrown if this is called without adding both this Component object and the Member it is on to the Transaction. Or if there simply isn't a Transaction.                                                                                                                                       |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html)         | Thrown if the lockable given is not a valid value for this specific lockable. The Message on the InvalidValueException will include the message we'd give to a user if they typed that value on the screen, so it's usable to present directly to a user if your application is interactive. |