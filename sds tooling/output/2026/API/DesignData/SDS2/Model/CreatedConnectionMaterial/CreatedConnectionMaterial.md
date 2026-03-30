# Class CreatedConnectionMaterial 

A container for the lists for materials, bolts, and welds created by a connection.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

CreatedConnectionMaterial

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
public class CreatedConnectionMaterial
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FCreatedConnectionMaterial%5FBolts)Bolts

Returns a list of bolts objects created by a connection.

##### Declaration

```
public BoltList Bolts { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltList](DesignData.SDS2.Model.BoltList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCreatedConnectionMaterial%5FMaterials)Materials

Returns a list of material objects created by a connection.

##### Declaration

```
public MaterialList Materials { get; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [MaterialList](DesignData.SDS2.Model.MaterialList.html) |             |

#### [](#DesignData%5FSDS2%5FModel%5FCreatedConnectionMaterial%5FWelds)Welds

Returns a list of welds objects created by a connection.

##### Declaration

```
public WeldList Welds { get; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [WeldList](DesignData.SDS2.Model.WeldList.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FCreatedConnectionMaterial%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A container for the lists for materials, bolts, and welds created by a connection.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FModel%5FCreatedConnectionMaterial%5FFinalize)\~CreatedConnectionMaterial()

A container for the lists for materials, bolts, and welds created by a connection.

##### Declaration

```
protected ~CreatedConnectionMaterial()
```

#### [](#DesignData%5FSDS2%5FModel%5FCreatedConnectionMaterial%5FGetConnection)GetConnection()

Returns the connection that created the listed materials.

##### Declaration

```
public int GetConnection()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |