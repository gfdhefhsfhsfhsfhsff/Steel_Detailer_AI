// ============================================================================
// CHECKER 1: Pre-Detailing Model Verification
// Purpose: Run BEFORE sheets are created to verify the model is complete
//          and ready for detailing. Includes a master report showing all
//          piecemarks categorized as User Marks vs System Marks.
//          Also performs bolt/hole/galv checks and optionally colors
//          flagged members RED in the model.
//
// OUTPUT: Excel spreadsheet with Summary, Issues, Master Report, and
//         Bolt/Hole Detail sheets.
//         Issues sheet has a "Resolved" checkbox column with strikethrough.
// ============================================================================
using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using DesignData.SDS2.Database;
using DesignData.SDS2.Model;
using OfficeOpenXml;
using OfficeOpenXml.Style;

namespace SDS2Workflow
{
    public class PreDetailModelChecker
    {
        private static readonly Regex SystemMarkPattern = new Regex(
            @"^[A-Z]{1,3}_\d+$", RegexOptions.Compiled);

        public class Issue
        {
            public int MemberNumber { get; set; }
            public string Piecemark { get; set; } = null!;
            public string IssueType { get; set; } = null!;
            public string Sequence { get; set; } = null!;
            public string Details { get; set; } = null!;
            public MemberHandle Handle { get; set; } = null!;
        }

        public class BoltHoleDetail
        {
            public int MemberNumber { get; set; }
            public string Piecemark { get; set; } = null!;
            public int MaterialCount { get; set; }
            public int TotalHoles { get; set; }
            public int MatchableHoles { get; set; }
            public int FieldBolts { get; set; }
            public int ShopBolts { get; set; }
            public bool MemberIsGalvanized { get; set; }
            public string BoltFinishes { get; set; } = "";
        }

        public class ConnectionDetail
        {
            public int MemberNumber { get; set; }
            public string Piecemark { get; set; } = null!;
            public string MemberTypeName { get; set; } = "";
            public string End { get; set; } = "";
            public string ConnectionType { get; set; } = "NONE";
            public bool IsForced { get; set; }
            public bool IsUserDefined { get; set; }
            public bool HasFailure { get; set; }
            public string FailureMessage { get; set; } = "";
        }

        public class LoadDetail
        {
            public int MemberNumber { get; set; }
            public string Piecemark { get; set; } = null!;
            public string MemberTypeName { get; set; } = "";
            public string End { get; set; } = "";
            public double ShearLoad { get; set; }
            public bool IsAutoShear { get; set; }
            public double MomentLoad { get; set; }
            public bool IsAutoMoment { get; set; }
            public double TensionLoad { get; set; }
            public bool IsAutoTension { get; set; }
            public string LoadSource { get; set; } = "Auto";
        }

        [STAThread]
        public static void Main(string[] args)
        {
            DataDirectory.Open(DataDirectory.Default);

            // --- Step 1: Select Repository ---
            var repositories = Repository.GetAllRepositories();
            Console.WriteLine("==========================================================");
            Console.WriteLine("  Available Repositories:");
            Console.WriteLine("==========================================================");
            for (int i = 0; i < repositories.Count; i++)
                Console.WriteLine($"  [{i + 1}] {repositories[i].Name}");

            Console.Write("\n  Select repository number: ");
            int repoIndex = int.Parse(Console.ReadLine().Trim()) - 1;
            var selectedRepo = repositories[repoIndex];

            // --- Step 2: Select Job ---
            var jobIds = selectedRepo.JobIdentifiers;
            Console.WriteLine($"\n  Jobs in '{selectedRepo.Name}':");
            Console.WriteLine("----------------------------------------------------------");
            for (int i = 0; i < jobIds.Count; i++)
                Console.WriteLine($"  [{i + 1}] {jobIds[i].Name}");

            Console.Write("\n  Select job number: ");
            int jobIndex = int.Parse(Console.ReadLine().Trim()) - 1;
            var selectedJobId = jobIds[jobIndex];

            var job = Job.FindJob(selectedJobId);
            job.Open();
            Console.WriteLine($"\n  Opened: {selectedJobId.Name}");

            // --- Step 3: Discover & Select Sequences ---
            Console.WriteLine("\n  Scanning sequences in model...");
            var allSequences = new Dictionary<string, int>();

            using (var scanTx = new ReadOnlyTransaction(job))
            {
                foreach (var handle in job.Members)
                {
                    var member = MemberBrief.Get(handle);
                    if (member.Sequence == null) continue;
                    string seqName = member.Sequence.Name;
                    if (allSequences.ContainsKey(seqName))
                        allSequences[seqName]++;
                    else
                        allSequences[seqName] = 1;
                }
            }

            Console.WriteLine("\n  Available Sequences:");
            Console.WriteLine("----------------------------------------------------------");
            var seqKeys = new List<string>(allSequences.Keys);
            seqKeys.Sort();
            for (int i = 0; i < seqKeys.Count; i++)
                Console.WriteLine($"  [{i + 1}] {seqKeys[i]}  ({allSequences[seqKeys[i]]} members)");
            Console.WriteLine($"  [A] All sequences");

            Console.Write("\n  Enter sequence numbers (comma-separated) or 'A' for all: ");
            string input = Console.ReadLine().Trim();

            var targetSequences = new List<string>();
            if (input.Equals("A", StringComparison.OrdinalIgnoreCase))
            {
                targetSequences = seqKeys;
            }
            else
            {
                foreach (var part in input.Split(','))
                {
                    int idx = int.Parse(part.Trim()) - 1;
                    if (idx >= 0 && idx < seqKeys.Count)
                        targetSequences.Add(seqKeys[idx]);
                }
            }

            Console.WriteLine($"\n  Checking sequences: {string.Join(", ", targetSequences)}\n");

            var issues = RunPreDetailCheck(job, selectedJobId.Name, targetSequences);

            var colorableIssues = issues.Where(i => i.Handle != null).ToList();
            if (colorableIssues.Count > 0)
            {
                Console.Write("\n  Apply RED color to flagged members in the model? (Y/N): ");
                string colorInput = Console.ReadLine().Trim();
                if (colorInput.Equals("Y", StringComparison.OrdinalIgnoreCase))
                {
                    ApplyStatusColors(job, colorableIssues);
                }
                else
                {
                    Console.WriteLine("  Color application skipped.");
                }
            }

            Console.WriteLine("\nPress Enter to exit...");
            Console.ReadLine();
        }

