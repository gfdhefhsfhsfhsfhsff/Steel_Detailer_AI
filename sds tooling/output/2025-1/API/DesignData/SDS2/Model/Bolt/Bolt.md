# Class Bolt 

Describes a bolt fastener: The bolt plus any washers and any nuts.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Bolt

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public sealed class Bolt
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5F%5Fctor)Bolt()

Creates a new Bolt object, this must be added to a Member, in a Transaction and that transaction must be committed before this will be in the model.

##### Declaration

```
public Bolt()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FBoltType)BoltType

Bolt setup information currently used on bolt

##### Declaration

```
public BoltType BoltType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FBreakoutNutAndWasherOnBill)BreakoutNutAndWasherOnBill

If true, then nuts and washers are broken out into their own lines on the bill of material.

##### Declaration

```
public bool BreakoutNutAndWasherOnBill { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FCombineMaterialPlateWashers)CombineMaterialPlateWashers

If true, then washers will be combined based on the PlateWasherCombinationMethod setting. If false, then each bolt will get its own plate washer.

##### Declaration

```
public bool CombineMaterialPlateWashers { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FConnectionEnd)ConnectionEnd

The end of the member this is a connection for, if ConnectionBolt is true. If ConnectionBolt is false, this will just be MemberEnd.Left

##### Declaration

```
public MemberEnd ConnectionEnd { get; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [MemberEnd](DesignData.SDS2.Database.MemberEnd.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FConnectionMember)ConnectionMember

The member this connection comes from, if ConnectionBolt is true. If ConnectionBolt is false, this will be null.

##### Declaration

```
public MemberBrief ConnectionMember { get; }
```

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FCustomPropertyMapHandle)CustomPropertyMapHandle

A handle to the custom properties for this bolt.

##### Declaration

```
public CustomPropertyMapHandle CustomPropertyMapHandle { get; }
```

##### Property Value

| Type                                                                             | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [CustomPropertyMapHandle](DesignData.SDS2.Database.CustomPropertyMapHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FDiameter)Diameter

The diameter of the bolt shaft.

##### Declaration

```
public double Diameter { get; set; }
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

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FFinish)Finish

The finish type of the bolt

##### Declaration

```
public BoltFinish Finish { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [BoltFinish](DesignData.SDS2.Model.BoltFinish.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGripLength)GripLength

The distance between the inside of the bolt head and inside of the nut

##### Declaration

```
public double GripLength { get; set; }
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

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGuid)Guid

The SDS2 Guid/UUID for this bolt.

##### Declaration

```
public Guid? Guid { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [Guid](https://learn.microsoft.com/dotnet/api/system.guid)? |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FHandle)Handle

The database handle for this object

##### Declaration

```
public BoltHandle Handle { get; }
```

##### Property Value

| Type                                                   | Description |
| ------------------------------------------------------ | ----------- |
| [BoltHandle](DesignData.SDS2.Database.BoltHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FHillsideWasherAngle)HillsideWasherAngle

The angle from perpendicular of the fastener axis to the fastened material surface.

##### Declaration

```
public double HillsideWasherAngle { get; set; }
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

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FIsBoltless)IsBoltless

If true then this bolt has only a bolt head

##### Declaration

```
public bool IsBoltless { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FIsConnectionBolt)IsConnectionBolt

True if this bolt was created for an SDS2 designed connection

##### Declaration

```
public bool IsConnectionBolt { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FIsFieldBolt)IsFieldBolt

True if this is a bolt to be installed in the field, false if it's to be installed in the shop

##### Declaration

```
public bool IsFieldBolt { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FIsHeadless)IsHeadless

If true, then this bolt has no bolt head.

##### Declaration

```
public bool IsHeadless { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FIsSystemGenerated)IsSystemGenerated

Indicates if a bolt was added by the system, during process, or if it was added by an interactive tool. Bolts created by custom members and components are considered system.

##### Declaration

```
public bool IsSystemGenerated { get; }
```

##### Property Value

| Type                                                          | Description                                  |
| ------------------------------------------------------------- | -------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | True if this bolt was created by the system. |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FIsTensionControl)IsTensionControl

True if this is a tension control bolt

##### Declaration

```
public bool IsTensionControl { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FLength)Length

The length of the bolt shaft

##### Declaration

```
public double Length { get; set; }
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

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FMaterialUnderHead)MaterialUnderHead

Retrieve the material under the head of this bolt

##### Declaration

```
public Material MaterialUnderHead { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html) |             |

##### Remarks

For some bolt types, like point to point, this may be null

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FMaterialUnderNut)MaterialUnderNut

Retrieve the material under the nut of this bolt

##### Declaration

```
public Material MaterialUnderNut { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html) |             |

