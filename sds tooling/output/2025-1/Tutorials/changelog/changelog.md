# Changelog

## [](#2025)2025

### [](#sidp-379482)SIDP-379482

Fixed a bug where the "AllShapes" method on the Setup.MaterialFile class would throw if the materialfile/shapes file contained a joist shape which had a chord section that was not in the shapes file. It will now give you that joist shape, and the property for that chord shape will be null.

## [](#2023i)2023i

### [](#w1080516829)W1080516829

Added GetPromptTabForLockableName and GetPromptGroupForLockableName. NOTE: These are intended for debugging purposes only and should not be used in production.

### [](#w1082959545)W1082959545

Exposed column member end "member setback" and "material setback" properties via a Model.ColumnEnd object. The enum ColumnEnd is moved to Database namespace.

### [](#w1080534977)W1080534977

Exposed lockable image label.

### [](#w1067944993)W1067944993

Exposed connection failure messages and connection changed messages on ConnectionComponent.

### [](#w1080494192)W1080494192

Exposed additional moment connection properties for Eurocode jobs

## [](#2023)2023

### [](#w820094248)W820094248

New MemberBrief properties SurfaceFinish and IsAutoSurfaceFinish. New Material property IsAutoSurfaceFinish.

### [](#w820130069)W820130069

New finishes can be added to setup via Setup.Job.Add(SurfaceFinish). New Setup.Job.DefaultSurfaceFinish property.

### [](#w1010018149)W1010018149

Fixed a bug where drawings that contained images would crash when exporting as a PDF from the API. This bug was fixed by forcing the APIs gl backend to be software.

### [](#w1021690341)W1021690341

Model.WeldPathSpecification is used to add welds by specifiying the materials to weld together or by specifying a list of WeldPathSegment for more control over the weld geometry.

### [](#w999154921)W999154921

When setting lockables on a ConnectionComponent, we will now validate the values given. If the value is outside of the range for that specific value it will throw InvalidValueError with the same message we would present a user with if they had typed that value in.

### [](#w1015825824)W1015825824

Setting lockables on a Component now requires that you've added that Component to a Transaction before attempting to set any lockables. This also applies to setting the input specification. In previous releases, this was allowed, but your changes would likely be dropped.

Warning: This is a substantial change, or was for our own tests. If you have code that sets the connection type, connection specification properties, or lockables on connections we suggest you look over that code and check if you need to add the Component you're modifying to the transaction.

So you might have code like either of the following two examples

```
	//EXAMPLE 1
	var beam = Member.Get(job.Members[5]) as Beam;
	xaction.Add(beam);
	xaction.Lock();

	beam.Ends[1].ConnectionComponent.InputSpecification = new ShearTabSpecification();
	xaction.Commit(processMembers:true);

	//EXAMPLE 2
	var beam = new Beam();
	xaction.Add(beam);
	xaction.Lock();
	xaction.Commit(processMembers:true);

	bream.End1[0].ConnectionComponent.InputSpecification = new ShearTabSpecification();
	xaction.Commit(processMembers:true);

```

These have to be changed such that the ConnectionComponent is added to the transaction and locked:

```
	//EXAMPLE 1
	var beam = Member.Get(job.Members[5]) as Beam;
	xaction.Add(beam);
        //this member already exists and is processed, we can add the component here
        xaction.Add(beam.Ends[1].ConnectionComponent);
	xaction.Lock();

	beam.Ends[1].ConnectionComponent.InputSpecification = new ShearTabSpecification();
	xaction.Commit(processMembers:true);

	//EXAMPLE 2
	var beam = new Beam();
	xaction.Add(beam);
	xaction.Lock();
	xaction.Commit(processMembers:true);

        //this member is new, and has to be processed before connection changes can be made
        xaction.Add(beam);
        xaction.Lock();
	bream.End1[0].ConnectionComponent.InputSpecification = new ShearTabSpecification();
	xaction.Commit(processMembers:true);

```

### [](#w950150501)W950150501

Added new class to DesignData.SDS2.Setup called UserSettings. This tracks settings from the user options screen. Currently it just exposed whether the user has chosen light or dark mode.

### [](#w983039707)W983039707

Exposed IsHeld, SubmittedForApproval, and ReceivedForApproval on the MemberBrief object.

###W1004937537

When calling DesignData.SDS2.Python.Module.Import with a module name that does NOT exist, instead of throwing an unhelpful generic exception about a "program error" we now pass on the python exception that occurred as a DesignData.SDS2.Exceptions.PythonException. This should make debugging easier and make improve code that's trying to handle an expected module being missing.

###W1001539243

When calling Transaction.Commit with processMembers:true, SDS2 will now always process the members involved. Previously it wasn't processing if the user had turned process off after modeling operations inside user settings.

### [](#w907011555)W907011555

Updated the Hole API to use the new HoleMachineOperations class instead of a list of HoleOperation objects.

