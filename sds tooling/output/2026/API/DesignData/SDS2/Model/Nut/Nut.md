# Class Nut 

A nut, on a bolt

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Nut

##### Inherited Members

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
public class Nut
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FNut%5FNutType)NutType

the type of nut used

##### Declaration

```
public NutType NutType { get; set; }
```

##### Property Value

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [NutType](DesignData.SDS2.Model.NutType.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FNut%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A nut, on a bolt

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FNut%5FFinalize)\~Nut()

A nut, on a bolt

##### Declaration

```
protected ~Nut()
```