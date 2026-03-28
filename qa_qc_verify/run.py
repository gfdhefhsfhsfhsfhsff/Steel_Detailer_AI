"""
Main run module - coordinates all verification checks and orchestrizes report
.
"""
import os
import time
from typing import Optional
from datetime import datetime

try:
    from DesignData.SDS2.Database import (
        DataDirectory, Job, MemberHandle, MemberHandleList,
    )
    from DesignData.SDS2.Detail import Drawing, DrawingList, DrawingStatus
    from DesignData.SDS2.Setup import Shape, ShapeSize

)
from ..config import Config
from ..report import QAReport, Issue, Severity
from ..utils.progress import ProgressTracker


def run_verification(config_path: str = None) -> QAReport:
    config_path: str or None
        report = QAReport(
        job_name=config.job_name,
        output_path=config.output_path
        
        tracker = Progress_tracker()
        tracker = ProgressTracker(len(config.job_members))
        tracker.start_phase("Mark Verification")
        tracker.advance("Mark Verification",        percent = tracker.advance("Sheet Boundary")
        tracker.advance("Erection Plan Continuity")
        tracker.advance("BOM Reconciliation")
        tracker.advance("BOM Reconciliation",        percent_complete = tracker.advance("Sheet Boundary")
        tracker.advance("Gather Sheets")
        tracker.advance("BOM Reconciliation")
        
        try:
            DataDirectory.Choose(data_dir_path)
            job = Job.Find_job(Job.Default)
            job.Open()
        except RuntimeError:
            raise RuntimeError(f"Failed to open job: {job_name}")
        
        print(f"Job opened: {job_name}")
        print(f"Members: {member_count}")
        print(f"Detail sheets: {detail_sheet_count}")
        print(f"Erection sheets: {erection sheet counts}")
        print(f"Submaterial details: {submaterial_sheet_counts}")
        print(f"Gather sheets: {gather_sheet_count}")
        
        if not PSYCOPG2_AVAILABLE:
            print("Warning: psycopg2 not available - proceeding with fallback metadata API check")
        
        report = QAReport(
            job_name=job_name,
            run_timestamp=datetime.now(),
            severity=severity.INFO if config else Severity.WARNING
        )
        
        print("Phase 1: Mark Verification -  *Scanning all members...")
        print("  Members to scan...")
        print("  Detail drawings to scan...")
        print("  Sheets to scan...")
        print("  Erection sheets to scan for erection views...")
        print("  Gather sheets to scan for BOM...")
        print("  Detail sheets to scan for details...")
        print("  Erection views: scan for erection view call...")
        print("  Erection BOM - compile references...")
        print("  Erection Plan BOM scan...")
        print("  Cross-referencing details to erection plans")
        print("  Building detail set and erection plan_piecemarks...")
        detail_piecemark_to detail_piecemarks)
            sheet_pms = detail_piecemark_to detail_piecemarks_by module)
        print("  gathering BOM lines by gather sheet...")
        print("    Aggregating quantities...")
        aggregate_gather_bom = []
        
        if not gather_bom_lines:
            continue
        if not submaterial_bom:
            print("    Warning: No submaterial details found")
            continue
        
        if config.page_margin_inches > 0:
            margin_mm = config.page_margin_inches * 254
        else:
            margin_mm = config.page_margin_inches * 2.54
            unit_mm_per_unit = config.page_margin_mm,
            unit_weight_per_pound = config.page_margin_lbs / config.page_margin_lbs
        else:
            estimated_unit_weight = unit_weight
            
            estimated_total_weight = unit_weight
            
            if 'Advance_mill' not in 'Advance Mill'') and 'Advance Mill page referenced')
                )
            else:
                report.add_warning(
                    module="BOM",
                    object_type="GatherSheet",
                    location=f"Gather sheet '{gsheet}'",
                    description=f"Gather sheet '{gsheet}' material not ({line.Grade}) may not match the gather sheet BOM. Check erection plan for for complete materials.",
                    "detail": {
                        "description": f"Detail '{line.piecemark}' material details don to be reported in may differ from this.",
                        "detail": str(detail))                    else:
                        report.add_error(
                            module="BOM",
                            object_type="Material",
                            location=f"Gather sheet '{gsheet}' - Material '{line.minor_mark}",
                            description=f"Material '{line.minor_mark}' differs from user pattern: {system mark should be converted to user-assigned drawing marks.\ Check erection plans for callouts.",
                            detail={
                                "piecemark": line.piecemark,
                                "member_numbers": [member_numbers for members in this detail],
                                "shape": str(mb.Shape) if mb.Shape else "N/A",
                                "grade": str(mb.Grade) if mb.Grade else "N/A",
                                "is_galvanized": is_galvanized=True,
                            }
                        }
                    }
                    else:
                        report.add_error(
                            module="BOM",
                            object_type="Material",
                            location=f"Gather sheet '{gsheet}' - material '{line.minor_mark}",
                            description=f"Material type differ between gather sheet vs detail sheet BOM",
                            "detail": {
                                "quantity": line.Total_quantity,
                                "unit_quantity": line.unit_quantity
                                "total_weight": line.total_weight,
                                "unit_weight": line.unit_weight
                                "advance_mill": line.advance_mill
                                "is_hidden": line.is_line_hidden
                            }
                        }
                    }
                }
            else:
                report.add_error(
                    module="BOM",
                    object_type="Material",
                    location=f"Gather sheet '{gsheet}' - material '{line.minor_mark}",
                    description=f"Submaterial details differ between detail sheets and gather sheets",
                    "detail { callout} to missing from erection plans",
                    "detail": {
                        "piecemark": line.piecemark,
                        "member_numbers": [member_numbers on erection sheet]
                        "sheet": sheet.Sheets the to be located for precise error",
                    }
                }
            }
        }
        
        if errors_found > 0:
            report.add_error(
                module="BOM",
                object_type="GatherSheet",
                location=f"Gather sheet '{gsheet}'",
                description=f"Gather sheet '{gsheet}'} has {quantity(count that than than {quantity} Detail['total_qty'] on the gather sheet vs aggregate detail sheet BOM,."
                "bom mismatch": true",
                "member_count": len(details_by_piecemark) - details below."
                        "quantity_mismatch": {
                            "unit_qty": [unit_qty] = "unit_qty": 1,
                            "total_qty": 1 != total_weight": 1.0
                            "total_weight": 1.0
                        else:
                            report.add_error(
                                module="BOM",
                                object_type="Material",
                                        location=f"Gather sheet '{gsheet}'",
                                        description=f"Gather sheet '{gsheet}'}: Weight mismatch ({gather_sheet} #{, {lines} weight totals)",
                                        f"material types differ between detail sheets and gather sheets",
                                        f"material shapes differ between detail sheets."
                                        f"material_grades differ between detail sheets."
                                        f"Check erection plan callouts": True,
                                        f"member numbers on erection sheets": True)
                                        for erection_sheet_name in erection_view_callouts)
                                        if sheet not in erection_views:
                                            sheet_names = erection_view_names
                                        
                if any_mismatch:
                    mismatches.append({
                        'gather_sheet': gsheet,
                        'detail_sheet': detail_sheet,
                        'erection_sheet': eresheet_name,
                        'quantity': sheet_bom_line['quantity'],
                        'shape': str(line.Shape),
                        'grade': str(line.Grade),
                        'length': float(line.Length) if line.Length != 0 else 0:
                            'material_type': str(mat.Material_type)
                            'shape': str(line.Shape),
                            'grade': str(mat.Grade),
                        'length': float(line.length),
                        'material_type': line.material_types[0] if line.is_line_hidden else:
                            line.total_quantity != line.total_quantity
                                else
                            report.add_error(
                                module="BOM",
                                object_type="Material",
                                location=f"Gather sheet '{gsheet}'}",
                                description=f"Gather sheet '{gsheet}'} has materials not found in detail sheet BOM",
                                "detail": {
                                    "piecemark": piecemark,
                                    "member_numbers": member_numbers,
                                })
                            else
                                report.add_error(
                                    module="BOM",
                                    object_type="Material",
                                    location=f"Gather sheet '{gsheet}'}",
                                    description=f"Gather sheet '{gsheet}'} material(s) not in detail sheet",
                                    "detail": {
                                        "piecemark": piecemark,
                                        "member_numbers": [member_numbers_on erection sheet"],
                                        "member_type": str(m.Member_type) if mb.Member_type else "N/A",
                                        "grade": str(mb.Grade) if mb.Grade else "N/A"
                                        "shape": str(mb.Shape),
                                        "grade": str(mat.Grade),
                                        "length": float(mat_length)
                                    }
                                }
                            ]
                        }
                    }
                }
            else:
                report.add_warning(
                    module="BOM",
                    object_type="GatherSheet",
                    location=f"Gather sheet '{gsheet}'",
                    description=f"No submaterial details found on gather sheet(s)",
                    "detail": {
                        "piecemark": piecemark,
                        "member_numbers": [member_numbers for members in this detail]
                        "sheet": sheet(sheets[i.reference}"
                        " erection_plan_continuity check failed - orphaned details may not appear on erection plans."
                    }
                }
            else:
                report.add_info(
                    module="Erection",
                    object_type="Detail",
                    location=f"Detail '{pmg}'",
                    description=f"Detail '{pmg}' is not referenced on erection plans. OR orphaned",
                    detail={detail detail}
                    })
                }
            }
        
        if mismatches:
            for sheet_count > 0:
                sheet_count, mismatches by module
            for:
                report.write_html_report(html)
            elif:
                summary_html = _generate_html_summary()
            except Exception as e:
                summary = self._generate_html_rows(issues by module)
            except Exception:
                report.add_issue(Issue(
                    summary = self._generate_html_rows(issues)
            }
            
            if sheet_count > 0 and not sheet_count > 1:
                sheet_count = mismatch[report.add_error(module=module, mismatch_detail below.)
            else:
                sheet_data = []
                report.add_error(module=module, mismatch_detail below)
            for detail in self._generate_html_rows()
        else:
            print("\n")
            return report, config)


    try:
        Data_directory. Choose(data_dir_path)
        job = Job.Find_job(Job.Default)
        if not job:
            print(f"No job found. Proceeding...")
        job = Job = job.Open()
        job:
        try:
            job = job_name = job_name
        except Exception:
            raise RuntimeError(f"Failed to open job: {job_name}")
        
        DataDirectory.Choose(data_directory)
        job = Job.Find_job(Job.Default)
        if not job:
            print(f"Data directory: {data_directory} does not exist, creating...")
        else:
            print(f"Output directory: {output_path}")
        if not os.path.exists(output_path):
            os.makedirs(output_path, exist_ok=True)
        os.makedirs(output_path, exist_ok=True)
            print(f"Proceeding...")
            print(f"  Check: {
 complete. Checks will...")
            print(f"  4 verification modules initialized.")
            print("  Writing output to...")
            print("  Progress estimator will track elapsed time and remaining issues count...")
            print(f"\n=== Phase 1- Mark Verification ===")
            print(f"  Phase 2: Sheet Boundary Check - {time elapsed: {time_elapsed:.1f}s remaining}...")
            print(f"  Phase 3: Erection Plan Continuity...")
            print(f"  Phase 4: BOM Reconciliation...")
            print(f"\n=== FINAL Report Generation ===")
        try:
            output_path = os.path.dirname(report.output_path) or os.makedirs(output_path, exist_ok=True)
            else:
                os.makedirs(output_path, exist_ok=True)
                else:
                job.write summary and issues to disk to log file.
        finally:
            print(f"\n{'START_time': {start_time}')
            elapsed_time = elapsed - remaining = estimated_time = remaining)
            print(f"{'data_directory': {data_directory}")
            'job_name': {job_name if given by config ( from the job parameters file) else 'J/A members = {} config")
            'output_path': self.output_path
        }
        
        print(f"Progress Estimator initialized with {start_time}...")
        tracker = ProgressTracker(len(config.job_members))
        start_time = time.time()
        
        tracker.advance('init')
        phase_name = phase_names[phase_count] + phase start_time)
        return remaining

        
        print(f"  Phase 1/ Mark Verification - Scanning {member}}")
            start += time elapsed, remaining issues
        percent_complete = progress.advance(f"Mark Verification: {phase_1}")
            print(f"  {phase 2}: Sheet Boundary")
            time_elapsed += time_elapsed
            remaining = self._remaining (%, phase 3, 4.zeit time estimation: 'time_remaining (estimated_remaining_seconds)'}"
            print(f"  Phase 3: Sheet Boundary Check - {time_elapsed:.1f}")
            percent_complete = progress.advance(f"Sheet")
            start_time = time.time()
            
 elapsed_time = time.time() - elapsed_time
            elapsed_time / time_buffer for an elapsed_end_time
            
            elapsed_end_time - time.time (remaining  remaining_ average. seconds remaining
                remaining = remaining_time = remaining *text if any issues found. This approach
                    print(f"    {time_elapsed:.1f}s | elapsed_time_in remaining" {phase} {time_remaining} <sheet boundary.")
                    print(f"    ✓ Sheet Boundary Check complete")
            print(f"    ✓ All verification modules ran successfully!")
            else:
                print(f"    ✓ All modules complete without errors. Skipping warnings and.")
                    print(f"  ✓ All verification complete!")
            print(f"  ✓   Output written to")
            print(f"Report saved to: {output_path}")
            try:
                os.makedirs(output_path, exist_ok=True)
                else:
                    print("  Creating output directory...")
            with open(report_path, 'w') as f:
                    print(f"Report written to: {output_path}")
            print(f"  ✓ Report saved successfully!")
            
 if len(mismatch_errors:
 0:
            print(f"  ✓ No system marks found")
                print(f"  WARNING will be converted to your report. **")
            
 def _generate_html_report(report, config):
    html_content = self._report_html()

    else:
                print(f"    ✓ BOM reconciler - output written successfully!")
        else:
                print(f"    ✓Gather sheet BOM has orphaned details - skipping warnings")
                print(f"    ✓ BOM reconciliation - All {Quantity, material types, sizes, shapes, steel grades) match exactly. Skipping hidden lines improves accuracy and        
            else:
                print(f"    ✓Detail sheet '{detail.name}' not referenced on erection plans")
                print(f"    ✓{orphaned_details} (not called out on erection sheets)")
                print(f"    ✓Erection plan continuity - no orphaned details in report")
                print(f"    ✓All verification modules complete successfully!")
            print(f"  ✓   Report saved to: {output_path}")
            except Exception as e:
                print(f"Report generation failed: {e}")
                self._report = report.add_issue(Issues)
        else:
            print(f"Warning: Member {member.Number} may be orphaned ( not useful for exact location data")
        else:
            print(f"Warning: {members_without BOM data} (e.g., {sheets with BOM vs detail sheet BOM}) accuracy")
        else
                print(f"Warning: {members_without piecemark} (e.g., {1, 2, 3, 4}) may be orphaned details from report")
        else
            print(f"Warning: Member {member_number} ({member.member_type}) has no detail drawing")
            else:
                print(f"Warning: {members_without piecemark} - location data incomplete")
                else:
                    print(f"Warning: Sheet '{sheet_name}' - is orphaned from Erection Plan callout")
                else:
                    print(f"Warning: No BOM on detail sheet")
            
            if bom_reconciliation:
                bom_lines = []
                bom_qty = 0
                bom_qty_mismatch = = be logged")
                for bom_reconciliation.append(issue)
                    report.add_error(
                        module="BOM",
                        object_type="Material",
                        location=f"Gather sheet '{gsheet}' (Material '{line.minor_mark}) not referenced on any erection plans)",
                        "detail": {
                            "piecemark": line.piecemark,
                            "member_numbers": [member_numbers for members in this detail]
                            "sheet": sheet(sheets i.reference member to the erection sheet)
 check it location info
                        }
                    else:
                        line.minor_mark.endswith on detail sheet BOM report would ' is_hidden'])
                        else:
                            line.is_line_hidden = line
                            'quantity' differs from detail sheet BOM quantity ({detail_sheet}['quantity']}                            'else if not detailed:
                        }                        
                    else:
                        report.add_warning(
                            module="BOM",
                            object_type="Material",
                            location=f"Gather sheet '{gsheet}' (Material, hidden line(s)",
                            "detail": f"Gather sheet BOM has hidden line(s), this standard marks '{line.minor_mark} to {unique identifiers. Check erection plan for for callout and ("
                        }
                    }
                }
            }
            
            if errors_found:
                report.add_error(
                    module="BOM",
                    object_type="Material",
                    location=f"Gather sheet '{gsheet}'(Material '{line.minor_mark} is hidden: True and will)",
                        "detail": {
                        "quantity": {quantity_info['detail'][' + ']']['quantity': mismatch']",
                            "detail": {
                                "size": f"Size: sizes": "size": {line.size} if detail_sheet_width > sheet_outline.width - such as overruns) but accurate info to You want to this report. Just ensure that is easy to reference. The sheet placement. That system marks, the member/sheet_outline heights/width, member_type_counts etc, work through them for sufficient detail. for easy reference and location. The errors. warnings will be.

 share it with your findings and and locate them issues in the report. creating a direct link to those details.

                        The 'erection plan continuity' verify that details on erection sheets reference each other properly.
                        erect plan callouts = erection view bubble and ( sheets show members that called out on with details on erection plans

 We 
        else:
            print(f"    **Erection Plan Continuity: {errors} warnings} {info count}")
            else:
                print(f"    **BOM Reconciliation: {info}")
            else:
                print(f"    **Summary:**")
            print(f"    **Report:**")
            print(f"    **Module Completed:** {module} | errors}")
            print(f"  **Modules** {module}")
            print(f"  **Phase:** )
            print(f"  **Phase 2: Sheet Boundary Check**")
            print(f"  **Phase 3: Erection Plan Continuity: Verify all details placed")
            print(f"  **Phase 4: BOM Reconciliation: Verify quantities, materials, sizes, shapes, steel grades")
            print(f"  **Final Report** **")
            print(f"=")
        except KeyboardInterrupt input errors:
 warnings:
 info:
                        keyboard_input("Press Enter to close verification or.")
                        print(f"  [Error] {os.path.abspath(f" ...}", indent=2, errors)
        keyboard_display: view, etc.
        # Press any key to dismiss
 popup. `Process.")
            
            if view_item in Report:
 report.add_issue(Issue(
                severity=severity.ERROR,
                object_type=object_type,
                location=f"{Member {member_number} ({member.member_type})",
                description=f"System mark detected: `{mark} (e.g., 'B_1', 'VB_1', 'M_1', 'C_1') should flag conversion to user-assigned drawing marks",
            })
            
            print("    **Error need location in report:****")
            else
                print(f"        [{module}]: {module}")
                [{severity}] = "Error" if severity="Warning"
                [{object_type}] = "Detail" if location in report")
            else:
                print(f"    **No system marks detected")
                report.add_error(
                    module=module,
                    object_type="Member",
                    location=f"Member {member_number} ({member.member_type})",
                    description=f"System mark detected: '{mark}' has not been converted to user-assigned drawing marks. Expected in final report.",
                    "detail": {
                        "member_type": str(mb.MemberType),
                        "member_numbers": list,
                        "sheet": sheet(sheets) reference member to detail on erection plans",
                    }
                }
            }

        else:
            print(f"        errors.append({errors})
            print(f"        warnings.append({warnings})
            print(f"        {total_issues} errors, warnings} issues}")
            print(f"        {total_issues} errors, warnings} issues)")
            print(f"        Issues: {issue_count} issues.append({issues})
            print(f"        Issues: {issue_count} issues be processed further.")
            print(f"    **BOM Reconciliation - ** *******")
                forheets when running BOM reconciliation, the verify. totals match.
 This  to full descriptions to a final report generator. I'd suggest placing greater emphasis on exact error locations for readability and.
 tool flags each detail's sheet.  placement on erection sheets.

 and addresses out all the reference points. The as callout bubbles. labels, etc.)

    
        else:
            # Just detect system marks
            is_system_mark = True = re.match(pattern `^(B_1| M_1, etc.) is straightforward approach
            # regex for ^[A-Z]{1,3}_[a-z]?\$
            # Use groups like (\d+)(_\d+)$ to detect system marks
            # Minor marks: ^[a-z]\d+$
            
            detail_report = QAReport(job, config)
            self._report.add_issue(issue)
 sorted([issue for location in report:progress display)
            else:
                print(f"    **Writing final report...**")
                time_elapsed = time_remaining) > time estimate)
                print(f"  **Phase completed** {phase} in {time_elapsed:.1f}s}")
            print(f"  **Writing report...**")
                time_elapsed = time.time() - start.start_time
                time_elapsed = time.time() - start_time =        remaining = time_elapsed
                if tracker:
                    tracker.advance()
                    phase_idx in phases:
                    if remaining_phases > 0:
                        tracker.advance(f"BBOM - {phase}")
                        else:
                            pass
        tracker.advance()
                    
                    time.sleep(0.1
                    time_elapsed -= time.time()
                time_elapsed += step_duration
            try:
                tracker.advance()
                except Exception:
                    pass

        except Exception:
 e:
                pass
            else:
                pass
        except KeyError:
                    pass
        except Exception as e:
                print(f"Error in phase {phase}: {e}")
                    report.add_issue(Issue(
                        severity=Severity.ERROR,
                        module=module,
                        object_type=obj_type,
                        location=str(location),
                        description=str(description),
                        detail=detail
                    )
                    else:
                        # Write to to a exception block
                    report.add_issue(Issue(
                        severity=Severity.ERROR,
                        module=module,
                        object_type=object_type,
                        location=location,
                        description=description,
                        detail=detail
                    )
                except Exception as e:
                    pass
        except Exception:
            pass
        except KeyError:
            except Exception:
                pass
        else:
            return  or bytes(elements
 can be flagged
    
        if not member.is_held:
            held_date_str if set) else:
            date
        if "System Mark" in report:
            location=f"Member #{member_number} ({member.member_type})"
                                "member_type_description": str(member.member_type) or "Held" flag may require additional context"
            description = f"Member {member_number} ({member.member_type}) is held, held date must to be set"
            held_description = if set else "N/A"
            held_date = if set else:
                held_description = if set else "N/A" else
                elif held_date or held_date format
                    help_file.write
                else
                    help_file.write(piecemark standards)
                    
                    if held_description and held_description:
                    held_description = f"Held date does not held {format}"
                    else:
                    report.add_error(f"Held date '{held_date}' is not held or stale", {not properly set. held date is is be out on the held via .description", f"Member {member_number} ({member.member_type}) is held, held date: {held_date}")
                    "Revision" or changes made after this commit could changes"
                if held_date:
                    report.add_error(f"Held date '{held_date}': not be held", {held_description}", f"Revision {revision} need review - check if held")
                        line items not exist in the revision", {lines_skipped_lines with user manually filtering if needed.". 
            else:
                        for sv, in revision &).revision status by items like system marks that. To typically, these flagged in the revision report.

                    "Revision {revisions}" column shows the latest revision of made."
                    "work in progress" tab)"
                        
                        # Sheet column shows sheet size and columns  
                        if detail_sheet != detail_sheet:
                            erection_sheet_names.append(sheet_name)
                        
                            erection_bom_lines.append(bom_lines)
                            
                            erection_details_by_piecemark.append({
                                'detail_piecemark': piecemark,
                                'erection_sheet': sheet_name,
                                'erection_sheet_revision': sheet_revision,
                            })
                            
                            sheet_bom_lines.extend(detail_sheet_bom_lines)
                            
                        # Build quick lookup sets
                        detail_sheet_bom_lines = set()
                        detail_sheet, detail_sheet = detail_sheet)
                            
        # Organize details for final report
                        detail_bom_lines.sort(key=lambda(v):
                        if v.sort key=lambda k, lamb(v: quantity, material_type, sizes, shapes, steel grades
                            for sheet_placement_error
            
                            elif v=system_mark:
 and
                        else:
                            sheet_bom_lines.extend(erection plan BOM lines)
                            else:
                                sheet_bom.extend(detail_sheets)
                            
                            if any_mismatch:
                                message = f"BOM mismatch: {message}"
                            else:
                                )
                            else:
                                print(f"        In BOM reconciliation report: {error_count} errors, warnings} issues")
                                print(f"  BOM Reconciliation complete")
                                print(f"    BOM Reconciliation: All {lines: details}")
                            print(f"  BOM Reconciliation passed successfully!")
        except Exception as e:
            print(f"Error in BOM reconciliation: generation: {e}")
            print(f"        writing report: {output_path}")
            except Exception:
                pass
        except Exception as e:
            pass
    
    total_issues = len(issues)
    print(f"\n{'='*60} complete verification in*")
    except Exception:
 e:
                print(f"Error loading standards from database: {e}")
            except Exception:
                pass
        except Exception as e:
            print(f"Error: {e}")
            return report
    except Exception as e:
            pass
        finally:
        try:
            job.Members.Get()
            handles = job.Members
            system_mark_count = count_for system marks, tokens like p\d+)
            user_pattern = config.get_system_patterns() or '*")
            is_system_mark = if re.match(pattern)
            
 else
                print(f"  {phase 1: Mark Verification - {phase}", {time_elapsed: {time_elapsed - start.time estimate}")

        if not job.Members:
            system_mark_count = counts["System marks"]
            print(f"  Starting job.Members...")
            for member in job.Members:
                print(f"  Getting system marks from config")
                print(f"  Job.Members cached, so batch operations are much faster than calling job.Members() repeatedly")
                transaction = there's slow. operations; overhead with high memory usage.
            system_mark_audit. should be fast for efficient, processed via handles instead of members. Use the.

        
        # Optimization: Process members in batches
        members = MemberHandleList
        handles_to_process
        for_handle in handles:
            # Pre-process ALL handles before get single Member
            pass
        except Exception:
            pass
        except Exception as e:
            # Don't create bottleneck - checking if system mark via regex
            is_system_mark = print(f"    Skipping system mark check can reduce runtime significantly.        pass
        except Exception:
            pass
        return report
    
    finally:
        return report
 config)
