# Configure your application

Once you have followed the instructions to create and run a .NET ["Hello World" app](https://code.visualstudio.com/docs/languages/dotnet), update the `csproj` file to reference the required assemblies from SDS2, e.g., under `<Project>`, add

```
  <ItemGroup>
    <Reference Include="DesignData.SDS2.Linker"
               HintPath="C:/Program Files/SDS2_2023/bin/DesignData.SDS2.Linker.dll">
        <Private>True</Private>
    </Reference>
    <Reference Include="DesignData.SDS2.Database"
               HintPath="C:/Program Files/SDS2_2023/bin/DesignData.SDS2.Database.dll">
        <Private>False</Private>
    </Reference>
    <Reference Include="DesignData.SDS2.Detail"
               HintPath="C:/Program Files/SDS2_2023/bin/DesignData.SDS2.Detail.dll">
        <Private>False</Private>
    </Reference>
    <Reference Include="DesignData.SDS2.Exceptions"
               HintPath="C:/Program Files/SDS2_2023/bin/DesignData.SDS2.Exceptions.dll">
        <Private>False</Private>
    </Reference>
    <Reference Include="DesignData.SDS2.Model"
               HintPath="C:/Program Files/SDS2_2023/bin/DesignData.SDS2.Model.dll">
        <Private>False</Private>
    </Reference>
    <Reference Include="DesignData.SDS2.Primitives"
               HintPath="C:/Program Files/SDS2_2023/bin/DesignData.SDS2.Primitives.dll">
        <Private>False</Private>
    </Reference>
    <Reference Include="DesignData.SDS2.Python"
               HintPath="C:/Program Files/SDS2_2023/bin/DesignData.SDS2.Python.dll">
        <Private>False</Private>
    </Reference>
    <Reference Include="DesignData.SDS2.Setup"
               HintPath="C:/Program Files/SDS2_2023/bin/DesignData.SDS2.Setup.dll">
        <Private>False</Private>
    </Reference>
  </ItemGroup>

```

We have two basic kinds of assemblies:

1. DesignData.SDS2.Linker.dll - this one is copied into your application and should be distributed with it. This tiny assembly knows how to find all the others when SDS2 is installed.
2. Everything else - these are the API. You should not copy them into your project or distribute them. They'll be found by DesignData.SDS2.Linker.dll at runtime within the user's SDS2 installation. These are not a complete API, there is a native component which they all depend on and must be perfectly matched to.

You'll also need to force your application to run as a 64-bit application. Under `<Project>`, add

```
  <PropertyGroup>
    <Platform>x64</Platform>
  </PropertyGroup>

```

If you are using .net core, or .net 5.0 or newer, and you decide after visual studio's new project tutorial that you would like to use winforms add the required assembly to the other required assemblies listed above.

```
    <Reference Include="DesignData.SDS2.WinForms"
               HintPath="C:/Program Files/SDS2_2023/bin/DesignData.SDS2.WinForms.dll">
        <Private>False</Private>
    </Reference>

```

Additionally, adjust the platform type to make winforms available. (If you're using framework, 4.7 or older, then you simply add the reference to the winforms assembly installed on your system).

```
  <PropertyGroup>
    <Platform>x64</Platform>
    <TargetFramework>net6.0-windows</TargetFramework>
  </PropertyGroup>

```

If you don't want winforms:

```
  <PropertyGroup>
    <Platform>x64</Platform>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>

```

To confirm that the `Database` library is installed and referenced correctly, revise the app's `Program.cs` so that instead of "hello world", it prints the SDS2 program version. But first, you'll need to call DesignData.SDS2.Linker.Link() to setup an assembly resolver for the rest of our dlls:

```
using System;

namespace hellosds2
{
    class Program
    {
        [STAThread]
        static void Main(string[] args)
        {
            //Main needs to call the Linker and make no reference to any SDS2 API symbols:
            if(!DesignData.SDS2.Linker.Link(DesignData.SDS2.MajorVersion.Linked))
            {
                //notify your users that the SDS2 installation isn't right
                return;
            }

            //code which references SDS2 API symbols can begin in our subordinate main function
            //which you can name anything you like:
            Run(args);
        }
        static void Run(string [] args)
        {
            //Before doing anything else, get your license checked out, and
            //if needed prompt the user for their license username and password:
            if(!DesignData.SDS2.WinForms.LicensingInitialization.Checkout())
            {
                Console.WriteLine("No SDS2 API2 license available");
                return;
            }
            var sds2Version =
                DesignData.SDS2.Database.Version.ProgramVersion.ToString();
            Console.WriteLine($"Hello SDS/2 v{sds2Version}");
        }
    }
}

```

Build and run the project. Its output should be something like

```
Hello SDS2 v8.000

```

### [](#changelog)Changelog

This tutorial has been modified since SDS2 2021 to resolve issues with .Net 5.0 and newer. In .Net 5.0 and newer the static variable assigned the result of the Link call seemed to not be evaluated until it's referenced. Which means if you never check it, Link is never called. And if you do check it, in Main, but Main also references SDS2 API symbols; then .Net tries to find those symbols in the appropriate assemblies before calling Link. This doesn't work because Link has to be called before .Net will be able to find the SDS2 API assemblies.