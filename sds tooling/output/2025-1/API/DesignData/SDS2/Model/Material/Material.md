# Class Material 

Material is the base class for all material types.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Material

[BoltMaterial](DesignData.SDS2.Model.BoltMaterial.html)

[Decking](DesignData.SDS2.Model.Decking.html)

[FlatBar](DesignData.SDS2.Model.FlatBar.html)

[Grating](DesignData.SDS2.Model.Grating.html)

[GratingTread](DesignData.SDS2.Model.GratingTread.html)

[Plate](DesignData.SDS2.Model.Plate.html)

[PythonMaterial](DesignData.SDS2.Model.PythonMaterial.html)

[Rail](DesignData.SDS2.Model.Rail.html)

[RectangularPlateEnd](DesignData.SDS2.Model.RectangularPlateEnd.html)

[ReferenceObjectAreaLayout](DesignData.SDS2.Model.ReferenceObjectAreaLayout.html)

[ReferenceObjectPerimeterLayout](DesignData.SDS2.Model.ReferenceObjectPerimeterLayout.html)

[RoundBar](DesignData.SDS2.Model.RoundBar.html)

[ShapeMaterial](DesignData.SDS2.Model.ShapeMaterial.html)

[ShearOrThreadedStud](DesignData.SDS2.Model.ShearOrThreadedStud.html)

[SquareBar](DesignData.SDS2.Model.SquareBar.html)

[StandardPart](DesignData.SDS2.Model.StandardPart.html)

[TurnedShellLayout](DesignData.SDS2.Model.TurnedShellLayout.html)

[TurnedSolidLayout](DesignData.SDS2.Model.TurnedSolidLayout.html)

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
public class Material
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FABM%5FID)ABM\_ID

The ABM id for this material

##### Declaration

```
public string ABM_ID { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the material is invalid.       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when the material is unlocked while setting the property. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FABM%5FLength)ABM\_Length

ABM length. Applicable when not using point to point length for the ABM.

##### Declaration

```
public double ABM_Length { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the material is invalid.       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when the material is unlocked while setting the property. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FABM%5FName)ABM\_Name

Name of the ABM this material is on

##### Declaration

```
public string ABM_Name { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Exceptions

| Type                                                                           | Condition                                                  |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the material is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FABM%5FNote)ABM\_Note

ABM note for this material

##### Declaration

```
public string ABM_Note { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the material is invalid.       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when the material is unlocked while setting the property. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FABM%5FPointToPointLength)ABM\_PointToPointLength

ABM point to point length. Applicable when using point to point length for the ABM.

##### Declaration

```
public double ABM_PointToPointLength { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the material is invalid.       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when the material is unlocked while setting the property. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FColor)Color

Get the color of the material

##### Declaration

```
public Color Color { get; set; }
```

##### Property Value

| Type                                           | Description |
| ---------------------------------------------- | ----------- |
| [Color](DesignData.SDS2.Primitives.Color.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FCustomPropertyMapHandle)CustomPropertyMapHandle

A handle to the custom properties for this material.

##### Declaration

```
public CustomPropertyMapHandle CustomPropertyMapHandle { get; }
```

##### Property Value

| Type                                                                             | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [CustomPropertyMapHandle](DesignData.SDS2.Database.CustomPropertyMapHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FDescription)Description

A description of the material. This is either a default, automatically generated, description or one entered by the user. If you set this, it will become a user description.

##### Declaration

```
public string Description { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

This string maxes out at 22 characters. SDS2 will cut off any text after that.

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FFinish)Finish

The surface finish of the material

##### Declaration

```
[Obsolete("Model.Material.Finish return type enum is deprecated. Use the SurfaceFinish property for the new type Setup.SurfaceFinish", false)]
public MaterialSurfaceFinish Finish { get; set; }
```

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [MaterialSurfaceFinish](DesignData.SDS2.Setup.MaterialSurfaceFinish.html) |             |

##### Remarks

For BoltMaterial, this property is ignored. And BoltFinish should be used.

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the material is invalid.       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when the material is unlocked while setting the property. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FGrade)Grade

Returns a steel grade, or null if not applicable

##### Declaration

