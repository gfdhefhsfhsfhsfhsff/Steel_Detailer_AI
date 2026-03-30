# Class Version 

Version reflects how SDS2 is versioned internally. These version numbers are not like assembly version numbers or semantic version numbers, are only loosely correlated with marketing versions, but reflect existing internal practice at SDS2.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Version

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class Version
```

##### **Remarks**

Version numbers are important to understand (A) capabilities of SDS2 and the C# interface and (B) compatible project data versions. 

Generally, over time, Program and Data version numbers of SDS2 increase. 

Generally, when a new marketing version number is seen, the most significant "minor" digit is incremented, overflowing to the "major" digit. 

Generally, Program version is equal to or greater than Data version. 

Projects with data versions equal to Version.DataVersion can be accessed freely, while projects with older data versions can be irrevocably converted to the current data version. 

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FVersion%5FDataVersion)DataVersion

The data version written by the loaded SDS2 DLL.

##### Declaration

```
public static Version DataVersion { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Version](DesignData.SDS2.Database.Version.html) |             |

##### Remarks

Version numbers are important to understand (A) capabilities of SDS2 and the C# interface and (B) compatible project data versions. 

Generally, over time, Program and Data version numbers of SDS2 increase. 

Generally, when a new marketing version number is seen, the most significant "minor" digit is incremented, overflowing to the "major" digit. 

Generally, Program version is equal to or greater than Data version. 

Projects with data versions equal to Version.DataVersion can be accessed freely, while projects with older data versions can be irrevocably converted to the current data version. 

#### [](#DesignData%5FSDS2%5FDatabase%5FVersion%5FMajor)Major

Major version releases, increments of this are likely to come with breaking API changes.

##### Declaration

```
public int Major { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Remarks

Version numbers are important to understand (A) capabilities of SDS2 and the C# interface and (B) compatible project data versions. 

Generally, over time, Program and Data version numbers of SDS2 increase. 

Generally, when a new marketing version number is seen, the most significant "minor" digit is incremented, overflowing to the "major" digit. 

Generally, Program version is equal to or greater than Data version. 

Projects with data versions equal to Version.DataVersion can be accessed freely, while projects with older data versions can be irrevocably converted to the current data version. 

#### [](#DesignData%5FSDS2%5FDatabase%5FVersion%5FMinor)Minor

Minor version changes may also contain breaking API changes, but some will not.

##### Declaration

```
public int Minor { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Remarks

Version numbers are important to understand (A) capabilities of SDS2 and the C# interface and (B) compatible project data versions. 

Generally, over time, Program and Data version numbers of SDS2 increase. 

Generally, when a new marketing version number is seen, the most significant "minor" digit is incremented, overflowing to the "major" digit. 

Generally, Program version is equal to or greater than Data version. 

Projects with data versions equal to Version.DataVersion can be accessed freely, while projects with older data versions can be irrevocably converted to the current data version. 

#### [](#DesignData%5FSDS2%5FDatabase%5FVersion%5FProgramVersion)ProgramVersion

The program version of the loaded SDS2 DLL.

##### Declaration

```
public static Version ProgramVersion { get; }
```

##### Property Value

| Type                                             | Description |
| ------------------------------------------------ | ----------- |
| [Version](DesignData.SDS2.Database.Version.html) |             |

##### Remarks

Version numbers are important to understand (A) capabilities of SDS2 and the C# interface and (B) compatible project data versions. 

Generally, over time, Program and Data version numbers of SDS2 increase. 

Generally, when a new marketing version number is seen, the most significant "minor" digit is incremented, overflowing to the "major" digit. 

Generally, Program version is equal to or greater than Data version. 

Projects with data versions equal to Version.DataVersion can be accessed freely, while projects with older data versions can be irrevocably converted to the current data version. 

#### [](#DesignData%5FSDS2%5FDatabase%5FVersion%5FRevision)Revision

Minor revisions that will not contain breaking API changes.

##### Declaration

```
public int Revision { get; }
```

##### Property Value

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Remarks

Version numbers are important to understand (A) capabilities of SDS2 and the C# interface and (B) compatible project data versions. 

Generally, over time, Program and Data version numbers of SDS2 increase. 

Generally, when a new marketing version number is seen, the most significant "minor" digit is incremented, overflowing to the "major" digit. 

Generally, Program version is equal to or greater than Data version. 

Projects with data versions equal to Version.DataVersion can be accessed freely, while projects with older data versions can be irrevocably converted to the current data version. 

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FVersion%5FFinalize)\~Version()

Version reflects how SDS2 is versioned internally. These version numbers are not like assembly version numbers or semantic version numbers, are only loosely correlated with marketing versions, but reflect existing internal practice at SDS2.

##### Declaration

```
protected ~Version()
```

##### Remarks

Version numbers are important to understand (A) capabilities of SDS2 and the C# interface and (B) compatible project data versions. 

Generally, over time, Program and Data version numbers of SDS2 increase. 

Generally, when a new marketing version number is seen, the most significant "minor" digit is incremented, overflowing to the "major" digit. 

Generally, Program version is equal to or greater than Data version. 

Projects with data versions equal to Version.DataVersion can be accessed freely, while projects with older data versions can be irrevocably converted to the current data version. 

#### [](#DesignData%5FSDS2%5FDatabase%5FVersion%5FToString)ToString()

Version reflects how SDS2 is versioned internally. These version numbers are not like assembly version numbers or semantic version numbers, are only loosely correlated with marketing versions, but reflect existing internal practice at SDS2.

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

##### Remarks

Version numbers are important to understand (A) capabilities of SDS2 and the C# interface and (B) compatible project data versions. 

Generally, over time, Program and Data version numbers of SDS2 increase. 

Generally, when a new marketing version number is seen, the most significant "minor" digit is incremented, overflowing to the "major" digit. 

Generally, Program version is equal to or greater than Data version. 

Projects with data versions equal to Version.DataVersion can be accessed freely, while projects with older data versions can be irrevocably converted to the current data version.