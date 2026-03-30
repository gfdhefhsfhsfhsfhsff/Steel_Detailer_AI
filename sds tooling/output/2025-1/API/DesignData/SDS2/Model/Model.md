# Namespace DesignData.SDS2.Model 

### [](#classes)Classes 

#### [](#angle)[Angle](DesignData.SDS2.Model.Angle.html)

An angle material

#### [](#autostandardspecification)[AutoStandardSpecification](DesignData.SDS2.Model.AutoStandardSpecification.html)

An auto standard connection tells the system to use the auto standard system to determine what type of connection to use based on the framing situation.

#### [](#beadedflat)[BeadedFlat](DesignData.SDS2.Model.BeadedFlat.html)

A beaded flat material

#### [](#beam)[Beam](DesignData.SDS2.Model.Beam.html)

A builtin steel beam member.

#### [](#beamend)[BeamEnd](DesignData.SDS2.Model.BeamEnd.html)

Beam specific end options

#### [](#beamendlist)[BeamEndList](DesignData.SDS2.Model.BeamEndList.html)

#### [](#beamendlist-beamendlistenumerator)[BeamEndList.BeamEndListEnumerator](DesignData.SDS2.Model.BeamEndList.BeamEndListEnumerator.html)

#### [](#bearingspecification)[BearingSpecification](DesignData.SDS2.Model.BearingSpecification.html)

A bearing connection specification

#### [](#bentplate)[BentPlate](DesignData.SDS2.Model.BentPlate.html)

A bent steel plate.

#### [](#bentplateend)[BentPlateEnd](DesignData.SDS2.Model.BentPlateEnd.html)

The end of a bent plate.

#### [](#bentplateendlist)[BentPlateEndList](DesignData.SDS2.Model.BentPlateEndList.html)

#### [](#bentplateendlist-bentplateendlistenumerator)[BentPlateEndList.BentPlateEndListEnumerator](DesignData.SDS2.Model.BentPlateEndList.BentPlateEndListEnumerator.html)

#### [](#bentplatelayout)[BentPlateLayout](DesignData.SDS2.Model.BentPlateLayout.html)

A bent plate formed by a planar list of points, a Layout3D, does not need to be a closed loop.

#### [](#bentplatespecification)[BentPlateSpecification](DesignData.SDS2.Model.BentPlateSpecification.html)

A bent plate connection

#### [](#bolt)[Bolt](DesignData.SDS2.Model.Bolt.html)

Describes a bolt fastener: The bolt plus any washers and any nuts.

#### [](#boltlist)[BoltList](DesignData.SDS2.Model.BoltList.html)

#### [](#boltlist-boltlistenumerator)[BoltList.BoltListEnumerator](DesignData.SDS2.Model.BoltList.BoltListEnumerator.html)

#### [](#boltmatchspecification)[BoltMatchSpecification](DesignData.SDS2.Model.BoltMatchSpecification.html)

This is a spec of options you can change when matching bolts, on the resulting bolts. Options you find on Bolt, but not here, are options we don't support changing during bolt match.

```
         Once you've got the options set, pass this to the Fasten function to create bolts
         which fasten 2 or more pieces of material.

         All options default to null.  If an option is null, then you will get the default
         value which is generally inherited from the holes that are bolted, or from setup.

```

#### [](#boltmaterial)[BoltMaterial](DesignData.SDS2.Model.BoltMaterial.html)

A bolt, added as a material, so that it will appear on the bill of material.

#### [](#channel)[Channel](DesignData.SDS2.Model.Channel.html)

A channel material

#### [](#clevis)[Clevis](DesignData.SDS2.Model.Clevis.html)

A steel clevis.

#### [](#clipanglespecification)[ClipAngleSpecification](DesignData.SDS2.Model.ClipAngleSpecification.html)

A clip angle connection

#### [](#clipflange)[ClipFlange](DesignData.SDS2.Model.ClipFlange.html)

Clips the flange based on the flange cut angle on the material, from the edge of the flange the center of the material

#### [](#clipplate)[ClipPlate](DesignData.SDS2.Model.ClipPlate.html)

Applies a single, linear cut

#### [](#clipweb)[ClipWeb](DesignData.SDS2.Model.ClipWeb.html)

Clip the web and flange at the corner

#### [](#coldformedchannel)[ColdFormedChannel](DesignData.SDS2.Model.ColdFormedChannel.html)

Cold formed channel material

#### [](#coldformedz)[ColdFormedZ](DesignData.SDS2.Model.ColdFormedZ.html)

Cold formed Z material

#### [](#column)[Column](DesignData.SDS2.Model.Column.html)

A builtin steel column member.

#### [](#columnautobasecapplatespecification)[ColumnAutoBaseCapPlateSpecification](DesignData.SDS2.Model.ColumnAutoBaseCapPlateSpecification.html)

A system designed base or cap plate, connecting to another steel member (generally a beam).

#### [](#columnend)[ColumnEnd](DesignData.SDS2.Model.ColumnEnd.html)

Column specific end options

#### [](#columnendlist)[ColumnEndList](DesignData.SDS2.Model.ColumnEndList.html)

#### [](#columnendlist-columnendlistenumerator)[ColumnEndList.ColumnEndListEnumerator](DesignData.SDS2.Model.ColumnEndList.ColumnEndListEnumerator.html)

#### [](#columnuserbasecapplatespecification)[ColumnUserBaseCapPlateSpecification](DesignData.SDS2.Model.ColumnUserBaseCapPlateSpecification.html)

A user specified base or cap plate connection

#### [](#component)[Component](DesignData.SDS2.Model.Component.html)

Base class for components on members

#### [](#componentlist)[ComponentList](DesignData.SDS2.Model.ComponentList.html)

#### [](#componentlist-componentlistenumerator)[ComponentList.ComponentListEnumerator](DesignData.SDS2.Model.ComponentList.ComponentListEnumerator.html)

#### [](#connectioncomponent)[ConnectionComponent](DesignData.SDS2.Model.ConnectionComponent.html)

A builtin connection component

#### [](#connectionspecification)[ConnectionSpecification](DesignData.SDS2.Model.ConnectionSpecification.html)

Specification to design specific connection types. This is a base class, all options are found on derived connection types.

#### [](#copefieldweldn1fema)[CopeFieldWeldN1FEMA](DesignData.SDS2.Model.CopeFieldWeldN1FEMA.html)

A cope for FEMA welds.

#### [](#copefieldweldn3)[CopeFieldWeldN3](DesignData.SDS2.Model.CopeFieldWeldN3.html)

Designates weld preparation and/or a cut to remove part of the top/bottom flange plus part of the web.

#### [](#copefieldweldn3standard)[CopeFieldWeldN3Standard](DesignData.SDS2.Model.CopeFieldWeldN3Standard.html)

Similar to a CopePlain, but for field welds

#### [](#copeplain)[CopePlain](DesignData.SDS2.Model.CopePlain.html)

A simple cut of the flange and web

#### [](#copeplate)[CopePlate](DesignData.SDS2.Model.CopePlate.html)

A 90 degree (L-shaped) cut with a rounded corner

#### [](#copeshopweldn1fema)[CopeShopWeldN1FEMA](DesignData.SDS2.Model.CopeShopWeldN1FEMA.html)

A cope for FEMA welds.

#### [](#copeshopweldn3)[CopeShopWeldN3](DesignData.SDS2.Model.CopeShopWeldN3.html)

Designates weld preparation and/or a cut to remove part of the top/bottom flange plus part of the web.

#### [](#createdconnectionmaterial)[CreatedConnectionMaterial](DesignData.SDS2.Model.CreatedConnectionMaterial.html)

A container for the lists for materials, bolts, and welds created by a connection.

#### [](#custompropertymap)[CustomPropertyMap](DesignData.SDS2.Model.CustomPropertyMap.html)

A set of custom properties for a member, material, bolt, weld, or other item with custom properties.

#### [](#custompropertyvaluetype)[CustomPropertyValueType](DesignData.SDS2.Model.CustomPropertyValueType.html)

This has been moved to DesignData.SDS2.Setup, please use that in new code. This is just a placeholder to autobox these so existing code will still compile.

#### [](#cutflangeflush)[CutFlangeFlush](DesignData.SDS2.Model.CutFlangeFlush.html)

For S shapes and W shapes and Wtees, it applies two flange cuts, one on the near side and the other on the far side. Both cut to the web. A zero near side or far side length means no cut is made on that side.

