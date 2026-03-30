# Class BoltMatchSpecification 

This is a spec of options you can change when matching bolts, on the resulting bolts. Options you find on Bolt, but not here, are options we don't support changing during bolt match.

```
         Once you've got the options set, pass this to the Fasten function to create bolts
         which fasten 2 or more pieces of material.

         All options default to null.  If an option is null, then you will get the default
         value which is generally inherited from the holes that are bolted, or from setup.

```

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

BoltMatchSpecification

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
public sealed class BoltMatchSpecification
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5F%5Fctor)BoltMatchSpecification()

Create an default BoltMatchSpecification

##### Declaration

```
public BoltMatchSpecification()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FBoltType)BoltType

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

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FBreakoutNutAndWasherOnBill)BreakoutNutAndWasherOnBill

If true, then nuts and washers are broken out into their own lines on the bill of material.

##### Declaration

```
public bool? BreakoutNutAndWasherOnBill { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)? |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FCombineMaterialPlateWashers)CombineMaterialPlateWashers

If true, then washers will be combined based on the PlateWasherCombinationMethod setting. If false, then each bolt will get its own plate washer.

##### Declaration

```
public bool? CombineMaterialPlateWashers { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)? |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FDiameter)Diameter

The diameter of the bolt shaft.

##### Declaration

```
public double? Diameter { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double)? |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FFinish)Finish

The finish type of the bolt

##### Declaration

```
public BoltFinish? Finish { get; set; }
```

##### Property Value

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [BoltFinish](DesignData.SDS2.Model.BoltFinish.html)? |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FIsFieldBolt)IsFieldBolt

True if this is a bolt to be installed in the field, false if it's to be installed in the shop

##### Declaration

```
public bool? IsFieldBolt { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)? |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FIsFirstMaterialUnderHead)IsFirstMaterialUnderHead

Decide whether the bolt head or nut should be on the first material passed into Fasten. If true, then the head will be on the side fastening the first material in the list. If false, then the nut will be.

```
         If the first material is not one either side (for example, the
         middle plate of 3 plates bolted together), then this field has no
         meaning and will not have any effect.  And the bolt direction
         will be consistent among all the bolts returned, but which
         direction that will be is undefined.

```

##### Declaration

```
public bool IsFirstMaterialUnderHead { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FIsTensionControl)IsTensionControl

True if this is a tension control bolt

##### Declaration

```
public bool? IsTensionControl { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean)? |             |

##### Exceptions

| Type                                                                     | Condition                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)   | Thrown when setting data on the object without having added it to a transaction                       |
| [NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html) | Thrown when reading or writing the property of a bolt that was added to a transaction but is unlocked |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FFasten%5FDesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FDesignData%5FSDS2%5FModel%5FMaterialList%5F)Fasten(BoltMatchSpecification, MaterialList)

Given a bolt spec, and a list of materials (with at least 2 materials in it) this will search for holes between any pairing of materials that match up, and fasten those material using those matched holes with bolts of the correct calculated length, and diameters based on the hole settings.

```
         This must be called with an existing Transaction.  This will
         call Transaction.Lock().

         The bolts will be added to the member that the first material in
         matchHolesOn is on.

```

##### Declaration

```
public static BoltList Fasten(BoltMatchSpecification specification, MaterialList matchHolesOn)
```

##### Parameters

| Type                                                                        | Name          | Description |
| --------------------------------------------------------------------------- | ------------- | ----------- |
| [BoltMatchSpecification](DesignData.SDS2.Model.BoltMatchSpecification.html) | specification |             |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html)                     | matchHolesOn  |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltList](DesignData.SDS2.Model.BoltList.html) |             |

##### Exceptions

| Type                                                                                   | Condition                                                   |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown if this is called outside of a writable Transaction. |

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FFasten%5FDesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FDesignData%5FSDS2%5FModel%5FMaterialList%5FDesignData%5FSDS2%5FModel%5FHoleList%5F)Fasten(BoltMatchSpecification, MaterialList, HoleList)

Same as the other overload of Fasten, except here you list the holes you want to be matched, no other holes are bolted through. These holes MUST BE ON THE FIRST MATERIAL IN matchHolesOn.

##### Declaration

```
public static BoltList Fasten(BoltMatchSpecification specification, MaterialList matchHolesOn, HoleList onlyMatchTheseHoles)
```

##### Parameters

| Type                                                                        | Name                | Description |
| --------------------------------------------------------------------------- | ------------------- | ----------- |
| [BoltMatchSpecification](DesignData.SDS2.Model.BoltMatchSpecification.html) | specification       |             |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html)                     | matchHolesOn        |             |
| [HoleList](DesignData.SDS2.Model.HoleList.html)                             | onlyMatchTheseHoles |             |

##### Returns

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltList](DesignData.SDS2.Model.BoltList.html) |             |

##### Exceptions

| Type                                                                                   | Condition                                                   |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown if this is called outside of a writable Transaction. |

#### [](#DesignData%5FSDS2%5FModel%5FBoltMatchSpecification%5FFinalize)\~BoltMatchSpecification()

This is a spec of options you can change when matching bolts, on the resulting bolts. Options you find on Bolt, but not here, are options we don't support changing during bolt match.

```
         Once you've got the options set, pass this to the Fasten function to create bolts
         which fasten 2 or more pieces of material.

         All options default to null.  If an option is null, then you will get the default
         value which is generally inherited from the holes that are bolted, or from setup.

```

##### Declaration

```
protected ~BoltMatchSpecification()
```