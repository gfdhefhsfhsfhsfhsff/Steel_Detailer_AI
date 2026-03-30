# Connection specifications

To set the connection type you need to assign a new object, of a type derived from [ConnectionSpecification](../api/DesignData.SDS2.Model.ConnectionSpecification.html), to the [InputSpecification](../api/DesignData.SDS2.Model.ConnectionComponent.html#DesignData%5FSDS2%5FModel%5FConnectionComponent%5FInputSpecification) property of a ConnectionComponent. This can be done on existing member objects, or newly created members that haven't yet been added.

```
static void SetConnectionSpec(Job job, int memberNumber)
{
    using(var transaction = new Transaction(job, new ImmediateLockHandler()))
    {
        var handle = new MemberHandle(memberNumber);
        Member member = Member.Get(handle);
        transaction.Add(member);
        transaction.Add(member.Ends[0].ConnectionComponent);
        transaction.Lock();
        ConnectionComponent left = member.Ends[0].ConnectionComponent;
        //set the left end connection to a shear tab:
        ShearTabSpecification shear = new ShearTabSpecification();
        left.InputSpecification = shear;

        //to see the impact of your change, you must process members with this change:
        transaction.Commit(processMembers:true);
    }
}

```