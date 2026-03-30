# Namespace DesignData.SDS2 

### [](#classes)Classes 

#### [](#linker)[Linker](DesignData.SDS2.Linker.html)

Before you do anything else with any SDS/2 assemblies, call Linker.Link with appropriate version requirements. This class will find the other SDS/2 .net assemblies from that. You should copy the assembly for this class and distribute it with your program (DesignData.SDS2.Linker.dll).

But that's the only SDS/2 assembly you should distribute/copy.

#### [](#linkerexception)[LinkerException](DesignData.SDS2.LinkerException.html)

Thrown when the Linker is not able to find the version requested or detects a problem with using that version.

### [](#enums)Enums 

#### [](#majorversion)[MajorVersion](DesignData.SDS2.MajorVersion.html)

A list of major versions with .net API support, so far.