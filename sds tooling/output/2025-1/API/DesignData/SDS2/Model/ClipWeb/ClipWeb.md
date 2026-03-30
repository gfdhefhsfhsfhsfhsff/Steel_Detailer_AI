# Class ClipWeb 

Clip the web and flange at the corner

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html)

ClipWeb

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
public sealed class ClipWeb : FlangeCutOperation
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FClipWeb%5F%5Fctor)ClipWeb()

Clip the web and flange at the corner

##### Declaration

```
public ClipWeb()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FClipWeb%5FDepth)Depth

The depth of the clip, this is the amount of web removed at the end of the material (the deepest part of the clip)

##### Declaration

```
public LockableDouble Depth { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FClipWeb%5FLength)Length

The length of the clip, along the cut web

##### Declaration

```
public LockableDouble Length { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FClipWeb%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

Clip the web and flange at the corner

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[FlangeCutOperation.Dispose(bool)](DesignData.SDS2.Model.FlangeCutOperation.html#DesignData%5FSDS2%5FModel%5FFlangeCutOperation%5FDispose%5FSystem%5FBoolean%5F)