#### [](#cutflangewidth)[CutFlangeWidth](DesignData.SDS2.Model.CutFlangeWidth.html)

For S shapes and W shapes and Wtees, it applies two flange cuts, one on the near side and the other on the far side. Both cut to the web. A zero near side or far side length means no cut is made on that side.

#### [](#cuttablematerialend)[CuttableMaterialEnd](DesignData.SDS2.Model.CuttableMaterialEnd.html)

A material end which can be setback or have a simple web or flange cut applied. Some derived classes offer significantly more cutting options.

#### [](#cuttablematerialendlist)[CuttableMaterialEndList](DesignData.SDS2.Model.CuttableMaterialEndList.html)

#### [](#cuttablematerialendlist-cuttablematerialendlistenumerator)[CuttableMaterialEndList.CuttableMaterialEndListEnumerator](DesignData.SDS2.Model.CuttableMaterialEndList.CuttableMaterialEndListEnumerator.html)

#### [](#databaseextensionmethods)[DatabaseExtensionMethods](DesignData.SDS2.Model.DatabaseExtensionMethods.html)

Extension methods for DesignData.SDS2.Database. These are all convenience methods and will appear to be on classes in DesignData.SDS2.Database.

#### [](#decking)[Decking](DesignData.SDS2.Model.Decking.html)

Deck material is prefabricated sheets of corrugated steel. Sometimes it is referred to as cellular roof deck or as form deck material. It may be used for stay-in-place forms for structural concrete slabs, but is also used without concrete. Deck is typically cut to fit form lengths and field welded to the top of beams and joists.

#### [](#deckingend)[DeckingEnd](DesignData.SDS2.Model.DeckingEnd.html)

The end of a decking material

#### [](#deckingendlist)[DeckingEndList](DesignData.SDS2.Model.DeckingEndList.html)

#### [](#deckingendlist-deckingendlistenumerator)[DeckingEndList.DeckingEndListEnumerator](DesignData.SDS2.Model.DeckingEndList.DeckingEndListEnumerator.html)

#### [](#detailview)[DetailView](DesignData.SDS2.Model.DetailView.html)

Information for a member view

#### [](#detailviewlist)[DetailViewList](DesignData.SDS2.Model.DetailViewList.html)

#### [](#detailviewlist-detailviewlistenumerator)[DetailViewList.DetailViewListEnumerator](DesignData.SDS2.Model.DetailViewList.DetailViewListEnumerator.html)

#### [](#endplatespecification)[EndPlateSpecification](DesignData.SDS2.Model.EndPlateSpecification.html)

An end plate connection

#### [](#endpreparation)[EndPreparation](DesignData.SDS2.Model.EndPreparation.html)

End preparation lockables for most builtin members types (such as beams and braces). These are convenience methods for looking up lockables normally found on ConnectionComponent.GetLockable

#### [](#flangecutoperation)[FlangeCutOperation](DesignData.SDS2.Model.FlangeCutOperation.html)

#### [](#flatbar)[FlatBar](DesignData.SDS2.Model.FlatBar.html)

A flat steel bar.

#### [](#flatplatelayout)[FlatPlateLayout](DesignData.SDS2.Model.FlatPlateLayout.html)

A flat plate formed by a planar loop of points, a Layout3D

#### [](#flushframedshearspecification)[FlushFramedShearSpecification](DesignData.SDS2.Model.FlushFramedShearSpecification.html)

A flush framed shear connection for joists.

#### [](#fullyweldedspecification)[FullyWeldedSpecification](DesignData.SDS2.Model.FullyWeldedSpecification.html)

A fully welded moment connection specification.

#### [](#girt)[Girt](DesignData.SDS2.Model.Girt.html)

A builtin steel girt member.

#### [](#grating)[Grating](DesignData.SDS2.Model.Grating.html)

Grating is material of different sizes of steel bar. It is considered to be a single material because it may be purchased from manufactures as a single piece of material.

#### [](#gratingend)[GratingEnd](DesignData.SDS2.Model.GratingEnd.html)

The end of a grating material

#### [](#gratingendlist)[GratingEndList](DesignData.SDS2.Model.GratingEndList.html)

#### [](#gratingendlist-gratingendlistenumerator)[GratingEndList.GratingEndListEnumerator](DesignData.SDS2.Model.GratingEndList.GratingEndListEnumerator.html)

#### [](#gratingtread)[GratingTread](DesignData.SDS2.Model.GratingTread.html)

GratingTread is material of different sizes of steel bar. It is considered to be a single material because it may be purchased from manufactures as a single piece of material.

#### [](#gridline)[GridLine](DesignData.SDS2.Model.GridLine.html)

Grid lines appear as lines, segments, circles, and arcs of a circle in the model.

#### [](#groupmember)[GroupMember](DesignData.SDS2.Model.GroupMember.html)

A GroupMember associates submembers that will be detailed as a single member with one piecemark.

#### [](#hole)[Hole](DesignData.SDS2.Model.Hole.html)

A single hole on a material

#### [](#holegroup)[HoleGroup](DesignData.SDS2.Model.HoleGroup.html)

A group of holes, and properties holes share with other holes in the same group.

#### [](#holelist)[HoleList](DesignData.SDS2.Model.HoleList.html)

#### [](#holelist-holelistenumerator)[HoleList.HoleListEnumerator](DesignData.SDS2.Model.HoleList.HoleListEnumerator.html)

#### [](#holemachinecounterboreshape)[HoleMachineCounterboreShape](DesignData.SDS2.Model.HoleMachineCounterboreShape.html)

Counterbore hole shape operation

#### [](#holemachinecountersinkshape)[HoleMachineCountersinkShape](DesignData.SDS2.Model.HoleMachineCountersinkShape.html)

Countersink hole shape operation

#### [](#holemachineoperationthreads)[HoleMachineOperationThreads](DesignData.SDS2.Model.HoleMachineOperationThreads.html)

Hole threading operation

#### [](#holemachineoperations)[HoleMachineOperations](DesignData.SDS2.Model.HoleMachineOperations.html)

'Machine/Tool operations' as seen in the hole edit screen

#### [](#holepattern)[HolePattern](DesignData.SDS2.Model.HolePattern.html)

HolePattern encapsulates information to create holes in the model. The local coordinate system of a HolePattern is an XY plane that can be translated to global coordinates and used to create holes on materials.

#### [](#horizontalbrace)[HorizontalBrace](DesignData.SDS2.Model.HorizontalBrace.html)

A builtin steel horizontal brace member.

#### [](#horizontalbraceend)[HorizontalBraceEnd](DesignData.SDS2.Model.HorizontalBraceEnd.html)

Horizontal brace specific end options

#### [](#horizontalbraceendlist)[HorizontalBraceEndList](DesignData.SDS2.Model.HorizontalBraceEndList.html)

#### [](#horizontalbraceendlist-horizontalbraceendlistenumerator)[HorizontalBraceEndList.HorizontalBraceEndListEnumerator](DesignData.SDS2.Model.HorizontalBraceEndList.HorizontalBraceEndListEnumerator.html)

#### [](#horzbraceplatespecification)[HorzBracePlateSpecification](DesignData.SDS2.Model.HorzBracePlateSpecification.html)

A specification for connecting a horizontal brace to one or more supporting members via a gusset plate and possibly clip angles.

#### [](#ifc2x3)[IFC2x3](DesignData.SDS2.Model.IFC2x3.html)

#### [](#ifc4)[IFC4](DesignData.SDS2.Model.IFC4.html)

#### [](#ifcoptions)[IFCOptions](DesignData.SDS2.Model.IFCOptions.html)

Class for miscellaneous options that can be passed to IFC Export functions.

#### [](#joist)[Joist](DesignData.SDS2.Model.Joist.html)

A builtin steel joist member.

#### [](#legacymiscellaneous)[LegacyMiscellaneous](DesignData.SDS2.Model.LegacyMiscellaneous.html)

A builtin/legacy miscellaneous member. This style of miscellaneous member does not go through process, it simply has a user added material as its main material.

```
        These can be added via the API by creating a LegacyMiscellanous and
        then adding a material to it.  Don't forget to set the material's
        ToGlobalCoordinates to match the member's AFTER setting workpoints
        and rotation on the member.

```

#### [](#lockable)[Lockable](DesignData.SDS2.Model.Lockable.html)

