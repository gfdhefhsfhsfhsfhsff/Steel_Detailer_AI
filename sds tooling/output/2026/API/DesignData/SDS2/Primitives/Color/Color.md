# Class Color 

A color compatible with SDS2's colors. This object knows how to translate to and from SDS2 pen numbers. It works on a 0-255 rgba color scale.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

Color

##### Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype) 

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object-system-object%29) 

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals) 

###### **Namespace**: [DesignData](DesignData.html).[SDS2](DesignData.SDS2.html).[Primitives](DesignData.SDS2.Primitives.html)

###### **Assembly**: DesignData.SDS2.Primitives.dll

##### Syntax

```
public sealed class Color
```

### [](#constructors)Constructors 

#### [](#DesignData%5FSDS2%5FPrimitives%5FColor%5F%5Fctor%5FDesignData%5FSDS2%5FPrimitives%5FPenColor%5F)Color(PenColor)

Create a color from the PenColor

##### Declaration

```
public Color(PenColor pen)
```

##### Parameters

| Type                                                 | Name | Description |
| ---------------------------------------------------- | ---- | ----------- |
| [PenColor](DesignData.SDS2.Primitives.PenColor.html) | pen  |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FColor%5F%5Fctor%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FInt32%5FSystem%5FInt32%5F)Color(int, int, int, int)

Create a color from rgba values, from 0-255

##### Declaration

```
public Color(int red, int green, int blue, int alpha = 255)
```

##### Parameters

| Type                                                       | Name  | Description |
| ---------------------------------------------------------- | ----- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | red   |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | green |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | blue  |             |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) | alpha |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FColor%5F%5Fctor%5FSystem%5FString%5F)Color(string)

Create a color from a hash or pound string, like in html: "#E6E6FA"

##### Declaration

```
public Color(string poundcolor)
```

##### Parameters

| Type                                                           | Name       | Description |
| -------------------------------------------------------------- | ---------- | ----------- |
| [string](https://learn.microsoft.com/dotnet/api/system.string) | poundcolor |             |

### [](#methods)Methods 

#### [](#DesignData%5FSDS2%5FPrimitives%5FColor%5FEquals%5FSystem%5FObject%5F)Equals(object)

A color compatible with SDS2's colors. This object knows how to translate to and from SDS2 pen numbers. It works on a 0-255 rgba color scale.

##### Declaration

```
public override bool Equals(object other)
```

##### Parameters

| Type                                                           | Name  | Description |
| -------------------------------------------------------------- | ----- | ----------- |
| [object](https://learn.microsoft.com/dotnet/api/system.object) | other |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

##### Overrides

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals%28system-object%29)

#### [](#DesignData%5FSDS2%5FPrimitives%5FColor%5FFinalize)\~Color()

A color compatible with SDS2's colors. This object knows how to translate to and from SDS2 pen numbers. It works on a 0-255 rgba color scale.

##### Declaration

```
protected ~Color()
```

#### [](#DesignData%5FSDS2%5FPrimitives%5FColor%5FGetHashCode)GetHashCode()

A color compatible with SDS2's colors. This object knows how to translate to and from SDS2 pen numbers. It works on a 0-255 rgba color scale.

##### Declaration

```
public override int GetHashCode()
```

##### Returns

| Type                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [int](https://learn.microsoft.com/dotnet/api/system.int32) |             |

##### Overrides

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

#### [](#DesignData%5FSDS2%5FPrimitives%5FColor%5FGetNearestPen)GetNearestPen()

Get the closest pen for this color. This is primarily used internally in SDS2 for pen plotter support.

##### Declaration

```
public PenColor GetNearestPen()
```

##### Returns

| Type                                                 | Description |
| ---------------------------------------------------- | ----------- |
| [PenColor](DesignData.SDS2.Primitives.PenColor.html) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FColor%5FToString)ToString()

Get the pound or hash string value of this color

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

### [](#operators)Operators 

#### [](#DesignData%5FSDS2%5FPrimitives%5FColor%5Fop%5FEquality%5FDesignData%5FSDS2%5FPrimitives%5FColor%5FDesignData%5FSDS2%5FPrimitives%5FColor%5F)operator ==(Color, Color)

A color compatible with SDS2's colors. This object knows how to translate to and from SDS2 pen numbers. It works on a 0-255 rgba color scale.

##### Declaration

```
public static bool operator ==(Color a, Color b)
```

##### Parameters

| Type                                           | Name | Description |
| ---------------------------------------------- | ---- | ----------- |
| [Color](DesignData.SDS2.Primitives.Color.html) | a    |             |
| [Color](DesignData.SDS2.Primitives.Color.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |

#### [](#DesignData%5FSDS2%5FPrimitives%5FColor%5Fop%5FInequality%5FDesignData%5FSDS2%5FPrimitives%5FColor%5FDesignData%5FSDS2%5FPrimitives%5FColor%5F)operator !=(Color, Color)

A color compatible with SDS2's colors. This object knows how to translate to and from SDS2 pen numbers. It works on a 0-255 rgba color scale.

##### Declaration

```
public static bool operator !=(Color a, Color b)
```

##### Parameters

| Type                                           | Name | Description |
| ---------------------------------------------- | ---- | ----------- |
| [Color](DesignData.SDS2.Primitives.Color.html) | a    |             |
| [Color](DesignData.SDS2.Primitives.Color.html) | b    |             |

##### Returns

| Type                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [bool](https://learn.microsoft.com/dotnet/api/system.boolean) |             |