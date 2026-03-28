# Class MemberBrief 

Member data that can be rapidly accessed. This is data stored in a fixed length database for each member inside the SDS2 database.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MemberBrief

[Member](DesignData.SDS2.Model.Member.html)

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
public class MemberBrief
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FApproval)Approval

The approval status of this member. See the returned union for values and meanings.

##### Declaration

```
public MemberApproval Approval { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [MemberApproval](DesignData.SDS2.Model.MemberApproval.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FCategory)Category

Get the category for this member.

##### Declaration

```
public CategoryDefinition Category { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [CategoryDefinition](DesignData.SDS2.Setup.CategoryDefinition.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FCustomPropertyMapHandle)CustomPropertyMapHandle

A handle to the custom properties for this member, or null if if member is a standalone member that has not been added to the database.

##### Declaration

```
public CustomPropertyMapHandle CustomPropertyMapHandle { get; }
```

##### Property Value

| Type                                                                             | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [CustomPropertyMapHandle](DesignData.SDS2.Database.CustomPropertyMapHandle.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                       |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the member handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FDoMaterialSurfaceFinishReset)DoMaterialSurfaceFinishReset

Indicates if all of the materials shipping with this member should have their surface finish reset to the finish indicated on the member when a transaction with this member is committed. After committing a transaction this will reset to false. Corresponds the to Reset checkbox on the member edit screen.

##### Declaration

```
public bool DoMaterialSurfaceFinishReset { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FEnds)Ends

Get both ends in a single list, left then right.

##### Declaration

```
public MemberEndBriefList Ends { get; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [MemberEndBriefList](DesignData.SDS2.Model.MemberEndBriefList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FErected)Erected

The date this member was erected at the job site.

##### Declaration

```
public DateTime? Erected { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

##### Remarks

The date returned will always have a time code of midnight. The granularity on this date is just to the day.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FFabricationCompleteDate)FabricationCompleteDate

The date this member's fabrication was completed.

##### Declaration

```
public DateTime? FabricationCompleteDate { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

##### Remarks

The date returned will always have a time code of midnight. The granularity on this date is just to the day.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FFabricationProjectedDate)FabricationProjectedDate

The date this member is projected to complete fabrication in the shop.

##### Declaration

```
public DateTime? FabricationProjectedDate { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

##### Remarks

The date returned will always have a time code of midnight. The granularity on this date is just to the day.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FFabricationShopDate)FabricationShopDate

The date this member detail was sent to the shop (released for fabrication).

##### Declaration

```
public DateTime? FabricationShopDate { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

##### Remarks

The date returned will always have a time code of midnight. The granularity on this date is just to the day.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FGrade)Grade

The grade which will be applied to main material on this member. Applies to all builtin steel member types (beams, columns, braces, etc), and many python member types.

##### Declaration

```
public SteelGrade Grade { get; set; }
```

##### Property Value

| Type                                                | Description                                                           |
| --------------------------------------------------- | --------------------------------------------------------------------- |
| [SteelGrade](DesignData.SDS2.Setup.SteelGrade.html) | If it's a builtin steel member, the grade is returned. Otherwise null |

##### Remarks

This grade must be from the appropriate list for the type of shape currently set on this member. So if you're setting Grade, and Shape, be sure to set Shape first. When Shape is switched to a different type the Grade will be reset to the first in the list

```
         This is not valid for members of type Miscellaneous, see Miscellaneous.Grade
         which overrides and hides this.

```

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                   |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown when attempting to set a grade on a member type that doesn't use this flag, which is pretty much any member that's not a builtin steel member (Beam, Column, Braces) |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html)         | Thrown when attempting to set this grade to null.                                                                                                                           |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FGroupMemberHandle)GroupMemberHandle

A GroupMemberHandle to a group that the member is a submember of or null if the member is not a member of a group.

##### Declaration

```
public GroupMemberHandle GroupMemberHandle { get; }
```

##### Property Value

| Type                                                                 | Description |
| -------------------------------------------------------------------- | ----------- |
| [GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FGuid)Guid

The SDS2 Guid/UUID for this member. Sometimes referred to as the "manufacturing guid"

##### Declaration

```
public Guid? Guid { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [Guid](https://learn.microsoft.com/dotnet/api/system.guid)? |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FHandle)Handle

The database handle for this object

##### Declaration

```
public MemberHandle Handle { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FHeldDate)HeldDate

Get the date when this member was set to held. If this is null then the member is not held. This hold date, if set, shows up on member details.

##### Declaration

```
public DateTime? HeldDate { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

##### Remarks

The date returned will always have a time code of midnight. The granularity on this date is just to the day.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FHeldDescription)HeldDescription

The user description (29 characters or less) of why the held date is set.

##### Declaration

```
public string HeldDescription { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Remarks

This string maxes out at 29 characters, SDS2 will cut off any text after that.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FIsExisting)IsExisting