        public static List<Issue> RunPreDetailCheck(Job job, string jobName, List<string> targetSequences)
        {
            Console.WriteLine("==========================================================");
            Console.WriteLine("  CHECKER 1: Pre-Detailing Model Verification");
            Console.WriteLine("==========================================================\n");

            int totalChecked      = 0;
            int notProcessedCount = 0;
            int notModelComplete  = 0;
            int noShapeAssigned   = 0;

            int missingFieldBolts = 0;
            int missingShopBolts  = 0;
            int mismatchedHoles  = 0;
            int missingHoles      = 0;
            int galvMismatch      = 0;

            int missingConnection    = 0;
            int forcedConnection     = 0;
            int userConnection       = 0;
            int baseCapPlateSchedule = 0;
            int embedsFound          = 0;
            int forcedUserPiecemark  = 0;
            int graphicalConnection  = 0;
            int momentConnection     = 0;
            int shearTabConnection   = 0;
            int clipAngleConnection  = 0;
            int endPlateConnection   = 0;
            int vbraceUserLoad       = 0;
            int beamUserLoad         = 0;

            var userMarks   = new List<string>();
            var systemMarks = new List<string>();
            var issues      = new List<Issue>();
            var boltHoleDetails = new List<BoltHoleDetail>();
            var connectionDetails = new List<ConnectionDetail>();
            var loadDetails = new List<LoadDetail>();

            using (var transaction = new ReadOnlyTransaction(job))
            {
                foreach (var handle in job.Members)
                {
                    var member = MemberBrief.Get(handle);

                    if (member.Sequence == null) continue;
                    string seqName = member.Sequence.Name;
                    if (!targetSequences.Contains(seqName)) continue;

                    totalChecked++;
                    string pcmk = member.Piecemark;

                    // Categorize mark
                    if (SystemMarkPattern.IsMatch(pcmk))
                    {
                        if (!systemMarks.Contains(pcmk)) systemMarks.Add(pcmk);
                    }
                    else
                    {
                        if (!userMarks.Contains(pcmk)) userMarks.Add(pcmk);
                    }

                    // --- Existing Check 1: NOT PROCESSED ---
                    if (member.IsMarkedForProcess)
                    {
                        notProcessedCount++;
                        issues.Add(new Issue
                        {
                            MemberNumber = member.Number,
                            Piecemark = pcmk,
                            IssueType = "NOT PROCESSED",
                            Sequence = seqName,
                            Details = "Member is still marked for process (stale solids)",
                            Handle = handle
                        });
                    }

                    // --- Existing Check 2: NOT MODEL COMPLETE ---
                    if (member.ModelCompleteDate == null)
                    {
                        notModelComplete++;
                        issues.Add(new Issue
                        {
                            MemberNumber = member.Number,
                            Piecemark = pcmk,
                            IssueType = "NOT MODEL COMPLETE",
                            Sequence = seqName,
                            Details = "No Model Complete date is set",
                            Handle = handle
                        });
                    }

                    // --- Existing Check 3: NO SHAPE ---
                    if (member.Shape == null)
                    {
                        noShapeAssigned++;
                        issues.Add(new Issue
                        {
                            MemberNumber = member.Number,
                            Piecemark = pcmk,
                            IssueType = "NO SHAPE",
                            Sequence = seqName,
                            Details = "No shape/section size assigned",
                            Handle = handle
                        });
                    }

                    // --- NEW: Bolt / Hole / Galv Checks ---
                    try
                    {
                        var fullMember = Member.Get(handle);
                        var bolts = fullMember.GetBolts();
                        var materials = fullMember.GetMaterial();

                        int fieldBoltCount = 0;
                        int shopBoltCount = 0;
                        bool hasNonGalvBolt = false;
                        bool hasGalvBolt = false;
                        var finishNames = new HashSet<string>();

                        foreach (var bolt in bolts)
                        {
                            if (bolt.IsFieldBolt)
                                fieldBoltCount++;
                            else
                                shopBoltCount++;

                            finishNames.Add(bolt.Finish.ToString());

                            bool thisBoltIsGalv = bolt.Finish == BoltFinish.HotDippedGalvanized
                                                || bolt.Finish == BoltFinish.MechanicallyGalvanized;
                            if (thisBoltIsGalv)
                                hasGalvBolt = true;
                            else
                                hasNonGalvBolt = true;
                        }

                        int totalHoles = 0;
                        int matchableHoles = 0;
                        int mainMatHoles = 0;
                        int connMatMatchable = 0;
                        bool foundMismatch = false;
                        string mismatchInfo = "";

                        foreach (var mat in materials)
                        {
                            var holes = mat.Holes;
                            int matMatchable = 0;

                            foreach (var hole in holes)
                            {
                                totalHoles++;
                                if (hole.IsMatchable) matMatchable++;

                                var grp = hole.Group;
                                if (grp != null)
                                {
                                    double diaDiff = Math.Abs(grp.Diameter - grp.BoltDiameter);
                                    if (diaDiff > 0.0625)
                                    {
                                        foundMismatch = true;
                                        mismatchInfo = $"Hole dia {grp.Diameter:F4}\" vs bolt dia {grp.BoltDiameter:F4}\" on \"{mat.Description}\" (diff {diaDiff:F4}\")";
                                    }
                                }
                            }

                            matchableHoles += matMatchable;

                            if (mat.IsMain)
                                mainMatHoles += holes.Count;
                            else
                                connMatMatchable += matMatchable;
                        }

                        // --- New Check 1: MISSING FIELD BOLTS ---
                        if (connMatMatchable > 0 && fieldBoltCount == 0)
                        {
                            missingFieldBolts++;
                            issues.Add(new Issue
                            {
                                MemberNumber = member.Number,
                                Piecemark = pcmk,
                                IssueType = "MISSING FIELD BOLTS",
                                Sequence = seqName,
                                Details = $"{connMatMatchable} matchable hole(s) on connection materials but 0 field bolts",
                                Handle = handle
                            });
                        }

                        // --- New Check 2: MISSING SHOP BOLTS ---
                        if (connMatMatchable > 0 && shopBoltCount == 0)
                        {
                            missingShopBolts++;
                            issues.Add(new Issue
                            {
                                MemberNumber = member.Number,
                                Piecemark = pcmk,
                                IssueType = "MISSING SHOP BOLTS",
                                Sequence = seqName,
                                Details = $"{connMatMatchable} matchable hole(s) on connection materials but 0 shop bolts",
                                Handle = handle
                            });
                        }

                        // --- New Check 3: MISMATCHED HOLES ---
                        if (foundMismatch)
                        {
                            mismatchedHoles++;
                            issues.Add(new Issue
                            {
                                MemberNumber = member.Number,
                                Piecemark = pcmk,
                                IssueType = "MISMATCHED HOLES",
                                Sequence = seqName,
                                Details = mismatchInfo,
                                Handle = handle
                            });
                        }

                        // --- New Check 4: MISSING HOLES ---
                        if (connMatMatchable > 0 && mainMatHoles == 0)
                        {
                            missingHoles++;
                            issues.Add(new Issue
                            {
                                MemberNumber = member.Number,
                                Piecemark = pcmk,
                                IssueType = "MISSING HOLES",
                                Sequence = seqName,
                                Details = $"Connection materials have {connMatMatchable} matchable hole(s) but main material has 0 holes",
                                Handle = handle
                            });
                        }

                        // --- New Check 5: GALVANIZED CHECK ---
                        bool memberIsGalv = member.IsGalvanized;

                        if (memberIsGalv && hasNonGalvBolt)
                        {
                            galvMismatch++;
                            issues.Add(new Issue
                            {
                                MemberNumber = member.Number,
                                Piecemark = pcmk,
                                IssueType = "GALVANIZED CHECK",
                                Sequence = seqName,
                                Details = $"Member is galvanized but has non-galvanized bolts ({string.Join(", ", finishNames)})",
                                Handle = handle
                            });
                        }
                        else if (!memberIsGalv && hasGalvBolt)
                        {
                            galvMismatch++;
                            issues.Add(new Issue
                            {
                                MemberNumber = member.Number,
                                Piecemark = pcmk,
                                IssueType = "GALVANIZED CHECK",
                                Sequence = seqName,
                                Details = "Member is NOT galvanized but has galvanized bolts",
                                Handle = handle
                            });
                        }

                        // Record bolt/hole detail for Excel
                        boltHoleDetails.Add(new BoltHoleDetail
                        {
                            MemberNumber = member.Number,
                            Piecemark = pcmk,
                            MaterialCount = materials.Count,
                            TotalHoles = totalHoles,
                            MatchableHoles = matchableHoles,
                            FieldBolts = fieldBoltCount,
                            ShopBolts = shopBoltCount,
                            MemberIsGalvanized = memberIsGalv,
                            BoltFinishes = finishNames.Count > 0 ? string.Join(", ", finishNames) : "(none)"
                        });

                        // ========== CONNECTION & LOAD CHECKS ==========
                        var memberType = member.MemberType;
                        string mtype = memberType.Name;
                        bool isBeam = memberType == typeof(Beam);
                        bool isColumn = memberType == typeof(Column);
                        bool isVBrace = memberType == typeof(VerticalBrace);
                        bool isHBrace = memberType == typeof(HorizontalBrace);
                        bool isJoist = memberType == typeof(Joist);
                        bool isMisc = memberType == typeof(Miscellaneous) || memberType == typeof(LegacyMiscellaneous);
                        bool needsConnection = isBeam || isColumn || isVBrace || isHBrace;

                        for (int ei = 0; ei < fullMember.Ends.Count; ei++)
                        {
                            var end = fullMember.Ends[ei];
                            string endLabel = (ei == 0) ? "Left" : "Right";
                            var conn = end.ConnectionComponent;
                            var designedSpec = conn.DesignedSpecification;
                            var inputSpec = conn.InputSpecification;

                            bool isForced = end.IsConnectionForced;
                            bool isUserDef = inputSpec is UserDefinedSpecification;
                            string failureMsg = conn.ConnectionFailureMessage ?? "";
                            bool hasFailure = !string.IsNullOrEmpty(failureMsg);

                            string specName = "NONE";
                            if (designedSpec != null)
                            {
                                if (designedSpec is AutoStandardSpecification) specName = "AutoStandard";
                                else if (designedSpec is ShearTabSpecification) specName = "ShearTab";
                                else if (designedSpec is ClipAngleSpecification) specName = "ClipAngle";
                                else if (designedSpec is EndPlateSpecification) specName = "EndPlate";
                                else if (designedSpec is FlushFramedShearSpecification) specName = "Moment(FlushFramed)";
                                else if (designedSpec is FullyWeldedSpecification) specName = "FullyWelded";
                                else if (designedSpec is PlainEndSpecification) specName = "PlainEnd";
                                else if (designedSpec is ColumnAutoBaseCapPlateSpecification) specName = "AutoBaseCapPlate";
                                else if (designedSpec is ColumnUserBaseCapPlateSpecification) specName = "UserBaseCapPlate";
                                else if (designedSpec is BearingSpecification) specName = "Bearing";
                                else if (designedSpec is BentPlateSpecification) specName = "BentPlate";
                                else if (designedSpec is SeatedSpecification) specName = "Seated";
                                else if (designedSpec is SplicePlateSpecification) specName = "SplicePlate";
                                else if (designedSpec is HorzBracePlateSpecification) specName = "HorzBracePlate";
                                else if (designedSpec is VertBracePlateSpecification) specName = "VertBracePlate";
                                else specName = designedSpec.GetType().Name;
                            }

                            connectionDetails.Add(new ConnectionDetail
                            {
                                MemberNumber = member.Number,
                                Piecemark = pcmk,
                                MemberTypeName = mtype,
                                End = endLabel,
                                ConnectionType = specName,
                                IsForced = isForced,
                                IsUserDefined = isUserDef,
                                HasFailure = hasFailure,
                                FailureMessage = failureMsg
                            });

                            // CHECK 9: MISSING CONNECTION
                            if (needsConnection && (designedSpec == null || designedSpec is PlainEndSpecification))
                            {
                                missingConnection++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "MISSING CONNECTION", Sequence = seqName,
                                    Details = $"No connection on {endLabel} end", Handle = handle
                                });
                            }

                            // CHECK 10: FORCED CONNECTION
                            if (isForced)
                            {
                                forcedConnection++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "FORCED CONNECTION", Sequence = seqName,
                                    Details = $"Connection on {endLabel} end is forced (design failed but applied anyway)", Handle = handle
                                });
                            }

                            // CHECK 11: USER CONNECTION
                            if (isUserDef)
                            {
                                userConnection++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "USER CONNECTION", Sequence = seqName,
                                    Details = $"User-defined connection on {endLabel} end", Handle = handle
                                });
                            }

                            // CHECK 12: BASE PLATE / CAP PLATE SCHEDULE
                            if (isColumn && (designedSpec is ColumnAutoBaseCapPlateSpecification || designedSpec is ColumnUserBaseCapPlateSpecification))
                            {
                                baseCapPlateSchedule++;
                                string bpDetail = designedSpec is ColumnUserBaseCapPlateSpecification ? "User-specified" : "Auto-designed";
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "BASE/CAP PLATE", Sequence = seqName,
                                    Details = $"Column has {bpDetail} base/cap plate on {endLabel} end", Handle = handle
                                });
                            }

                            // CHECK 13: EMBEDS
                            if (designedSpec is BearingSpecification)
                            {
                                embedsFound++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "EMBEDS", Sequence = seqName,
                                    Details = $"Bearing connection with embed plates on {endLabel} end", Handle = handle
                                });
                            }

                            // CHECK 15: GRAPHICAL CONNECTION (user-defined where designed != input)
                            if (isUserDef && designedSpec != null && designedSpec.GetType() != inputSpec.GetType())
                            {
                                graphicalConnection++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "GRAPHICAL CONNECTION", Sequence = seqName,
                                    Details = $"Graphical connection on {endLabel} end: requested {inputSpec.GetType().Name}, system applied {specName}", Handle = handle
                                });
                            }

                            // CHECK 16: MOMENT CONNECTION
                            if (designedSpec is FlushFramedShearSpecification || designedSpec is EndPlateSpecification)
                            {
                                momentConnection++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "MOMENT CONNECTION", Sequence = seqName,
                                    Details = $"Moment connection ({specName}) on {endLabel} end", Handle = handle
                                });
                            }

                            // CHECK 17: SHEAR TAB CONNECTION
                            if (designedSpec is ShearTabSpecification)
                            {
                                shearTabConnection++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "SHEAR TAB CONNECTION", Sequence = seqName,
                                    Details = $"Shear tab connection on {endLabel} end", Handle = handle
                                });
                            }

                            // CHECK 18: CLIP ANGLE CONNECTION
                            if (designedSpec is ClipAngleSpecification)
                            {
                                clipAngleConnection++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "CLIP ANGLE CONNECTION", Sequence = seqName,
                                    Details = $"Clip angle connection on {endLabel} end", Handle = handle
                                });
                            }

                            // CHECK 19: END PLATE CONNECTION
                            if (designedSpec is EndPlateSpecification)
                            {
                                endPlateConnection++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "END PLATE CONNECTION", Sequence = seqName,
                                    Details = $"End plate connection on {endLabel} end", Handle = handle
                                });
                            }

                            // Load checks per end
                            bool autoShear = end.IsAutoShearLoad;
                            bool autoMoment = end.IsAutoMomentLoad;
                            double shear = end.ShearLoad;
                            double moment = end.MomentLoad;
                            double tension = 0;
                            bool autoTension = true;

                            if (isVBrace)
                            {
                                var vbEnd = end as VerticalBraceEnd;
                                if (vbEnd != null) { tension = end.TensionLoad; autoTension = !vbEnd.IsAutoTensionLoad; }
                            }
                            else
                            {
                                tension = end.TensionLoad;
                                autoTension = true;
                            }

                            string loadSource = (autoShear && autoMoment && autoTension) ? "Auto" : "User";

                            loadDetails.Add(new LoadDetail
                            {
                                MemberNumber = member.Number, Piecemark = pcmk,
                                MemberTypeName = mtype, End = endLabel,
                                ShearLoad = shear, IsAutoShear = autoShear,
                                MomentLoad = moment, IsAutoMoment = autoMoment,
                                TensionLoad = tension, IsAutoTension = autoTension,
                                LoadSource = loadSource
                            });

                            // CHECK 20: VERTICAL BRACE USER ENTERED LOAD
                            if (isVBrace)
                            {
                                var vbEnd = end as VerticalBraceEnd;
                                bool hasUserLoad = !autoShear || !autoMoment;
                                if (vbEnd != null && !vbEnd.IsAutoTensionLoad) hasUserLoad = true;
                                if (hasUserLoad)
                                {
                                    string ldParts = "";
                                    if (!autoShear) ldParts += $"Shear={shear:F1} ";
                                    if (!autoMoment) ldParts += $"Moment={moment:F1} ";
                                    if (vbEnd != null && !vbEnd.IsAutoTensionLoad) ldParts += $"Tension={tension:F1} ";
                                    vbraceUserLoad++;
                                    issues.Add(new Issue
                                    {
                                        MemberNumber = member.Number, Piecemark = pcmk,
                                        IssueType = "VBRACE USER LOAD", Sequence = seqName,
                                        Details = $"Vertical brace {endLabel} end has user-entered load(s): {ldParts.Trim()}", Handle = handle
                                    });
                                }
                            }

                            // CHECK 21: BEAM USER ENTERED LOAD
                            if (isBeam)
                            {
                                bool hasUserLoad = !autoShear || !autoMoment || !end.IsAutoTieForce;
                                if (hasUserLoad)
                                {
                                    string ldParts = "";
                                    if (!autoShear) ldParts += $"Shear={shear:F1} ";
                                    if (!autoMoment) ldParts += $"Moment={moment:F1} ";
                                    if (!end.IsAutoTieForce) ldParts += $"TieForce ";
                                    beamUserLoad++;
                                    issues.Add(new Issue
                                    {
                                        MemberNumber = member.Number, Piecemark = pcmk,
                                        IssueType = "BEAM USER LOAD", Sequence = seqName,
                                        Details = $"Beam {endLabel} end has user-entered load(s): {ldParts.Trim()}", Handle = handle
                                    });
                                }
                            }
                        }

                        // CHECK 14: FORCED USER PIECE MARKS
                        if (!SystemMarkPattern.IsMatch(pcmk) && !member.IsMarkedForProcess && member.ModelCompleteDate != null)
                        {
                            bool looksLikeAutoName = pcmk.Length <= 4 && char.IsLetter(pcmk[0]) && pcmk.Skip(1).All(char.IsDigit);
                            if (!looksLikeAutoName)
                            {
                                forcedUserPiecemark++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number, Piecemark = pcmk,
                                    IssueType = "FORCED USER PIECEMARK", Sequence = seqName,
                                    Details = $"Piecemark '{pcmk}' appears to be a manually assigned user piecemark", Handle = handle
                                });
                            }
                        }
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"  Warning: Bolt/hole check skipped for member {member.Number}: {ex.Message}");
                    }
                }
            }

            // Console summary
            Console.WriteLine($"  Total members checked:       {totalChecked}");
            Console.WriteLine($"  Need processing:             {notProcessedCount}");
            Console.WriteLine($"  Not marked Model Complete:   {notModelComplete}");
            Console.WriteLine($"  Missing shape assignment:    {noShapeAssigned}");
            Console.WriteLine($"  Missing field bolts:         {missingFieldBolts}");
            Console.WriteLine($"  Missing shop bolts:          {missingShopBolts}");
            Console.WriteLine($"  Mismatched holes:            {mismatchedHoles}");
            Console.WriteLine($"  Missing holes on main mat:   {missingHoles}");
            Console.WriteLine($"  Galvanized mismatch:         {galvMismatch}");
            Console.WriteLine($"  Missing connections:         {missingConnection}");
            Console.WriteLine($"  Forced connections:          {forcedConnection}");
            Console.WriteLine($"  User-defined connections:    {userConnection}");
            Console.WriteLine($"  Base/cap plate schedule:     {baseCapPlateSchedule}");
            Console.WriteLine($"  Embeds found:                {embedsFound}");
            Console.WriteLine($"  Forced user piecemarks:      {forcedUserPiecemark}");
            Console.WriteLine($"  Graphical connections:       {graphicalConnection}");
            Console.WriteLine($"  Moment connections:          {momentConnection}");
            Console.WriteLine($"  Shear tab connections:       {shearTabConnection}");
            Console.WriteLine($"  Clip angle connections:      {clipAngleConnection}");
            Console.WriteLine($"  End plate connections:       {endPlateConnection}");
            Console.WriteLine($"  VBrace user-entered loads:   {vbraceUserLoad}");
            Console.WriteLine($"  Beam user-entered loads:     {beamUserLoad}");

            // Generate Excel
            userMarks.Sort();
            systemMarks.Sort();

            string timestamp = DateTime.Now.ToString("yyyy-MM-dd_HHmmss");
            string fileName = $"Checker1_{jobName}_{timestamp}.xlsx";
            string outputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, fileName);

            using (var package = new ExcelPackage())
            {
                // ====== SHEET 1: Summary ======
                var wsSummary = package.Workbook.Worksheets.Add("Summary");
                StyleHeader(wsSummary, "A1:B1", "Pre-Detailing Model Verification");

                wsSummary.Cells["A3"].Value = "Job Name";
                wsSummary.Cells["B3"].Value = jobName;
                wsSummary.Cells["A4"].Value = "Run Date";
                wsSummary.Cells["B4"].Value = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
                wsSummary.Cells["A5"].Value = "Sequences Checked";
                wsSummary.Cells["B5"].Value = string.Join(", ", targetSequences);

                wsSummary.Cells["A7"].Value = "Check";
                wsSummary.Cells["B7"].Value = "Count";
                wsSummary.Cells["C7"].Value = "Status";
                StyleTableHeader(wsSummary, "A7:C7");

                int r = 8;
                AddSummaryRow(wsSummary, r++, "Total Members Checked", totalChecked, "");
                AddSummaryRow(wsSummary, r++, "Need Processing", notProcessedCount,
                    notProcessedCount == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Not Model Complete", notModelComplete,
                    notModelComplete == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Missing Shape", noShapeAssigned,
                    noShapeAssigned == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Missing Field Bolts", missingFieldBolts,
                    missingFieldBolts == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Missing Shop Bolts", missingShopBolts,
                    missingShopBolts == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Mismatched Holes", mismatchedHoles,
                    mismatchedHoles == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Missing Holes (Main Mat)", missingHoles,
                    missingHoles == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Galvanized Mismatch", galvMismatch,
                    galvMismatch == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Missing Connections", missingConnection,
                    missingConnection == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Forced Connections", forcedConnection,
                    forcedConnection == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "User-Defined Connections", userConnection,
                    userConnection == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Base/Cap Plate Schedule", baseCapPlateSchedule, "");
                AddSummaryRow(wsSummary, r++, "Embeds Found", embedsFound, "");
                AddSummaryRow(wsSummary, r++, "Forced User Piecemarks", forcedUserPiecemark,
                    forcedUserPiecemark == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Graphical Connections", graphicalConnection, "");
                AddSummaryRow(wsSummary, r++, "Moment Connections", momentConnection, "");
                AddSummaryRow(wsSummary, r++, "Shear Tab Connections", shearTabConnection, "");
                AddSummaryRow(wsSummary, r++, "Clip Angle Connections", clipAngleConnection, "");
                AddSummaryRow(wsSummary, r++, "End Plate Connections", endPlateConnection, "");
                AddSummaryRow(wsSummary, r++, "VBrace User Loads", vbraceUserLoad,
                    vbraceUserLoad == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Beam User Loads", beamUserLoad,
                    beamUserLoad == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Unique User Marks", userMarks.Count, "");
                AddSummaryRow(wsSummary, r++, "Unique System Marks", systemMarks.Count, "");

                wsSummary.Column(1).Width = 28;
                wsSummary.Column(2).Width = 40;
                wsSummary.Column(3).Width = 12;

                // ====== SHEET 2: Issues ======
                var wsIssues = package.Workbook.Worksheets.Add("Issues");
                StyleHeader(wsIssues, "A1:F1", $"Issues Found: {issues.Count}");

                wsIssues.Cells["A3"].Value = "Resolved";
                wsIssues.Cells["B3"].Value = "Member #";
                wsIssues.Cells["C3"].Value = "Piecemark";
                wsIssues.Cells["D3"].Value = "Issue Type";
                wsIssues.Cells["E3"].Value = "Sequence";
                wsIssues.Cells["F3"].Value = "Details";
                StyleTableHeader(wsIssues, "A3:F3");

                for (int i = 0; i < issues.Count; i++)
                {
                    int row = i + 4;
                    wsIssues.Cells[row, 1].Value = false;
                    wsIssues.Cells[row, 2].Value = issues[i].MemberNumber;
                    wsIssues.Cells[row, 3].Value = issues[i].Piecemark;
                    wsIssues.Cells[row, 4].Value = issues[i].IssueType;
                    wsIssues.Cells[row, 5].Value = issues[i].Sequence;
                    wsIssues.Cells[row, 6].Value = issues[i].Details;

                    var validation = wsIssues.DataValidations.AddListValidation(
                        wsIssues.Cells[row, 1].Address);
                    validation.Formula.Values.Add("TRUE");
                    validation.Formula.Values.Add("FALSE");
                    validation.ShowErrorMessage = true;
                    validation.ErrorTitle = "Invalid";
                    validation.Error = "Select TRUE or FALSE";

                    if (i % 2 == 1)
                    {
                        wsIssues.Cells[row, 1, row, 6].Style.Fill.PatternType = ExcelFillStyle.Solid;
                        wsIssues.Cells[row, 1, row, 6].Style.Fill.BackgroundColor.SetColor(
                            Color.FromArgb(242, 242, 242));
                    }
                }

                if (issues.Count > 0)
                {
                    int lastRow = issues.Count + 3;
                    var cfRange = wsIssues.Cells[4, 1, lastRow, 6];
                    var cf = wsIssues.ConditionalFormatting.AddExpression(cfRange);
                    cf.Formula = "$A4=TRUE";
                    cf.Style.Font.Strike = true;
                    cf.Style.Font.Color.Color = Color.Gray;
                }

                wsIssues.Column(1).Width = 12;
                wsIssues.Column(2).Width = 12;
                wsIssues.Column(3).Width = 16;
                wsIssues.Column(4).Width = 24;
                wsIssues.Column(5).Width = 12;
                wsIssues.Column(6).Width = 60;

                // ====== SHEET 3: Master Report ======
                var wsMaster = package.Workbook.Worksheets.Add("Master Report");
                StyleHeader(wsMaster, "A1:D1", "Piecemark Master Report");

                wsMaster.Cells["A3"].Value = "User Marks";
                wsMaster.Cells["C3"].Value = "System Marks";
                StyleTableHeader(wsMaster, "A3:A3");
                StyleTableHeader(wsMaster, "C3:C3");

                for (int i = 0; i < Math.Max(userMarks.Count, systemMarks.Count); i++)
                {
                    int row = i + 4;
                    if (i < userMarks.Count)
                        wsMaster.Cells[row, 1].Value = userMarks[i];
                    if (i < systemMarks.Count)
                        wsMaster.Cells[row, 3].Value = systemMarks[i];
                }

                wsMaster.Cells[3, 2].Value = $"({userMarks.Count})";
                wsMaster.Cells[3, 4].Value = $"({systemMarks.Count})";

                wsMaster.Column(1).Width = 20;
                wsMaster.Column(2).Width = 8;
                wsMaster.Column(3).Width = 20;
                wsMaster.Column(4).Width = 8;

                // ====== SHEET 4: Bolt/Hole Detail ======
                var wsBoltHole = package.Workbook.Worksheets.Add("Bolt/Hole Detail");
                StyleHeader(wsBoltHole, "A1:I1", "Per-Member Bolt & Hole Summary");

                wsBoltHole.Cells["A3"].Value = "Member #";
                wsBoltHole.Cells["B3"].Value = "Piecemark";
                wsBoltHole.Cells["C3"].Value = "Materials";
                wsBoltHole.Cells["D3"].Value = "Total Holes";
                wsBoltHole.Cells["E3"].Value = "Matchable Holes";
                wsBoltHole.Cells["F3"].Value = "Field Bolts";
                wsBoltHole.Cells["G3"].Value = "Shop Bolts";
                wsBoltHole.Cells["H3"].Value = "Galvanized";
                wsBoltHole.Cells["I3"].Value = "Bolt Finishes";
                StyleTableHeader(wsBoltHole, "A3:I3");

                for (int i = 0; i < boltHoleDetails.Count; i++)
                {
                    int row = i + 4;
                    var d = boltHoleDetails[i];
                    wsBoltHole.Cells[row, 1].Value = d.MemberNumber;
                    wsBoltHole.Cells[row, 2].Value = d.Piecemark;
                    wsBoltHole.Cells[row, 3].Value = d.MaterialCount;
                    wsBoltHole.Cells[row, 4].Value = d.TotalHoles;
                    wsBoltHole.Cells[row, 5].Value = d.MatchableHoles;
                    wsBoltHole.Cells[row, 6].Value = d.FieldBolts;
                    wsBoltHole.Cells[row, 7].Value = d.ShopBolts;
                    wsBoltHole.Cells[row, 8].Value = d.MemberIsGalvanized ? "Yes" : "No";
                    wsBoltHole.Cells[row, 9].Value = d.BoltFinishes;

                    if (i % 2 == 1)
                    {
                        wsBoltHole.Cells[row, 1, row, 9].Style.Fill.PatternType = ExcelFillStyle.Solid;
                        wsBoltHole.Cells[row, 1, row, 9].Style.Fill.BackgroundColor.SetColor(
                            Color.FromArgb(242, 242, 242));
                    }
                }

                wsBoltHole.Column(1).Width = 12;
                wsBoltHole.Column(2).Width = 16;
                wsBoltHole.Column(3).Width = 12;
                wsBoltHole.Column(4).Width = 14;
                wsBoltHole.Column(5).Width = 18;
                wsBoltHole.Column(6).Width = 14;
                wsBoltHole.Column(7).Width = 14;
                wsBoltHole.Column(8).Width = 14;
                wsBoltHole.Column(9).Width = 30;

                // ====== SHEET 5: Connection Detail ======
                var wsConn = package.Workbook.Worksheets.Add("Connection Detail");
                StyleHeader(wsConn, "A1:I1", "Per-End Connection Summary");

                wsConn.Cells["A3"].Value = "Member #";
                wsConn.Cells["B3"].Value = "Piecemark";
                wsConn.Cells["C3"].Value = "Type";
                wsConn.Cells["D3"].Value = "End";
                wsConn.Cells["E3"].Value = "Connection";
                wsConn.Cells["F3"].Value = "Forced";
                wsConn.Cells["G3"].Value = "User Defined";
                wsConn.Cells["H3"].Value = "Failed";
                wsConn.Cells["I3"].Value = "Failure Message";
                StyleTableHeader(wsConn, "A3:I3");

                for (int i = 0; i < connectionDetails.Count; i++)
                {
                    int row = i + 4;
                    var d = connectionDetails[i];
                    wsConn.Cells[row, 1].Value = d.MemberNumber;
                    wsConn.Cells[row, 2].Value = d.Piecemark;
                    wsConn.Cells[row, 3].Value = d.MemberTypeName;
                    wsConn.Cells[row, 4].Value = d.End;
                    wsConn.Cells[row, 5].Value = d.ConnectionType;
                    wsConn.Cells[row, 6].Value = d.IsForced ? "Yes" : "No";
                    wsConn.Cells[row, 7].Value = d.IsUserDefined ? "Yes" : "No";
                    wsConn.Cells[row, 8].Value = d.HasFailure ? "Yes" : "No";
                    wsConn.Cells[row, 9].Value = d.FailureMessage;

                    if (d.IsForced) wsConn.Cells[row, 6].Style.Font.Color.SetColor(Color.FromArgb(231, 76, 60));
                    if (d.HasFailure) wsConn.Cells[row, 8].Style.Font.Color.SetColor(Color.FromArgb(231, 76, 60));

                    if (i % 2 == 1)
                    {
                        wsConn.Cells[row, 1, row, 9].Style.Fill.PatternType = ExcelFillStyle.Solid;
                        wsConn.Cells[row, 1, row, 9].Style.Fill.BackgroundColor.SetColor(
                            Color.FromArgb(242, 242, 242));
                    }
                }

                wsConn.Column(1).Width = 12;
                wsConn.Column(2).Width = 16;
                wsConn.Column(3).Width = 16;
                wsConn.Column(4).Width = 8;
                wsConn.Column(5).Width = 20;
                wsConn.Column(6).Width = 10;
                wsConn.Column(7).Width = 14;
                wsConn.Column(8).Width = 10;
                wsConn.Column(9).Width = 50;

                // ====== SHEET 6: Load Detail ======
                var wsLoad = package.Workbook.Worksheets.Add("Load Detail");
                StyleHeader(wsLoad, "A1:J1", "Per-End Load Summary");

                wsLoad.Cells["A3"].Value = "Member #";
                wsLoad.Cells["B3"].Value = "Piecemark";
                wsLoad.Cells["C3"].Value = "Type";
                wsLoad.Cells["D3"].Value = "End";
                wsLoad.Cells["E3"].Value = "Shear (kips)";
                wsLoad.Cells["F3"].Value = "Auto Shear";
                wsLoad.Cells["G3"].Value = "Moment (k-in)";
                wsLoad.Cells["H3"].Value = "Auto Moment";
                wsLoad.Cells["I3"].Value = "Tension (kips)";
                wsLoad.Cells["J3"].Value = "Source";
                StyleTableHeader(wsLoad, "A3:J3");

                for (int i = 0; i < loadDetails.Count; i++)
                {
                    int row = i + 4;
                    var d = loadDetails[i];
                    wsLoad.Cells[row, 1].Value = d.MemberNumber;
                    wsLoad.Cells[row, 2].Value = d.Piecemark;
                    wsLoad.Cells[row, 3].Value = d.MemberTypeName;
                    wsLoad.Cells[row, 4].Value = d.End;
                    wsLoad.Cells[row, 5].Value = d.ShearLoad;
                    wsLoad.Cells[row, 6].Value = d.IsAutoShear ? "Auto" : "USER";
                    wsLoad.Cells[row, 7].Value = d.MomentLoad;
                    wsLoad.Cells[row, 8].Value = d.IsAutoMoment ? "Auto" : "USER";
                    wsLoad.Cells[row, 9].Value = d.TensionLoad;
                    wsLoad.Cells[row, 10].Value = d.LoadSource;

                    if (!d.IsAutoShear) wsLoad.Cells[row, 6].Style.Font.Color.SetColor(Color.FromArgb(231, 76, 60));
                    if (!d.IsAutoMoment) wsLoad.Cells[row, 8].Style.Font.Color.SetColor(Color.FromArgb(231, 76, 60));

                    if (i % 2 == 1)
                    {
                        wsLoad.Cells[row, 1, row, 10].Style.Fill.PatternType = ExcelFillStyle.Solid;
                        wsLoad.Cells[row, 1, row, 10].Style.Fill.BackgroundColor.SetColor(
                            Color.FromArgb(242, 242, 242));
                    }
                }

                wsLoad.Column(1).Width = 12;
                wsLoad.Column(2).Width = 16;
                wsLoad.Column(3).Width = 16;
                wsLoad.Column(4).Width = 8;
                wsLoad.Column(5).Width = 14;
                wsLoad.Column(6).Width = 12;
                wsLoad.Column(7).Width = 14;
                wsLoad.Column(8).Width = 14;
                wsLoad.Column(9).Width = 14;
                wsLoad.Column(10).Width = 10;

                package.SaveAs(new FileInfo(outputPath));
            }

            Console.WriteLine($"\n  Excel report saved to:\n  {outputPath}");
            Console.WriteLine("==========================================================\n");

            return issues;
        }

        public static void ApplyStatusColors(Job job, List<Issue> flaggedIssues)
        {
            var uniqueMembers = flaggedIssues
                .GroupBy(i => i.MemberNumber)
                .Select(g => g.First())
                .ToList();

            int colored = 0;
            int failed = 0;

            Console.WriteLine($"\n  Applying RED color to {uniqueMembers.Count} flagged member(s)...");

            foreach (var issue in uniqueMembers)
            {
                try
                {
                    using (var xaction = new Transaction(job, new ImmediateLockHandler()))
                    {
                        xaction.Add(issue.Handle);
                        xaction.Lock();

                        var member = Member.Get(issue.Handle);
                        var materials = member.GetMaterial();

                        foreach (var mat in materials)
                        {
                            xaction.Add(mat.Handle);
                        }

                        xaction.Lock();

                        foreach (var mat in materials)
                        {
                            mat.Color = new DesignData.SDS2.Primitives.Color(255, 0, 0);
                        }

                        var result = xaction.Commit(processMembers: true);
                        if (result)
                        {
                            colored++;
                            Console.WriteLine($"    Member {issue.MemberNumber} ({issue.Piecemark}) -> RED");
                        }
                        else
                        {
                            failed++;
                            Console.WriteLine($"    Member {issue.MemberNumber} -> FAILED: {result.Reason}");
                        }
                    }
                }
                catch (Exception ex)
                {
                    failed++;
                    Console.WriteLine($"    Member {issue.MemberNumber} -> ERROR: {ex.Message}");
                }
            }

            Console.WriteLine($"\n  Color application complete: {colored} colored, {failed} failed.");
        }

        // --- Styling Helpers ---
        private static void StyleHeader(ExcelWorksheet ws, string range, string title)
        {
            ws.Cells[range].Merge = true;
            ws.Cells[range].Value = title;
            ws.Cells[range].Style.Font.Size = 16;
            ws.Cells[range].Style.Font.Bold = true;
            ws.Cells[range].Style.Font.Color.SetColor(Color.White);
            ws.Cells[range].Style.Fill.PatternType = ExcelFillStyle.Solid;
            ws.Cells[range].Style.Fill.BackgroundColor.SetColor(Color.FromArgb(44, 62, 80));
            ws.Cells[range].Style.HorizontalAlignment = ExcelHorizontalAlignment.Left;
            ws.Row(1).Height = 36;
            ws.Cells[range].Style.VerticalAlignment = ExcelVerticalAlignment.Center;
        }

        private static void StyleTableHeader(ExcelWorksheet ws, string range)
        {
            ws.Cells[range].Style.Font.Bold = true;
            ws.Cells[range].Style.Font.Color.SetColor(Color.White);
            ws.Cells[range].Style.Fill.PatternType = ExcelFillStyle.Solid;
            ws.Cells[range].Style.Fill.BackgroundColor.SetColor(Color.FromArgb(52, 73, 94));
            ws.Cells[range].Style.Border.Bottom.Style = ExcelBorderStyle.Thin;
        }

        private static void AddSummaryRow(ExcelWorksheet ws, int row, string label, int count, string status)
        {
            ws.Cells[row, 1].Value = label;
            ws.Cells[row, 2].Value = count;

            if (!string.IsNullOrEmpty(status))
            {
                ws.Cells[row, 3].Value = status;
                ws.Cells[row, 3].Style.Font.Bold = true;
                if (status == "PASS")
                {
                    ws.Cells[row, 3].Style.Font.Color.SetColor(Color.FromArgb(39, 174, 96));
                }
                else if (status == "FAIL")
                {
                    ws.Cells[row, 3].Style.Font.Color.SetColor(Color.FromArgb(231, 76, 60));
                }
            }
        }
    }
}