Base class for lockable values. Lockable values are values in SDS2 which can be locked to a user value, or unlocked and set by process to a system generated value.

#### [](#lockableattachtomember)[LockableAttachToMember](DesignData.SDS2.Model.LockableAttachToMember.html)

A lockable for the AttachToMember enum

#### [](#lockablebaseplateweldinner)[LockableBasePlateWeldInner](DesignData.SDS2.Model.LockableBasePlateWeldInner.html)

Lockable value for BasePlateWeldInner

#### [](#lockablebaseplateweldouter)[LockableBasePlateWeldOuter](DesignData.SDS2.Model.LockableBasePlateWeldOuter.html)

Lockable value for BasePlateWeldOuter

#### [](#lockablebaseplateweldwithgroove)[LockableBasePlateWeldWithGroove](DesignData.SDS2.Model.LockableBasePlateWeldWithGroove.html)

Lockable value for BasePlateWeldWithGroove

#### [](#lockablebaseplateweldwithoutgroove)[LockableBasePlateWeldWithoutGroove](DesignData.SDS2.Model.LockableBasePlateWeldWithoutGroove.html)

Lockable value for BasePlateWeldWithoutGroove

#### [](#lockablebeamextensionplateweldtype)[LockableBeamExtensionPlateWeldType](DesignData.SDS2.Model.LockableBeamExtensionPlateWeldType.html)

Lockable value for beam extension plate welds

#### [](#lockablebool)[LockableBool](DesignData.SDS2.Model.LockableBool.html)

A lockable value holding an boolean

#### [](#lockablebracefilllocation)[LockableBraceFillLocation](DesignData.SDS2.Model.LockableBraceFillLocation.html)

A lockable value for BraceFillLocation

#### [](#lockablecutlocation)[LockableCutLocation](DesignData.SDS2.Model.LockableCutLocation.html)

Lockable value for CutLocation

#### [](#lockablecutoperation)[LockableCutOperation](DesignData.SDS2.Model.LockableCutOperation.html)

Lockable value for CutOperation

#### [](#lockabledictionary)[LockableDictionary](DesignData.SDS2.Model.LockableDictionary.html)

#### [](#lockabledictionary-lockabledictionaryenumerator)[LockableDictionary.LockableDictionaryEnumerator](DesignData.SDS2.Model.LockableDictionary.LockableDictionaryEnumerator.html)

#### [](#lockabledouble)[LockableDouble](DesignData.SDS2.Model.LockableDouble.html)

A lockable value holding a double

#### [](#lockableendcuttype)[LockableEndCutType](DesignData.SDS2.Model.LockableEndCutType.html)

Lockable value for end cuts

#### [](#lockableholetype)[LockableHoleType](DesignData.SDS2.Model.LockableHoleType.html)

Lockable value for hole types

#### [](#lockableint)[LockableInt](DesignData.SDS2.Model.LockableInt.html)

A lockable value holding an integer

#### [](#lockableplateside)[LockablePlateSide](DesignData.SDS2.Model.LockablePlateSide.html)

#### [](#lockableshape)[LockableShape](DesignData.SDS2.Model.LockableShape.html)

A lockable value holding a reference to a Shape in the job

#### [](#lockableshearweldtype)[LockableShearWeldType](DesignData.SDS2.Model.LockableShearWeldType.html)

Lockable value for ShearWeldType

#### [](#lockablespacing)[LockableSpacing](DesignData.SDS2.Model.LockableSpacing.html)

Variable spacings describe the spacings between a row of bolts, possibly varying between each bolt

#### [](#lockablesteelgrade)[LockableSteelGrade](DesignData.SDS2.Model.LockableSteelGrade.html)

A lockable value for a SteelGrade

#### [](#lockablestiffclip)[LockableStiffClip](DesignData.SDS2.Model.LockableStiffClip.html)

Lockable value for stiffener clips

#### [](#lockablethreaddirection)[LockableThreadDirection](DesignData.SDS2.Model.LockableThreadDirection.html)

Lockable value for ThreadDirection

#### [](#material)[Material](DesignData.SDS2.Model.Material.html)

Material is the base class for all material types.

#### [](#materiallist)[MaterialList](DesignData.SDS2.Model.MaterialList.html)

#### [](#materiallist-materiallistenumerator)[MaterialList.MaterialListEnumerator](DesignData.SDS2.Model.MaterialList.MaterialListEnumerator.html)

#### [](#materialuse)[MaterialUse](DesignData.SDS2.Model.MaterialUse.html)

MaterialUse is a class with a fixed set of possible values describing how a material is being used in the model. Objects of this class have ShortDescription, LongDescription, and Value properties.

#### [](#materialuselist)[MaterialUseList](DesignData.SDS2.Model.MaterialUseList.html)

#### [](#materialuselist-materialuselistenumerator)[MaterialUseList.MaterialUseListEnumerator](DesignData.SDS2.Model.MaterialUseList.MaterialUseListEnumerator.html)

#### [](#member)[Member](DesignData.SDS2.Model.Member.html)

All member data, including data which is slow to access in the SDS2 database.

#### [](#memberbrief)[MemberBrief](DesignData.SDS2.Model.MemberBrief.html)

Member data that can be rapidly accessed. This is data stored in a fixed length database for each member inside the SDS2 database.

#### [](#memberbrieflist)[MemberBriefList](DesignData.SDS2.Model.MemberBriefList.html)

#### [](#memberbrieflist-memberbrieflistenumerator)[MemberBriefList.MemberBriefListEnumerator](DesignData.SDS2.Model.MemberBriefList.MemberBriefListEnumerator.html)

#### [](#memberend)[MemberEnd](DesignData.SDS2.Model.MemberEnd.html)

The fully inclusive set of end data on a member

#### [](#memberendbrief)[MemberEndBrief](DesignData.SDS2.Model.MemberEndBrief.html)

The fixed length (rapid access) data on a member.

#### [](#memberendbrieflist)[MemberEndBriefList](DesignData.SDS2.Model.MemberEndBriefList.html)

#### [](#memberendbrieflist-memberendbrieflistenumerator)[MemberEndBriefList.MemberEndBriefListEnumerator](DesignData.SDS2.Model.MemberEndBriefList.MemberEndBriefListEnumerator.html)

#### [](#memberendlist)[MemberEndList](DesignData.SDS2.Model.MemberEndList.html)

#### [](#memberendlist-memberendlistenumerator)[MemberEndList.MemberEndListEnumerator](DesignData.SDS2.Model.MemberEndList.MemberEndListEnumerator.html)

#### [](#miscellaneous)[Miscellaneous](DesignData.SDS2.Model.Miscellaneous.html)

Processable miscellaneous members created using the custom members from the custom member plugin MiscellaneousCM.

```
         These miscellaneous members should be available in a typical SDS2
         install, but it is possible a user has disabled them.  And so you
         should check IsAvailable before proceeding to create new ones.

         You can use the PythonObject property on these to set various properties
         normally available in python.

```

#### [](#miscellaneousbentplate)[MiscellaneousBentPlate](DesignData.SDS2.Model.MiscellaneousBentPlate.html)

A member with a single bent plate material.

#### [](#miscellaneousbentplateend)[MiscellaneousBentPlateEnd](DesignData.SDS2.Model.MiscellaneousBentPlateEnd.html)

End properties for a miscellaneous bent plate, should be largely the same as to Model.BentPlateEnd

#### [](#miscellaneousbentplateendlist)[MiscellaneousBentPlateEndList](DesignData.SDS2.Model.MiscellaneousBentPlateEndList.html)

#### [](#miscellaneousbentplateendlist-miscellaneousbentplateendlistenume)[MiscellaneousBentPlateEndList.MiscellaneousBentPlateEndListEnumerator](DesignData.SDS2.Model.MiscellaneousBentPlateEndList.MiscellaneousBentPlateEndListEnumerator.html)

#### [](#miscellaneousbentplatelayout)[MiscellaneousBentPlateLayout](DesignData.SDS2.Model.MiscellaneousBentPlateLayout.html)

A member with a single bent plate layout material.

#### [](#miscellaneousclevis)[MiscellaneousClevis](DesignData.SDS2.Model.MiscellaneousClevis.html)

A member with a single clevis material.

#### [](#miscellaneousdecking)[MiscellaneousDecking](DesignData.SDS2.Model.MiscellaneousDecking.html)