Tells you whether this member has been marked as pre-existing, meaning already erected, or not.

##### Declaration

```
public bool IsExisting { get; set; }
```

##### Property Value

| Type                                                          | Description                                                      |
| ------------------------------------------------------------- | ---------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | true if the member is pre-existing, false if it is a new member. |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FIsGalvanized)IsGalvanized

Sets the surface finish of all submaterials to galvanized or duplex coating.

##### Declaration

```
public bool IsGalvanized { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FIsHeld)IsHeld

True if the member is being held. Typically this means the drawing is being held from release to the shop.

##### Declaration

```
public bool IsHeld { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FIsMarkedForDetail)IsMarkedForDetail

True if this piecemark (which this member has) needs to be detailed. This flag can be flipped on or off at any time, but special consideration should be given to turning it off. That could cause users to piecemarks with stale drawings that don't match the model.

##### Declaration

```
public bool IsMarkedForDetail { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                                  |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown when attempting to set this property on a standalone member. Since standalone members can't have piecemarks or details attached, you can't flip this flag on or off |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FIsMarkedForNodeMatch)IsMarkedForNodeMatch

True when this member has been shifted and so the node data for it is stale and must be recalculated. False if the node data for this member is up to date.

##### Declaration

```
public bool IsMarkedForNodeMatch { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FIsMarkedForProcess)IsMarkedForProcess

True if this member needs to be processed before it will have solids. False if it has been processed and so the solids are up to date with the inputs on the member.

```
         This can only be set to true.  One which is already set to true
         cannot be set to false, the flag can only be flipped off by
         processing the member.

```

##### Declaration

```
public bool IsMarkedForProcess { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Exceptions

| Type                                                                                   | Condition                                                        |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown when attempting to unset this flag, e.g. set it to false. |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FLeft)Left

Gets the left end of the member. The left end is defined as follows: For columns:

* The end with the lowest Z coordinate value
* If that matches, then the lowest X coordinate
* If those match, then the lowest Y coordinate For all other members:
* The end with the lowest X coordinate value
* If that matches, then the lowest Y coordinate
* If those match, then the lowest Z coordinate

Unless the member has its ends set to swapped, then it's the reverse of that.

##### Declaration

```
public MemberEndBrief Left { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [MemberEndBrief](DesignData.SDS2.Model.MemberEndBrief.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FMemberDescription)MemberDescription

The member description. This can be system generated (descriptions like "COLUMN") or it can be set by users. It can be 19 characters or less.

##### Declaration

```
public string MemberDescription { get; set; }
```

##### Property Value

| Type                                                           | Description             |
| -------------------------------------------------------------- | ----------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | A UTF-8 encoded string. |

##### Remarks

This string maxes out at 19 characters, SDS2 will cut off any text after that.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FMemberType)MemberType

The class type for this Member object, should you request the full member object from the database. This can be compared to the typeof a member to see if it's that member. Example: MemberBrief member\_brief; if(typeof(DesignData.SDS2.Model.Beam) == member\_brief.MemberType) Console.WriteLine("It's a beam!");

##### Declaration

```
public Type MemberType { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [Type](https://learn.microsoft.com/dotnet/api/system.type) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FModelCompleteDate)ModelCompleteDate

Get the date when this member was set to model complete. Model complete means that the member will not be modified anymore inside of the model. This will be null if this member has not been marked model complete.

##### Declaration

```
public DateTime? ModelCompleteDate { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

##### Remarks

The date returned will always have a time code of midnight. The granularity on this date is just to the day.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FModelCompleteMode)ModelCompleteMode

Defines what mode model complete will operate in (or if it will just decide based on setup) when ModelCompleteDate is set to a date

##### Declaration

```
public ModelCompleteMode ModelCompleteMode { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [ModelCompleteMode](DesignData.SDS2.Model.ModelCompleteMode.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FNumber)Number

Member numbers are unique identifiers, within an SDS2 job or project, for members. These are relied upon in many places inside of SDS2 and in generated reports.

##### Declaration

```
public int Number { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FPiecemark)Piecemark

The piecemark of the member.

##### Declaration

```
public string Piecemark { get; }
```

##### Property Value

| Type                                                           | Description             |
| -------------------------------------------------------------- | ----------------------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | A UTF-8 encoded string. |

##### Exceptions

| Type                                                                           | Condition                                                       |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException thrown when the member handle is invalid. |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FProjectedShipDate)ProjectedShipDate

The date this member is projected to ship from the shop.

##### Declaration

