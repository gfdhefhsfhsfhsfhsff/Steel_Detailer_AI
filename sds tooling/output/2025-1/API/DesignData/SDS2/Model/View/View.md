# Class View 

Data representing a view of the model.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

View

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public sealed class View
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FModel%5FView%5F%5Fctor)View()

Data representing a view of the model.

##### Declaration

```
public View()
```

#### [](#DesignData%5FSDS2%5FModel%5FView%5F%5Fctor%5FDesignData%5FSDS2%5FModel%5FView%5F)View(View)

Data representing a view of the model.

##### Declaration

```
public View(View other)
```

##### Parameters

| Type                                    | Name  | Description |
| --------------------------------------- | ----- | ----------- |
| [View](DesignData.SDS2.Model.View.html) | other |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FView%5FClippingToGlobalCoordinates)ClippingToGlobalCoordinates

Matrix, in inches, representing a transformation from clipping coordinates to global coordinates. The clipping coordinates define a plane in the model in which DepthNear and DepthFar are used to clip solids out of the view.

##### Declaration

```
public Matrix ClippingToGlobalCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FView%5FDepthFar)DepthFar

The distance, in inches, from the origin of the clipping coordinates to the negative Z clipping plane

##### Declaration

```
public double DepthFar { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FView%5FDepthNear)DepthNear

The distance, in inches, from the origin of the clipping coordinates to the positive Z clipping plane

##### Declaration

```
public double DepthNear { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FModel%5FView%5FIsDepthCheckOn)IsDepthCheckOn

Specifies whether the objects in the view are clipped by the DepthNear and DepthFar clipping planes

##### Declaration

```
public bool IsDepthCheckOn { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FModel%5FView%5FToClippingCoordinates)ToClippingCoordinates

Matrix, in inches, representing a transformation from global coordinates to the clipping coordinates. The clipping coordinates define a plane in the model in which DepthNear and DepthFar are used to clip solids out of the view.

##### Declaration

```
public Matrix ToClippingCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FView%5FToGlobalCoordinates)ToGlobalCoordinates

Matrix, in inches, representing a transformation from view coordinates to global coordinates

##### Declaration

```
public Matrix ToGlobalCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FView%5FToViewCoordinates)ToViewCoordinates

Matrix, in inches, representing a transformation from global coordinates to the view coordinates

##### Declaration

```
public Matrix ToViewCoordinates { get; set; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Matrix](DesignData.SDS2.Primitives.Matrix.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FView%5FViewableArea)ViewableArea

Area of view coordinates that is visable

##### Declaration

```
public BoundingBox2D ViewableArea { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [BoundingBox2D](DesignData.SDS2.Primitives.BoundingBox2D.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FView%5FEquals%5FSystem%5FObject%5F)Equals(object)

Data representing a view of the model.

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

#### [](#DesignData%5FSDS2%5FModel%5FView%5FFinalize)\~View()

Data representing a view of the model.

##### Declaration

```
protected ~View()
```

#### [](#DesignData%5FSDS2%5FModel%5FView%5FGetHashCode)GetHashCode()

Data representing a view of the model.

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