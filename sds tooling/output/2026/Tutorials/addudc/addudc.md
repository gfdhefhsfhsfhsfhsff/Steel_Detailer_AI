# Adding a new user defined connection to a job

First we create a new UDC (user defined connection) within a transaction and commit it. We have to commit it before we can apply it to any members.

```
using(var xaction =
      new Database.Transaction(job, new Database.ImmediateLockHandler()))
{
    //the name (string literal) here will show up in the list user's pick from:
    var udc = new Model.UserDefinedConnection("clip angle");

    //be sure to set your condition BEFORE your input spec:
    udc.Condition.MemberType = Setup.MemberType.Beam;
    udc.Condition.MaterialType = Setup.MaterialType.WideFlange;

    //same ClipAngleSpecification we'd apply to the end of a beam in place:
    var clipangle = new Model.ClipAngleSpecification();
    //set any properties you need on clipangle here

    //we need to do this before we try to set lockables
    udc.SetInputSpecification(clipangle);

    //now we can start setting lockables
    var rows_osl = new Model.LockableInt();
    rows_osl.Value = 6;
    //when making a UDC, the LockType should ALWAYS be ViaUserDefined.
    rows_osl.LockType = Model.LockType.ViaUserDefined;
    udc.SetLockable("ns.rows_osl", rows_osl);

    //this Add is from an extension method in the DesignData.SDS2.Model namespace
    xaction.Add(udc);
    xaction.Lock();
    xaction.Commit();

```

Here are the members we create to apply this UDC to:

```
    var mtrl_file = Setup.MaterialFile.Get();
    var column = new Model.Column();
    column.Shape = mtrl_file.Find("W10x49");
    column.Ends[0].Location = new Primitives.Point3D();
    column.Ends[1].Location = new Primitives.Point3D(0.0, 0.0, 120.0);
    
    var column2 = new Model.Column();
    column2.Shape = mtrl_file.Find("W10x49");
    column2.Ends[0].Location = new Primitives.Point3D(120.0, 0.0, 0.0);
    column2.Ends[1].Location = new Primitives.Point3D(120.0, 0.0, 120.0);
    
    var beam = new Model.Beam();
    beam.Shape = mtrl_file.Find("W16x26");
    beam.Ends[0].Location = new Primitives.Point3D(0.0, 0.0, 60.0);
    beam.Ends[1].Location = new Primitives.Point3D(120.0, 0.0, 60.0);
    beam.Ends[0].IsAutoShearLoad = true;
    beam.Ends[1].IsAutoShearLoad = true;

```

And now we can apply this UDC to members (new or existing). We do this by getting the left or right end component and use a UserDefinedSpecification to apply the UDC. If we still have a reference to the original object we can use that, or we can look it up using [UserDefinedConnection.Find](../api/DesignData.SDS2.Model.UserDefinedConnection.html#DesignData%5FSDS2%5FModel%5FUserDefinedConnection%5FFind%5FSystem%5FString%5F).

```
    var cs = new Model.UserDefinedSpecification();
    //udc here is the variable created earlier, this could also be:
    //cs.UserDefinedConnection = Model.UserDefinedConnection.Find("clip angle");
    cs.UserDefinedConnection = udc;
    var beamcomponents = beam.GetComponents();
    var leftend = beamcomponents[0] as Model.ConnectionComponent;
    leftend.InputSpecification = cs;

```

And finally we commit like normal, making sure to process members so we can see our results right away.

```
    xaction.Add(column);
    xaction.Add(column2);
    xaction.Add(beam);
    xaction.Lock();
    xaction.Commit(processMembers:true);
}

```

The using declarations used for this. The "using DesignData.SDS2.Model" is necessary to get the extension method Add on Transaction for the UDC.

```
using System;
using DesignData.SDS2.Model;
using Database = DesignData.SDS2.Database;
using Setup = DesignData.SDS2.Setup;
using Model = DesignData.SDS2.Model;
using Primitives = DesignData.SDS2.Primitives;

```