A member with a single deck material.

#### [](#miscellaneousflatbar)[MiscellaneousFlatBar](DesignData.SDS2.Model.MiscellaneousFlatBar.html)

A member with a single flat bar material.

#### [](#miscellaneousflatbarend)[MiscellaneousFlatBarEnd](DesignData.SDS2.Model.MiscellaneousFlatBarEnd.html)

End properties for a miscellaneous bent plate, should be largely the same as to Model.FlatBarEnd

#### [](#miscellaneousflatbarendlist)[MiscellaneousFlatBarEndList](DesignData.SDS2.Model.MiscellaneousFlatBarEndList.html)

#### [](#miscellaneousflatbarendlist-miscellaneousflatbarendlistenumerato)[MiscellaneousFlatBarEndList.MiscellaneousFlatBarEndListEnumerator](DesignData.SDS2.Model.MiscellaneousFlatBarEndList.MiscellaneousFlatBarEndListEnumerator.html)

#### [](#miscellaneousflatplatelayout)[MiscellaneousFlatPlateLayout](DesignData.SDS2.Model.MiscellaneousFlatPlateLayout.html)

A member with a single plate layout material.

#### [](#miscellaneousgrating)[MiscellaneousGrating](DesignData.SDS2.Model.MiscellaneousGrating.html)

A member with a single grate material.

#### [](#miscellaneousgratingend)[MiscellaneousGratingEnd](DesignData.SDS2.Model.MiscellaneousGratingEnd.html)

End properties for a miscellaneous bent plate, should be largely the same as to Model.GratingEnd

#### [](#miscellaneousgratingendlist)[MiscellaneousGratingEndList](DesignData.SDS2.Model.MiscellaneousGratingEndList.html)

#### [](#miscellaneousgratingendlist-miscellaneousgratingendlistenumerato)[MiscellaneousGratingEndList.MiscellaneousGratingEndListEnumerator](DesignData.SDS2.Model.MiscellaneousGratingEndList.MiscellaneousGratingEndListEnumerator.html)

#### [](#miscellaneousgratingtread)[MiscellaneousGratingTread](DesignData.SDS2.Model.MiscellaneousGratingTread.html)

A member with a single grate tread material.

#### [](#miscellaneousrectangularplate)[MiscellaneousRectangularPlate](DesignData.SDS2.Model.MiscellaneousRectangularPlate.html)

A member with a single rectangular plate material.

#### [](#miscellaneousrectangularplateend)[MiscellaneousRectangularPlateEnd](DesignData.SDS2.Model.MiscellaneousRectangularPlateEnd.html)

End properties for a miscellaneous round bar, should be largely the same as to Model.RectangularPlateEnd

#### [](#miscellaneousrectangularplateendlist)[MiscellaneousRectangularPlateEndList](DesignData.SDS2.Model.MiscellaneousRectangularPlateEndList.html)

#### [](#miscellaneousrectangularplateendlist-miscellaneousrectangularpla)[MiscellaneousRectangularPlateEndList.MiscellaneousRectangularPlateEndListEnumerator](DesignData.SDS2.Model.MiscellaneousRectangularPlateEndList.MiscellaneousRectangularPlateEndListEnumerator.html)

#### [](#miscellaneousrolledplate)[MiscellaneousRolledPlate](DesignData.SDS2.Model.MiscellaneousRolledPlate.html)

A member with a single rolled plate material.

#### [](#miscellaneousrolledshape)[MiscellaneousRolledShape](DesignData.SDS2.Model.MiscellaneousRolledShape.html)

A member with a single rolled shape material

#### [](#miscellaneousrolledshapeend)[MiscellaneousRolledShapeEnd](DesignData.SDS2.Model.MiscellaneousRolledShapeEnd.html)

End properties for a miscellaneous rolled shape/section, should be largely the same as to Model.ShapeMaterialEnd

#### [](#miscellaneousrolledshapeendlist)[MiscellaneousRolledShapeEndList](DesignData.SDS2.Model.MiscellaneousRolledShapeEndList.html)

#### [](#miscellaneousrolledshapeendlist-miscellaneousrolledshapeendliste)[MiscellaneousRolledShapeEndList.MiscellaneousRolledShapeEndListEnumerator](DesignData.SDS2.Model.MiscellaneousRolledShapeEndList.MiscellaneousRolledShapeEndListEnumerator.html)

#### [](#miscellaneousroundbar)[MiscellaneousRoundBar](DesignData.SDS2.Model.MiscellaneousRoundBar.html)

A member with a single round bar material

#### [](#miscellaneousroundbarend)[MiscellaneousRoundBarEnd](DesignData.SDS2.Model.MiscellaneousRoundBarEnd.html)

End properties for a miscellaneous round bar, should be largely the same as to Model.RoundBarEnd

#### [](#miscellaneousroundbarendlist)[MiscellaneousRoundBarEndList](DesignData.SDS2.Model.MiscellaneousRoundBarEndList.html)

#### [](#miscellaneousroundbarendlist-miscellaneousroundbarendlistenumera)[MiscellaneousRoundBarEndList.MiscellaneousRoundBarEndListEnumerator](DesignData.SDS2.Model.MiscellaneousRoundBarEndList.MiscellaneousRoundBarEndListEnumerator.html)

#### [](#miscellaneousroundplate)[MiscellaneousRoundPlate](DesignData.SDS2.Model.MiscellaneousRoundPlate.html)

A member with a single round plate

#### [](#miscellaneousshearorthreadedstud)[MiscellaneousShearOrThreadedStud](DesignData.SDS2.Model.MiscellaneousShearOrThreadedStud.html)

A member with a single shear stud material

#### [](#miscellaneoussquarebar)[MiscellaneousSquareBar](DesignData.SDS2.Model.MiscellaneousSquareBar.html)

A member with a single square bar material

#### [](#miscellaneoussquarebarend)[MiscellaneousSquareBarEnd](DesignData.SDS2.Model.MiscellaneousSquareBarEnd.html)

End properties for a miscellaneous round bar, should be largely the same as to Model.SquareBarEnd

#### [](#miscellaneoussquarebarendlist)[MiscellaneousSquareBarEndList](DesignData.SDS2.Model.MiscellaneousSquareBarEndList.html)

#### [](#miscellaneoussquarebarendlist-miscellaneoussquarebarendlistenume)[MiscellaneousSquareBarEndList.MiscellaneousSquareBarEndListEnumerator](DesignData.SDS2.Model.MiscellaneousSquareBarEndList.MiscellaneousSquareBarEndListEnumerator.html)

#### [](#miscellaneousturnbuckle)[MiscellaneousTurnbuckle](DesignData.SDS2.Model.MiscellaneousTurnbuckle.html)

A member with a single turnbuckle material

#### [](#modelviewdescription)[ModelViewDescription](DesignData.SDS2.Model.ModelViewDescription.html)

This has been renamed ModelViewDefinition, please reference that class from now on.

#### [](#momentspecification)[MomentSpecification](DesignData.SDS2.Model.MomentSpecification.html)

The moment specification options.

#### [](#notchboth)[NotchBoth](DesignData.SDS2.Model.NotchBoth.html)

Notch the Top/Bottom and Near/Far sides of a hollow section.

#### [](#notchflange)[NotchFlange](DesignData.SDS2.Model.NotchFlange.html)

Notch the Top/Bottom sides of a hollow section.

#### [](#notchweb)[NotchWeb](DesignData.SDS2.Model.NotchWeb.html)

Notch the Near/Far sides of a hollow section.

#### [](#note)[Note](DesignData.SDS2.Model.Note.html)

Notes are for authoring and reviewing comments related the the model or to the project.

#### [](#notecomment)[NoteComment](DesignData.SDS2.Model.NoteComment.html)

Notes are for authoring and reviewing comments related the the model or to the project.

#### [](#notecommentlist)[NoteCommentList](DesignData.SDS2.Model.NoteCommentList.html)

#### [](#notecommentlist-notecommentlistenumerator)[NoteCommentList.NoteCommentListEnumerator](DesignData.SDS2.Model.NoteCommentList.NoteCommentListEnumerator.html)

#### [](#nut)[Nut](DesignData.SDS2.Model.Nut.html)

A nut, on a bolt

#### [](#nutlist)[NutList](DesignData.SDS2.Model.NutList.html)

