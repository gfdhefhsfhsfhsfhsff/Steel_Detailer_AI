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

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public static class DatabaseExtensionMethods
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FModel%5FBolt%5F)Add(Transaction, Bolt)

Add a bolt to the transaction so that it can be modified. You will need to Lock() again after adding bolts.

##### Declaration

```
public static void Add(this Transaction transaction, Bolt bolt)
```

##### Parameters

| Type                                                     | Name        | Description |
| -------------------------------------------------------- | ----------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction |             |
| [Bolt](DesignData.SDS2.Model.Bolt.html)                  | bolt        |             |

##### Remarks

This is the same as transaction.Add(bolt.Handle);

#### [](#DesignData%5FSDS2%5FModel%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FModel%5FComponent%5F)Add(Transaction, Component)

Add a component to the transaction before locking so that it can be modified.

##### Declaration

```
public static void Add(this Transaction transaction, Component component)
```

##### Parameters

| Type                                                     | Name        | Description |
| -------------------------------------------------------- | ----------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction |             |
| [Component](DesignData.SDS2.Model.Component.html)        | component   |             |

##### Remarks

This is the same as transaction.Add(component.Handle);

#### [](#DesignData%5FSDS2%5FModel%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FModel%5FHole%5F)Add(Transaction, Hole)

Add a hole to the transaction so that it can be modified. You will need to Lock() again after adding holes.

##### Declaration

```
public static void Add(this Transaction transaction, Hole hole)
```

##### Parameters

| Type                                                     | Name        | Description |
| -------------------------------------------------------- | ----------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction |             |
| [Hole](DesignData.SDS2.Model.Hole.html)                  | hole        |             |

##### Remarks

This is the same as transaction.Add(hole.Handle);

#### [](#DesignData%5FSDS2%5FModel%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FModel%5FMaterial%5F)Add(Transaction, Material)

Add a material to the transaction so that it can be modified. You will need to Lock() again after adding materials.

##### Declaration

```
public static void Add(this Transaction transaction, Material material)
```

##### Parameters

| Type                                                     | Name        | Description |
| -------------------------------------------------------- | ----------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction |             |
| [Material](DesignData.SDS2.Model.Material.html)          | material    |             |

##### Remarks

This is the same as transaction.Add(material.Handle);

#### [](#DesignData%5FSDS2%5FModel%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FModel%5FMember%5F)Add(Transaction, Member)

Add a member to the transaction before locking so that it can be modified.

##### Declaration

```
public static void Add(this Transaction transaction, Member member)
```

##### Parameters

| Type                                                     | Name        | Description |
| -------------------------------------------------------- | ----------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction |             |
| [Member](DesignData.SDS2.Model.Member.html)              | member      |             |

##### Remarks

This is the same as transaction.Add(member.Handle);

#### [](#DesignData%5FSDS2%5FModel%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FModel%5FMemberBrief%5F)Add(Transaction, MemberBrief)

Add a member to the transaction before locking so that it can be modified.

##### Declaration

```
public static void Add(this Transaction transaction, MemberBrief member)
```

##### Parameters

| Type                                                     | Name        | Description |
| -------------------------------------------------------- | ----------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction |             |
| [MemberBrief](DesignData.SDS2.Model.MemberBrief.html)    | member      |             |

##### Remarks

This is the same as transaction.Add(member.Handle);

#### [](#DesignData%5FSDS2%5FModel%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FModel%5FUserDefinedConnection%5F)Add(Transaction, UserDefinedConnection)

Add a user defined connection to the transaction, this will then append that user defined connection to the model on commit.

##### Declaration

```
public static void Add(this Transaction transaction, UserDefinedConnection userDefinedConnection)
```

##### Parameters

| Type                                                                      | Name                  | Description |
| ------------------------------------------------------------------------- | --------------------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html)                  | transaction           |             |
| [UserDefinedConnection](DesignData.SDS2.Model.UserDefinedConnection.html) | userDefinedConnection |             |

#### [](#DesignData%5FSDS2%5FModel%5FDatabaseExtensionMethods%5FAdd%5FDesignData%5FSDS2%5FDatabase%5FTransaction%5FDesignData%5FSDS2%5FModel%5FWeld%5F)Add(Transaction, Weld)

Add a bolt to the transaction so that it can be modified. You will need to Lock() again after adding welds.

##### Declaration

```
public static void Add(this Transaction transaction, Weld weld)
```

##### Parameters

| Type                                                     | Name        | Description |
| -------------------------------------------------------- | ----------- | ----------- |
| [Transaction](DesignData.SDS2.Database.Transaction.html) | transaction |             |
| [Weld](DesignData.SDS2.Model.Weld.html)                  | weld        |             |

##### Remarks

This is the same as transaction.Add(weld.Handle);