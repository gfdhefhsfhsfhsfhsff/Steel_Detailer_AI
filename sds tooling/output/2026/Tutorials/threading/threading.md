# Threading and SDS2 API objects

## [](#single-threaded-apartment)Single Threaded Apartment

We recommend that you configure your application with \[STAThread\]. MTAThread introduces some race conditions into our startup procedure.

<https://docs.microsoft.com/en-us/dotnet/api/system.stathreadattribute>

## [](#thread-safety)Thread safety

The SDS2 API is **not** thread safe. This means that the API doesn't do any checking when calls are made to make sure there are no conflicts between threads. The API assumes it's only called from a single thread, or if called from multiple threads those threads are using mutexes (lock(object)) to prevent multiple threads from calling into the API at once.

## [](#lockobject-and-proxy-objects)lock(object) and proxy objects

The SDS2 API makes heavy use of proxy objects without a guarantee that each time you fetch an object you get the same .net object. Often you get a new proxy object pointing at the same underlying SDS2 object. You can lock() these, but it's not recommended because a lock() on two different proxy objects pointing at the same SDS2 object will not cause a mutual exclusion. Because csharp's lock() only acts on the .net proxy objects.

So we recommend you create your own object to pass to lock and use that to create a mutual exclusion if you intend to access the SDS2 API from multiple threads. A single object to lock the whole SDS2 API would be the safest model.

### [](#good-example)Good example

```
//one global lock object for the SDS2 API
static private object SDS2_API = new object();
static void ThreadWorker()
{
    lock(SDS2_API) //globally lock the SDS2 API safely.
    {              //take care that you only end up with ONE
                   //SDS2_API variable in your whole program.
        var job = Job.FindJob(Job.Default);
        using(var reader = new ReadOnlyTransaction(job))
        {
            var member = Member.Get(job.Members[0]);
            //if our mutual exclusion works this then we'll see independent
            //lines, if not, then we will see a jumbled mess:
            foreach(char ch in member.Piecemark)
            {
                Console.Write(ch);
                System.Threading.Thread.Sleep(100);
            }
            Console.WriteLine("");
        }
    }
}

[STAThread]
static void Main(string[] args)
{
    DataDirectory.Open(DataDirectory.Default);
    var job = Job.FindJob(Job.Default);
    job.Open();

    List<System.Threading.Tasks.Task> threads = new List<System.Threading.Tasks.Task>();
    for(int i=0; i < 10; ++i)
    {
        threads.Add(System.Threading.Tasks.Task.Run(ThreadWorker));
    }
    foreach(var task in threads)
        task.Wait();
}

```

This outputs (in a job where member 1 is 15C1):

```
15C1
15C1
15C1
15C1
15C1
15C1
15C1
15C1
15C1
15C1

```

### [](#bad-example)Bad example

This example doesn't even run, it tends to just crash because SDS2 crashes trying to read the member at once in multiple threads.

```
static void ThreadWorker(Member member)
{
    var job = Job.FindJob(Job.Default);
    lock(job) //this job ref will be unique in every call
    {         //even though it refers to a single underlying
              //SDS2 job object, because we return proxy objects
              //in most cases.
        //if our mutual exclusion works this then we'll see independent
        //lines, if not, then we will see a jumbled mess:
        foreach(char ch in member.Piecemark)
        {
            Console.Write(ch);
            System.Threading.Thread.Sleep(100);
        }
        Console.WriteLine("");
    }
}

static void Main(string[] args)
{
    DataDirectory.Open(DataDirectory.Default);
    var job = Job.FindJob(Job.Default);
    job.Open();
    Member member;
    //doing our read up front to give this any chance of not crashing:
    using(var reader = new ReadOnlyTransaction(job))
    {
        reader.RefreshTable(Table.Member);
        member = Member.Get(job.Members[0]);
    }
    List<System.Threading.Tasks.Task> threads = new List<System.Threading.Tasks.Task>();
    for(int i=0; i < 10; ++i)
    {
        threads.Add(System.Threading.Tasks.Task.Run(() => ThreadWorker(member)));
    }
    foreach(var task in threads)
        task.Wait();
}

```