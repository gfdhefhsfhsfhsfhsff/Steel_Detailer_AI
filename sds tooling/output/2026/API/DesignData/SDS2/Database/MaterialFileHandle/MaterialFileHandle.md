# Class MaterialFileHandle 

A handle for a material file

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialFileHandle

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class MaterialFileHandle
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialFileHandle%5F%5Fctor)MaterialFileHandle()

A material file handle to the current job's material file

##### Declaration

```
public MaterialFileHandle()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialFileHandle%5F%5Fctor%5FSystem%5FString%5F)MaterialFileHandle(string)

A material file handle to a material file outside of the current job

##### Declaration

```
public MaterialFileHandle(string location)
```

##### Parameters

| Type                                                           | Name     | Description |
| -------------------------------------------------------------- | -------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | location |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialFileHandle%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A handle for a material file

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialFileHandle%5FEquals%5FSystem%5FObject%5F)Equals(object)

A handle for a material file

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

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialFileHandle%5FFinalize)\~MaterialFileHandle()

A handle for a material file

##### Declaration

```
protected ~MaterialFileHandle()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FMaterialFileHandle%5FGetHashCode)GetHashCode()

A handle for a material file

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