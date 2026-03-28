# Class HoleMachineOperationThreads 

Hole threading operation

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

HoleMachineOperationThreads

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public sealed class HoleMachineOperationThreads
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperationThreads%5F%5Fctor)HoleMachineOperationThreads()

Hole threading operation

##### Declaration

```
public HoleMachineOperationThreads()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperationThreads%5FDepth)Depth

The depth of the threads

##### Declaration

```
public double Depth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperationThreads%5FFitClass)FitClass

Hole threading operation

##### Declaration

```
public string FitClass { get; set; }
```

##### Property Value

| Type                                                           | Description                                          |
| -------------------------------------------------------------- | ---------------------------------------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | A UTF-8 encoded string that is 7 or fewer bytes long |

##### Exceptions

| Type                                                                           | Condition                                                                      |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when FitClass is set to a string that is too long |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperationThreads%5FIsLeftHanded)IsLeftHanded

Specifies if the thread direction is left handed

##### Declaration

```
public bool IsLeftHanded { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperationThreads%5FSeries)Series

The form or series of the threads

##### Declaration

```
public HoleMachineOperationThreadSeries Series { get; set; }
```

##### Property Value

| Type                                                                                            | Description |
| ----------------------------------------------------------------------------------------------- | ----------- |
| [HoleMachineOperationThreadSeries](DesignData.SDS2.Model.HoleMachineOperationThreadSeries.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperationThreads%5FSize)Size

The nominal diameter of the threaded hole

##### Declaration

```
public double Size { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperationThreads%5FThreadsPerUnit)ThreadsPerUnit

The number of threads per unit. Inch if the operations are Imperial and pitch if they are metric

##### Declaration

```
public uint ThreadsPerUnit { get; set; }
```

##### Property Value

| Type                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [uint](https://learn.microsoft.com/dotnet/api/system.uint32) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperationThreads%5FFinalize)\~HoleMachineOperationThreads()

Hole threading operation

##### Declaration

```
protected ~HoleMachineOperationThreads()
```

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperationThreads%5FGetHashCode)GetHashCode()

Hole threading operation

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)