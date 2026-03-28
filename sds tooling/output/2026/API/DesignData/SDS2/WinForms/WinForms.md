# Namespace DesignData.SDS2.WinForms 

### [](#classes)Classes 

#### [](#interactivelockhandler)[InteractiveLockHandler](DesignData.SDS2.WinForms.InteractiveLockHandler.html)

Pass one of these to Transaction.Lock to get a GUI lock screen when locks aren't immediately available. Users will be able to abort waiting for locks which will cause your Lock() call to return false.

#### [](#licensinginitialization)[LicensingInitialization](DesignData.SDS2.WinForms.LicensingInitialization.html)

Helper functions for licensing, which sometimes has to be interactive since the user must login to their license account if no credentials are on file.