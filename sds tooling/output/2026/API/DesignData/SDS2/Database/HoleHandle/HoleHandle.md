# Class HoleHandle 

A handle specifically for holes

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

HoleHandle

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
public class HoleHandle
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleHandle%5F%5Fctor%5FDesignData%5FSDS2%5FDatabase%5FMaterialHandle%5FSystem%5FInt32%5F)HoleHandle(MaterialHandle, int)

Create a hole handle from a material handle and the index of the hole.

##### Declaration

```
public HoleHandle(MaterialHandle materialHandle, int holeIndex)
```

##### Parameters

| Type                                                           | Name           | Description |
| -------------------------------------------------------------- | -------------- | ----------- |
| [MaterialHandle](DesignData.SDS2.Database.MaterialHandle.html) | materialHandle |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32)     | holeIndex      |             |

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleHandle%5FHoleIndex)HoleIndex

The index of this hole on that material.

##### Declaration

```
public int HoleIndex { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleHandle%5FMaterial)Material

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

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleHandle%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A handle specifically for holes

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleHandle%5FEquals%5FSystem%5FObject%5F)Equals(object)

A handle specifically for holes

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

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleHandle%5FFinalize)\~HoleHandle()

A handle specifically for holes

##### Declaration

```
protected ~HoleHandle()
```

#### [](#DesignData%5FSDS2%5FDatabase%5FHoleHandle%5FGetHashCode)GetHashCode()

A handle specifically for holes

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