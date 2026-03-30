# Class Washer 

A washer, on a bolt

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Washer

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
public class Washer
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FWasher%5FHorizontalEdgeDistance)HorizontalEdgeDistance

Distance, in inches, from the nearest horizontal edge of the plate washer to the center of the nearest hole, on each side. This only applies to washers of type MaterialPlate.

```
         The wording is odd here because what the nearest horizontal edge is varies depending on
         if you combine material plate washers and how.

```

##### Declaration

```
public double HorizontalEdgeDistance { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasher%5FQuantity)Quantity

Indicates how many of this kind of washer to put in this position.

##### Declaration

```
public uint Quantity { get; set; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWasher%5FRotation)Rotation

The rotation of the washer, in radians.

##### Declaration

```
public double Rotation { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWasher%5FThickness)Thickness

The thickness of the washer.

##### Declaration

```
public double Thickness { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWasher%5FVerticalEdgeDistance)VerticalEdgeDistance

Distance, in inches, from the nearest vertical edge of the plate washer to the center of the nearest hole, on each side. This only applies to washers of type MaterialPlate

##### Declaration

```
public double VerticalEdgeDistance { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasher%5FWasherType)WasherType

the type of washer used

##### Declaration

```
public WasherType WasherType { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [WasherType](DesignData.SDS2.Model.WasherType.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FWasher%5FWidth)Width

The width of the washer.

##### Declaration

```
public double Width { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FWasher%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A washer, on a bolt

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FWasher%5FFinalize)\~Washer()

A washer, on a bolt

##### Declaration

```
protected ~Washer()
```