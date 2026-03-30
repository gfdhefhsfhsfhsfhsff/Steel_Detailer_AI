# Fetch drawings

To grab all drawings of one type, start with the [Job](../api/DesignData.SDS2.Database.Job.html) object to get a list of drawing handles. These handles may then be passed to [Drawing.Get](../api/DesignData.SDS2.Detail.Drawing.html#DesignData%5FSDS2%5FDetail%5FDrawing%5FGet%5FDesignData%5FSDS2%5FDatabase%5FDrawingHandle%5F)to get each drawing.

```
using DesignData.SDS2.Database;
using DesignData.SDS2.Detail;

```

```
var handles = job.GetDrawingHandles(TableWithDrawings.ErectionSheet);
Drawing first_evu_sheet = Drawing.Get(handles[0]);
Console.WriteLine($"Detail Complete: {first_evu_sheet.Status.DetailCompleteDate}");

```

To find a drawing by name, use [Drawing.Find](../api/DesignData.SDS2.Detail.Drawing.html#DesignData%5FSDS2%5FDetail%5FDrawing%5FFind%5FDesignData%5FSDS2%5FDatabase%5FTableWithDrawings%5FSystem%5FString%5F). Since there may be more than one drawing with a given name, a list of drawings is returned rather than a single drawing.

```
DrawingList gather_sheet_a1 = Drawing.Find(TableWithDrawings.GatherSheet, "a1");
Console.WriteLine($"Detail Complete: {gather_sheet_a1[0].Status.DetailCompleteDate}");

```

Similarly, to find a drawing for a piecemark:

```
DrawingList drawing_1B1 = Drawing.Find(PiecemarkType.Major, "1B1");
Console.WriteLine($"Detail Complete: {drawing_1B1[0].Status.DetailCompleteDate}");

```