##### Remarks

For some bolt types, like point to point, this may be null

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FNuts)Nuts

The list of nuts. This list is a copy, so modifying this list will not remove, add, or reorder nuts. Use AddNut and RemoveNut if you need to do so.

##### Declaration

```
public NutList Nuts { get; }
```

##### Property Value

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [NutList](DesignData.SDS2.Model.NutList.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FPlateWasherCombinationMethod)PlateWasherCombinationMethod

Return the plate washer method set.

##### Declaration

```
public PlateWasherCombinationMethod PlateWasherCombinationMethod { get; set; }
```

##### Property Value

| Type                                                                                    | Description |
| --------------------------------------------------------------------------------------- | ----------- |
| [PlateWasherCombinationMethod](DesignData.SDS2.Model.PlateWasherCombinationMethod.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FPointUnderHead)PointUnderHead

This is the point under the head of the bolt relative to the member the bolt is on. To get the global point, use ToGlobalCoordinates.Transform on this point.

##### Declaration

```
public Point3D PointUnderHead { get; set; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FPointUnderNut)PointUnderNut

This is the point under the nut of the bolt relative to the member the bolt is on. To get the global point, use ToGlobalCoordinates.Transform on this point.

##### Declaration

```
public Point3D PointUnderNut { get; set; }
```

##### Property Value

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Point3D](DesignData.SDS2.Primitives.Point3D.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FRotation)Rotation

The rotation of the bolt

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

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FToGlobalCoordinates)ToGlobalCoordinates

The position and orientation of the bolt in global coordinates.

##### Declaration

```
public Matrix ToGlobalCoordinates { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FToMemberCoordinates)ToMemberCoordinates

The position and orientation of the bolt in member coordinates.

##### Declaration

```
public Matrix ToMemberCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FWasherHeadPrimary)WasherHeadPrimary

Primary washer under the bolt head. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer WasherHeadPrimary { get; }
```

##### Property Value

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FWasherHeadSecondary)WasherHeadSecondary

Secondary washer under the bolt head. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer WasherHeadSecondary { get; }
```

##### Property Value

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FWasherHeadTertiary)WasherHeadTertiary

Tertiary washer under the bolt head. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer WasherHeadTertiary { get; }
```

##### Property Value

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FWasherNutPrimary)WasherNutPrimary

Primary washer under the nut. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer WasherNutPrimary { get; }
```

##### Property Value

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FWasherNutSecondary)WasherNutSecondary

Secondary washer under the nut. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer WasherNutSecondary { get; }
```

##### Property Value

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FWasherNutTertiary)WasherNutTertiary

Tertiary washer under the nut. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer WasherNutTertiary { get; }
```

##### Property Value

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FWashersUnderHead)WashersUnderHead

A list of washers on this bolt under the nut with some positive quantity and non WasherType.None. Note that modifying the list will not add, remove, or re-order the washers on the bolt.

##### Declaration

```
public WasherList WashersUnderHead { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [WasherList](DesignData.SDS2.Model.WasherList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FWashersUnderNut)WashersUnderNut

A list of washers on this bolt under the nut with some positive quantity and non WasherType.None. Note that modifying the list will not add, remove, or re-order the washers on the bolt.

##### Declaration

```
public WasherList WashersUnderNut { get; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [WasherList](DesignData.SDS2.Model.WasherList.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FAddNut)AddNut()

Added a nut into the first free slot. There are two nuts allowed for each bolt, this will find the first of those two that's set to NutType.None and put in a NutType.HeavyHex and return it. If all slots are full, this will return null.

##### Declaration

```
public Nut AddNut()
```

##### Returns

| Type                                  | Description |
| ------------------------------------- | ----------- |
| [Nut](DesignData.SDS2.Model.Nut.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FAddWasherHead)AddWasherHead()

Added a washer into the first free slot. There are three washers allowed for each bolt (ignoring the Quantity field), this will find the first of those three that's set to WasherType.None and put in a WasherType.Hardened or set with quantity 0 and set to a quantity of 1 and return it. If all slots are full, this will return null.

##### Declaration

```
public Washer AddWasherHead()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FAddWasherNut)AddWasherNut()

Added a washer into the first free slot. There are three washers allowed for each bolt (ignoring the Quantity field), this will find the first of those three that's set to WasherType.None and put in a WasherType.Hardened or set with quantity 0 and set to a quantity of 1 and return it. If all slots are full, this will return null.

##### Declaration

```
public Washer AddWasherNut()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FFinalize)\~Bolt()

Describes a bolt fastener: The bolt plus any washers and any nuts.

##### Declaration

```
protected ~Bolt()
```

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FFindMaterialUnderHead)FindMaterialUnderHead()

See documentation for FindMaterialUnderHead, it's the same but this looks under the head not the nut

```
         If there's only one material along the bolt's grip, these will return the same material.

