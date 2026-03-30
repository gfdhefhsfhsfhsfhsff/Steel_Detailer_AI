# Retrieve members

To read members, use a [ReadOnlyTransaction](../api/DesignData.SDS2.Database.ReadOnlyTransaction.html). There are two static methods of [Member](../api/DesignData.SDS2.Model.Member.html) and [MemberBrief](../api/DesignData.SDS2.Model.MemberBrief.html) that may be used to read members: [Get()](../api/DesignData.SDS2.Model.Member.html#DesignData%5FSDS2%5FModel%5FMember%5FGet%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F) returns a full Member object, and [GetBrief()](../api/DesignData.SDS2.Model.MemberBrief.html#DesignData%5FSDS2%5FModel%5FMemberBrief%5FGet%5FDesignData%5FSDS2%5FDatabase%5FMemberHandle%5F) returns a fixed-size object of type MemberBrief which has a subset of the fields of Member. MemberBrief is intended for use in performance sensitive situations, as it is faster than Member. Member objects returned by `Member.Get()` may be cast to derived types such as Beam and Column where MemberBrief objects returned by `MemberBrief.Get()`cannot.

```
using DesignData.SDS2.Database;
using DesignData.SDS2.Model;

```

```
[STAThread]
static void Main(string[] args)
{
    DataDirectory.Open(DataDirectory.Default);
    var job = Job.FindJob(Job.Default);
    job.Open();

    using(var reader = new ReadOnlyTransaction(job))
    {
        foreach( var handle in job.Members)
        {
            // var member = MemberBrief.Get(handle);
            // System.Console.WriteLine(
            //     $"Member number:{handle.Index} pcmk:{member.Piecemark}");
            var member = Member.Get(handle);
            var mtrl_count = member.GetMaterial().Count;
            System.Console.WriteLine(
                $"Member number:{handle.Index} pcmk:{member.Piecemark} mtrl:{mtrl_count}");
        }
    }
}

```