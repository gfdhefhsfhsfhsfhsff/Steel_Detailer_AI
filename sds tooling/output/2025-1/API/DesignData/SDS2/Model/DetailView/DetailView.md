# Class DetailView 

Information for a member view

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DetailView

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
public sealed class DetailView
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5F%5Fctor)DetailView()

Information for a member view

##### Declaration

```
public DetailView()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FClippingBounds)ClippingBounds

The view clipping bounds, in inches.

##### Declaration

```
public BoundingBox3D ClippingBounds { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [BoundingBox3D](DesignData.SDS2.Primitives.BoundingBox3D.html) |             |

##### Remarks

The maximum coordinate representing no bounds is 240,000 and the minimum is -240,000

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FCutFrom)CutFrom

The view used to cut this view from, or null if not cut from another view

##### Declaration

```
public DetailView CutFrom { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [DetailView](DesignData.SDS2.Model.DetailView.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FIsForced)IsForced

Specifies if the view is forced on the detail

##### Declaration

```
public bool IsForced { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Legacy, i.e. non template, detailing sometimes requires certain system views to be forced before they will be added to a detail.

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FIsInsideClipBox)IsInsideClipBox

Specifies if the view is inside the clipping bounds

##### Declaration

```
public bool IsInsideClipBox { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FIsProjectedFromCutView)IsProjectedFromCutView

Specifies if the view is projected from the CutFrom view

##### Declaration

```
public bool IsProjectedFromCutView { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FIsUserCreated)IsUserCreated

Specifies if the view is user created

##### Declaration

```
public bool IsUserCreated { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FMiscellaneousOffset)MiscellaneousOffset

An offset for the view

##### Declaration

```
public double MiscellaneousOffset { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FProjectionUse)ProjectionUse

Specifies the projected view use

##### Declaration

```
public ViewProjectionUse ProjectionUse { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [ViewProjectionUse](DesignData.SDS2.Model.ViewProjectionUse.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FScale)Scale

The scale of the view

##### Declaration

```
public double Scale { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

The typical scale is 1.0

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FToViewCoordinates)ToViewCoordinates

Matrix, in inches, representing a transformation from global coordinates to view coordinates

##### Declaration

```
public Matrix ToViewCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FViewType)ViewType

Type of the view

##### Declaration

```
public PresetView ViewType { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [PresetView](DesignData.SDS2.Model.PresetView.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FViewUse)ViewUse

Specifies the view use

##### Declaration

```
public ViewUse ViewUse { get; set; }
```

##### Property Value

| Type                                          | Description |
| --------------------------------------------- | ----------- |
| [ViewUse](DesignData.SDS2.Model.ViewUse.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FFinalize)\~DetailView()

Information for a member view

##### Declaration

```
protected ~DetailView()
```

#### [](#DesignData%5FSDS2%5FModel%5FDetailView%5FMemberPreset%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5FDesignData%5FSDS2%5FModel%5FPresetView%5F)MemberPreset(MemberHandle, PresetView)

A view corresponding to the specified member and preset view

##### Declaration

```
public static DetailView MemberPreset(MemberHandle member, PresetView view)
```

##### Parameters

| Type                                                       | Name   | Description |
| ---------------------------------------------------------- | ------ | ----------- |
| [MemberHandle](DesignData.SDS2.Database.MemberHandle.html) | member |             |
| [PresetView](DesignData.SDS2.Model.PresetView.html)        | view   |             |

##### Returns

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [DetailView](DesignData.SDS2.Model.DetailView.html) |             |