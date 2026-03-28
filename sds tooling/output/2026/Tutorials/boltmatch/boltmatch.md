# Adding holes and bolts to material

Let's walk through adding two plates, putting holes in them, and bolting them together. This example leaves out transaction work. Before adding plates to a member it needs to be added to a transaction and lock needs to be called. And before passing bolts to BoltMatchSpecification.Fasten those material must be committed to the database, so you would also need to call Commit on a transaction between the code hunks shown.

First let's add plates to a member in the job ("member" in this example is of type DesignData.SDS2.Model.Member):

```

//a simple grid hole pattern with 9 holes and 3" spacing
//flowing down and to the right from the point it's located at:
var pattern = HolePattern.GridPattern(HolePatternRelativeGridPosition.AboveLeft,
                                      3, 0.0, 3.0,
                                      3, 0.0, 3.0);
pattern.HoleDiameter = 1.0;
pattern.BoltDiameter = 0.75;
//a minimal, but non-zero, surface gap
pattern.MaximumSurfaceGap = 0.001;

//going to add identical plates, right up to each other and drill
//holes using the same hole pattern
var plates = new MaterialList();
for(int i=0; i < 2; ++i)
{
    var plate = new RectangularPlate();
    //a comically large and thin plate
    plate.Width = 120.0;
    plate.Thickness = 0.25;
    plate.WorkpointLength = 120.0;

    //set a plate location and orientation
    var xrot_pi_2 = Matrix.XRotation(Math.PI/2);
    var xlate = Matrix.Translation(new Point3D(0.0, -24.0, 0.25*i));
    plate.ToGlobalCoordinates = xlate * xrot_pi_2 * member.ToGlobalCoordinates;

    //base the holes on the plate's location and orientation, but 5 feet in and down
    pattern.ToGlobalCoordinates = plate.ToGlobalCoordinates * Matrix.Translation(new Point3D(60.0, 60.0, 0.0));
    plate.Drill(pattern);
    member.Add(plate);
    plates.Add(plate); //need to know which plates are ours to bolt match later
}

```

Now we can fasten these two plates together using any holes that lineup (which should be all of the holes we just added):

```
var bolt_spec = new BoltMatchSpecification();
//set properties on the bolt match spec
//this could also be done in the loop below with the same result,
//these are just a convenient way to set some common properties:
bolt_spec.IsTensionControl = true;
//this chooses direction of the bolt based on the first material
//in the list plates.  Normally the bolt head goes on that side,
//but if you set this to false it goes the other way.
bolt_spec.IsFirstMaterialUnderHead = false;
var bolts = BoltMatchSpecification.Fasten(bolt_spec, plates);
foreach(var bolt in bolts)
{
    //add a head washer to every bolt we added
    bolt.AddWasherHead();
}

```

And when you're done you will need to commit your transaction. The bolts created by Fasten are already added to the member.