# List projects

Work in SDS2 is organized in projects, and projects reside within repositories. When you embed SDS2, a basic step in your workflow will be to allow the user to select an existing project to work with.

Within the API, projects are often called Jobs.

The following code shows how to list all projects within all repositories.

```
using DesignData.SDS2.Database;

```

```
DataDirectory.Open(DataDirectory.Default);
var repositories = Repository.GetAllRepositories();
foreach( var repo in repositories )
    foreach( var id in repo.JobIdentifiers )
    {
        System.Console.WriteLine($"Repository \"{repo.Name}\": \"{id.Name}\"");
    }

```