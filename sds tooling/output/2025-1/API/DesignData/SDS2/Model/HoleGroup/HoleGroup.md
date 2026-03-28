# Class HoleGroup 

A group of holes, and properties holes share with other holes in the same group.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

HoleGroup

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
public class HoleGroup
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FBoltDiameter)BoltDiameter

The expected bolt diameter for the hole. If bolts are added to this hole their diameter will follow this property.

##### Declaration

```
public double BoltDiameter { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FDiameter)Diameter

The diameter of the hole.

##### Declaration

```
public double Diameter { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FHandle)Handle

The database handle for this object

##### Declaration

```
public HoleGroupHandle Handle { get; }
```

##### Property Value

| Type                                                             | Description |
| ---------------------------------------------------------------- | ----------- |
| [HoleGroupHandle](DesignData.SDS2.Database.HoleGroupHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FIsAutoPreferredBoltType)IsAutoPreferredBoltType

Specifies if the preferred bolt type for the hole should use the default bolt type defined in setup.

##### Declaration

```
public bool IsAutoPreferredBoltType { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Assigning PreferredBoltType to null will turn on IsAutoPreferredBoltType. Setting it to a non-null bolt type will turn off IsAutoPreferredBoltType.

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FPreferredBoltType)PreferredBoltType

The bolt type for the hole

##### Declaration

```
public BoltType PreferredBoltType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

##### Remarks

Assigning PreferredBoltType to null will turn on IsAutoPreferredBoltType. Setting it to a non-null bolt type will turn off IsAutoPreferredBoltType.

##### Exceptions

| Type                                                                           | Condition                                                   |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | Throw when passed a bolt type that is not defined in setup. |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FSlotLength)SlotLength

The widest part of a slot hole, its slot length

##### Declaration

```
public double SlotLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FSlotRotation)SlotRotation

Slot rotation that is offset PI/2 from what is seen in the edit screen

##### Declaration

```
public double SlotRotation { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FSlotRotation2)SlotRotation2

Slot rotation of the group that matches the slot rotation seen in the hole edit screen. The original SlotRotation property is offset by PI/2 radians.

##### Declaration

```
public double SlotRotation2 { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FToGlobalCoordinates)ToGlobalCoordinates

The relative location and orientation of the hole group in global coordinates

##### Declaration

```
public Matrix ToGlobalCoordinates { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FToMaterialCoordinates)ToMaterialCoordinates

The relative location and orientation of the hole group on the material being drilled.

##### Declaration

```
public Matrix ToMaterialCoordinates { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FUseTrueGageOfOutsideLegFromMaterial)UseTrueGageOfOutsideLegFromMaterial

True if this should be referenced on the outside leg gage of a clip angle. The actual measurement comes from the material being drilled, this just controls whether that measurement will be used or not.

##### Declaration

```
public bool UseTrueGageOfOutsideLegFromMaterial { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A group of holes, and properties holes share with other holes in the same group.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FEquals%5FSystem%5FObject%5F)Equals(object)

A group of holes, and properties holes share with other holes in the same group.

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

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FFinalize)\~HoleGroup()

A group of holes, and properties holes share with other holes in the same group.

##### Declaration

```
protected ~HoleGroup()
```

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FGet%5FDesignData%5FSDS2%5FDatabase%5FHoleGroupHandle%5F)Get(HoleGroupHandle)

Returns a HoleGroup object from a HoleGroupHandle if it exists in the job. Otherwise, returns null.

##### Declaration

```
public static HoleGroup Get(HoleGroupHandle handle)
```

##### Parameters

| Type                                                             | Name   | Description |
| ---------------------------------------------------------------- | ------ | ----------- |
| [HoleGroupHandle](DesignData.SDS2.Database.HoleGroupHandle.html) | handle |             |

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [HoleGroup](DesignData.SDS2.Model.HoleGroup.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FGetHashCode)GetHashCode()

A group of holes, and properties holes share with other holes in the same group.

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

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FGetHolePattern)GetHolePattern()

Return a hole pattern representing all the holes in the group.

##### Declaration

```
public HolePattern GetHolePattern()
```

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [HolePattern](DesignData.SDS2.Model.HolePattern.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FHoleGroup%5FGetHoles)GetHoles()

All the holes in the group.

##### Declaration

```
public HoleList GetHoles()
```

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [HoleList](DesignData.SDS2.Model.HoleList.html) |             |