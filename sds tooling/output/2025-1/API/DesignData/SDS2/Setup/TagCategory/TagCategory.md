# Class TagCategory 

A TagCategory consists of a category name, a list of standard tags for the category, and a flag specifying if users are permitted to add not defined in the standard tags. By default SDS2 setup is initialized with three tag categories named Discipline, Status, and Custom. These three category names can be changed by the user, but the API refers to them by the default name. For example, the Note API has a property DisciplineTags although the user could have changed the name of the category.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

TagCategory

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
public class TagCategory
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategory%5FAllowNonStandardTags)AllowNonStandardTags

Specifies whether users can add tags that are not defined as one of the standard tags

##### Declaration

```
public bool AllowNonStandardTags { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategory%5FName)Name

The name of the tag category.

##### Declaration

```
public string Name { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategory%5FStandardTags)StandardTags

The standard tags associated with the category

##### Declaration

```
public StringList StandardTags { get; set; }
```

##### Property Value

| Type                                                     | Description |
| -------------------------------------------------------- | ----------- |
| [StringList](DesignData.SDS2.Primitives.StringList.html) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategory%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

A TagCategory consists of a category name, a list of standard tags for the category, and a flag specifying if users are permitted to add not defined in the standard tags. By default SDS2 setup is initialized with three tag categories named Discipline, Status, and Custom. These three category names can be changed by the user, but the API refers to them by the default name. For example, the Note API has a property DisciplineTags although the user could have changed the name of the category.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

#### [](#DesignData%5FSDS2%5FSetup%5FTagCategory%5FFinalize)\~TagCategory()

A TagCategory consists of a category name, a list of standard tags for the category, and a flag specifying if users are permitted to add not defined in the standard tags. By default SDS2 setup is initialized with three tag categories named Discipline, Status, and Custom. These three category names can be changed by the user, but the API refers to them by the default name. For example, the Note API has a property DisciplineTags although the user could have changed the name of the category.

##### Declaration

```
protected ~TagCategory()
```