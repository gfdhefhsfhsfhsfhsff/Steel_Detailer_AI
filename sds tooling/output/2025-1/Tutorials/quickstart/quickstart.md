# Open default project

To get right into the user's default project, we just need three simple lines of boilerplate code:

```
//open the system's default data directory
DataDirectory.Open(DataDirectory.Default);
//find the user's default job
var job = Job.FindJob(Job.Default);
//Open that job so we can access data in it
job.Open();

```

All of this is in the DesignData.SDS2.Database namespace:

```
using DesignData.SDS2.Database;

```