### [](#w907007478)W907007478

Changed HoleGroup.PreferredBoltType from an int to a Setup.BoltType. Previously int was an index into setup's list of bolt types and -1 indicated the group should use the job's "auto" bolt type. Now, "auto" is indicated by a new property IsAutoPreferredBoltType and PreferredBoltType will be a reference to a Setup.BoltType instance.

### [](#w907007814)W907007814

Fixed a bug where holes were always == to each other. Now they are equal if there handles are ==

## [](#2022i)2022i

### [](#w874205381)W874205381

Added the IsDummy property to the Material class in the DesignData.SDS2.Model namepsace.

### [](#w864910000)W864910000

Add ability to read governing (max) loads. Properties added to the ConnectionComponent class in the DesignData.SDS2.Model namespace. New properties exposed: MaxMoment, MaxCompression, MaxTyingResistance, MaxPanelMoment, MaxTension, MaxShear, MaxTensionUnity, MaxCompressionUnity, MaxShearUnity, MaxMomentUnity, MaxTyingResistanceUnity, MaxPanelMomentUnity.

## [](#2022)2022

### [](#w813510680)W813510680

Representing surfaces finishes with the eunum Setup.MaterialSurfaceFinish is deprecated and now will be represented with a new class Setup.SurfaceFinish. We've deprecated methods and properties that have MaterialSurfaceFinish in the signature and introduced new methods and properties with new signatures using Setup.SurfaceFinish.

### [](#w791263644)W791263644

Attempting to get a list of Repository objects or open a Job before calling DataDirectory.Open will now result in an InvalidOperationException. This is because, without opening a data directory, SDS2 will have difficult to debug problems once you start working with the database of a job.

### [](#w738535480)W738535480

SDS2 licensing with 10duke now requires login credentials (username and password) to get a license, and that includes API2 licenses. So 3rd party programs using the SDS2 API now need to prompt (if credentials aren't set). See [end of Configure an Application tutorial](configure.html) or [documentation on the helper](../api/DesignData.SDS2.WinForms.LicensingInitialization.html) or [the Licensing class documentation.](../api/DesignData.SDS2.Database.Licensing.html)

### [](#w718817710---enum-modelviewdescription-has-been-deprecated)W718817710 - enum ModelViewDescription has been deprecated

This enumeration has been deprecated in favor of the IFC standard name `ModelViewDefinition`. A boxing class is provided to let existing code compile, with obsoletion warnings.

The `modelViewDescription` parameter of `IFC2x3.Export` and `IFC4.Export` has been renamed to `modelViewDefinition`. If you are directly referencing the `modelViewDescription` parameter, this will need to be upated.

### [](#w726082413---enum-modelcustompropertyvaluetype-moved-to-setupcustompropertyvaluetype)W726082413 - enum Model.CustomPropertyValueType moved to Setup.CustomPropertyValueType

This enumeration was moved into setup to support CustomPropertySchema being a setup type. There is a boxing class left behind to smooth existing code (most existing code should compile with obsoletion warnings).

But code should be adjusted to refer to the new type. The obsolete type will be removed in a future version.

### [](#w702801408---modelclipanglespecificationextendpastflange-renamed-to-usewebextensionplate)W702801408 - Model.ClipAngleSpecification.ExtendPastFlange renamed to UseWebExtensionPlate

This property is being renamed to better represent its function and match the rename in the model. An obsoleted property exists for the old property but will be removed in a future version. To resolve this just swap out the old property name for the new one.

### [](#w729005717---read-get-access-to-objects-between-transactionadd-and-transactionlock)W729005717 - read (get) access to objects between Transaction.Add() and Transaction.Lock

Previously, calling a getter on an object after adding it to the transaction, but before locking the transaction would result in an exception. This has been changed, and this is now allowed.

### [](#w692236868---memberends-returns-most-derived-type)W692236868 - Member.Ends returns most derived type

Previously, calling .Ends on a member would return objects of type MemberEnd. Now it will return a BeamEnd if the member is actually a Beam, and HorizontalBraceEnd if it's a HorizontalBrace and VerticalBraceEnd if it's a VerticalBrace.

### [](#w688146930---non-builtin-members-return-null-for-their-grades)W688146930 - Non-builtin members return null for their grades

The SteelGrade returned on MemberBrief was returning the default steel grade for non-steel member types and for steel member types (such as handrail) which don't use that value. This has been changed and now only members which use that field return a SteelGrade from MemberBrief.Grade. Others simply return null.

## [](#202102-beta-2)2021.02 (Beta 2)

1. Most objects no longer implement IDisposable. ReadOnlyTransaction and Transaction still implement IDisposable and should still be used with a using statement. Other objects do not. There resources will be cleaned up with normal garbage collection.

## [](#202101-beta-1)2021.01 (Beta 1)

1. Initial release