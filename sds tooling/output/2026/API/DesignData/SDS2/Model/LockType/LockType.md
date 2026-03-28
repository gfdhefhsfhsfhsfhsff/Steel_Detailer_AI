# Enum LockType 

These "lock strengths" are used by connection design and member \* edit to determine whether a LockableValue::value can be overridden or \* not. \* \* A lower enum value represents a weaker lock strength. A stronger \* lockable cannot and should not be overridden by a weaker lock.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public enum LockType
```

### [](#fields)Fields 

| Name           | Description                                                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Unlocked       | Unlock this value, it will be set by process                                                                                               |
| ViaDesign      | This value is locked by the system during design                                                                                           |
| ViaMemberEdit  | This value was locked, with user input, specifically on this connection. Not necessarily on member edit, but possibly through an API call. |
| ViaUserDefined | This value was locked, with user input, in a user defined connection.                                                                      |