```
public SteelGrade Grade { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) |             |

##### Remarks

To set a grade look for the Grade property on the derived class. You'll need to choose a grade from an appropriate grade list for that material type. Which can be found in a static property, on that class, called AvailableSteelGrades.

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FHandle)Handle

The database handle for this object

##### Declaration

```
public MaterialHandle Handle { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [MaterialHandle](DesignData.SDS2.Database.MaterialHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FHoles)Holes

The list of holes drilled into this material.

##### Declaration

```
public HoleList Holes { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [HoleList](DesignData.SDS2.Model.HoleList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsAutoSurfaceFinish)IsAutoSurfaceFinish

When true, IsAutoSurfaceFinish indicates the material follows the finish set for the member. When false, the finish can be different from the member finish.

##### Declaration

```
public bool IsAutoSurfaceFinish { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                     | Condition                                                        |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when the material is unlocked while setting the property. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsBent)IsBent

Returns true if a bend operation was applied to the material.

##### Declaration

```
public bool IsBent { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsCNCDownloaded)IsCNCDownloaded

True if a cnc download file has been generated for this material.

##### Declaration

```
public bool IsCNCDownloaded { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsCNCScribeOntoOther)IsCNCScribeOntoOther

True if this material can be scribed onto other materials it attaches to

##### Declaration

```
public bool IsCNCScribeOntoOther { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsDummy)IsDummy

A dummy material is assigned a submaterial mark prefix of d. In other words, dummy materials are assigned piecemarks such as d1, d2, d3, etc. Dummy material is not included in reports (such as the Joist Report or Connection Calculations or Expanded Connection Design Calculations), and it is not listed in any member's bill of material. Dummy material does appear on member details, but is not automatically included in the member bill of material and is not called out or dimensioned on the member detail. Detail Submaterial cannot detail dummy material.

##### Declaration

```
public bool IsDummy { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsFitted)IsFitted

Returns true if a fit operation was applied to the material.

##### Declaration

```
public bool IsFitted { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsInABM)IsInABM

Indicator if the material should be included in the ABM

##### Declaration

```
public bool IsInABM { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the material is invalid.       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when the material is unlocked while setting the property. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsMain)IsMain

If true, then this material is "main" material. Meaning that things are assembled by attaching them to this material.

##### Declaration

```
public bool IsMain { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsStretched)IsStretched

Returns true if a stretch operation was applied to the material.

##### Declaration

```
public bool IsStretched { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsSystem)IsSystem

True if a material was generated by the system and has not been modified by the user. False if it's been modified by the user, or was originally created by the user. The distinction between system and user is about whether material is created inside process, by software (system), or if it's created by the user outside of process either through the API or with builtin tools.

##### Declaration

```
public bool IsSystem { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FIsUserDescription)IsUserDescription

True if the description set is a user set description, or set through the API

##### Declaration

```
public bool IsUserDescription { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FMaterialUse)MaterialUse

An enumeration-like value describing why this material is being used in the job

##### Declaration

```
public MaterialUse MaterialUse { get; }
```

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [MaterialUse](DesignData.SDS2.Model.MaterialUse.html) |             |

##### Remarks

This is not a user facing field

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FPiecemark)Piecemark

Piecemark is the string identifying any material identical to this material.

##### Declaration

```
public string Piecemark { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

Piecemarks are assigned automatically, and should not typically be otherwise assigned. Piecemarks are typically composed of a prefix string from setup indicating the material type followed by a number.

##### Exceptions

| Type                                                                   | Condition                                                                        |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [MaterialException](DesignData.SDS2.Exceptions.MaterialException.html) | Assigning a piecemark may throw an exception if the piecemark is already in use. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FQuantity)Quantity

Material is the base class for all material types.

##### Declaration

```
public int Quantity { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FReferenceLocation)ReferenceLocation

The offset from the materials origin point to the materials origin reference point.

##### Declaration

```
public Point3D ReferenceLocation { get; set; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FRevisionDate)RevisionDate

The last date this was revised

##### Declaration

```
public DateTime? RevisionDate { get; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FRevisionLevel)RevisionLevel

Material is the base class for all material types.

##### Declaration

```
public int RevisionLevel { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FRoute1)Route1

The Mult. Cutting # routing. Assign these from the first list in the routing table on DesignData.SDS2.Setup.RoutingDefinitions.

##### Declaration

```
public RoutingDefinition Route1 { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) |             |

##### Remarks

The definition of this routing could change in the future

##### Exceptions

| Type                                                                           | Condition                                                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | If the type of routing set is not correct: You can't set a routing value from Route2 to Route1, for example. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FRoute2)Route2

The labor code routing. Assign these from the second list in the routing table on DesignData.SDS2.Setup.RoutingDefinitions.

##### Declaration

