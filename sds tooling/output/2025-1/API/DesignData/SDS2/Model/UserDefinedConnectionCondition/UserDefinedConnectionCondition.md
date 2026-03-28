# Class UserDefinedConnectionCondition 

These settings describe the condition you expect this user defined connection to apply. It's possible it will apply in other conditions, but generally you want to target this to the situation where it will be applied. A wide flange beam framed to a column, for example.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

UserDefinedConnectionCondition

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
public sealed class UserDefinedConnectionCondition
```

##### **Remarks**

Each property describes when it applies in the documentation here, failing to set some just results in defaults, and setting ones which don't apply won't result in an error. So you should be able to set what makes sense for the condition you're interested in and ignore the rest.

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FBraceRotation)BraceRotation

The orientation of a vertical or horizontal brace, whether it's long leg/web vertical or horizontal

##### Declaration

```
public BraceRotationType BraceRotation { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [BraceRotationType](DesignData.SDS2.Model.BraceRotationType.html) |             |

##### Remarks

Only applies if the MemberType is VerticalBrace and MaterialType is WTee, WideFlange, WeldedWideFlange, SFlange, or STee

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FEmbed)Embed

The embed plate used for a concrete connection

##### Declaration

```
public Embed Embed { get; set; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Embed](DesignData.SDS2.Setup.Embed.html) |             |

##### Remarks

Only applies if MemberType is Beam and FramesToConcreteWall is true

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FFramesToConcreteWall)FramesToConcreteWall

Whether the connection is to a concrete wall or not

##### Declaration

```
public bool FramesToConcreteWall { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Only applies if MemberType is either Beam or Joist

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FHorizontalBracePlateType)HorizontalBracePlateType

Describes the gusset plate conditions if this is a horizontal brace connection (MemberType)

##### Declaration

```
public HorizontalBracePlateType HorizontalBracePlateType { get; set; }
```

##### Property Value

| Type                                                                            | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [HorizontalBracePlateType](DesignData.SDS2.Model.HorizontalBracePlateType.html) |             |

##### Remarks

Only applies if MemberType is HorizontalBrace

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FIsDoubleMaterial)IsDoubleMaterial

If MaterialType is one which SDS2 can double up, setting this to true will apply when that material is double and not single.

##### Declaration

```
public bool IsDoubleMaterial { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Only applies if MemberType is VerticalBrace or HorizontalBrace and MaterialType is Angle

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FMaterialType)MaterialType

The material type of the main material of the supported member, or the member the connection would be applied to.

##### Declaration

```
public MaterialType MaterialType { get; set; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [MaterialType](DesignData.SDS2.Setup.MaterialType.html) |             |

##### Remarks

Each property describes when it applies in the documentation here, failing to set some just results in defaults, and setting ones which don't apply won't result in an error. So you should be able to set what makes sense for the condition you're interested in and ignore the rest.

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FMemberType)MemberType

The member type supported, or the member type this connection would be applied to.

##### Declaration

```
public MemberType MemberType { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [MemberType](DesignData.SDS2.Setup.MemberType.html) |             |

##### Remarks

Each property describes when it applies in the documentation here, failing to set some just results in defaults, and setting ones which don't apply won't result in an error. So you should be able to set what makes sense for the condition you're interested in and ignore the rest.

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FSideOfGusset)SideOfGusset

The side of the gusset the brace would be on

##### Declaration

```
public ToeIO SideOfGusset { get; set; }
```

##### Property Value

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [ToeIO](DesignData.SDS2.Model.ToeIO.html) |             |

##### Remarks

Only applies if MemberType is VerticalBrace or HorizontalBrace and MaterialType is Angle. BothSides is only valid if DoubleMaterial is true.

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FVerticalBracePlateType)VerticalBracePlateType

Describes the gusset plate conditions if this is a vertical brace connection (MemberType)

##### Declaration

```
public VerticalBracePlateType VerticalBracePlateType { get; set; }
```

##### Property Value

| Type                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [VerticalBracePlateType](DesignData.SDS2.Model.VerticalBracePlateType.html) |             |

##### Remarks

Only applies if MemberType is VerticalBrace. If you look at the graphical user interface for in user defined connection edit for this property, you'll also see a wide flange variant. This is the same one, both of those fields in that screen store their value in the same place.

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FWebRotation)WebRotation

Describes how the end of the beam is rotates to meet up to the supporting member. These options have different meaning depending on if it's a column or beam supporting it.

##### Declaration

```
public MemberEndRotationType WebRotation { get; set; }
```

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [MemberEndRotationType](DesignData.SDS2.Model.MemberEndRotationType.html) |             |

##### Remarks

Only applies if MemberType is Beam

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FUserDefinedConnectionCondition%5FFinalize)\~UserDefinedConnectionCondition()

These settings describe the condition you expect this user defined connection to apply. It's possible it will apply in other conditions, but generally you want to target this to the situation where it will be applied. A wide flange beam framed to a column, for example.

##### Declaration

```
protected ~UserDefinedConnectionCondition()
```

##### Remarks

Each property describes when it applies in the documentation here, failing to set some just results in defaults, and setting ones which don't apply won't result in an error. So you should be able to set what makes sense for the condition you're interested in and ignore the rest.