# Class MomentSpecification 

The moment specification options.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

MomentSpecification

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Model](DesignData.SDS2.Model.html)

###### **Assembly**: DesignData.SDS2.Model.dll

##### Syntax

```
public class MomentSpecification
```

##### **Remarks**

Since moment options are largely shared, and there are only two distinct connection types, we just have one class for moment connections. Simply set the MomentType and proceed to set applicable properties.

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FBoltDiameter)BoltDiameter

The bolt diameter to use for bolts fastening moment connection material

##### Declaration

```
public double BoltDiameter { get; set; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [double](https://learn.microsoft.com/dotnet/api/system.double) |             |

##### Remarks

Only valid when MomentType is Bolted and AutoBoltDiameter is false.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FBoltPattern)BoltPattern

The bolt pattern to use in a moment plate

##### Declaration

```
public MomentBoltPattern BoltPattern { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [MomentBoltPattern](DesignData.SDS2.Model.MomentBoltPattern.html) |             |

##### Remarks

Only valid for end plate bolted. If ConnectionType is to be MBMA, set that first or this may not work. Then set EndPlates.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FBoltType)BoltType

The BoltType to use for bolts attaching moment connection material.

##### Declaration

```
public BoltType BoltType { get; set; }
```

##### Property Value

| Type                                            | Description |
| ----------------------------------------------- | ----------- |
| [BoltType](DesignData.SDS2.Setup.BoltType.html) |             |

##### Remarks

Only valid when MomentType is Bolted and AutoBoltType is false

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FColumnReinforcement)ColumnReinforcement

Indicates the column web reinforcement

##### Declaration

```
public ColumnReinforcementType ColumnReinforcement { get; set; }
```

##### Property Value

| Type                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [ColumnReinforcementType](DesignData.SDS2.Model.ColumnReinforcementType.html) |             |

##### Remarks

Only applies to Eurocode jobs. For non Eurocode jobs use DesignForDoublers

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FColumnWebDoublerSide)ColumnWebDoublerSide

The location of a doubler plate on the web of a column.

##### Declaration

```
public ColumnWebDoublerSide ColumnWebDoublerSide { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [ColumnWebDoublerSide](DesignData.SDS2.Model.ColumnWebDoublerSide.html) |             |

##### Remarks

Since moment options are largely shared, and there are only two distinct connection types, we just have one class for moment connections. Simply set the MomentType and proceed to set applicable properties.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FConnectionMaterial)ConnectionMaterial

The kind of extra material to add to a connection for the moment

##### Declaration

```
public MomentConnectionMaterial ConnectionMaterial { get; set; }
```

##### Property Value

| Type                                                                            | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [MomentConnectionMaterial](DesignData.SDS2.Model.MomentConnectionMaterial.html) |             |

##### Remarks

Since moment options are largely shared, and there are only two distinct connection types, we just have one class for moment connections. Simply set the MomentType and proceed to set applicable properties.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FConnectionType)ConnectionType

The moment specification options.

##### Declaration

```
public MomentConnectionType ConnectionType { get; set; }
```

##### Property Value

| Type                                                                    | Description |
| ----------------------------------------------------------------------- | ----------- |
| [MomentConnectionType](DesignData.SDS2.Model.MomentConnectionType.html) |             |

##### Remarks

Only valid for any value besides AISC\_Eurocode if it's an AISC bolted moment end plate connection. Then it can be MBMA

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FDesignHaunch)DesignHaunch

Indicates if a haunch is designed with a bolted moment connection

##### Declaration

```
public AutomaticYesNo DesignHaunch { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

##### Remarks

Only applies to Eurocode jobs

##### Exceptions

| Type                                                                                   | Condition                                                       |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | Thrown when setting this property when MomentType is not Bolted |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FEndPlates)EndPlates

Options for the ends of the end plates used

##### Declaration

```
public EndPlateEndOption EndPlates { get; set; }
```

##### Property Value

| Type                                                              | Description |
| ----------------------------------------------------------------- | ----------- |
| [EndPlateEndOption](DesignData.SDS2.Model.EndPlateEndOption.html) |             |

##### Remarks

This field is only valid if ConnectionType is MBMA. Set this before setting BoltPattern.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FGrooveAngle)GrooveAngle

The angle of bevel on the flange of the beam. From a very short list of allowed options, named in degrees.

##### Declaration

```
public GrooveAngle GrooveAngle { get; set; }
```

##### Property Value

| Type                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [GrooveAngle](DesignData.SDS2.Model.GrooveAngle.html) |             |

##### Remarks

Only valid when MomentType is Welded

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FIsAutoBoltDiameter)IsAutoBoltDiameter

If true, the system will determine a bolt diameter automatically.

##### Declaration

```
public bool IsAutoBoltDiameter { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Only valid when MomentType is Bolted

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FIsAutoBoltType)IsAutoBoltType

If true, set BoltType based on settings from setup. If false, this must be set by the user or API

##### Declaration

```
public bool IsAutoBoltType { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Only valid when MomentType is Bolted

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FIsDesignForDoublers)IsDesignForDoublers

applies when MomentType is Bolted or Welded and when this end of the beam frames to the flange of a column whose shape is a flanged shape such as wide flange.

