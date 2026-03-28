# Class CutFlangeFlush 

For S shapes and W shapes and Wtees, it applies two flange cuts, one on the near side and the other on the far side. Both cut to the web. A zero near side or far side length means no cut is made on that side.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html)

CutFlangeFlush

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
public sealed class CutFlangeFlush : FlangeCutOperation
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FCutFlangeFlush%5F%5Fctor)CutFlangeFlush()

For S shapes and W shapes and Wtees, it applies two flange cuts, one on the near side and the other on the far side. Both cut to the web. A zero near side or far side length means no cut is made on that side.

##### Declaration

```
public CutFlangeFlush()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FCutFlangeFlush%5FLengthFarSide)LengthFarSide

The length to cut back from the end of the flange along the work line for the far side flange cut. 0 for no cut

##### Declaration

```
public LockableDouble LengthFarSide { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

#### [](#DesignData%5FSDS2%5FModel%5FCutFlangeFlush%5FLengthNearSide)LengthNearSide

The length to cut back from the end of the flange along the work line for the near side flange cut. 0 for no cut

##### Declaration

```
public LockableDouble LengthNearSide { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [LockableDouble](DesignData.SDS2.Model.LockableDouble.html) |             |

##### Remarks

If this cut operation is on a material, then lockables are always in a locked state. For members, the locked state matters. When assigning one of these values using a primitive double, it will lock and assign that value. When working directly with the LockableDouble, you will need to lock the value in addition to assigning it to override the system value.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FCutFlangeFlush%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

For S shapes and W shapes and Wtees, it applies two flange cuts, one on the near side and the other on the far side. Both cut to the web. A zero near side or far side length means no cut is made on that side.

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