# Update members

To update members, use a [Transaction](../api/DesignData.SDS2.Database.Transaction.html). Transaction objects are similar to [ReadOnlyTransaction](../api/DesignData.SDS2.Database.ReadOnlyTransaction.html) objects, but with additional [Add()](../api/DesignData.SDS2.Database.Transaction.html#DesignData%5FSDS2%5FDatabase%5FTransaction%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FBoltHandle%5F), [Lock()](../api/DesignData.SDS2.Database.Transaction.html#DesignData%5FSDS2%5FDatabase%5FTransaction%5FLock), and [Commit()](../api/DesignData.SDS2.Database.Transaction.html#DesignData%5FSDS2%5FDatabase%5FTransaction%5FCommit%5FSystem%5FBoolean%5F) methods, to allow writing changes to the database.

Transaction objects must be defined with a `using` statement to ensure locks are released at the end of the code block.

```
using DateTime = System.Nullable<System.DateTime>;

```

```
/// <summary>
///   Set the ModelCompleteDate of all members in a job using a
///   single Transaction.
/// </summary>
static void SetModelCompleteAtomically( Job job, DateTime date )
{
    using(var transaction = new Transaction(job, new ImmediateLockHandler()))
    {
        // Don't read job.Members separately for each loop; the
        // members in the job could change, and we rely here
        // on the list being the same for both loops.
        var handles = job.Members;
        foreach(var handle in handles)
            transaction.Add(handle);

        if( transaction.Lock() )
        {
            int count = 0;
            var today = System.DateTime.Today;
            foreach(var handle in handles)
            {
                var member = MemberBrief.Get(handle);
                if( member.ModelCompleteDate != date)
                {
                    count++;
                    member.ModelCompleteDate = today;
                }
            }

            if( transaction.Commit())
                System.Console.WriteLine(
                    $"Set ModelComplete on {count} members.");
            else
                System.Console.WriteLine("Unable to commit transaction.");
        }
        else
        {
            System.Console.WriteLine("Unable to lock a transaction item.");
        }
    } // End of transaction scope
}

/// <summary>
///   Set the ModelCompleteDate of all members in a job using
///   one Transaction per member.
/// </summary>
static void SetModelCompleteIncrementally( Job job,
                                           DateTime date )
{
    var handles = job.Members;
    int count = 0;
    var today = System.DateTime.Today;
    foreach(var handle in handles)
    {
        using(var transaction = new Transaction(job, new ImmediateLockHandler()))
        {
            transaction.Add(handle);
            if( transaction.Lock())
            {
                MemberBrief member = MemberBrief.Get(handle);
                if( member.ModelCompleteDate == date )
                    continue;

                member.ModelCompleteDate = date;
                if( transaction.Commit())
                {
                    count++;
                    System.Console.WriteLine(
                        $"Set ModelComplete on [{handle.Index}] {member.Piecemark}.");
                }
            }
        }
    }
    System.Console.WriteLine($"Updated {count} members.");
}

[STAThread]
static void Main(string[] args)
{
    DataDirectory.Open(DataDirectory.Default);
    var job = OpenNamedJob("Default Repository", "Building_101j");
    DateTime date = System.DateTime.Today;
    SetModelCompleteIncrementally(job, date);
    date = null;
    SetModelCompleteAtomically(job, date);
}

```