```
public DateTime? ProjectedShipDate { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

##### Remarks

The date returned will always have a time code of midnight. The granularity on this date is just to the day.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FReceivedForApproval)ReceivedForApproval

The meaning of this can vary by shop, but generally this is the date the drawings or design calculations were received by an engineer for approval

##### Declaration

```
public DateTime? ReceivedForApproval { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FReceivedOnJobSite)ReceivedOnJobSite

The date this member was received on the job site.

##### Declaration

```
public DateTime? ReceivedOnJobSite { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

##### Remarks

The date returned will always have a time code of midnight. The granularity on this date is just to the day.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FRevision)Revision

Gets the current revision structure for this member

##### Declaration

```
public MemberRevision Revision { get; set; }
```

##### Property Value

| Type                                                        | Description                                      |
| ----------------------------------------------------------- | ------------------------------------------------ |
| [MemberRevision](DesignData.SDS2.Setup.MemberRevision.html) | The revision object associated with this member. |

##### Exceptions

| Type                                                                           | Condition                   |
| ------------------------------------------------------------------------------ | --------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | If the revision set is null |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FRight)Right

Member data that can be rapidly accessed. This is data stored in a fixed length database for each member inside the SDS2 database.

##### Declaration

```
public MemberEndBrief Right { get; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [MemberEndBrief](DesignData.SDS2.Model.MemberEndBrief.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FRoute1)Route1

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

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FRoute2)Route2

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

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FRoute3)Route3

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

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FRoute4)Route4

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

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FSequence)Sequence

The fabrication sequence that this member is in. This same sequence can be found under Sequences on the Database.Job object.

##### Declaration

```
public JobSequence Sequence { get; set; }
```

##### Property Value

| Type                                                  | Description                                         |
| ----------------------------------------------------- | --------------------------------------------------- |
| [JobSequence](DesignData.SDS2.Setup.JobSequence.html) | The JobSequence object associated with this member. |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FShape)Shape

The Shape for the member if the member's main material references a shape in the material file. For members that do not reference a shape in the material file, the value will be null.

##### Declaration

```
public Shape Shape { get; set; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

##### Remarks

If the new Shape is a different type of material then the Grade will be reset to the first Grade in the list for that type of material

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FShipDate)ShipDate

The date this member shipped from shop.

##### Declaration

```
public DateTime? ShipDate { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

##### Remarks

The date returned will always have a time code of midnight. The granularity on this date is just to the day.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FSubmittedForApproval)SubmittedForApproval

The meaning of this can vary by shop, but generally this is the date the drawings or design calculations were sent to an engineer for approval

##### Declaration

```
public DateTime? SubmittedForApproval { get; set; }
```

##### Property Value

| Type                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)? |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FSurfaceFinish)SurfaceFinish

This affects the colors of solid members on erection views in the Drawing Editor.

##### Declaration

```
public SurfaceFinish SurfaceFinish { get; set; }
```

##### Property Value

| Type                                                      | Description |
| --------------------------------------------------------- | ----------- |
| [SurfaceFinish](DesignData.SDS2.Setup.SurfaceFinish.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FSwapEnds)SwapEnds

If true, then the physical left end of the member will be considered the right end on details. This allows two members which are the same except one is rotated differently to get the same piecemark.

##### Declaration

```
public bool SwapEnds { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

The left end is defined based on whether x, y, or z is less (in that order, so if x is less but y is greater, this is the left end) for everything but columns. For columhns it is z, x, y.

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FToGlobalCoordinates)ToGlobalCoordinates

Position and orientation of the member in global coordinates

##### Declaration

```
public Matrix ToGlobalCoordinates { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FAllGroups)AllGroups()

All the GroupMemberHandles where the member is a submember

##### Declaration

```
public GroupMemberHandleList AllGroups()
```

##### Returns

| Type                                                                         | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [GroupMemberHandleList](DesignData.SDS2.Database.GroupMemberHandleList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Member data that can be rapidly accessed. This is data stored in a fixed length database for each member inside the SDS2 database.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FFinalize)\~MemberBrief()

Member data that can be rapidly accessed. This is data stored in a fixed length database for each member inside the SDS2 database.

##### Declaration

```
protected ~MemberBrief()
```

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FGet%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F)Get(MemberHandle)

Get a MemberBrief object for the MemberHandle passed in.

##### Declaration

```
public static MemberBrief Get(MemberHandle memberHandle)
```

##### Parameters

| Type                                                       | Name         | Description |
| ---------------------------------------------------------- | ------------ | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) | memberHandle |             |

##### Returns

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FMemberBrief%5FRefreshDatabaseTable)RefreshDatabaseTable()

Refresh the the primary table for objects of this type.

##### Declaration

```
public static void RefreshDatabaseTable()
```