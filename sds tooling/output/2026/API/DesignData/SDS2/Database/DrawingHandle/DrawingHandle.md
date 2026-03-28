# Class DrawingHandle 

A TableIndexHandle specific for tables which contain drawings

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[TableIndexHandle](DesignData.SDS2.Database.TableIndexHandle.html)

DrawingHandle

##### Inherited Members

[TableIndexHandle.GetHashCode()](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FGetHashCode) 

[TableIndexHandle.Equals(object)](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FEquals%5FSystem%5FObject%5F) 

[TableIndexHandle.ToString()](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FToString) 

[TableIndexHandle.Table](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FTable) 

[TableIndexHandle.Index](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FIndex) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class DrawingHandle : TableIndexHandle
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FTableWithDrawings%5FSystem%5FInt32%5F)DrawingHandle(TableWithDrawings, int)

A TableIndexHandle specific for tables which contain drawings

##### Declaration

```
public DrawingHandle(TableWithDrawings table, int indexInTable)
```

##### Parameters

| Type                                                                 | Name         | Description                                    |
| -------------------------------------------------------------------- | ------------ | ---------------------------------------------- |
| [TableWithDrawings](DesignData.SDS2.Database.TableWithDrawings.html) | table        | See the Table enumeration for possible values. |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)           | indexInTable | The index into that table.                     |

##### Remarks

It's recommended that you avoid constructing handles in this manner. If you need a long lasting identifier for an element in the SDS2 database you should find a GUID on that item and search for it to look it back up.

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FDrawingHandle%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A TableIndexHandle specific for tables which contain drawings

##### Declaration

```
protected override void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Overrides

[TableIndexHandle.Dispose(bool)](DesignData.SDS2.Database.TableIndexHandle.html#DesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FDispose%5FSystem%5FBoolean%5F)