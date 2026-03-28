# Open a project

SDS2 has a single global project that most of the API uses implicitly. The following code demonstrates how to set this global project (or "Job").

```
static Job OpenNamedJob(string repoName, string jobName)
{
    var repositories = Repository.GetAllRepositories();
    Identifier jobId = null;
    foreach (var repo in repositories)
    {
        if(repo.Name != repoName) continue;
        foreach (var id in repo.JobIdentifiers)
        {
            if(id.Name == jobName)
            {
                jobId = id;
            }
        }
    }
    var job = Job.FindJob(jobId);
    job.Open(); // Set this job as the global job.
    return job;
}

[STAThread]
static void Main(string[] args)
{
    DataDirectory.Open(DataDirectory.Default);
    var job = OpenNamedJob("Default Repository", "Building_101j");
    System.Console.WriteLine($"Job has {job.Members.Count} members");
}

```