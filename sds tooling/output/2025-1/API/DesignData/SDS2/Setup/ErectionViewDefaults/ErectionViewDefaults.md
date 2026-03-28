# Class ErectionViewDefaults 

Setup options for erection view detail drawings.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

ErectionViewDefaults

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public sealed class ErectionViewDefaults
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5F%5Fctor)ErectionViewDefaults()

Setup options for erection view detail drawings.

##### Declaration

```
public ErectionViewDefaults()
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FAddDimensionToSectionViewGrids)AddDimensionToSectionViewGrids

Applies when AnnotateErectionViews is true. When true, an overall dimension is added when 3 or more grid lines have been dimensioned in the elevation view. The overall dimension reports the sum of the dimensions that are below or to the right of the structure.

##### Declaration

```
public bool AddDimensionToSectionViewGrids { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FAddOverallDimensionBottomRight)AddOverallDimensionBottomRight

Applies when DimensionGridsBottomRight is true. When true, an overall dimension is added where applicable.

##### Declaration

```
public bool AddOverallDimensionBottomRight { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FAddOverallDimensionTopLeft)AddOverallDimensionTopLeft

Applies when DimensionGridsTopLeft is true. When true, an overall dimension is added where applicable.

##### Declaration

```
public bool AddOverallDimensionTopLeft { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FAllowBreakLinesAndWireMemEdges)AllowBreakLinesAndWireMemEdges

Controls if a member's piecemark, section size, camber, left/right end elevation, and ABM page-line will be allowed to break lines and wire member edges.

##### Declaration

```
public bool AllowBreakLinesAndWireMemEdges { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FAnchorBoltScale)AnchorBoltScale

Applies when ScaleAnchorBoltLayout is true. The normal Drawing Scale of the erection view is multiplied by this factor to scale the base plates, their anchor bolt holes, and their columns' cross sections. Dimension labels and other labels remain their same size, and their text is frozen. A scale change does _not_ reposition the center of a column or its base plate.

##### Declaration

```
public double AnchorBoltScale { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FAnnotateErectionViews)AnnotateErectionViews

When set to true, a label will be generated with the name of the to-be-detailed erection view, grid lines will be dimensioned, and/or the elevation of a plan view will be shown.

##### Declaration

```
public bool AnnotateErectionViews { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FAnnotateFiniteGridLinesInPlace)AnnotateFiniteGridLinesInPlace

Applies when AnnotateErectionViews is true. When true, grid lines that are set to "Finite" in Modeling will be drawn similar to how they are shown in Modeling.

##### Declaration

```
public bool AnnotateFiniteGridLinesInPlace { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FBottomOfBasePlatePrefix)BottomOfBasePlatePrefix

String for noting the elevation of the bottom of base plates on an anchor bolt layout.

##### Declaration

```
public string BottomOfBasePlatePrefix { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FBubblePlacementOnPrimary)BubblePlacementOnPrimary

Applies when AnnotateErectionViews is true. When false, secondary grid markers are shown below the primary dimension line. When true, markers are shown above the placement line.

##### Declaration

```
public bool BubblePlacementOnPrimary { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FCheckPiecemarkOverwriting)CheckPiecemarkOverwriting

Controls if auto detailing will find piecemarks/section sizes that overlap and move them if possible.

##### Declaration

