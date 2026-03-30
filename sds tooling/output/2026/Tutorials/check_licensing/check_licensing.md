# Check Licensing

You can use the SDS2 License API to check which api features are available. Currently there are five license features that can be checked:

1. API - Provides basic functionality, such as read/write/add members, materials, be checked via the `Licensing.IsLicensed` property
2. Detailing - Allows creation of new drawings.
3. Processing - Allows member processing through the API. Without this feature, `Transaction.Commit(processMembers:true)` will throw a `` NotLicensedException`.` ``
4. ModelLink - Allows for exporting data from the model in various formats.
5. Toolbox - Grants access to python plugins toolbox.

The following code demonstrates how to check what license features are available.

```
using DesignData.SDS2.Database

using(var Host = new SDSTestHost(argv))
{
    Host.OpenDataDirectory();
    var job = Host.OpenJob();

    var member1 = MemberBrief.Get(job.Members[0]);
    var member2 = MemberBrief.Get(job.Members[1]);

    Console.WriteLine(member2.MemberDescription);
    Host.Assert("API license feature is valid",
                Licensing.IsLicensed);
    Host.Assert("Detailing license feature is valid",
                Licensing.HasFeature(LicenseFeatures.Detailing));
    Host.Assert("Processing license feature is valid",
                Licensing.HasFeature(LicenseFeatures.Processing));
    Host.Assert("ModelLink license feature is valid",
                Licensing.HasFeature(LicenseFeatures.ModelLink));
}


```