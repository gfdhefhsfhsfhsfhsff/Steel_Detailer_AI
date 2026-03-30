# Class MaterialFile 

A collection of material shape definitions

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MaterialFile

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
public class MaterialFile
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialFile%5FHandle)Handle

A database handle for this material file

##### Declaration

```
public MaterialFileHandle Handle { get; }
```

##### Property Value

| Type                                                                   | Description |
| ---------------------------------------------------------------------- | ----------- |
| [MaterialFileHandle](DesignData.SDS2.Database.MaterialFileHandle.html) |             |

##### Remarks

This is internal only, because of dependency requirements between Setup and Database (Database depends on Setup, it can't be the other way around right now)

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialFile%5FAdd%5FDesignData%5FSDS2%5FSetup%5FShape%5F)Add(Shape)

Add a new shape to this material file.

##### Declaration

```
public void Add(Shape shape)
```

##### Parameters

| Type                                      | Name  | Description |
| ----------------------------------------- | ----- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) | shape |             |

##### Remarks

You must add this material file to the transaction before doing this.

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialFile%5FAllRoundBars)AllRoundBars()

All the RoundBarShapes in the material file

##### Declaration

```
public RoundBarShapeList AllRoundBars()
```

##### Returns

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [RoundBarShapeList](DesignData.SDS2.Setup.RoundBarShapeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialFile%5FAllShapes)AllShapes()

All the shapes in the material file

##### Declaration

```
public ShapeList AllShapes()
```

##### Returns

| Type                                              | Description |
| ------------------------------------------------- | ----------- |
| [ShapeList](DesignData.SDS2.Setup.ShapeList.html) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialFile%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A collection of material shape definitions

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialFile%5FFinalize)\~MaterialFile()

A collection of material shape definitions

##### Declaration

```
protected ~MaterialFile()
```

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialFile%5FFind%5FSystem%5FInt32%5F)Find(int)

The shape in the material file at the specified index (1-based)

##### Declaration

```
public Shape Find(int material_index)
```

##### Parameters

| Type                                                       | Name            | Description |
| ---------------------------------------------------------- | --------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | material\_index |             |

##### Returns

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the material file does not contain a shape with the specified index. |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialFile%5FFind%5FSystem%5FString%5F)Find(string)

The shape in the material file with the specified section size.

##### Declaration

```
public Shape Find(string section_size)
```

##### Parameters

| Type                                                           | Name          | Description |
| -------------------------------------------------------------- | ------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | section\_size |             |

##### Returns

| Type                                      | Description |
| ----------------------------------------- | ----------- |
| [Shape](DesignData.SDS2.Setup.Shape.html) |             |

##### Exceptions

| Type                                                                           | Condition                                                                                                           |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| [InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html) | InvalidValueException will be thrown if the material file does not contain a shape with the specified section size. |

#### [](#DesignData%5FSDS2%5FSetup%5FMaterialFile%5FGet)Get()

Get the material file for the currently open/active job

##### Declaration

```
public static MaterialFile Get()
```

##### Returns

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [MaterialFile](DesignData.SDS2.Setup.MaterialFile.html) |             |