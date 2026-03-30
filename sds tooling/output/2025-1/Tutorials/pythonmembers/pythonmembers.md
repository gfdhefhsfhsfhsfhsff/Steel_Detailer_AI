# Python custom members

Working with members implemented in Python is very different from builtin members. Since these are implemented in Python, and are often implemented outside of SDS2, we can't offer a proper .Net interface.

What we provide instead of access to these as csharp dynamic types. This lets you do just about anything in .Net to them that you could do in Python (exceptions include: inheritance).

To access an attribute, just get the dynamic python object, and then access that attribute and cast it to the type you know it is:

```
using DesignData.SDS2.Database;
using DesignData.SDS2.Model;

```

```
static string GetHandRailPostMtrlType(Job job, int memberNumber)
{
    using(var reader = new ReadOnlyTransaction(job))
    {
        var handle = new MemberHandle(memberNumber);
        PythonMember memberObject =
            Member.Get(handle)
            as PythonMember;
        dynamic handRail = memberObject.PythonObject;

        return (string)handRail.post_mtrl_type;
    }
}

```

To call a function, just call that function naturally on the dynamic python object:

```
static string CalculateHandRailPiecemark(Job job, int memberNumber, int number)
{
    using(var reader = new ReadOnlyTransaction(job))
    {
        var handle = new MemberHandle(memberNumber);
        PythonMember memberObject =
            Member.Get(handle)
            as PythonMember;
        dynamic handRail = memberObject.PythonObject;

        return (string)handRail.Piecemark(number);
    }
}

```

You can also modify custom members following the same rules as you use for builtin members:

```
static void SetHandRailWalkSide(Job job, int memberNumber, string walkside)
{
    using(var xaction = new Transaction(job, new ImmediateLockHandler()))
    {
        var handle = new MemberHandle(memberNumber);
        xaction.Add(handle);
        xaction.Lock();
        PythonMember memberObject =
            Member.Get(handle)
            as PythonMember;
        dynamic handRail = memberObject.PythonObject;
        handRail.walkside = walkside;
        xaction.Commit(processMembers:true);
    }
}

```