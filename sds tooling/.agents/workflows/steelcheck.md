---
description: Load the SDS2 SteelCheck QA/QC tooling context (Checker1, Checker2, VerifyBOM)
---

# /steelcheck — SDS2 SteelCheck QA/QC Suite

When this workflow is invoked, load the full SteelCheck knowledge base to get up to speed on the project.

## Steps

1. Read the knowledge artifact for full context:
   - Path: Look in the brain artifacts for `sds2_steelcheck_knowledge.md`
   - This contains: all scripts, API patterns, build/run commands, known bugs, and future plans.

2. The key source files live in the `sds tooling/` directory (relative to repo root):
   - `Checker1_PreDetailModelVerify.cs` — Pre-detailing model verification
   - `Checker2_PostDetailSheetVerify.cs` — Post-detailing sheet/drawing verification
   - `VerifyBOM.cs` — Helper BOM verification methods
   - `Checker1\Checker1.csproj` / `Checker2\Checker2.csproj` — .NET 4.8 projects

3. The SDS2 .NET API documentation is at `sds tooling/output/` (relative to repo root):
   - `output/API/` — Class/method docs (follow namespace hierarchy)
   - `output/Tutorials/` — Workflow tutorials
   - `agents.md` — Agent navigation guide

4. Build commands (run from repo root or adjust paths accordingly):
```powershell
dotnet build "sds tooling\Checker1\Checker1.csproj"
dotnet build "sds tooling\Checker2\Checker2.csproj"
```

5. Run commands (run from repo root or adjust paths accordingly):
```powershell
& "sds tooling\Checker1\bin\net48\Checker1.exe"
& "sds tooling\Checker2\bin\net48\Checker2.exe"
```
