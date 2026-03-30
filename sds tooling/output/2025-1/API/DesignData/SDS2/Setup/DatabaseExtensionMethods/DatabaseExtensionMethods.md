# Class DatabaseExtensionMethods 

Extension methods for DesignData.SDS2.Database. These are all convenience methods and will appear to be on classes in DesignData.SDS2.Database.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

DatabaseExtensionMethods

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Setup](DesignData.SDS2.Setup.html)

###### **Assembly**: DesignData.SDS2.Setup.dll

##### Syntax

```
public static class DatabaseExtensionMethods
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FSetup%5FFabricator%5F)Add(Transaction, Fabricator)

Add fabricator to the transaction so that it can be modified. You will need to Lock() again after adding fabricator.

##### Declaration

```
public static void Add(this Transaction transaction, Fabricator fabricator)
```

##### Parameters

| Type                                                     | Name        | Description |
| -------------------------------------------------------- | ----------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction |             |
| [Fabricator](DesignData.SDS2.Setup.Fabricator.html)      | fabricator  |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FSetup%5FJob%5F)Add(Transaction, Job)

Add job setup to the transaction so that it can be modified. You will need to Lock() again after adding job setup.

##### Declaration

```
public static void Add(this Transaction transaction, Job job)
```

##### Parameters

| Type                                                     | Name        | Description |
| -------------------------------------------------------- | ----------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction |             |
| [Job](DesignData.SDS2.Setup.Job.html)                    | job         |             |

#### [](#DesignData%5FSDS2%5FSetup%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FSetup%5FMaterialFile%5F)Add(Transaction, MaterialFile)

Add a material file to the transaction so that it can be modified. You will need to Lock() again after adding materials.

##### Declaration

```
public static void Add(this Transaction transaction, MaterialFile materialFile)
```

##### Parameters

| Type                                                     | Name         | Description |
| -------------------------------------------------------- | ------------ | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction  |             |
| [MaterialFile](DesignData.SDS2.Setup.MaterialFile.html)  | materialFile |             |

##### Remarks

This is the same as transaction.Add(materialFile.Handle);