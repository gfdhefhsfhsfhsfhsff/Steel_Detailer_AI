# Class DynamicPython 

For internal use. This wraps python objects and gives access for .Net users. This class is visible, but should always be used with the special "dynamic" type.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject)

DynamicPython

##### Implements

[IDynamicMetaObjectProvider](https://learn.microsoft.com/dotnet/api/system.dynamic.idynamicmetaobjectprovider)

##### Inherited Members

[DynamicObject.TryDeleteMember(DeleteMemberBinder)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trydeletemember) 

[DynamicObject.TryInvokeMember(InvokeMemberBinder, object\[\], out object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.tryinvokemember) 

[DynamicObject.TryConvert(ConvertBinder, out object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.tryconvert) 

[DynamicObject.TryCreateInstance(CreateInstanceBinder, object\[\], out object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trycreateinstance) 

[DynamicObject.TryBinaryOperation(BinaryOperationBinder, object, out object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trybinaryoperation) 

[DynamicObject.TryUnaryOperation(UnaryOperationBinder, out object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.tryunaryoperation) 

[DynamicObject.TryGetIndex(GetIndexBinder, object\[\], out object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trygetindex) 

[DynamicObject.TrySetIndex(SetIndexBinder, object\[\], object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trysetindex) 

[DynamicObject.TryDeleteIndex(DeleteIndexBinder, object\[\])](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trydeleteindex) 

[DynamicObject.GetDynamicMemberNames()](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.getdynamicmembernames) 

[DynamicObject.GetMetaObject(Expression)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.getmetaobject) 

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone) 

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Python](DesignData.SDS2.Python.html)

###### **Assembly**: DesignData.SDS2.Python.dll

##### Syntax

```
public class DynamicPython : DynamicObject, IDynamicMetaObjectProvider
```

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPython%5FDynamicPython%5FToString)ToString()

Return the string representation of the python object. overriding object.ToString()

##### Declaration

```
public override string ToString()
```

##### Returns

| Type                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) |             |

##### Overrides

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

#### [](#DesignData%5FSDS2%5FPython%5FDynamicPython%5FTryGetMember%5FSystem%5FDynamic%5FGetMemberBinder%5FSystem%5FObject%5F%5F)TryGetMember(GetMemberBinder, out object)

For internal use. This fetches a named property from a python object and returns a DynamicPython wrapper for it.

##### Declaration

```
public override bool TryGetMember(GetMemberBinder binder, out object result)
```

##### Parameters

| Type                                                                                     | Name   | Description |
| ---------------------------------------------------------------------------------------- | ------ | ----------- |
| [GetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.getmemberbinder) | binder |             |
| [object](https://learn.microsoft.com/dotnet/api/system.object)                           | result |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[DynamicObject.TryGetMember(GetMemberBinder, out object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trygetmember)

#### [](#DesignData%5FSDS2%5FPython%5FDynamicPython%5FTryInvoke%5FSystem%5FDynamic%5FInvokeBinder%5FSystem%5FObject%5F%5F%5FSystem%5FObject%5F%5F)TryInvoke(InvokeBinder, object\[\], out object)

If this property is a python callable, you can call it

##### Declaration

```
public override bool TryInvoke(InvokeBinder binder, object[] arguments, out object result)
```

##### Parameters

| Type                                                                               | Name      | Description |
| ---------------------------------------------------------------------------------- | --------- | ----------- |
| [InvokeBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.invokebinder) | binder    |             |
| [object](https://learn.microsoft.com/dotnet/api/system.object)\[\]                 | arguments |             |
| [object](https://learn.microsoft.com/dotnet/api/system.object)                     | result    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[DynamicObject.TryInvoke(InvokeBinder, object\[\], out object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.tryinvoke)

#### [](#DesignData%5FSDS2%5FPython%5FDynamicPython%5FTrySetMember%5FSystem%5FDynamic%5FSetMemberBinder%5FSystem%5FObject%5F)TrySetMember(SetMemberBinder, object)

Sets an attribute on a python object.

##### Declaration

```
public override bool TrySetMember(SetMemberBinder binder, object value)
```

##### Parameters

| Type                                                                                     | Name   | Description |
| ---------------------------------------------------------------------------------------- | ------ | ----------- |
| [SetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.setmemberbinder) | binder |             |
| [object](https://learn.microsoft.com/dotnet/api/system.object)                           | value  |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[DynamicObject.TrySetMember(SetMemberBinder, object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trysetmember)

### [](#implements)Implements

[IDynamicMetaObjectProvider](https://learn.microsoft.com/dotnet/api/system.dynamic.idynamicmetaobjectprovider)