```
public RoutingDefinition Route2 { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) |             |

##### Remarks

The definition of this routing could change in the future

##### Exceptions

| Type                                                                           | Condition                                                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | If the type of routing set is not correct: You can't set a routing value from Route2 to Route1, for example. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FRoute3)Route3

The job cost code routing. Assign these from the third list in the routing table on DesignData.SDS2.Setup.RoutingDefinitions.

##### Declaration

```
public RoutingDefinition Route3 { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) |             |

##### Remarks

The definition of this routing could change in the future

##### Exceptions

| Type                                                                           | Condition                                                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | If the type of routing set is not correct: You can't set a routing value from Route2 to Route1, for example. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FRoute4)Route4

The remarks routing. Assign these from the fourth list in the routing table on DesignData.SDS2.Setup.RoutingDefinitions.

##### Declaration

```
public RoutingDefinition Route4 { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [RoutingDefinition](DesignData.SDS2.Setup.RoutingDefinition.html) |             |

##### Remarks

The definition of this routing could change in the future

##### Exceptions

| Type                                                                           | Condition                                                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | If the type of routing set is not correct: You can't set a routing value from Route2 to Route1, for example. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FSurfaceArea)SurfaceArea

The surface area around the whole material. This will not subtract out holes but it will subtract out material cuts and clips

##### Declaration

```
public double SurfaceArea { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

In square inches

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FSurfaceFinish)SurfaceFinish

The surface finish of the material

##### Declaration

```
public SurfaceFinish SurfaceFinish { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [SurfaceFinish](DesignData.SDS2.Setup.SurfaceFinish.html) |             |

##### Remarks

For BoltMaterial, this property is ignored. And BoltFinish should be used.

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the material is invalid.       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when the material is unlocked while setting the property. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FToGlobalCoordinates)ToGlobalCoordinates

Position and orientation of the material in global coordinates

##### Declaration

```
public Matrix ToGlobalCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FToMemberCoordinates)ToMemberCoordinates

Position and orientation of the material with respect to the member

##### Declaration

```
public Matrix ToMemberCoordinates { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FUsage)Usage

The usage description for this material. This can be taken from a table in setup, or it can be set it any 29 character (or shorter) string.

##### Declaration

```
public string Usage { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

This must be 29 characters or shorter.

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FUseAutoLengthInABM)UseAutoLengthInABM

False iff the ABM length is static data that does not change. Otherwise, the length is calculated dynamically by SDS2 as it changes.

##### Declaration

```
public bool UseAutoLengthInABM { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the material is invalid.       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when the material is unlocked while setting the property. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FUsePointToPointLengthInABM)UsePointToPointLengthInABM

True iff ABM length is based on the material's point to point length. Otherwise, ABM length is based on the standard ABM length.

##### Declaration

```
public bool UsePointToPointLengthInABM { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                           | Condition                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the material is invalid.       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)       | Thrown when the material is unlocked while setting the property. |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FWeight)Weight

The weight of the material.

##### Declaration

```
public double Weight { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

In pounds

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Material is the base class for all material types.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FDrill%5FDesignData%5FSDS2%5FModel%5FHolePattern%5F)Drill(HolePattern)

Create holes on the material given the hole pattern specification.

Drill will return the subset of holes in the pattern that are on a face of the material and are far enough from any other holes on the material. Drill will replace existing holes with no diameter, i.e. "marks", with actual holes.

Drill can be called on material that has not been added to the job, i.e. "standalone" material, or called on material that has been added to a transaction. Drill should not be mixed with other hole transactions such as edit. References to previous holes should be considered invalid after Drill.

##### Declaration

```
public HoleList Drill(HolePattern pattern)
```

##### Parameters

| Type                                                  | Name    | Description |
| ----------------------------------------------------- | ------- | ----------- |
| [HolePattern](DesignData.SDS2.Model.HolePattern.html) | pattern |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [HoleList](DesignData.SDS2.Model.HoleList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FFinalize)\~Material()

Material is the base class for all material types.

##### Declaration

```
protected ~Material()
```

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FGet%5FDesignData%5FSDS2%5FDatabase%5FMaterialHandle%5F)Get(MaterialHandle)

Get a Material object from a MaterialHandle for the current job.

##### Declaration

```
public static Material Get(MaterialHandle handle)
```

##### Parameters

| Type                                                           | Name   | Description |
| -------------------------------------------------------------- | ------ | ----------- |
| [MaterialHandle](DesignData.SDS2.Database.MaterialHandle.html) | handle |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMaterial%5FGetSurface)GetSurface()

Retrieve material polygons.

##### Declaration

```
public Surface GetSurface()
```

##### Returns

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html) |             |