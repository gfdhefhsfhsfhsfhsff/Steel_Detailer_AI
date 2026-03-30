# Adding welds

Welds can be added by simplying specifiying the materials involved in the weld. Or you can have more control over the weld path by specifying a list of segments.

The code below creates a two plates orthogonal to each other and a third plate skewed by 15 degrees.

```
using(var transaction =
      new Database.Transaction(job, new Database.ImmediateLockHandler()))
{
        var member = new Model.Beam();
        member.Shape = Setup.MaterialFile.Get().Find("W12x22");
        member.Ends[0].Location = new Primitives.Point3D(0.0, -60.0, 0.0);
        member.Ends[1].Location = new Primitives.Point3D(60.0, -60.0, 0.0);

        var toGlobal = Primitives.Matrix.XRotation(-Math.PI/2) * member.ToGlobalCoordinates;

        var seated_plate = new Model.RectangularPlate();
        seated_plate.Width = 6.0;
        seated_plate.Thickness = 0.25;
        seated_plate.WorkpointLength = 6.0;
        seated_plate.ToGlobalCoordinates = (
            Primitives.Matrix.ToCoordinateSystemXY(
                new Primitives.Point3D(0.0, 3.0, 0.0),
                new Primitives.Vector3D(1.0, 0.0, 0.0),
                new Primitives.Vector3D(0.0, 1.0, 0.0)
                )
            * toGlobal
            );

        var back_plate = new Model.RectangularPlate();
        back_plate.Width = 4.25;
        back_plate.Thickness = 0.25;
        back_plate.WorkpointLength = 6.0;
        back_plate.ToGlobalCoordinates = (
            Primitives.Matrix.ToCoordinateSystemXY(
                new Primitives.Point3D(0.0, -3.0, 0.0),
                new Primitives.Vector3D(0.0, 1.0, 0.0),
                new Primitives.Vector3D(0.0, 0.0, -1.0)
                )
            * toGlobal
            );

        var skewed_plate = new Model.RectangularPlate();
        skewed_plate.Width = 6.0;
        skewed_plate.Thickness = 0.25;
        skewed_plate.WorkpointLength = 4.0;
        var cope = new Model.ClipPlate();
        cope.Length = 0.25;
        cope.Width = 0.5;
        skewed_plate.Ends[0].TopPlateCutOperation = cope;
        skewed_plate.ToGlobalCoordinates = (
            Primitives.Matrix.ToCoordinateSystemXY(
                new Primitives.Point3D(0.0, 0.0, 0.25),
                new Primitives.Vector3D(0.0, 0.0, 1.0),
                new Primitives.Vector3D(-1.0, 0.0, 0.0)
                )
            * Primitives.Matrix.Rotation(15.0 * Math.PI / 180.0, new Primitives.Vector3D(0.0, 0.0, 1.0))
            * toGlobal
            );

        member.Add(seated_plate);
        member.Add(back_plate);
        member.Add(skewed_plate);
        transaction.Add(member);
        transaction.Lock();
        transaction.Commit(true);  // welds require valid material handles, so commit the new materials

```

The code below welds two of the plates by letting SDS2 determine the weld path

```
    var weld_size = 0.25;
    // Create welds from the seated plate to the back plate and skew plate
    // using SDS2 builtin weld path logic
    var seated_plate_welds = new Model.WeldPathSpecification();
    seated_plate_welds.CreateDistinctWeldsPerSegment = false;
    var seated_plate_arrow = seated_plate_welds.ArrowSide;
    seated_plate_arrow.WeldSize = weld_size;
    seated_plate_arrow.WeldType = Setup.WeldType.Fillet;
    var back_and_skew = new Model.MaterialList();
    back_and_skew.Add(back_plate);
    back_and_skew.Add(skewed_plate);
    seated_plate_welds.GenerateWelds(seated_plate, back_and_skew);

```

Weld paths can also be explicitly specified by setting WeldPathSpecification.Segments. These segments do not have to touch each. For example, one weld can be used to generate one segment on the near side of a plate and a second segment can be used to generate the weld on the far side of a plate (all segments use the same weld type, weld size, contour, etc).

There are three helper functions to help create individual segments of the weld path. See WeldPathSegment.FromLayout(), WeldPathSegment.FromFilletSegment(), and WeldProfileFillet.FromPlanes() plus WeldProfileFillet.GetWeldPathSegment(). The code below illustrates creating two different segments via FromFilletSegment and FromPlanes.

```
    // Create skewed fillet weld for the skew plate to the back plate
    var skewed_welds = new Model.WeldPathSpecification();
    skewed_welds.CreateDistinctWeldsPerSegment = false;
    var arrow = skewed_welds.ArrowSide;
    arrow.WeldSize = weld_size;
    arrow.WeldType = Setup.WeldType.Fillet;
    var segments = skewed_welds.Segments;  // new WeldPathSegmentList();
    var skewed_plate_to_global = skewed_plate.ToGlobalCoordinates;
    var skewed_plate_origin = skewed_plate_to_global.Origin;
    var skewed_plate_x = skewed_plate_to_global.XAxis;
    var skewed_plate_ns = skewed_plate_to_global.ZAxis;
    var skewed_plate_fs = -skewed_plate_ns;
    var fs_segment_endpoint0 = (
            skewed_plate_origin
            + skewed_plate_x * weld_size
            );
    var fs_segment_endpoint1 = (
            fs_segment_endpoint0
            + skewed_plate_x * (skewed_plate.WorkpointLength - weld_size)
            );
    var back_plate_to_global = back_plate.ToGlobalCoordinates;
    var back_plate_fs = -back_plate_to_global.ZAxis;
    // In this example the far side edge of the skew plate touches
    // the far side surface of the back plate
    // Use the WeldPathSegment factory for two points on a
    // segment and two surface normals to create ths far side segment
    var fs_segment = Model.WeldPathSegment.FromFilletSegment(
            fs_segment_endpoint0,
            fs_segment_endpoint1,
            back_plate_fs,
            skewed_plate_fs,
            weld_size);
    segments.Add(fs_segment);
    var segment_length = 4.0 - weld_size;
    // Another way to create a segment is to create an
    // intermediate WeldProfileFillet from two planes
    // The Root of the profile will be closest to the
    // point specified for the first plane, so this
    // example picks a point on the skewed plate's near
    // side that will be result in a
    // WeldPathSegment.ToGlobalCoordinates
    // Origin and XAxis that generates the correct weld
    var ns_profile = Model.WeldProfileFillet.FromPlanes(
            fs_segment_endpoint1
                + skewed_plate_ns * skewed_plate.Thickness
                + skewed_plate_x * -segment_length,
            skewed_plate_ns,
            back_plate_to_global.Origin,
            back_plate_fs);
    // Then convert the profile to a WeldPathSegment
    var ns_segment = ns_profile.GetWeldPathSegment(segment_length, weld_size);
    segments.Add(ns_segment);
    skewed_welds.Segments = segments;
    var only_back_plate = new Model.MaterialList();
    only_back_plate.Add(back_plate);
    
    skewed_welds.GenerateWelds(skewed_plate, only_back_plate);
    transaction.Commit(false);  // no need to process

```