#### [](#nutlist-nutlistenumerator)[NutList.NutListEnumerator](DesignData.SDS2.Model.NutList.NutListEnumerator.html)

#### [](#pipe)[Pipe](DesignData.SDS2.Model.Pipe.html)

A pipe material

#### [](#plainendspecification)[PlainEndSpecification](DesignData.SDS2.Model.PlainEndSpecification.html)

This tells the system not to design a connection.

#### [](#plate)[Plate](DesignData.SDS2.Model.Plate.html)

Base class for steel plates.

#### [](#platecutoperation)[PlateCutOperation](DesignData.SDS2.Model.PlateCutOperation.html)

Base class for plate cut operations

#### [](#purlin)[Purlin](DesignData.SDS2.Model.Purlin.html)

A builtin steel purlin member.

#### [](#pythoncomponent)[PythonComponent](DesignData.SDS2.Model.PythonComponent.html)

A component implemented in python

#### [](#pythonmaterial)[PythonMaterial](DesignData.SDS2.Model.PythonMaterial.html)

A material implemented in python. This can be accessed or modified by using the PythonObject property with the 'dynamic' type.

#### [](#pythonmember)[PythonMember](DesignData.SDS2.Model.PythonMember.html)

A "custom" member implemented in python. Access properties on these types through the Dynamic property on this object, as a csharp 'dynamic' type.

#### [](#rail)[Rail](DesignData.SDS2.Model.Rail.html)

Rail material

#### [](#rectangularplate)[RectangularPlate](DesignData.SDS2.Model.RectangularPlate.html)

A rectangular steel plate.

#### [](#rectangularplateend)[RectangularPlateEnd](DesignData.SDS2.Model.RectangularPlateEnd.html)

The end of a plate

#### [](#rectangularplateendlist)[RectangularPlateEndList](DesignData.SDS2.Model.RectangularPlateEndList.html)

#### [](#rectangularplateendlist-rectangularplateendlistenumerator)[RectangularPlateEndList.RectangularPlateEndListEnumerator](DesignData.SDS2.Model.RectangularPlateEndList.RectangularPlateEndListEnumerator.html)

#### [](#referenceobjectarealayout)[ReferenceObjectAreaLayout](DesignData.SDS2.Model.ReferenceObjectAreaLayout.html)

A flat reference material formed by a planar loop of points, a Layout3D

#### [](#referenceobjectperimeterlayout)[ReferenceObjectPerimeterLayout](DesignData.SDS2.Model.ReferenceObjectPerimeterLayout.html)

A reference material formed by a planar list of points, a Layout3D, does not need to be a closed loop.

#### [](#rolledplate)[RolledPlate](DesignData.SDS2.Model.RolledPlate.html)

A plate rolled around its first workpoint

#### [](#rolledshapematerial)[RolledShapeMaterial](DesignData.SDS2.Model.RolledShapeMaterial.html)

A material primarily defined by its associated Shape

#### [](#roundbar)[RoundBar](DesignData.SDS2.Model.RoundBar.html)

A round steel bar.

#### [](#roundbarend)[RoundBarEnd](DesignData.SDS2.Model.RoundBarEnd.html)

The end of a round bar

#### [](#roundbarendlist)[RoundBarEndList](DesignData.SDS2.Model.RoundBarEndList.html)

#### [](#roundbarendlist-roundbarendlistenumerator)[RoundBarEndList.RoundBarEndListEnumerator](DesignData.SDS2.Model.RoundBarEndList.RoundBarEndListEnumerator.html)

#### [](#roundplate)[RoundPlate](DesignData.SDS2.Model.RoundPlate.html)

A round steel plate.

#### [](#sflange)[SFlange](DesignData.SDS2.Model.SFlange.html)

A S flange material

#### [](#stee)[STee](DesignData.SDS2.Model.STee.html)

A S tee material

#### [](#seatedspecification)[SeatedSpecification](DesignData.SDS2.Model.SeatedSpecification.html)

A seated connection

#### [](#seismiccopefieldweld)[SeismicCopeFieldWeld](DesignData.SDS2.Model.SeismicCopeFieldWeld.html)

A cope for seismic field welds.

#### [](#seismiccopeshopweld)[SeismicCopeShopWeld](DesignData.SDS2.Model.SeismicCopeShopWeld.html)

A cope for seismic shop welds.

#### [](#shapematerial)[ShapeMaterial](DesignData.SDS2.Model.ShapeMaterial.html)

A material whose definition is based on a Shape from the MaterialFile

#### [](#shapematerialend)[ShapeMaterialEnd](DesignData.SDS2.Model.ShapeMaterialEnd.html)

Collection of information about a rolled material's end

#### [](#shapematerialendlist)[ShapeMaterialEndList](DesignData.SDS2.Model.ShapeMaterialEndList.html)

#### [](#shapematerialendlist-shapematerialendlistenumerator)[ShapeMaterialEndList.ShapeMaterialEndListEnumerator](DesignData.SDS2.Model.ShapeMaterialEndList.ShapeMaterialEndListEnumerator.html)

#### [](#shearorthreadedstud)[ShearOrThreadedStud](DesignData.SDS2.Model.ShearOrThreadedStud.html)

A flat steel bar.

#### [](#sheartabspecification)[ShearTabSpecification](DesignData.SDS2.Model.ShearTabSpecification.html)

A shear tab connection

#### [](#spliceplatespecification)[SplicePlateSpecification](DesignData.SDS2.Model.SplicePlateSpecification.html)

A splice plate connection

#### [](#squarebar)[SquareBar](DesignData.SDS2.Model.SquareBar.html)

A square steel bar.

#### [](#stair)[Stair](DesignData.SDS2.Model.Stair.html)

A builtin stair member.

#### [](#stairconnection)[StairConnection](DesignData.SDS2.Model.StairConnection.html)

Connection for an end and side of a stair stringer

#### [](#stairconnectionattachmentbolted)[StairConnectionAttachmentBolted](DesignData.SDS2.Model.StairConnectionAttachmentBolted.html)

Bolted StairConnection attachment

#### [](#stairconnectionattachmentspecification)[StairConnectionAttachmentSpecification](DesignData.SDS2.Model.StairConnectionAttachmentSpecification.html)

Base class for StairConnection attachments

#### [](#stairconnectionattachmentwelded)[StairConnectionAttachmentWelded](DesignData.SDS2.Model.StairConnectionAttachmentWelded.html)

Welded StairConnection attachment

#### [](#stairconnectionclipangle)[StairConnectionClipAngle](DesignData.SDS2.Model.StairConnectionClipAngle.html)

Clip angle connection between stair stringer and supporting material

#### [](#stairconnectionfloorclip)[StairConnectionFloorClip](DesignData.SDS2.Model.StairConnectionFloorClip.html)

Clip angle connection between stair stringer and supporting floor material

#### [](#stairconnectionplainend)[StairConnectionPlainEnd](DesignData.SDS2.Model.StairConnectionPlainEnd.html)

No stair connection material

#### [](#stairconnectionshearplate)[StairConnectionShearPlate](DesignData.SDS2.Model.StairConnectionShearPlate.html)

Shear plate connection between stair stringer and supporting material

#### [](#stairconnectionspecification)[StairConnectionSpecification](DesignData.SDS2.Model.StairConnectionSpecification.html)

Base class for StairConnection types

#### [](#stairstringer)[StairStringer](DesignData.SDS2.Model.StairStringer.html)

The left/right ns/fs stringer data for a stair

#### [](#standardpart)[StandardPart](DesignData.SDS2.Model.StandardPart.html)

A standard part, in SDS2, is a piece of material that the system knows nothing about beyond a few basic attributes like material color and grade. It could come from a library of parts, or it could come from fusing together two pieces of material.

#### [](#tube)[Tube](DesignData.SDS2.Model.Tube.html)

A tube material

#### [](#turnbuckle)[Turnbuckle](DesignData.SDS2.Model.Turnbuckle.html)

A steel turnbuckle.

#### [](#turnedshelllayout)[TurnedShellLayout](DesignData.SDS2.Model.TurnedShellLayout.html)

A turned shell formed by a planar loop of points, a Layout3D

#### [](#turnedsolidlayout)[TurnedSolidLayout](DesignData.SDS2.Model.TurnedSolidLayout.html)

A turned solid formed by a planar loop of points, a Layout3D

#### [](#userdefinedconnection)[UserDefinedConnection](DesignData.SDS2.Model.UserDefinedConnection.html)

