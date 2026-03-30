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

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Detail](DesignData.SDS2.Detail.html)

###### **Assembly**: DesignData.SDS2.Detail.dll

##### Syntax

```
public static class DatabaseExtensionMethods
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDetail%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FDetail%5FDrawing%5F)Add(Transaction, Drawing)

Add a drawing to the transaction so that it can be modified. You will need to Lock() again after adding drawings.

##### Declaration

```
public static void Add(this Transaction transaction, Drawing drawing)
```

##### Parameters

| Type                                                     | Name        | Description |
| -------------------------------------------------------- | ----------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction |             |
| [Drawing](DesignData.SDS2.Detail.Drawing.html)           | drawing     |             |

##### Remarks

This is the same as transaction.Add(drawing.Handle);