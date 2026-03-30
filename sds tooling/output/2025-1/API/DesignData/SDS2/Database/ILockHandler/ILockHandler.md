# Interface ILockHandler 

This interface defines the callbacks that must be provided for locking feedback. Either informing a user, or making decisions without user intervention, about how to handle situations where a desired piece cannot be locked.

The only choices are to wait for a lock or give up, if any locks couldn't be made.

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Database](DesignData.SDS2.Database.html)

###### **Assembly**: DesignData.SDS2.Database.dll

##### Syntax

```
public interface ILockHandler
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FDatabase%5FILockHandler%5FEventLoop)EventLoop()

This is called at the end of each attempt to lock everything. If you're implementing this as a single threaded GUI you can process events here. We won't make another lock attempt until this method exits, and .1 seconds has passed (to avoid spamming the database).

If you do nothing with this we'll wait .1 seconds and attempt to lock again.

Your return here decides if we continue trying for the lock.

This will not be called if we successfully lock everything on the first attempt.

##### Declaration

```
bool EventLoop()
```

##### Returns

| Type                                                          | Description                           |
| ------------------------------------------------------------- | ------------------------------------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) | true if you want to continue waiting. |

#### [](#DesignData%5FSDS2%5FDatabase%5FILockHandler%5FLockFailed%5FDesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5FSystem%5FString%5F)LockFailed(TableIndexHandle, string)

This is called whenever we try to lock an item and can't get the lock. This may be called over and over and over.

##### Declaration

```
void LockFailed(TableIndexHandle databaseItem, string userMessage)
```

##### Parameters

| Type                                                               | Name         | Description                                                                      |
| ------------------------------------------------------------------ | ------------ | -------------------------------------------------------------------------------- |
| [TableIndexHandle](DesignData.SDS2.Database.TableIndexHandle.html) | databaseItem | The item we could not lock                                                       |
| [string](https://learn.microsoft.com/dotnet/api/system.string)     | userMessage  | A helpful message you can display to the user to explain why it can't be locked. |

##### Remarks

At this point it's too late to decide you don't need a modification if you can't get a lock. Either the whole transaction has to be aborted, or you wait for the lock.

#### [](#DesignData%5FSDS2%5FDatabase%5FILockHandler%5FLockSucceeded%5FDesignData%5FSDS2%5FDatabase%5FTableIndexHandle%5F)LockSucceeded(TableIndexHandle)

This is called whenever we're able to lock an item. This will be called at most once per item.

##### Declaration

```
void LockSucceeded(TableIndexHandle databaseItem)
```

##### Parameters

| Type                                                               | Name         | Description |
| ------------------------------------------------------------------ | ------------ | ----------- |
| [TableIndexHandle](DesignData.SDS2.Database.TableIndexHandle.html) | databaseItem |             |