This describes a user defined connection in this model. Every connection using this user defined connection shares this same data (there is one list, by name, of all UserDefinedConnections in each job).

#### [](#userdefinedconnectioncondition)[UserDefinedConnectionCondition](DesignData.SDS2.Model.UserDefinedConnectionCondition.html)

These settings describe the condition you expect this user defined connection to apply. It's possible it will apply in other conditions, but generally you want to target this to the situation where it will be applied. A wide flange beam framed to a column, for example.

#### [](#userdefinedspecification)[UserDefinedSpecification](DesignData.SDS2.Model.UserDefinedSpecification.html)

Defines the connection specification for a user defined connection. This is only ever an InputSpecification, the DesignedSpecification that results will match the kind of connection specified by the UDC chosen here, or possibly something different if applying that connection as an input would result in a change (for example, a shear tab because a clip angle was chosen on a non-perpindicular beam connection).

#### [](#vertbraceplatespecification)[VertBracePlateSpecification](DesignData.SDS2.Model.VertBracePlateSpecification.html)

A specification for connecting a vertical brace to one or more supporting members via a gusset plate and possibly clip angles.

#### [](#verticalbrace)[VerticalBrace](DesignData.SDS2.Model.VerticalBrace.html)

A builtin steel vertical brace member.

#### [](#verticalbraceend)[VerticalBraceEnd](DesignData.SDS2.Model.VerticalBraceEnd.html)

Vertical brace specific end options

#### [](#verticalbraceendlist)[VerticalBraceEndList](DesignData.SDS2.Model.VerticalBraceEndList.html)

#### [](#verticalbraceendlist-verticalbraceendlistenumerator)[VerticalBraceEndList.VerticalBraceEndListEnumerator](DesignData.SDS2.Model.VerticalBraceEndList.VerticalBraceEndListEnumerator.html)

#### [](#view)[View](DesignData.SDS2.Model.View.html)

Data representing a view of the model.

#### [](#wtee)[WTee](DesignData.SDS2.Model.WTee.html)

A W tee material

#### [](#washer)[Washer](DesignData.SDS2.Model.Washer.html)

A washer, on a bolt

#### [](#washerlist)[WasherList](DesignData.SDS2.Model.WasherList.html)

#### [](#washerlist-washerlistenumerator)[WasherList.WasherListEnumerator](DesignData.SDS2.Model.WasherList.WasherListEnumerator.html)

#### [](#weld)[Weld](DesignData.SDS2.Model.Weld.html)

Weld provides access to information about welds on a member.

#### [](#weldlist)[WeldList](DesignData.SDS2.Model.WeldList.html)

#### [](#weldlist-weldlistenumerator)[WeldList.WeldListEnumerator](DesignData.SDS2.Model.WeldList.WeldListEnumerator.html)

#### [](#weldpathsegment)[WeldPathSegment](DesignData.SDS2.Model.WeldPathSegment.html)

Represents the orientation and length of one segment of a WeldPathSpecification.Segments

#### [](#weldpathsegmentlist)[WeldPathSegmentList](DesignData.SDS2.Model.WeldPathSegmentList.html)

#### [](#weldpathsegmentlist-weldpathsegmentlistenumerator)[WeldPathSegmentList.WeldPathSegmentListEnumerator](DesignData.SDS2.Model.WeldPathSegmentList.WeldPathSegmentListEnumerator.html)

#### [](#weldpathspecification)[WeldPathSpecification](DesignData.SDS2.Model.WeldPathSpecification.html)

Class representing all the weld information about how a new weld should be created

#### [](#weldprofilefillet)[WeldProfileFillet](DesignData.SDS2.Model.WeldProfileFillet.html)

WeldProfileFillet represents the profile of a fillet weld and can be used to generate the WeldPathSegment for a given weld size.

#### [](#weldsegment)[WeldSegment](DesignData.SDS2.Model.WeldSegment.html)

WeldSegment represents the position and orientation in the model of a logical segment of a weld. The segment may be stitched, so the weld between the two points of the segment may not be continuous.

#### [](#weldsegmentlist)[WeldSegmentList](DesignData.SDS2.Model.WeldSegmentList.html)

#### [](#weldsegmentlist-weldsegmentlistenumerator)[WeldSegmentList.WeldSegmentListEnumerator](DesignData.SDS2.Model.WeldSegmentList.WeldSegmentListEnumerator.html)

#### [](#weldside)[WeldSide](DesignData.SDS2.Model.WeldSide.html)

WeldSide provides access to the arrow and other side information of a weld

#### [](#weldedbox)[WeldedBox](DesignData.SDS2.Model.WeldedBox.html)

Welded plate box material

#### [](#weldedwideflange)[WeldedWideFlange](DesignData.SDS2.Model.WeldedWideFlange.html)

Welded plate wide flange material

#### [](#wideflange)[WideFlange](DesignData.SDS2.Model.WideFlange.html)

A wide flange material

### [](#interfaces)Interfaces 

#### [](#icuttableendmaterial)[ICuttableEndMaterial](DesignData.SDS2.Model.ICuttableEndMaterial.html)

Interface for materials which provide a list of ends that are CuttableMaterialEnds

#### [](#imemberrollingoperation)[IMemberRollingOperation](DesignData.SDS2.Model.IMemberRollingOperation.html)

Interface for rolling operation properties.

#### [](#irollingoperation)[IRollingOperation](DesignData.SDS2.Model.IRollingOperation.html)

Interface for rolling operation properties.

#### [](#istitchplatesettings)[IStitchPlateSettings](DesignData.SDS2.Model.IStitchPlateSettings.html)

Interface for stitch plate settings (on brace main material)

### [](#enums)Enums 

#### [](#arctype)[ArcType](DesignData.SDS2.Model.ArcType.html)

Enumerated curved grid arc types

#### [](#attachtomember)[AttachToMember](DesignData.SDS2.Model.AttachToMember.html)

Which member to ship the connection material with

#### [](#attachmentmethod)[AttachmentMethod](DesignData.SDS2.Model.AttachmentMethod.html)

The method to attach connection material to supported or supporting material.

#### [](#attachmentmethodwithautomatic)[AttachmentMethodWithAutomatic](DesignData.SDS2.Model.AttachmentMethodWithAutomatic.html)

The method to attach connection material to supported or supporting material.

#### [](#autoclipcope)[AutoClipCope](DesignData.SDS2.Model.AutoClipCope.html)

Set of connection specification values, typically for plates, represeting automatic, clip, and cope

#### [](#autogussetsupporting)[AutoGussetSupporting](DesignData.SDS2.Model.AutoGussetSupporting.html)

Attachment method for clip to connection.

#### [](#autosupportingsupported)[AutoSupportingSupported](DesignData.SDS2.Model.AutoSupportingSupported.html)

Set of connection specification values describing possible sides of a material

#### [](#automaticyesno)[AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html)

Many options in SDS2 can either be on, off, or determined based on some criteria by the system. Usually that criteria is a setup setting

#### [](#axialloadcheckoption)[AxialLoadCheckOption](DesignData.SDS2.Model.AxialLoadCheckOption.html)

Values for the AxialLoadCheck option on ShearTabSpecification

#### [](#baseplateweldinner)[BasePlateWeldInner](DesignData.SDS2.Model.BasePlateWeldInner.html)

Weld options for the inside weld of base plates

#### [](#baseplateweldouter)[BasePlateWeldOuter](DesignData.SDS2.Model.BasePlateWeldOuter.html)

Weld options for the outside weld of base plates

#### [](#baseplateweldwithgroove)[BasePlateWeldWithGroove](DesignData.SDS2.Model.BasePlateWeldWithGroove.html)

Base plate weld options when there is a groove

#### [](#baseplateweldwithoutgroove)[BasePlateWeldWithoutGroove](DesignData.SDS2.Model.BasePlateWeldWithoutGroove.html)

Base plate weld options when there is no groove

#### [](#beamextensionplateweldtype)[BeamExtensionPlateWeldType](DesignData.SDS2.Model.BeamExtensionPlateWeldType.html)

Beam extension plate weld options

#### [](#beamtoclipattachmentmethod)[BeamToClipAttachmentMethod](DesignData.SDS2.Model.BeamToClipAttachmentMethod.html)

Set of end connection values describing possible connections for a beam-to-clip.

