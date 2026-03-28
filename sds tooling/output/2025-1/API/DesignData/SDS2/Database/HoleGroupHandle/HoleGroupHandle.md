# Class HoleGroupHandle 

A handle to a hole group

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

HoleGroupHandle

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
public class HoleGroupHandle
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleGroupHandle%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FMaterialHandle%5FSystem%5FInt32%5F)HoleGroupHandle(MaterialHandle, int)

Create a hole group handle from a material handle and the index of the group.

##### Declaration

```
public HoleGroupHandle(MaterialHandle materialHandle, int index)
```

##### Parameters

| Type                                                           | Name           | Description |
| -------------------------------------------------------------- | -------------- | ----------- |
| [MaterialHandle](DesignData.SDS2.Database.MaterialHandle.html) | materialHandle |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | index          |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleGroupHandle%5FHoleGroupIndex)HoleGroupIndex

The index of this group on that material.

##### Declaration

```
public int HoleGroupIndex { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleGroupHandle%5FMaterial)Material

The material this hole is drilling

##### Declaration

```
public MaterialHandle Material { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [MaterialHandle](DesignData.SDS2.Database.MaterialHandle.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleGroupHandle%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A handle to a hole group

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleGroupHandle%5FEquals%5FSystem%5FObject%5F)Equals(object)

A handle to a hole group

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

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleGroupHandle%5FFinalize)\~HoleGroupHandle()

A handle to a hole group

##### Declaration

```
protected ~HoleGroupHandle()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleGroupHandle%5FGetHashCode)GetHashCode()

A handle to a hole group

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