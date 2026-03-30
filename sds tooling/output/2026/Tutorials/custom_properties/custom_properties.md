# Custom properties

Every object that has custom properties will have a [CustomPropertyMapHandle](../api/DesignData.SDS2.Database.CustomPropertyMapHandle.html)property which can be passed to [CustomPropertyMap.Get()](../api/DesignData.SDS2.Model.CustomPropertyMap.html#DesignData%5FSDS2%5FModel%5FCustomPropertyMap%5FGet%5FSystem%5FString%5FSystem%5FBoolean%5F%5F) to access the properties for the handle.

Members, materials, holes, bolts, welds, group members, and jobs have custom properties. The following examples show how to read and write the `Notes`property for a job.

Reading custom properties:

```
var properties_handle = job.CustomPropertyMapHandle;
var properties = CustomPropertyMap.Get(properties_handle);
string notes = "";
properties.Get("Notes", ref notes);

```

Writing custom properties:

```
using(var xaction = new Transaction(job, new ImmediateLockHandler()))
{
    var properties_handle = job.CustomPropertyMapHandle;
    xaction.Add(properties_handle);
    xaction.Lock();
    var properties = CustomPropertyMap.Get(properties_handle);
    properties.Set("Notes", "hello world");
    xaction.Commit();
}

```