#### [](#boltfinish)[BoltFinish](DesignData.SDS2.Model.BoltFinish.html)

The finish of a bolt

#### [](#bothnearfar)[BothNearFar](DesignData.SDS2.Model.BothNearFar.html)

Set of connection specification values describing possible sides of a material

#### [](#bracefilllocation)[BraceFillLocation](DesignData.SDS2.Model.BraceFillLocation.html)

#### [](#bracerotationtype)[BraceRotationType](DesignData.SDS2.Model.BraceRotationType.html)

The rotation of a brace

#### [](#clipanglegage)[ClipAngleGage](DesignData.SDS2.Model.ClipAngleGage.html)

Gage settings specific to clip angle connections

#### [](#clipangleside)[ClipAngleSide](DesignData.SDS2.Model.ClipAngleSide.html)

Which side of the beam to place clip angles on

#### [](#clipanglestagger)[ClipAngleStagger](DesignData.SDS2.Model.ClipAngleStagger.html)

Specifies where to stagger the bolts when clip angles share the same bolts.

#### [](#columnplateweldpattern)[ColumnPlateWeldPattern](DesignData.SDS2.Model.ColumnPlateWeldPattern.html)

Weld pattern types for column base and cap plates

#### [](#columnreinforcementtype)[ColumnReinforcementType](DesignData.SDS2.Model.ColumnReinforcementType.html)

#### [](#columnspliceattachmentmethod)[ColumnSpliceAttachmentMethod](DesignData.SDS2.Model.ColumnSpliceAttachmentMethod.html)

The method to attach spliced columns.

#### [](#columnwebdoublerside)[ColumnWebDoublerSide](DesignData.SDS2.Model.ColumnWebDoublerSide.html)

The location of a doubler plate on the web of a column.

#### [](#connspecholetypesubset)[ConnSpecHoleTypeSubset](DesignData.SDS2.Model.ConnSpecHoleTypeSubset.html)

Set of connection specification values representing a subset of hole types appropriate for a connection

#### [](#connectionextensiontype)[ConnectionExtensionType](DesignData.SDS2.Model.ConnectionExtensionType.html)

Options for how to extend connection material to the supporting material

#### [](#connectionspecificationendleftrightboth)[ConnectionSpecificationEndLeftRightBoth](DesignData.SDS2.Model.ConnectionSpecificationEndLeftRightBoth.html)

When a value space is restricted to left end, right end, or both ends.

#### [](#cutlocation)[CutLocation](DesignData.SDS2.Model.CutLocation.html)

The location of a cut

#### [](#cutoperation)[CutOperation](DesignData.SDS2.Model.CutOperation.html)

Cut operations for plates

#### [](#endcuttype)[EndCutType](DesignData.SDS2.Model.EndCutType.html)

The type or method of cut

#### [](#endplateendoption)[EndPlateEndOption](DesignData.SDS2.Model.EndPlateEndOption.html)

Options for the ends of the end plates used

#### [](#endplatesafetyconnection)[EndPlateSafetyConnection](DesignData.SDS2.Model.EndPlateSafetyConnection.html)

The end plate safety connections that SDS2 can handle.

#### [](#erectionboltspecification)[ErectionBoltSpecification](DesignData.SDS2.Model.ErectionBoltSpecification.html)

A specification for the number of bolts used connecting a HSS wide flange brace to the gusset plate.

#### [](#erectionviewtype)[ErectionViewType](DesignData.SDS2.Model.ErectionViewType.html)

Erection view types

#### [](#flangeplateonsheartabend)[FlangePlateOnShearTabEnd](DesignData.SDS2.Model.FlangePlateOnShearTabEnd.html)

#### [](#gridtype)[GridType](DesignData.SDS2.Model.GridType.html)

Enumerated grid line types

#### [](#grooveangle)[GrooveAngle](DesignData.SDS2.Model.GrooveAngle.html)

The angle of bevel on the flange of the beam. From a very short list of allowed options, named in degrees.

#### [](#holemachineoperationthreadseries)[HoleMachineOperationThreadSeries](DesignData.SDS2.Model.HoleMachineOperationThreadSeries.html)

The form or series

#### [](#holepatternrelativegridposition)[HolePatternRelativeGridPosition](DesignData.SDS2.Model.HolePatternRelativeGridPosition.html)

Relative positions describing the SDS2 grid hole patterns

#### [](#horizontalbraceplatetype)[HorizontalBracePlateType](DesignData.SDS2.Model.HorizontalBracePlateType.html)

Specifies a framing situation for a horizontal brace connection with a gusset plate.

#### [](#horzbracehssattachmentmethod)[HorzBraceHssAttachmentMethod](DesignData.SDS2.Model.HorzBraceHssAttachmentMethod.html)

A specification for how a HSS wide flange horizontal brace connects to the gusset plate.

#### [](#ifrequirednever)[IfRequiredNever](DesignData.SDS2.Model.IfRequiredNever.html)

See documentation on property using this to see meaning

#### [](#joiststabilizingmaterial)[JoistStabilizingMaterial](DesignData.SDS2.Model.JoistStabilizingMaterial.html)

What kind of stabilizing material to use for a joist connection

#### [](#linetype)[LineType](DesignData.SDS2.Model.LineType.html)

Enumerated line types

#### [](#locktype)[LockType](DesignData.SDS2.Model.LockType.html)

These "lock strengths" are used by connection design and member edit to determine whether a LockableValue::value can be overridden or not.

```
         A lower enum value represents a weaker lock strength. A stronger
         lockable cannot and should not be overridden by a weaker lock.

```

#### [](#longleg)[LongLeg](DesignData.SDS2.Model.LongLeg.html)

Defines the which leg of an angle brace with unequal legs is bolted to the gusset plate.

#### [](#materialsetbacktype)[MaterialSetbackType](DesignData.SDS2.Model.MaterialSetbackType.html)

Determines the meaning of the MaterialSetbackValue on the end of the main material.

#### [](#materialuse-id)[MaterialUse.ID](DesignData.SDS2.Model.MaterialUse.ID.html)

All the possible material use values that SDS2 knows about

#### [](#memberapproval)[MemberApproval](DesignData.SDS2.Model.MemberApproval.html)

Possible approval states for a member

#### [](#memberendrotationtype)[MemberEndRotationType](DesignData.SDS2.Model.MemberEndRotationType.html)

This determines how the end of a supported beam is rotated to match a supporting beam or column

#### [](#membersetbacktype)[MemberSetbackType](DesignData.SDS2.Model.MemberSetbackType.html)

Determines the meaning of the MemberSetbackValue on the end of a member.

#### [](#miscellaneousrectangularplatecutoperation)[MiscellaneousRectangularPlateCutOperation](DesignData.SDS2.Model.MiscellaneousRectangularPlateCutOperation.html)

Cut operations for plates

#### [](#modelcompletemode)[ModelCompleteMode](DesignData.SDS2.Model.ModelCompleteMode.html)

SDS2 has two distinct modes for model complete. A legacy mode that's not very strict and generally just warns users to not change a member. And a restrictive mode which actively prevents changes.

#### [](#modelviewdefinition)[ModelViewDefinition](DesignData.SDS2.Model.ModelViewDefinition.html)

The order of these model view definition values is critical, and MUST stay in sync with the MVD\_XXX defines in mdl\_link\_ext.h

#### [](#momentboltpattern)[MomentBoltPattern](DesignData.SDS2.Model.MomentBoltPattern.html)

The bolt pattern to use in a moment plate

#### [](#momentconnectionmaterial)[MomentConnectionMaterial](DesignData.SDS2.Model.MomentConnectionMaterial.html)

The kind of extra material to add to a connection for the moment

#### [](#momentconnectiontype)[MomentConnectionType](DesignData.SDS2.Model.MomentConnectionType.html)

The standard the moment connection follows

#### [](#momentplatelocation)[MomentPlateLocation](DesignData.SDS2.Model.MomentPlateLocation.html)

Where to put the moment plates for the moment connection

#### [](#momenttype)[MomentType](DesignData.SDS2.Model.MomentType.html)

The type of moment connection

#### [](#nuttype)[NutType](DesignData.SDS2.Model.NutType.html)

The style of nut

#### [](#pinheadside)[PinHeadSide](DesignData.SDS2.Model.PinHeadSide.html)

Side the pin head is on.

#### [](#pintype)[PinType](DesignData.SDS2.Model.PinType.html)

