# Class Hole 

A single hole on a material

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Hole

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class Hole
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FCombineOnDetail)CombineOnDetail

Indicates if this hole should be combined with others, when possible, on details.

##### Declaration

```
public bool CombineOnDetail { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FCustomPropertyMapHandle)CustomPropertyMapHandle

A handle to the custom properties for this hole.

##### Declaration

```
public CustomPropertyMapHandle CustomPropertyMapHandle { get; }
```

##### Property Value

| Type                                                                             | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [CustomPropertyMapHandle](DesignData.SDS2.Database.CustomPropertyMapHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FGroup)Group

The group object for this hole, with properties shared by all holes in this group.

##### Declaration

```
public HoleGroup Group { get; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [HoleGroup](DesignData.SDS2.Model.HoleGroup.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FHandle)Handle

The database handle for this object

##### Declaration

```
public HoleHandle Handle { get; }
```

##### Property Value

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [HoleHandle](DesignData.SDS2.Database.HoleHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FHoleType)HoleType

The kind of hole to drill

##### Declaration

```
public HoleType HoleType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [HoleType](DesignData.SDS2.Setup.HoleType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FIsBlind)IsBlind

A hole which is blind is one what isn't drilled all the way through the material.

##### Declaration

```
public bool IsBlind { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FIsMatchable)IsMatchable

Indicates if this hole can be used to "match" against other material, which would create a corresponding hole on that material in line with this hole. If this is false, then this hole will be ignored during hole matching.

##### Declaration

```
public bool IsMatchable { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FIsSystemGenerated)IsSystemGenerated

Indicates if a hole was added by the system, during process, or if it was added by an interactive tool. Holes created by custom members and components are considered system.

##### Declaration

```
public bool IsSystemGenerated { get; }
```

##### Property Value

| Type                                                          | Description                                  |
| ------------------------------------------------------------- | -------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | True if this hole was created by the system. |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FLength)Length

The drill length of the hole

##### Declaration

```
public double Length { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FPlugType)PlugType

The plug type for this hole

##### Declaration

```
public PlugType PlugType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [PlugType](DesignData.SDS2.Model.PlugType.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FPoint1)Point1

The starting point where this hole is drilled, in material coordinates

##### Declaration

```
public Point3D Point1 { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

##### Remarks

This is the same as ReferenceLocation

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FPoint2)Point2

The ending point where this hole is drilled, in material coordinates

##### Declaration

```
public Point3D Point2 { get; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FReferenceLocation)ReferenceLocation

The reference location, in material coordinates, of the hole

##### Declaration

```
public Point3D ReferenceLocation { get; set; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FToGlobalCoordinates)ToGlobalCoordinates

The relative location and orientation of the hole in global coordinates

##### Declaration

```
public Matrix ToGlobalCoordinates { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Exceptions

| Type                                                                             | Condition                                                                                   |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [InvalidHandleException](DesignData.SDS2.Exceptions.InvalidHandleException.html) | Thrown if the hole transform cannot be retrieved. This typically indicates data corruption. |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A single hole on a material

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FEquals%5FSystem%5FObject%5F)Equals(object)

A single hole on a material

##### Declaration

```
public override bool Equals(object other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | other |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FFinalize)\~Hole()

A single hole on a material

##### Declaration

```
protected ~Hole()
```

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FGet%5FDesignData%5FSDS2%5FDatabase%5FHoleHandle%5F)Get(HoleHandle)

Returns a Hole object from a HoleHandle if it exists in the job. Otherwise, returns null.

##### Declaration

```
public static Hole Get(HoleHandle handle)
```

##### Parameters

| Type                                                   | Name   | Description |
| ------------------------------------------------------ | ------ | ----------- |
| [HoleHandle](DesignData.SDS2.Database.HoleHandle.html) | handle |             |

##### Returns

| Type                                    | Description |
| --------------------------------------- | ----------- |
| [Hole](DesignData.SDS2.Model.Hole.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FGetHashCode)GetHashCode()

A single hole on a material

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

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FGetOperations)GetOperations()

A deep copy of the the machine/tool operations for the hole

##### Declaration

```
public HoleMachineOperations GetOperations()
```

##### Returns

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [HoleMachineOperations](DesignData.SDS2.Model.HoleMachineOperations.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FGetSurface)GetSurface()

This gives a faceted solid Surface representing the shape of the hole in the material in hole local coordinates. The ends of the hole are lifted 0.005" off the surface of the material (this aids with display).

```
         This is also true for blind holes (holes that don't go all the way
         through).  The end of this hole Surface will be 0.005" past where the
         blind hole is detailed to drill to.

```

##### Declaration

```
public Surface GetSurface()
```

##### Returns

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FSetNominalHoleDimensions%5FDesignData%5FSDS2%5FSetup%5FHoleType%5FDesignData%5FSDS2%5FSetup%5FBoltType%5FSystem%5FDouble%5F)SetNominalHoleDimensions(HoleType, BoltType, double)

Set the hole diameter and slot length based on the hole type, bolt type and bolt diameter. Also, sets the hole type, bolt type, and bolt diameter to the specified values.

##### Declaration

```
public void SetNominalHoleDimensions(HoleType holeType, BoltType boltType, double boltDiameter)
```

##### Parameters

| Type                                                           | Name         | Description |
| -------------------------------------------------------------- | ------------ | ----------- |
| [HoleType](DesignData.SDS2.Setup.HoleType.html)                | holeType     |             |
| [BoltType](DesignData.SDS2.Setup.BoltType.html)                | boltType     |             |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | boltDiameter |             |

#### [](#DesignData%5FSDS2%5FModel%5FHole%5FSetOperations%5FDesignData%5FSDS2%5FModel%5FHoleMachineOperations%5F)SetOperations(HoleMachineOperations)

A deep copy of the the machine/tool operations for the hole

##### Declaration

```
public void SetOperations(HoleMachineOperations operations)
```

##### Parameters

| Type                                                                      | Name       | Description |
| ------------------------------------------------------------------------- | ---------- | ----------- |
| [HoleMachineOperations](DesignData.SDS2.Model.HoleMachineOperations.html) | operations |             |