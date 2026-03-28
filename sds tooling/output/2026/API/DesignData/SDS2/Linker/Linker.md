# Class Linker 

Before you do anything else with any SDS/2 assemblies, call Linker.Link with appropriate version requirements. This class will find the other SDS/2 .net assemblies from that. You should copy the assembly for this class and distribute it with your program (DesignData.SDS2.Linker.dll).

But that's the only SDS/2 assembly you should distribute/copy.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Linker

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html)

###### **Assembly**: DesignData.SDS2.Linker.dll

##### Syntax

```
public class Linker
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FLinker%5F%5Fctor)Linker()

Before you do anything else with any SDS/2 assemblies, call Linker.Link with appropriate version requirements. This class will find the other SDS/2 .net assemblies from that. You should copy the assembly for this class and distribute it with your program (DesignData.SDS2.Linker.dll).

But that's the only SDS/2 assembly you should distribute/copy.

##### Declaration

```
public Linker()
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FLinker%5FIsValidInstallation%5FSystem%5FString%5F)IsValidInstallation(string)

Return true if the current installation at a given path has the required binaries to run the API.

##### Declaration

```
public static bool IsValidInstallation(string path)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | path |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FLinker%5FLink%5FDesignData%5FSDS2%5FMajorVersion%5FSystem%5FInt32%5F)Link(MajorVersion, int)

Call this to find the installed SDS/2 libraries on the system and use them.

This has to be called before entering a function that used any other SDS/2 assemblies. So, if your Main method doesn't you can call this there, or if it does you can simply declare a static readonly bool and assign it to the result of calling this. That variable will be initialized (and so this will be called) before entering Main, and before .Net will try to load any other SDS/2 assemblies.

##### Declaration

```
public static bool Link(MajorVersion major, int minor = 0)
```

##### Parameters

| Type                                                       | Name  | Description                                                                                                                                                    |
| ---------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [MajorVersion](DesignData.SDS2.MajorVersion.html)          | major | The major version of SDS/2 to grab libraries for.                                                                                                              |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | minor | The minimum minor version required, often this should just be zero, unless there's a known problem with your program running against an earlier minor version. |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

This will not allow you to link against multiple major versions with the same program. You have to choose one to use at the start. You can only call this once, any more calls will throw.

#### [](#DesignData%5FSDS2%5FLinker%5FLink%5FSystem%5FInt32%5FSystem%5FInt32%5F)Link(int, int)

Call this to find the installed SDS/2 libraries on the system and use them.

##### Declaration

```
public static bool Link(int major, int minor = 0)
```

##### Parameters

| Type                                                       | Name  | Description                                                                                                                                                    |
| ---------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | major | The major version of SDS/2 to grab libraries for.                                                                                                              |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | minor | The minimum minor version required, often this should just be zero, unless there's a known problem with your program running against an earlier minor version. |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

This will not allow you to link against multiple major versions with the same program. You have to choose one to use at the start. You can only call this once, any more calls will throw.

#### [](#DesignData%5FSDS2%5FLinker%5FLink%5FSystem%5FString%5F)Link(string)

If you need to supply the full path to the SDS/2 installation. This directory should contain all SDS/2 assemblies and sds2native.dll as well as other dlls packaged with it.

##### Declaration

```
public static bool Link(string path)
```

##### Parameters

| Type                                                           | Name | Description |
| -------------------------------------------------------------- | ---- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | path |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Generally you don't want this, you want a versioned variant which will find this path by looking at installation artifacts in the windows registry.