Type of Pin.

#### [](#plateside)[PlateSide](DesignData.SDS2.Model.PlateSide.html)

Which side the plate goes on

#### [](#platewashercombinationmethod)[PlateWasherCombinationMethod](DesignData.SDS2.Model.PlateWasherCombinationMethod.html)

The method of combining plate washers for a set of bolts

#### [](#plugtype)[PlugType](DesignData.SDS2.Model.PlugType.html)

Hole plug type

#### [](#presetview)[PresetView](DesignData.SDS2.Model.PresetView.html)

Preset detail view types

#### [](#reentrantcut)[ReEntrantCut](DesignData.SDS2.Model.ReEntrantCut.html)

The re-entrant cut method to use for a welded moment connection

#### [](#rightorleftend)[RightOrLeftEnd](DesignData.SDS2.Model.RightOrLeftEnd.html)

The right or left end of a member. See documentation on property using it to see how it's used.

#### [](#rolltype)[RollType](DesignData.SDS2.Model.RollType.html)

The type of roll made along the length of a material.

#### [](#rolledplatefabricationmethod)[RolledPlateFabricationMethod](DesignData.SDS2.Model.RolledPlateFabricationMethod.html)

Methods for fabricating rolled material

#### [](#safetyseatlocation)[SafetySeatLocation](DesignData.SDS2.Model.SafetySeatLocation.html)

Location options for where to place a safety seat with respect to the beam

#### [](#seatspecificationbottomchordrestraintmaterial)[SeatSpecificationBottomChordRestraintMaterial](DesignData.SDS2.Model.SeatSpecificationBottomChordRestraintMaterial.html)

Allowed materials for seated connections for joist bottom chord restraints

#### [](#seatspecificationmaterial)[SeatSpecificationMaterial](DesignData.SDS2.Model.SeatSpecificationMaterial.html)

Allowed materials for seated connection specifications

#### [](#seismicmomentframetype)[SeismicMomentFrameType](DesignData.SDS2.Model.SeismicMomentFrameType.html)

The seismic moment frame type for a member's seismic moment design

#### [](#shearmaterialtype)[ShearMaterialType](DesignData.SDS2.Model.ShearMaterialType.html)

Material types which can be used for shear tabs

#### [](#shearplateside)[ShearPlateSide](DesignData.SDS2.Model.ShearPlateSide.html)

Which side of the supported member to put the shear tab on

#### [](#shearsupportcondition)[ShearSupportCondition](DesignData.SDS2.Model.ShearSupportCondition.html)

For ASD9 and LRFD3 design codes.

#### [](#shearthroughplate)[ShearThroughPlate](DesignData.SDS2.Model.ShearThroughPlate.html)

Through plate options for shear tabs attaching to tubes

#### [](#shearweldtype)[ShearWeldType](DesignData.SDS2.Model.ShearWeldType.html)

Options for the weld on a shear tab

#### [](#stairconnectionlonglegto)[StairConnectionLongLegTo](DesignData.SDS2.Model.StairConnectionLongLegTo.html)

Long leg placement for stair connection clip angle material

#### [](#stairconnectionstringerside)[StairConnectionStringerSide](DesignData.SDS2.Model.StairConnectionStringerSide.html)

Stringer side placement for stair connection material

#### [](#stairstringerendcondition)[StairStringerEndCondition](DesignData.SDS2.Model.StairStringerEndCondition.html)

The options for stringer end conditions

#### [](#stiffclip)[StiffClip](DesignData.SDS2.Model.StiffClip.html)

Stiffener clip options

#### [](#stiffeneralignment)[StiffenerAlignment](DesignData.SDS2.Model.StiffenerAlignment.html)

Stiffener alignment options, whether it should be aligned to the beam or column, or if it should look to setup for which to align to

#### [](#stitchtype)[StitchType](DesignData.SDS2.Model.StitchType.html)

Enumerated weld stitch types

#### [](#stringerlength)[StringerLength](DesignData.SDS2.Model.StringerLength.html)

Enumeration denoting the stringer length reported in the stair's BOM.

#### [](#stringermark)[StringerMark](DesignData.SDS2.Model.StringerMark.html)

Enumeration denoting CNC marks to place on stair stringers.

#### [](#studtype)[StudType](DesignData.SDS2.Model.StudType.html)

Type of Stud.

#### [](#thicknessreferencepoint)[ThicknessReferencePoint](DesignData.SDS2.Model.ThicknessReferencePoint.html)

The reference plane from which a plate's thickness expands out.

#### [](#threaddirection)[ThreadDirection](DesignData.SDS2.Model.ThreadDirection.html)

Fastener thread direction

#### [](#threadtype)[ThreadType](DesignData.SDS2.Model.ThreadType.html)

Thread direction.

#### [](#toedirection)[ToeDirection](DesignData.SDS2.Model.ToeDirection.html)

For materials with a "toe" (such as a flange on one side) the toe direction is the direction these materials are flipped.

#### [](#toeio)[ToeIO](DesignData.SDS2.Model.ToeIO.html)

Toe I/O of Member.

#### [](#turnedshelllayoutreference)[TurnedShellLayoutReference](DesignData.SDS2.Model.TurnedShellLayoutReference.html)

The thickness reference for TurnedShellLayout material.

#### [](#ufmspecialcase)[UFMSpecialCase](DesignData.SDS2.Model.UFMSpecialCase.html)

A specification for how the system spreads the load between the connection and supporting column and beams.

#### [](#vertbracebeamclipsizespecification)[VertBraceBeamClipSizeSpecification](DesignData.SDS2.Model.VertBraceBeamClipSizeSpecification.html)

A specification for how a clip angle is sized when a vertical brace gusset plate connects to a column and beam.

#### [](#vertbracehssattachmentmethod)[VertBraceHssAttachmentMethod](DesignData.SDS2.Model.VertBraceHssAttachmentMethod.html)

A specification for how a HSS wide flange vertical brace connects to the gusset plate.

#### [](#vertbracesupportingattachmentmethod)[VertBraceSupportingAttachmentMethod](DesignData.SDS2.Model.VertBraceSupportingAttachmentMethod.html)

A specification for how a vertical brace gusset plate connects to the supporting member(s).

#### [](#vertbracewideflangeattachmentmethod)[VertBraceWideFlangeAttachmentMethod](DesignData.SDS2.Model.VertBraceWideFlangeAttachmentMethod.html)

A specification for how the flanges of a vertical wide flange brace connects to the gusset plate.

#### [](#vertbracewideflangehorzconnectionarrangement)[VertBraceWideFlangeHorzConnectionArrangement](DesignData.SDS2.Model.VertBraceWideFlangeHorzConnectionArrangement.html)

A specification for how a horizontal wide flange brace connects to the gusset plate.

#### [](#vertbracewideflangewebattachmentmethod)[VertBraceWideFlangeWebAttachmentMethod](DesignData.SDS2.Model.VertBraceWideFlangeWebAttachmentMethod.html)

A specification for how the web of a vertical wide flange brace connects to the gusset plate.

#### [](#verticalbraceplatetype)[VerticalBracePlateType](DesignData.SDS2.Model.VerticalBracePlateType.html)

Specifies a framing situation for a vertical brace connection with a gusset plate.

#### [](#viewprojectionuse)[ViewProjectionUse](DesignData.SDS2.Model.ViewProjectionUse.html)

View projection usages

#### [](#viewuse)[ViewUse](DesignData.SDS2.Model.ViewUse.html)

View usages

#### [](#washertype)[WasherType](DesignData.SDS2.Model.WasherType.html)

Enumeration of valid values for the WasherType attribute of Bolt.

#### [](#weldcontour)[WeldContour](DesignData.SDS2.Model.WeldContour.html)

Enumerated weld contours indicating contour symbols for a weld

#### [](#weldjointtype)[WeldJointType](DesignData.SDS2.Model.WeldJointType.html)

Enumerated weld joint types

#### [](#weldpenetrationtype)[WeldPenetrationType](DesignData.SDS2.Model.WeldPenetrationType.html)

Enumerated weld penetration types

#### [](#weldpositiontype)[WeldPositionType](DesignData.SDS2.Model.WeldPositionType.html)

Enumerated weld positions

#### [](#weldprocesstype)[WeldProcessType](DesignData.SDS2.Model.WeldProcessType.html)

Enumerated weld process types