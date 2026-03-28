# Class HoleMachineOperations 

'Machine/Tool operations' as seen in the hole edit screen

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

HoleMachineOperations

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
public sealed class HoleMachineOperations
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5F%5Fctor)HoleMachineOperations()

'Machine/Tool operations' as seen in the hole edit screen

##### Declaration

```
public HoleMachineOperations()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FBlindHoleDepth)BlindHoleDepth

The depth of the blind hole

##### Declaration

```
public double BlindHoleDepth { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FHasAnyOperations)HasAnyOperations

Returns true iff the object has a blind hole, or has threads, or is not straight shaped.

##### Declaration

```
public bool HasAnyOperations { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FIsBlind)IsBlind

Specifies if the hole is a blind hole

##### Declaration

```
public bool IsBlind { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FIsMetric)IsMetric

The units of operations are always stored in inches, but this flag indicates what units are displayed to the user in the hole edit screen and client code should ensure the actual distances stored are consistent with this flag, e.g. storing 6mm should be saved as .24 when IsMetric is true. When IsMetric is false the correct distance saved should probably be 1/4in or .25

##### Declaration

```
public bool IsMetric { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FIsStraightShape)IsStraightShape

Indicates if the shape of the hole is straight. The shape will be one of straight, countersink, or counterbore

##### Declaration

```
public bool IsStraightShape { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FNotes)Notes

The notes for the operations

##### Declaration

```
public string Notes { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FClearAllOperations)ClearAllOperations()

Clear all operations

##### Declaration

```
public void ClearAllOperations()
```

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FFinalize)\~HoleMachineOperations()

'Machine/Tool operations' as seen in the hole edit screen

##### Declaration

```
protected ~HoleMachineOperations()
```

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FGetCounterboreShape)GetCounterboreShape()

A deep copy of the Counterbore shape of the hole or null if the shape is not counterbore. The shape will be one of straight, countersink, or counterbore

##### Declaration

```
public HoleMachineCounterboreShape GetCounterboreShape()
```

##### Returns

| Type                                                                                  | Description |
| ------------------------------------------------------------------------------------- | ----------- |
| [HoleMachineCounterboreShape](DesignData.SDS2.Model.HoleMachineCounterboreShape.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FGetCountersinkShape)GetCountersinkShape()

A deep copy of the Countersink shape of the hole or null if the shape is not countersink. The shape will be one of straight, countersink, or counterbore

##### Declaration

```
public HoleMachineCountersinkShape GetCountersinkShape()
```

##### Returns

| Type                                                                                  | Description |
| ------------------------------------------------------------------------------------- | ----------- |
| [HoleMachineCountersinkShape](DesignData.SDS2.Model.HoleMachineCountersinkShape.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FGetHashCode)GetHashCode()

'Machine/Tool operations' as seen in the hole edit screen

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

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FGetThreads)GetThreads()

A deep copy of the threads of the hole. Null indicates no threads

##### Declaration

```
public HoleMachineOperationThreads GetThreads()
```

##### Returns

| Type                                                                                  | Description |
| ------------------------------------------------------------------------------------- | ----------- |
| [HoleMachineOperationThreads](DesignData.SDS2.Model.HoleMachineOperationThreads.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FSetCounterboreShape%5FDesignData%5FSDS2%5FModel%5FHoleMachineCounterboreShape%5F)SetCounterboreShape(HoleMachineCounterboreShape)

A deep copy of the Counterbore shape of the hole or null if the shape is not counterbore. The shape will be one of straight, countersink, or counterbore

##### Declaration

```
public void SetCounterboreShape(HoleMachineCounterboreShape bore)
```

##### Parameters

| Type                                                                                  | Name | Description |
| ------------------------------------------------------------------------------------- | ---- | ----------- |
| [HoleMachineCounterboreShape](DesignData.SDS2.Model.HoleMachineCounterboreShape.html) | bore |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FSetCountersinkShape%5FDesignData%5FSDS2%5FModel%5FHoleMachineCountersinkShape%5F)SetCountersinkShape(HoleMachineCountersinkShape)

A deep copy of the Countersink shape of the hole or null if the shape is not countersink. The shape will be one of straight, countersink, or counterbore

##### Declaration

```
public void SetCountersinkShape(HoleMachineCountersinkShape sink)
```

##### Parameters

| Type                                                                                  | Name | Description |
| ------------------------------------------------------------------------------------- | ---- | ----------- |
| [HoleMachineCountersinkShape](DesignData.SDS2.Model.HoleMachineCountersinkShape.html) | sink |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleMachineOperations%5FSetThreads%5FDesignData%5FSDS2%5FModel%5FHoleMachineOperationThreads%5F)SetThreads(HoleMachineOperationThreads)

A deep copy of the threads of the hole. Null indicates no threads

##### Declaration

```
public void SetThreads(HoleMachineOperationThreads threads)
```

##### Parameters

| Type                                                                                  | Name    | Description |
| ------------------------------------------------------------------------------------- | ------- | ----------- |
| [HoleMachineOperationThreads](DesignData.SDS2.Model.HoleMachineOperationThreads.html) | threads |             |