# Class TransactionFailure 

A commit, authentication, or locking failure from a Transaction

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

TransactionFailure

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public class TransactionFailure
```

### [](#properties)Properties 

#### [](#DesignData%5FSDS2%5FDatabase%5FTransactionFailure%5FCode)Code

The type or cause of failure

##### Declaration

```
public TransactionFailureCode Code { get; }
```

##### Property Value

| Type                                                                           | Description |
| ------------------------------------------------------------------------------ | ----------- |
| [TransactionFailureCode](DesignData.SDS2.Database.TransactionFailureCode.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FTransactionFailure%5FReason)Reason

A string description of this failure, localized and ready to be presented to the user.

##### Declaration

```
public string Reason { get; }
```

##### Property Value

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FTransactionFailure%5FTransactionFailed)TransactionFailed

True if the operation failed, if this is the case you can check Code and Reason to see why

##### Declaration

```
public bool TransactionFailed { get; }
```

##### Property Value

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FTransactionFailure%5FFinalize)\~TransactionFailure()

A commit, authentication, or locking failure from a Transaction

##### Declaration

```
protected ~TransactionFailure()
```

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FDatabase%5FTransactionFailure%5Fop%5FImplicit%5FDesignData%5FSDS2%5FDatabase%5FTransactionFailure%5F%5FDesignData%5FSDS2%5FDatabase%5FTransactionFailureCode)implicit operator TransactionFailureCode(TransactionFailure)

Implicit conversion to success/failure code

##### Declaration

```
public static implicit operator TransactionFailureCode(TransactionFailure value)
```

##### Parameters

| Type                                                                   | Name  | Description |
| ---------------------------------------------------------------------- | ----- | ----------- |
| [TransactionFailure](DesignData.SDS2.Database.TransactionFailure.html) | value |             |

##### Returns

| Type                                                                           | Description |
| ------------------------------------------------------------------------------ | ----------- |
| [TransactionFailureCode](DesignData.SDS2.Database.TransactionFailureCode.html) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FTransactionFailure%5Fop%5FImplicit%5FDesignData%5FSDS2%5FDatabase%5FTransactionFailure%5F%5FSystem%5FBoolean)implicit operator bool(TransactionFailure)

Implicit conversion to success/failure bool. True meaning the transaction passed, false meaning it failed. So the opposite of TransactionFailed.

##### Declaration

```
public static implicit operator bool(TransactionFailure value)
```

##### Parameters

| Type                                                                   | Name  | Description |
| ---------------------------------------------------------------------- | ----- | ----------- |
| [TransactionFailure](DesignData.SDS2.Database.TransactionFailure.html) | value |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FDatabase%5FTransactionFailure%5Fop%5FImplicit%5FDesignData%5FSDS2%5FDatabase%5FTransactionFailure%5F%5FSystem%5FString)implicit operator string(TransactionFailure)

Implicit conversion to user visible string

##### Declaration

```
public static implicit operator string(TransactionFailure value)
```

##### Parameters

| Type                                                                   | Name  | Description |
| ---------------------------------------------------------------------- | ----- | ----------- |
| [TransactionFailure](DesignData.SDS2.Database.TransactionFailure.html) | value |             |

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |