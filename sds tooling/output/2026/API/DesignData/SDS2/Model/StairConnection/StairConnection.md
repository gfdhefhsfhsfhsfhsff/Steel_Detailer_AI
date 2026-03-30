# Class StairConnection 

Connection for an end and side of a stair stringer

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[Component](DesignData.SDS2.Model.Component.html)

[PythonComponent](DesignData.SDS2.Model.PythonComponent.html)

StairConnection

##### Inherited Members

[PythonComponent.FindCreatedMaterial()](DesignData.SDS2.Model.PythonComponent.html#DesignData%5FSDS2%5FModel%5FPythonComponent%5FFindCreatedMaterial) 

[PythonComponent.PythonObject](DesignData.SDS2.Model.PythonComponent.html#DesignData%5FSDS2%5FModel%5FPythonComponent%5FPythonObject) 

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
public class StairConnection : PythonComponent
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FConnection)Connection

Specifies the connection between a stringer its support.

##### Declaration

```
public StairConnectionSpecification Connection { get; set; }
```

##### Property Value

| Type                                                                                    | Description |
| --------------------------------------------------------------------------------------- | ----------- |
| [StairConnectionSpecification](DesignData.SDS2.Model.StairConnectionSpecification.html) |             |

##### Remarks

This data is a copy of the connection

##### Exceptions

| Type                                                                           | Condition                   |
| ------------------------------------------------------------------------------ | --------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Thrown for null connection. |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FElevation)Elevation

The elevation, in inches, of the connection reference point

##### Declaration

```
public double Elevation { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FIsBottomEnd)IsBottomEnd

Specifies if the connection is on the bottom end of the stair

##### Declaration

```
public bool IsBottomEnd { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FIsLeft)IsLeft

Specifies if the connection is on the left end of the stair

##### Declaration

```
public bool IsLeft { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FIsNearSide)IsNearSide

Specifies if the connection is on the near side of the stair

##### Declaration

```
public bool IsNearSide { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FSupportingMember)SupportingMember

The supporting member.

##### Declaration

```
public MemberHandle SupportingMember { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) |             |

##### Remarks

StairConnection may disregard the set supporting member if it determines a connection cannot be made to it. In that case it may try to find a different member that it can connect to.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Connection for an end and side of a stair stringer

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[PythonComponent.Dispose(bool)](DesignData.SDS2.Model.PythonComponent.html#DesignData%5FSDS2%5FModel%5FPythonComponent%5FDispose%5FSystem%5FBoolean%5F)

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FIsClipAngleConnection)IsClipAngleConnection()

Indicates if a StairConnectionClipAngle is used

##### Declaration

```
public bool IsClipAngleConnection()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FIsFloorClipConnection)IsFloorClipConnection()

Indicates if a StairConnectionFloorClip is used

##### Declaration

```
public bool IsFloorClipConnection()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FIsPlainEndConnection)IsPlainEndConnection()

Indicates if a StairConnectionPlainEnd is used

##### Declaration

```
public bool IsPlainEndConnection()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FStairConnection%5FIsShearPlateConnection)IsShearPlateConnection()

Indicates if a StairConnectionShearPlate is used

##### Declaration

```
public bool IsShearPlateConnection()
```

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |