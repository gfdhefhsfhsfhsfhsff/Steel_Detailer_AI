# Steel Detailer AI - Development Handoff (03/28/2026)

## Project Overview
**Steel Detailer AI** is an automation and verification suite for SDS/2 structural steel detailing. It utilizes a **Hybrid Plugin Architecture** to leverage the high-speed data transaction capabilities of the SDS2 `.NET 8.0` API combined with the live, in-model UI interaction capabilities of the native SDS2 Python API.

### Current Architecture Summary
- **The Engine (C# .NET)**: Standalone console application (`Program.cs`) encapsulating heavy logic (Transaction locking, Custom Property mapping, gathering Bill of Materials, Pre/Post detail checks). Since the SDS2 .NET API is "headless", this code runs independently of the Modeling window and manipulates the database directly.
- **The UI Bridge (Python)**: Scripts meant to be executed natively via SDS/2's `Run Script` or toolbar buttons. Python interfaces directly with the user's live 3D Modeling viewport (e.g., retrieving Highlighted Members) and seamlessly passes those object handles to the C# application via background `subprocess` calls.

---

## 🟢 Items Completed
1. **Interactive CLI Integration (`Program.cs`)**: Merged all independent checkers into a singular, persistent interactive loop.
    - Option 1: Pre-Detail Model Checker
    - Option 2: Post-Detail Sheet Checker
    - Option 3: Verify BOM & Gather Sheets
    - Option 4: Run QA/QC Verification (Python tool wrapper)
    - Option 5: Bulk Custom Property Updater
2. **Build Stability (`Steel Detailer AI.csproj`)**: Resolved overlapping `Program.cs` namespace issues and cleanly referenced required `DesignData.SDS2.*.dll` and `EPPlus` libraries.
3. **Bulk Custom Property Updater (`Automator1_BulkPropertyUpdater.cs`)**: 
    - Implemented a robust `Transaction` and `ImmediateLockHandler` mechanism to safely modify `Member` objects without corrupting active draftsperson workflows.
    - Implemented **Silent Mode** argument parsing (`--job`, `--repo`, `--handles`, `--prop`, `--val`) to support immediate background execution.
4. **Python Launch Bridge (`BulkUpdaterLauncher.py`)**:
    - Created a Native SDS/2 Tkinter UI macro to grab `selection.MemberSelection()` (highlighted members) directly from the live modeling screen and execute the C# `.NET` code instantly.

---

## 🟡 Items to Complete (Next Priorities)
1. **Title Block Stamper Automator**: Create an automated system to read/write drawing revisions, statuses, and title block metadata globally.
2. **Hole / Bolt Verification Automator**: Automatically check for non-standard framing conditions or apply bulk modifications to fastener properties across sequences.
3. **Expand Python Bridge Macros**: Build standard Python launcher scripts (like `BulkUpdaterLauncher.py`) for the other `.NET` checkers so users can run the `Pre-Detail Model Checker` from an SDS/2 Toolbar button instead of a separate CLI program.
4. **Compile for Production**: Package the repository into a distributable installation folder (`.exe`, `.dll`s, and `.py` macros).

---

## 🔴 Outstanding Issues & Refactoring Needs
1. **CS8602 Null Reference Warnings**:
    - `VerifyBOM.cs` has 4 instances of potentially dereferencing null objects (e.g., missing members on gather sheets).
    - `Checker1` and `Checker2` have multiple `CS8618` warnings for non-nullable properties (PieceMark, Sequence, Details) exiting constructors uninitialized.
2. **Hardcoded Testing Paths**:
    - `BulkUpdaterLauncher.py` currently utilizes `subprocess.run(["dotnet", "run", "--project", ...])` pointing directly to `d:\Steel_Detailer_AI\Steel Detailer AI.csproj`. For production delivery to other detailers, this Python script must be modified to call the compiled executable (`Steel Detailer AI.exe`) via relative paths. 
3. **SDS/2 API Python Dependency**:
    - Relying on SDS/2's local Python interpreter requires ensuring future versions of SDS/2 (e.g., v2027) maintain standard `sds2` module bindings, specifically `selection.MemberSelection()`.

---

## 📘 Agent Handoff Context & Technical Notes
- **Workspace Location**: `d:\Steel_Detailer_AI`
- **SDS/2 Dependencies**: The project requires `C:\Program Files\SDS2_2026\2026\bin\` to compile. Standard `DataDirectory.Open(DataDirectory.Default)` is used.
- **Crucial Rule on SDS2 .NET Locking**: Never bypass `ILockHandler`. Always instantiate `new Transaction(job, new ImmediateLockHandler())`, execute `.Add(handle)`, verify `.Lock()`, alter properties, and call `.Commit()`. The `.NET` API will crash or corrupt data if properties are changed outside an active lock.
- **Reference Docs**: The user has successfully scraped `.md` API documentation locally. Utilize `grep_search` heavily on `d:\Steel_Detailer_AI\sds tooling\output\2026\API\` to discover properties and handle constraints (e.g., `CustomPropertyMapHandle`).