```
        When true, the system initially creates the connection with web
        doubler plates only if doublers are necessary given the moment
        load on this end of the beam. Connection design locks
        for "Column Web Doublers" become available regardless of whether or
        not web doublers are actually designed. If valid entries are made
        to one or more of these locks, web doublers are designed around
        those entries even if doublers are not required.

        When false, the system does not check to see if doublers are
        needed and, as a result, will not design doublers. A warning in
        the Connection Design Calculations and Expanded Connection Design
        Calculations tells you that the check has been turned off.

```

##### Declaration

```
public bool IsDesignForDoublers { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Since moment options are largely shared, and there are only two distinct connection types, we just have one class for moment connections. Simply set the MomentType and proceed to set applicable properties.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FIsDesignForStiffeners)IsDesignForStiffeners

applies when this beam end's MomentType is Bolted or Welded and that same end of the beam frames to the flange of a column whose shape is a flanged shape such as wide flange.

```
        When true, the system creates column flange stiffeners opposite
        to the beam moment connection based on the choice made to Job
        Setup > Moment Plate Design Criteria > the "Flange stiffeners"
        section > "Design depth." That option sets whether connection
        design always designs full-depth stiffeners or sometimes designs
        half-depth stiffeners or sometimes designs no
        stiffeners. Connection design locks for " Column Flange
        Stiffeners" become available regardless of whether or not the
        stiffeners are actually designed. If valid entries are made to
        one or more of these locks, flange stiffeners are designed per
        those entries even if the stiffeners are not required.

        When false, the system does not check to see if stiffeners are
        needed and, as a result, does not design stiffeners. A warning in
        the Connection Design Calculations and Expanded Connection Design
        Calculations tells you that the check has been turned off.

```

##### Declaration

```
public bool IsDesignForStiffeners { get; set; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Remarks

Since moment options are largely shared, and there are only two distinct connection types, we just have one class for moment connections. Simply set the MomentType and proceed to set applicable properties.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FMomentPlateLocation)MomentPlateLocation

Where to put the moment plates for the moment connection

##### Declaration

```
public MomentPlateLocation MomentPlateLocation { get; set; }
```

##### Property Value

| Type                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [MomentPlateLocation](DesignData.SDS2.Model.MomentPlateLocation.html) |             |

##### Remarks

Only valid for end plate bolted

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FMomentType)MomentType

The moment connection type to set

##### Declaration

```
public MomentType MomentType { get; set; }
```

##### Property Value

| Type                                                | Description |
| --------------------------------------------------- | ----------- |
| [MomentType](DesignData.SDS2.Model.MomentType.html) |             |

##### Remarks

Since moment options are largely shared, and there are only two distinct connection types, we just have one class for moment connections. Simply set the MomentType and proceed to set applicable properties.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FReEntrantCut)ReEntrantCut

The re-entrant cut method to use for a welded moment connection

##### Declaration

```
public ReEntrantCut ReEntrantCut { get; set; }
```

##### Property Value

| Type                                                    | Description |
| ------------------------------------------------------- | ----------- |
| [ReEntrantCut](DesignData.SDS2.Model.ReEntrantCut.html) |             |

##### Remarks

Only valid when MomentType is Welded

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FSeismicMomentConnection)SeismicMomentConnection

The moment specification options.

##### Declaration

```
public AutomaticYesNo SeismicMomentConnection { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

##### Remarks

Since moment options are largely shared, and there are only two distinct connection types, we just have one class for moment connections. Simply set the MomentType and proceed to set applicable properties.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FUseInnerFlangePlates)UseInnerFlangePlates

Automatic applies a setup choice (Job Setup > Design Criteria > "Use inner flange plates for beam splice moment").

Yes specifies that the system design the bolted moment connection using inner flange plates. A total of four inner flange plates may be designed: 1) an upper NS inner flange plate, 2) an upper FS inner flange plate, 3) a lower NS inner flange plate and 4) a lower FS inner flange plate.

No instructs the system to create only top and bottom bolted moment flange plates.

##### Declaration

```
public AutomaticYesNo UseInnerFlangePlates { get; set; }
```

##### Property Value

| Type                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [AutomaticYesNo](DesignData.SDS2.Model.AutomaticYesNo.html) |             |

##### Remarks

This field is only effective if this is a splice plate connection, with a Bolted MomentType and the ConnectionMaterial is set to Plate.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FDispose%5FSystem%5FBoolean%5F)Dispose(bool)

The moment specification options.

##### Declaration

```
protected virtual void Dispose(bool disposing)
```

##### Parameters

| Type                                                          | Name      | Description |
| ------------------------------------------------------------- | --------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | disposing |             |

##### Remarks

Since moment options are largely shared, and there are only two distinct connection types, we just have one class for moment connections. Simply set the MomentType and proceed to set applicable properties.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |

#### [](#DesignData%5FSDS2%5FModel%5FMomentSpecification%5FFinalize)\~MomentSpecification()

The moment specification options.

##### Declaration

```
protected ~MomentSpecification()
```

##### Remarks

Since moment options are largely shared, and there are only two distinct connection types, we just have one class for moment connections. Simply set the MomentType and proceed to set applicable properties.

##### Exceptions

| Type                                                                                   | Condition                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html) | This will be thrown when attempting to set a value that is not valid for the current MomentType. Be sure to set MomentType first, then set other parameters. |