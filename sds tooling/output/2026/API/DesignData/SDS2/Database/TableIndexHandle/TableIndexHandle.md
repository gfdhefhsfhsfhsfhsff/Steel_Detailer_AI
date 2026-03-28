# Class TableIndexHandle 

A handle for an element in the SDS2 database.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

TableIndexHandle

[DrawingHandle](DesignData.SDS2.Database.DrawingHandle.html)

[GridLineHandle](DesignData.SDS2.Database.GridLineHandle.html)

[GroupMemberHandle](DesignData.SDS2.Database.GroupMemberHandle.html)

[MemberHandle](DesignData.SDS2.Database.MemberHandle.html)

[NoteHandle](DesignData.SDS2.Database.NoteHandle.html)

[UserDefinedConnectionHandle](DesignData.SDS2.Database.UserDefinedConnectionHandle.html)

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class TableIndexHandle
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FTable%5FSystem%5FInt32%5F)TableIndexHandle(Table, int)

A handle for an element in the SDS2 database.

##### Declaration

```
public TableIndexHandle(Table table, int indexInTable)
```

##### Parameters

| Type                                                       | Name         | Description                                    |
| ---------------------------------------------------------- | ------------ | ---------------------------------------------- |
| [Table](DesignData.SDS2.Database.Table.html)               | table        | See the Table enumeration for possible values. |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | indexInTable | The index into that table.                     |

##### Remarks

It's recommended that you avoid constructing handles in this manner. If you need a long lasting identifier for an element in the SDS2 database you should find a GUID on that item and search for it to look it back up.

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FIndex)Index

The index into the table for this item.

##### Declaration

```
public int Index { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FTable)Table

The table enumeration value for this handle. Ex: Member

##### Declaration

```
public Table Table { get; }
```

##### Property Value

| Type                                         | Description |
| -------------------------------------------- | ----------- |
| [Table](DesignData.SDS2.Database.Table.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A handle for an element in the SDS2 database.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FEquals%5FSystem%5FObject%5F)Equals(object)

A handle for an element in the SDS2 database.

##### Declaration

```
public override bool Equals(object other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | other |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

#### [](#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FFinalize)\~TableIndexHandle()

A handle for an element in the SDS2 database.

##### Declaration

```
protected ~TableIndexHandle()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FGetHashCode)GetHashCode()

A handle for an element in the SDS2 database.

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

#### [](#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FToString)ToString()

A handle for an element in the SDS2 database.

##### Declaration

```
public override string ToString()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Overrides

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)