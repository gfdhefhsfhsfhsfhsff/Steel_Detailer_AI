# Editing a group of holes

When editing a holes, you typically want to edit the entire group of holes at once. The following code illustrates changing a group of blind holes into threaded holes.

```
var group_holes = group.GetHoles();
foreach(Hole h in group_holes)
{
    transaction.Add(h);
}
transaction.Lock();
foreach(Hole h in group_holes)
{
    // turn off blind holes
    // can set IsBlind indirectly via Operations or direclty via IsBlind
    h.IsBlind = false;
    // when turning off blind holes we have to update the hole length
    // this group goes through a surface that is 1.25" thick
    h.Length = 1.25;
    // turn on threads
    var threads = new HoleMachineOperationThreads();
    threads.Size = 5.0 / 16.0;
    threads.ThreadsPerUnit = 16;
    threads.Series = HoleMachineOperationThreadSeries.UNC;
    threads.FitClass = "2";
    threads.IsLeftHanded = false;
    threads.Depth = 0.25;
    var ops = h.GetOperations();  // returns a deep copy
    ops.SetThreads(threads);  // sets a deep copy
    h.SetOperations(ops);  // sets a deep copy
}

```