```

##### Declaration

```
public Material FindMaterialUnderHead()
```

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [Material](DesignData.SDS2.Model.Material.html) |             |

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | thrown if this bolt hasn't been added to a member, or it's been added but that hasn't been committed yet. This is a requirement because this needs to know what member the bolt is on to know the global location of the bolt since bolts are always relative to a member's coordinate system. |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FFindMaterialUnderNut)FindMaterialUnderNut()

Scan the space under the bolt's nut to see if there's a material there. If so, regardless of holes, we'll return that and you can set it to MaterialUnderNut if it also passes your checks.

```
         Bolt mybolt;
         mybolt.MaterialUnderNut = mybolt.FindMaterialUnderNut();

```

##### Declaration

```
public Material FindMaterialUnderNut()
```

##### Returns

| Type                                            | Description                                                             |
| ----------------------------------------------- | ----------------------------------------------------------------------- |
| [Material](DesignData.SDS2.Model.Material.html) | true a material if one was found and used. null if none could be found. |

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | thrown if this bolt hasn't been added to a member, or it's been added but that hasn't been committed yet. This is a requirement because this needs to know what member the bolt is on to know the global location of the bolt since bolts are always relative to a member's coordinate system. |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGetNuts)GetNuts()

The list of nuts. This list is a copy, so modifying this list will not remove, add, or reorder nuts. Use AddNut and RemoveNut if you need to do so.

##### Declaration

```
public NutList GetNuts()
```

##### Returns

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [NutList](DesignData.SDS2.Model.NutList.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGetSurface)GetSurface()

The Surface, or polygons, for this bolt, in bolt local coordinates. To get these into global coordinates, transform by the bolt transform, then by the member transform.

##### Declaration

```
public Surface GetSurface()
```

##### Returns

| Type                                               | Description |
| -------------------------------------------------- | ----------- |
| [Surface](DesignData.SDS2.Primitives.Surface.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGetWasherHeadPrimary)GetWasherHeadPrimary()

Primary washer under the bolt head. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer GetWasherHeadPrimary()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGetWasherHeadSecondary)GetWasherHeadSecondary()

Secondary washer under the bolt head. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer GetWasherHeadSecondary()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGetWasherHeadTertiary)GetWasherHeadTertiary()

Tertiary washer under the bolt head. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer GetWasherHeadTertiary()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGetWasherNutPrimary)GetWasherNutPrimary()

Primary washer under the nut. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer GetWasherNutPrimary()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGetWasherNutSecondary)GetWasherNutSecondary()

Secondary washer under the nut. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer GetWasherNutSecondary()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGetWasherNutTertiary)GetWasherNutTertiary()

Tertiary washer under the nut. A washer with WasherType.None indicates there is no washer.

##### Declaration

```
public Washer GetWasherNutTertiary()
```

##### Returns

| Type                                        | Description |
| ------------------------------------------- | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGetWashersUnderHead)GetWashersUnderHead()

A list of washers on this bolt under the nut with some positive quantity and non WasherType.None. Note that modifying the list will not add, remove, or re-order the washers on the bolt.

##### Declaration

```
public WasherList GetWashersUnderHead()
```

##### Returns

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [WasherList](DesignData.SDS2.Model.WasherList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FGetWashersUnderNut)GetWashersUnderNut()

A list of washers on this bolt under the nut with some positive quantity and non WasherType.None. Note that modifying the list will not add, remove, or re-order the washers on the bolt.

##### Declaration

```
public WasherList GetWashersUnderNut()
```

##### Returns

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [WasherList](DesignData.SDS2.Model.WasherList.html) |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FRemoveNut%5FDesignData%5FSDS2%5FModel%5FNut%5F)RemoveNut(Nut)

This will clear the slot represented by the nut passed in.

##### Declaration

```
public void RemoveNut(Nut nut)
```

##### Parameters

| Type                                  | Name | Description |
| ------------------------------------- | ---- | ----------- |
| [Nut](DesignData.SDS2.Model.Nut.html) | nut  |             |

#### [](#DesignData%5FSDS2%5FModel%5FBolt%5FRemoveWasher%5FDesignData%5FSDS2%5FModel%5FWasher%5F)RemoveWasher(Washer)

This will clear the slot represented by the washer passed in.

##### Declaration

```
public void RemoveWasher(Washer washer)
```

##### Parameters

| Type                                        | Name   | Description |
| ------------------------------------------- | ------ | ----------- |
| [Washer](DesignData.SDS2.Model.Washer.html) | washer |             |