```
public bool CheckPiecemarkOverwriting { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FConcreteHatchingScale)ConcreteHatchingScale

A (positive) number specifying the scale of concrete hatches.

##### Declaration

```
public double ConcreteHatchingScale { get; set; }
```

##### Property Value

| Type                                                           | Description                                                                                                                            |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) | Smaller numbers generate denser hatches with smaller triangles. The size of the triangles is in direct proportion to the chosen scale. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FConcreteStyle)ConcreteStyle

Sets how concrete is drawn in the erection view.

##### Declaration

```
public DrawingStyle ConcreteStyle { get; set; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [DrawingStyle](DesignData.SDS2.Setup.DrawingStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FDetailRevisions)DetailRevisions

Applies to to-be-detailed erection views that have already been placed on erection sheets. When true, revision annotations (clouds, etc.) are added to the detail.

##### Declaration

```
public bool DetailRevisions { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FDimensionAnchorBoltLayout)DimensionAnchorBoltLayout

Applies to Member style. Does not apply to isometric views. The view being detailed must be a plan view or a partial plan view that shows columns with base plates. When true, holes in base plates on columns in any plan views selected will be dimensioned.

##### Declaration

```
public bool DimensionAnchorBoltLayout { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FDimensionGridsBottomRight)DimensionGridsBottomRight

Applies when AnnotateErectionViews is true. When true, straight grid lines will be dimensioned below and to the right of structural members that appear in the to-be-detailed erection view.

##### Declaration

```
public bool DimensionGridsBottomRight { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FDimensionGridsTopLeft)DimensionGridsTopLeft

Applies when AnnotateErectionViews is true.

##### Declaration

```
public bool DimensionGridsTopLeft { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                    |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, straight grid lines will be dimensioned above and to the lef of structural members that appear in the to-be-detailed erection view. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FDrawEachRebarThreshold)DrawEachRebarThreshold

The number of rebar in any one direction. If the number is less than the number of rebar runs, a rebar run symbol is generated. If it is greater than or equal to the number of rebar runs, individual rebars are shown in the erection view.

##### Declaration

```
public int DrawEachRebarThreshold { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FElevationDisplayOnMember)ElevationDisplayOnMember

Applies when AnnotateErectionViews is true. Controls how elevation is displayed for a member.

##### Declaration

```
public ElevationDisplayMode ElevationDisplayOnMember { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [ElevationDisplayMode](DesignData.SDS2.Setup.ElevationDisplayMode.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionDenoteNonstandardMaterial)ErectionDenoteNonstandardMaterial

Applies to members whose main material has been assigned a wide flange, plate, tee, channel, angle, pipe, or tube steel grade that has a "Nonstandard Notation" entered on its setup table. When true, members on erection views whose auto detailing is controlled by this view are permitted to have a nonstandard notation printed with their section size.

##### Declaration

```
public bool ErectionDenoteNonstandardMaterial { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionEndReactionsAuto)ErectionEndReactionsAuto

Setup options for erection view detail drawings.

##### Declaration

```
public bool ErectionEndReactionsAuto { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionEndReactionsUser)ErectionEndReactionsUser

Setup options for erection view detail drawings.

##### Declaration

```
public bool ErectionEndReactionsUser { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionShowCamber)ErectionShowCamber

Affects the display of camber on beams. When true, beams with their Rolling Operation set to "Camber Annotation" or "Camber (Both)" will have their mid-ordinate value reported as camber on the to-be-detailed erection view selected.

##### Declaration

```
public bool ErectionShowCamber { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionShowConnectionCubes)ErectionShowConnectionCubes

Controls if connection cubes are called out on the to-be-detailed erection view.

##### Declaration

```
public bool ErectionShowConnectionCubes { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionShowCustomProperties)ErectionShowCustomProperties

Controls if member custom property values will be shown on appropriate members displayed in the erection view.

##### Declaration

```
public bool ErectionShowCustomProperties { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionShowEndReactions)ErectionShowEndReactions

Setup options for erection view detail drawings.

##### Declaration

```
public bool ErectionShowEndReactions { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionShowFieldWelds)ErectionShowFieldWelds

Controls if field welds are called out on the to-be-detailed erection view.

##### Declaration

```
public bool ErectionShowFieldWelds { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionShowMemberNumber)ErectionShowMemberNumber

Controls if the erection view will append the member number for each piecemark that is shown on the to-be-detailed erection view.

##### Declaration

```
public bool ErectionShowMemberNumber { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionShowNonstandardFieldBolts)ErectionShowNonstandardFieldBolts

Controls if non-standard field bolts are called out on the to-be-detailed erection view.

##### Declaration

```
public bool ErectionShowNonstandardFieldBolts { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionShowSectionSizeOnCustomMembers)ErectionShowSectionSizeOnCustomMembers

Applies when the plugin code of a custom member includes the GetSectionSize method. When true, the section sizes of custom members on the erection view will be displayed on the relevant erection view drawings.

##### Declaration

```
public bool ErectionShowSectionSizeOnCustomMembers { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FErectionShowStudCountOnMember)ErectionShowStudCountOnMember

Applies to beams on erection view drawings. When true, and when "Number of studs" are entered on the Beam Edit window, view will include the number of studs that are entered. The shear stud count will be a part of the section size.

##### Declaration

```
public bool ErectionShowStudCountOnMember { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FExistingMemberLineType)ExistingMemberLineType

Sets the style of line drawing to use.

##### Declaration

```
public LineType ExistingMemberLineType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [LineType](DesignData.SDS2.Setup.LineType.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FExistingMemberPenType)ExistingMemberPenType

An index into a list of preset colors to use for line drawing.

##### Declaration

```
public int ExistingMemberPenType { get; set; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FExplodedErectionView)ExplodedErectionView

When true, views which show members with defined exploded view positions will be detailed so that they depict those members in their exploded positions. When false, members in the to-be-detailed erection views will be shown in their actual, unexploded locations.

##### Declaration

```
public bool ExplodedErectionView { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FFieldWeldLengthDisplayMode)FieldWeldLengthDisplayMode

Applies when ErectionShowFieldWelds is true. Controls if weld lengths are shown on the to-be-detailed erection view.

##### Declaration

```
public FieldWeldLengthDisplaySetting FieldWeldLengthDisplayMode { get; set; }
```

##### Property Value

| Type                                                                                      | Description |
| ----------------------------------------------------------------------------------------- | ----------- |
| [FieldWeldLengthDisplaySetting](DesignData.SDS2.Setup.FieldWeldLengthDisplaySetting.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FGenerateNamedLocations)GenerateNamedLocations

When true, each resulting erection view drawing will include named locations. These named locations will be invisible unless you use a template development tool such as Mark Named Locations, Nearest Names, or Find Property.

##### Declaration

```
public bool GenerateNamedLocations { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FGridBubbleLabelHeight)GridBubbleLabelHeight

The actual height (in millimeters) of grid marker labels.

##### Declaration

```
public double GridBubbleLabelHeight { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FHiddenLineStyle)HiddenLineStyle

Sets how hidden lines are drawn. Only applies when member style is "Wire" or "StickAndWire".

##### Declaration

```
public LineDrawingStyle HiddenLineStyle { get; set; }
```

##### Property Value

| Type                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [LineDrawingStyle](DesignData.SDS2.Setup.LineDrawingStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FHideJoistPiecemarks)HideJoistPiecemarks

Controls if Joist piecemarks will appear on the erection view.

##### Declaration

```
public bool HideJoistPiecemarks { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FMemberStyle)MemberStyle

Sets how steel is drawn in the erection view.

##### Declaration

```
public DrawingStyle MemberStyle { get; set; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [DrawingStyle](DesignData.SDS2.Setup.DrawingStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FMinPiecemarkAndSectionSizeHeight)MinPiecemarkAndSectionSizeHeight

The minimum character height (in millimeters) of piecemarks and section sizes on drawings.

##### Declaration

```
public double MinPiecemarkAndSectionSizeHeight { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FMoveGridLinesForCranePlacement)MoveGridLinesForCranePlacement

Applies when AnnotateErectionViews is enabled.

##### Declaration

```
public bool MoveGridLinesForCranePlacement { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                                                                             |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, grid lines and their associated dimensions will be moved to clear crane placements that appear in the to-be-detailed erection view. When false, grid lines and dimensions will not be moved. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FNewNonSectionPiecemarkStyle)NewNonSectionPiecemarkStyle

Controls the show style of non-cross section piecemarks that are to be detailed for the first time.

##### Declaration

```
public ShowStyle NewNonSectionPiecemarkStyle { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShowStyle](DesignData.SDS2.Setup.ShowStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FNewNonSectionSizeStyle)NewNonSectionSizeStyle

Controls the show style of non-cross section sizes that are to be detailed for the first time.

##### Declaration

```
public ShowStyle NewNonSectionSizeStyle { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShowStyle](DesignData.SDS2.Setup.ShowStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FNewSectionPiecemarkStyle)NewSectionPiecemarkStyle

Controls the show style of piecemarks that are to be detailed for the first time

##### Declaration

```
public ShowStyle NewSectionPiecemarkStyle { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShowStyle](DesignData.SDS2.Setup.ShowStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FNewSectionSizeStyle)NewSectionSizeStyle

Controls the show style of cross section sizes that are to be detailed for the first time.

##### Declaration

```
public ShowStyle NewSectionSizeStyle { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShowStyle](DesignData.SDS2.Setup.ShowStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FNonPlanarHorizontalBraceShowStyle)NonPlanarHorizontalBraceShowStyle

Sets the ShowStyle for horizontal braces that slope out of an elevation view.

##### Declaration

```
public ShowStyle NonPlanarHorizontalBraceShowStyle { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShowStyle](DesignData.SDS2.Setup.ShowStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FNonPlanarVerticalBraceShowStyle)NonPlanarVerticalBraceShowStyle

Sets the ShowStyle for vertical braces that slope out of a plan view.

##### Declaration

```
public ShowStyle NonPlanarVerticalBraceShowStyle { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShowStyle](DesignData.SDS2.Setup.ShowStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FOldNonSectionPiecemarkStyle)OldNonSectionPiecemarkStyle

Controls the show style of already detailed non-cross section piecemarks that are to be detailed again.

##### Declaration

```
public ShowStyle OldNonSectionPiecemarkStyle { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShowStyle](DesignData.SDS2.Setup.ShowStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FOldNonSectionSizeStyle)OldNonSectionSizeStyle

Controls the show style of already detailed non-cross section sizes that are to be detailed again.

##### Declaration

```
public ShowStyle OldNonSectionSizeStyle { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShowStyle](DesignData.SDS2.Setup.ShowStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FOldSectionPiecemarkStyle)OldSectionPiecemarkStyle

Controls the show style of already detailed piecemarks that are to be detailed again.

##### Declaration

```
public ShowStyle OldSectionPiecemarkStyle { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShowStyle](DesignData.SDS2.Setup.ShowStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FOldSectionSizeStyle)OldSectionSizeStyle

Controls the show style of already detailed cross section sizes that are to be detailed again.

##### Declaration

```
public ShowStyle OldSectionSizeStyle { get; set; }
```

##### Property Value

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShowStyle](DesignData.SDS2.Setup.ShowStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FRebarMaterialStyle)RebarMaterialStyle

Sets how rebar material is drawn in the erection view. Only applies when concrete style is _not_ "Stick".

##### Declaration

```
public DrawingStyle RebarMaterialStyle { get; set; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [DrawingStyle](DesignData.SDS2.Setup.DrawingStyle.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FRelocatePiecemarks)RelocatePiecemarks

Controls if piecemarks, section sizes, camber, left/right elevation, shared elevation and member custom properties that have been moved will be automatically moved back to the location specified in Erection View Member Labels.

##### Declaration

```
public bool RelocatePiecemarks { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FRemoveAnnotations)RemoveAnnotations

Applies when erection view has been detailed and you now want to update it with changes from the 3D model.

##### Declaration

```
public RemoveAnnotationsMode RemoveAnnotations { get; set; }
```

##### Property Value

| Type                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [RemoveAnnotationsMode](DesignData.SDS2.Setup.RemoveAnnotationsMode.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FResetMemberLinePens)ResetMemberLinePens

Applies to already detailed erection views that you now want to update with changes from the 3D model where the member style is "Stick" or "StickAndWire".

##### Declaration

```
public bool ResetMemberLinePens { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, the auto detailing program applies the member pen color in Drawing Presentation to all stick member lines shown in the to-be-detailed erection view. When false, the pen number that was assigned to member lines during Erection View Cleanup is retained. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FScaleAnchorBoltLayout)ScaleAnchorBoltLayout

Applies when DimensionAnchorBoltLayout is true. When true, an anchor bolt layout can be scaled up based on the AnchorBoltScale property. The centers of columns and base plates are not affected by the scale factor. Dimension labels remain the same. Base plates, hole diameters and column cross sections are depicted per the scale factor.

##### Declaration

```
public bool ScaleAnchorBoltLayout { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowBasePlateElevationBottomAsRef)ShowBasePlateElevationBottomAsRef

Applies when DimensionAnchorBoltLayout is true. When true, the drawing notes the difference between the Reference Elevation and the bottom-of-base-plate elevation for each of those same base plates. When false, the resulting drawing notes the true elevation of the bottom surface of each base plate that is at an elevation other than the Reference Elevation of the plan view (Absolute).

##### Declaration

```
public bool ShowBasePlateElevationBottomAsRef { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowBasePlateMinorPiecemarks)ShowBasePlateMinorPiecemarks

Applies when DimensionAnchorBoltLayout is true. Controls if auto detailing will draw an anchor bolt layout that shows the submaterial piecemark on each base plate.

##### Declaration

```
public bool ShowBasePlateMinorPiecemarks { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowConcreteHatching)ShowConcreteHatching

Sets if hatches are shown on concrete.

##### Declaration

```
public bool ShowConcreteHatching { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowCranePlacement)ShowCranePlacement

Sets if crane placements are shown in the erection view.

##### Declaration

```
public bool ShowCranePlacement { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowFieldBolts)ShowFieldBolts

Applies when member style is "Wire" or "Solid" or "StickAndWire".

##### Declaration

```
public bool ShowFieldBolts { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                              |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, field bolts will be drawn on the to-be-detailed erection view. When false, field bolts will not be drawn on the to-be-detailed erection view. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowFieldWelds)ShowFieldWelds

Applies when member style is "Wire" or "Solid" or "StickAndWire".

##### Declaration

```
public bool ShowFieldWelds { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                              |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, field welds will be drawn on the to-be-detailed erection view. When false, field welds will not be drawn on the to-be-detailed erection view. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowGridNamesOnNonPlanView)ShowGridNamesOnNonPlanView

Applies when AnnotateErectionViews is true. When true, the names of the erection views will be displayed above the elevations associated with those views.

##### Declaration

```
public bool ShowGridNamesOnNonPlanView { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowHoles)ShowHoles

Applies when member style is "Wire" or "Solid" or "StickAndWire".

##### Declaration

```
public bool ShowHoles { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                  |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, holes will be drawn on the to-be-detailed erection view. When false, holes will not be drawn on the to-be-detailed erection view. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowMainMemberMaterial)ShowMainMemberMaterial

Applies when member style is "Wire" or "Solid" or "StickAndWire".

##### Declaration

```
public bool ShowMainMemberMaterial { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                                          |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, member main material is show on the to-be-detailed erection view. When false, member main material will not be drawn on the to-be-detailed erection view. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowNewNonSectionPiecemarks)ShowNewNonSectionPiecemarks

Controls if new non-cross section piecemarks will be shown on the to-be-detailed erection view.

##### Declaration

```
public bool ShowNewNonSectionPiecemarks { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowNewNonSectionSizes)ShowNewNonSectionSizes

Controls if new non-cross section sizes will be shown on the to-be-detailed erection view.

##### Declaration

```
public bool ShowNewNonSectionSizes { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowNewSectionPiecemarks)ShowNewSectionPiecemarks

Controls if new cross section piecemarks will be shown on the to-be-detailed erection views.

##### Declaration

```
public bool ShowNewSectionPiecemarks { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowNewSectionSizes)ShowNewSectionSizes

Controls if new cross section sizes will be shown on the to-be-detailed erection view.

##### Declaration

```
public bool ShowNewSectionSizes { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowShearTabLocation)ShowShearTabLocation

Applies when member style is "Stick".

##### Declaration

```
public bool ShowShearTabLocation { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                                                                             |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, the location of shear plates (shear tabs) is shown using shear plate side indicators on the ends of beams that have such connections. When false, the location of shear plates is not shown. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowShopBolts)ShowShopBolts

Applies when member style is "Wire" or "Solid" or "StickAndWire".

##### Declaration

```
public bool ShowShopBolts { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                            |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, shop bolts will be drawn on the to-be-detailed erection view. When false, shop bolts will not be drawn on the to-be-detailed erection view. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowShopWelds)ShowShopWelds

Applies when member style is "Wire" or "Solid" or "StickAndWire".

##### Declaration

```
public bool ShowShopWelds { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                            |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, shop welds will be drawn on the to-be-detailed erection view. When false, shop welds will not be drawn on the to-be-detailed erection view. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowStairOutline)ShowStairOutline

Applies when member style is "Stick".

##### Declaration

```
public bool ShowStairOutline { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                                                            |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, an outline of the stair's stringers, risers, and tread nosings is shown in addition to the stair memeber line. When false, stairs are represented by the stair member line. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowSteelLaydown)ShowSteelLaydown

Sets if crane placement's furthest laydown point is shown in the erection view.

##### Declaration

```
public bool ShowSteelLaydown { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FShowSubMaterial)ShowSubMaterial

Applies when member style is "Wire" or "Solid" or "StickAndWire".

##### Declaration

```
public bool ShowSubMaterial { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                            |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, connection materials will be drawn on the to-be-detailed erection view. When false, connection materials will not be drawn. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FUseExistingMemberLineType)UseExistingMemberLineType

Applies to the lines that are drawn to depict an "Existing member" when the member style is "Stick" or "Wire" or "StickAndWire".

##### Declaration

```
public bool UseExistingMemberLineType { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                                                      |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, members that have the status of "Existing" will be drawn with the line type that is selected. When false, members that are "Existing" will be drawn with solid lines. |

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FUseExistingMemberPen)UseExistingMemberPen

Applies to lines that are drawn to depict an "existing member" when the member style is "Stick" or "Wire" or "StickAndWire".

##### Declaration

```
public bool UseExistingMemberPen { get; set; }
```

##### Property Value

| Type                                                          | Description                                                                                                                                                                                                             |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | When true, members that have the status of "Existing" will be drawn with the pen number that is selected. When false, members that are "Existing" will be drawn using the member pen color set in Drawing Presentation. |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FErectionViewDefaults%5FFinalize)\~ErectionViewDefaults()

Setup options for erection view detail drawings.

##### Declaration

```
protected ~ErectionViewDefaults()
```