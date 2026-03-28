# Namespace DesignData.SDS2.Exceptions 

### [](#classes)Classes 

#### [](#custompropertymissingexception)[CustomPropertyMissingException](DesignData.SDS2.Exceptions.CustomPropertyMissingException.html)

Thrown when a requested custom property is not in the custom property schema for this job.

#### [](#custompropertytypemismatchexception)[CustomPropertyTypeMismatchException](DesignData.SDS2.Exceptions.CustomPropertyTypeMismatchException.html)

Thrown when a requested custom property is in the custom property schema for this job, but the type is not what was requested.

#### [](#ifcexception)[IFCException](DesignData.SDS2.Exceptions.IFCException.html)

This is thrown when there is an issue with the settings passed to IFCExport functions

#### [](#invalidhandleexception)[InvalidHandleException](DesignData.SDS2.Exceptions.InvalidHandleException.html)

Thrown when retrieving a Handle's object from the database, but the object does not exist in the database.

#### [](#invalidoperationexception)[InvalidOperationException](DesignData.SDS2.Exceptions.InvalidOperationException.html)

When an operation constraint is not satisfied, usually something like: not using a Transaction when setting properties, or failing to .Add an object and .Lock before modifing any object.

#### [](#invalidpolygonexception)[InvalidPolygonException](DesignData.SDS2.Exceptions.InvalidPolygonException.html)

Thrown when a given polygon is not valid.

#### [](#invalidvalueexception)[InvalidValueException](DesignData.SDS2.Exceptions.InvalidValueException.html)

Thrown when a value given does not meet the validation requirements.

#### [](#jobnotopenexception)[JobNotOpenException](DesignData.SDS2.Exceptions.JobNotOpenException.html)

This exception is thrown when a property or method is accessed on an object from a job that is not the currently opened job.

#### [](#materialexception)[MaterialException](DesignData.SDS2.Exceptions.MaterialException.html)

Thrown for various material-related errors.

#### [](#noprocesslicenseexception)[NoProcessLicenseException](DesignData.SDS2.Exceptions.NoProcessLicenseException.html)

This is thrown when you attempt to process members from python/C# code when the workstation does not have the API\_PROCESSING license featrue. To resolve this you need to either remove transaction commits with processMembers: true or acquire the API\_PROCESSING license feature

#### [](#notaddedexception)[NotAddedException](DesignData.SDS2.Exceptions.NotAddedException.html)

This is thrown when an attempt to set an object's data without first adding it to a transaction. It's necessary to add things to transactions so they can be locked and refreshed.

#### [](#notlicensedexception)[NotLicensedException](DesignData.SDS2.Exceptions.NotLicensedException.html)

The existence of this summary silences a compiler warning. Somebody should replace this with a real description of this exception.

#### [](#notlockedexception)[NotLockedException](DesignData.SDS2.Exceptions.NotLockedException.html)

This is thrown when you attempt to access or modify something that's not locked primarily when under a writeable Transaction. To resolve this you usually need to add that object to the transaction: Transaction.Add(object)

#### [](#piecemarkexistsexception)[PiecemarkExistsException](DesignData.SDS2.Exceptions.PiecemarkExistsException.html)

Thrown when piecemark assigned is already in use by a different object.

#### [](#programexception)[ProgramException](DesignData.SDS2.Exceptions.ProgramException.html)

Thrown when there's an internal error in SDS/2's native implementation.

#### [](#pythonexception)[PythonException](DesignData.SDS2.Exceptions.PythonException.html)

Thrown when there's an exception in a python call