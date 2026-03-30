# Database Structure

## [](#handles)Handles

The SDS2 API makes fairly heavy use of the concept of handles. These are small, serializable, objects which tell us where to find a specific type of element in a job. This provides us with an abstraction over something like a member number or a uuid along with type checking to reduce the risk of mixing up what kind of item your handle is looking for.

So, if we had an int to represent a member there's always a risk it could be mixed up and used for something else. Or another integer could be used to lookup a member. But with a [MemberHandle](../api/DesignData.SDS2.Database.MemberHandle.html) we know that is refers to a member. We know it doesn't represent an end on a member, or an index into a member's array of materials. And with a MemberHandle we have some freedom to change the underlying implementation.

The same would go for a uuid which could represent a weld, bolt, material, or member.

## [](#active-job)Active Job

SDS2 only supports having one active job at a time in an operating system process. So you must open a job to read from or make changes to it. While it's open you can't work with any other job.

## [](#structure-of-an-sds2-job)Structure of an SDS2 Job

### [](#members)Members

The top-level item in SDS2 is the member. In some products this is called an assembly. These are collections of materials, bolts, and welds which would generally be assembled at the fabricator and shipped assembled. Multiple members may share a single piecemark (shipping mark, major mark), in which case they may be referred to as "batched" together.

### [](#materials)Materials

A [material](../api/DesignData.SDS2.Model.Material.html) is a single piece of material in the model, on a single member. Internally, materials point at something called a "sub material." This has the full, fabricatable, definition of the material on it. And many materials may share the same "sub material." This has to do with how SDS2 handles minor marks (submaterial piecemarks). This concept of a submaterial is mostly hidden from the API, but it will show up in some places and end users are aware of it. It's especially visible in areas like detailing.

#### [](#supportedsupporting)Supported/Supporting

Materials for connections are either assembled with the supported member, or the supporting member. The connection is always on the supported member.

#### [](#submaterials)Submaterials

This is the fabricatable definition of a material. It's usually shared by many individual pieces in one model. Similar to how members are "batched" under a piecemark, many materials are "batched" using a submaterial.

Conceptually this is mostly hidden from the API.

#### [](#material-file)Material file

In the API we call this [Shapes](../api/DesignData.SDS2.Setup.Shape.html). These are generally extrudable sections like rolled sections (wide flanges, angles, etc) or cold formed shapes. There is one global material file, or set of Shapes, in each job. This is why you cannot set an arbitrary Shape for a beam, it must be a Shape from that job's [MaterialFile](../api/DesignData.SDS2.Setup.MaterialFile.html).

Plates are not in the material file.

### [](#bolts-and-welds)Bolts and Welds

These are just what you'd think, bolts and welds, used to fasten materials on a member. Since materials from different members have to fasten to other members (for example, you need to bolt that beam clip angle to the column) it is often the case that a bolt or weld is on one member but only one of the pieces of material it fastens is on that member.

### [](#connections)Connections

Each member has a left and right connection. These contain the design properties for that connection, which will then generate material, bolts, and welds as needed.

#### [](#lockables)Lockables

Each connection has a set of [Lockables](../api/DesignData.SDS2.Model.Lockable.html). These are values which can either be calculated by the system (unlocked) or be set by the user (locked), and the system has to take the user set values into account when calculating other values.

### [](#setup)Setup

Each job has a large repository of settings which we generally call "setup." This is broken up into [Job](../api/DesignData.SDS2.Setup.Job.html) and [Fabricator](../api/DesignData.SDS2.Setup.Fabricator.html) setup. In general, fabricator settings are those specific to fabricating elements of the job. Where job settings are about the job itself. So things like steel design codes are in job setup, where specifications about how to format details are in fabrication settings.

The API is mostly limited to reading setup values. In some cases we allow adding more items. This is to prevent setup changes from having surprising and far reaching consequences inside jobs.

## [](#2d)2D

Drawings are a part of the job, but they often feel disjointed. They're very much a generated product from the model. They're often hand modified by end users, and so they can't be blindly updated with the model.

### [](#details)Details

These are for members. There is one detail for every major mark (piecemark, shipping mark).

### [](#detail-sheet)Detail sheet

This is a sheet with one or more member details on it.

### [](#submaterial)Submaterial

These are for materials. There will be one detail for every minor mark.

### [](#gather-sheet)Gather sheet

This is a sheet with one or more submaterial details on it.

### [](#erection-view)Erection view

This is a detail of a planar section of the model.

### [](#erection-sheet)Erection sheet

A sheet with one or more erection views on it.

## [](#data-directories-and-job-repositories)Data directories and job repositories

Every SDS2 installation keeps its data in a [DataDirectory](../api/DesignData.SDS2.Database.DataDirectory.html). This includes a job repository (although users can make other repositories outside of the DataDirectory). It also includes things like standard details, setup files for creating new jobs.