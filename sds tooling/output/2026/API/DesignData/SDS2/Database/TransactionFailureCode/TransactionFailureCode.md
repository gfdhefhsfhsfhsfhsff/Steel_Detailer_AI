# Enum TransactionFailureCode 

Reasons a transaction may fail to commit

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public enum TransactionFailureCode
```

### [](#fields)Fields 

| Name                               | Description                                                                                                                                                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BrokenApartMemberGroupingViolation | An attempt was made to remove part of a linked member (generally these are the pieces of a broken apart member) from a group without removing all of the other members in that link.                                                                                            |
| ConnectionDesignFailure            | Connection design failed.                                                                                                                                                                                                                                                       |
| DefunctModifier                    | Usually an internal issue, an element of the transaction seems to have disappeared during commit.                                                                                                                                                                               |
| InvalidMemberOrientation           | Attempt to set an orientation flag for a member which SDS2 does not support.                                                                                                                                                                                                    |
| InvalidStitchPlateValue            | The user stitch plate settings given are not necessarily possible, so the change is being rejected.                                                                                                                                                                             |
| InvalidValue                       | Some value on an object in the transaction is not legal                                                                                                                                                                                                                         |
| KeepPiecemarkDisallowed            | An attempt was made to perform a keep piecemark operation, but in this case it cannot be allowed.                                                                                                                                                                               |
| LockedByAnotherUser                | A needed element was already locked by another process, possibly another process under this current user or one from another user.          This can be, somewhat, addressed by implementingw or using a          LockHandler which will wait until that element can be locked. |
| LockedEnd                          | Attempt to change a member end which is locked (not a temporary lock to prevent two users from changing something at the same time, but a user lock flag on the end is set to prevent future modifications).                                                                    |
| MembersOverlap                     | The changes made would cause two members to overlap in an illegal way.                                                                                                                                                                                                          |
| ModelComplete                      | The operation could not proceed because it would change a member which is model complete (restrictive)                                                                                                                                                                          |
| PiecemarkIsFrozen                  | The operation could not proceed because it would require changing a member with a frozen piecemark.                                                                                                                                                                             |
| StationRestriction                 | The current station type, or license, does not allow this type of change.                                                                                                                                                                                                       |