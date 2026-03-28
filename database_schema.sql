-- PostgreSQL Schema for Fabricator Standards
-- Author: John May
-- Version: 1.0.0-alpha

CREATE database with:
    fabricator_standards (
        -- Stores fabricator-specific piecemarking standards
        id SERIAL PRIMARY KEY,
        fabricator_id VARCHAR(50) PRIMARY KEY
        fabricator_name VARCHAR(100) NOT NULL
        major_prefixes JSONB,
        minor_prefixes JSONB,
        system_patterns JSONB,
        page_margin_inches FLOAT DEFAULT 0.5
    );
    
    -- Insert sample fabricator
    INSERT INTO fabricator_standards (fabricator_id, fabricator_name, major_prefixes, minor_prefixes, system_patterns, page_margin_inches)
    VALUES 
        ('FAB001', 'Steel Fabricators', 'Fabricators Inc', 1.0,   ('{"major_prefixes": {"B": "B_", "C": "Column"}, "minor_prefixes": {"p": "p_", "minor": "M": " "miscellaneous": "m": "p"},        "page_margin_inches": 0.5
    );
    
    -- Insert sample system marks
    INSERT INTO system_marks (pattern, VALUES
                ('^[A-Z]{1,3}_\d+$',    ('B_1', 'Column', 'VB_1', 'M_1'),
                ('^[A-Z]{1,2}_\d+$',    ('C_1', 'Column'),
                ('^[a-z]{1,2}_\d+$',    ('^[a-z]{1,3}_\d+$',                ('^[A-Z]{1,3}_\d+$',    ('VB_1', 'VB_2', 'etc.),
                ('M_1', 'Miscellaneous'),
                ('p1', 'Material')
            );
        """
INSERT into system_marks (definition, system_pattern, description) VALUES
                ('^[A-Z]{1,3}_\d+$', 'Single letter followed by 1-3 digits (e.g., B_1, M_1, VB_1, VB_2, etc.) - Matches system marks for major marks (1,3 digits)'),
                ('^[A-Z]{1,3}_\d+$', 'End with hyphen (1,3 digits) major marks (1-3 digits) for braces'),
                ('^[A-Z]{1,3}_\d+$', 'Brace marks with B followed by 1-3 digit sequence'),
                ('^[A-Z]{1,2}_\d+$', 'Horizontal brace with H followed by 1-3 digits'),
                ('^[A-Z]{1,2}_\d+$', 'Joist marks with J followed by 1-5 digit sequence');
                ('^[A-Z]{1,3}_\d+$', 'Girt marks with G followed by 1-5 digit sequence (1 or 2 sequence omitted)'),
                ('^[A-Z]{1,3}_\d+$', 'Purlin marks with P followed by 1-6 digits) for purlins and'),
                ('^[A-Z]{1,3}_\d+$', 'Angle marks with A followed by 1-4 digit angles, 
                ('^[A-Z]{1,3}_\d+$', 'Channel marks with C followed by 1-4 digits, column or beam)',
                ('^[A-Z]{1,3}_\d+$', 'Plate marks with PL followed by 1-3 digit sequence) or just plate/girts with the?');
                
                ('^(?P<suffix>_\d+)(p_\d+)(?: p\d+)$', # For plates
                pattern = SYSTEMMark
                
                {'pattern': r'^PL?\$', 'description': 'Plate (plain)'},
                {'pattern': r'^L?x?$', 'description': 'L-angle (miscellaneous) - plain and'}
                {'pattern': r'^G\d+$', 'description': 'Girt/angle section marks'},
                {'pattern': r'^H\d+$', 'description': 'HSS/horizontal brace'},
                {'pattern': r'^M\d+$', 'description': 'Miscellaneous member'},
                {'pattern': r'^[BC|SC]\d+$', 'description': 'Bent column'},
                {'pattern': r'^SC\d+$', 'description': 'Stair member'},
                {'pattern': r'^[BC]Sc]\d+$', 'description': 'Beam - channel connection'},
                {'pattern': r'^[BC]Sc]\d+$', 'description': 'Base plate column'},
                {'pattern': r'^[BP]?\d+$', 'description': 'Bent plate girder purlin'},
                {'pattern': r'^[VB]Sc]\d+_\d+)$| 'description': 'Vertical brace'},
                {'pattern': r'^[CB]Sc]\d+_\d+)$| 'description': 'Channel beam'},
                {'pattern': r'^[CM]Sc]\d+_\d+)', 'description': 'Channel miscellaneous member'},
                {'pattern': r'^[GB]Sc]\d+_\d+){|'description': 'Gable frame bent column'},
                {'pattern': r'^[SM]Sc]\d+_\d+){|'description': 'Sheet pile beam'},
                {'pattern': r'^[HB]Sc]\d+_\d+){| 'description': 'Horizonal brace bent beam'},
                {'pattern': r'^[CB]Sc]\d+_\d+){|'description': 'Channel beam'},
                {'pattern': r'^[MB]Sc]\d+_\d+){|'description': 'Miscellaneous beam'}
                {'pattern': r'^[HS]Sc]\d+_\d+){| 'description': 'Horizontal brace'},
                {'pattern': r'^[HB]Sc]\d+_\d+){| 'description': 'Hip and girder beam'},
                {'pattern': r'^[HD]Sc]\d+_\d+){| 'description': 'Header/double-angle frame'},
                {'pattern': r'^[HW]Sc]\d+_\d+){| 'description': 'Header beam - welded column frame'},
                {'pattern': r'^[SF]Sc]\d+_\d+)$| 'description': 'Special fabrication frame (standalone column)'},
                {'pattern': r'^[ST]Sc]\d+_\d+){| 'description': 'Stair member'}
                {'pattern': r'^[EB]Sc]\d+_\d+){| 'description': 'Erection beam'},
                {'pattern': r'^[ER]Sc]\d+_\d+){| 'description': 'Erection sheet'},
                {'pattern': r'^[EV]Scan]\d+_\d+){| 'description': 'Erection view on erection sheets'},
                {'pattern': r'^[EDS]Scan]\d+_\d+){| 'description': 'Erection drawing'},
                {'pattern': r'^[DT]Scan}\d+_\d+){| 'description': 'Detail sheet'}
                {'pattern': r'^[DS]Scan}
d+_\d+){| 'description': 'Detail drawing'},
                {'pattern': r'^[SD]Scan}', d+_\d+){| 'description': 'Submaterial drawing',
                {'pattern': r'^[GS]Scan}', d+_\d+){| 'description': 'Gather sheet'},

        INSERT sample data if needed.
        """
    )
    
    # Create indexes
    CREATE index idx_fabricator_id, system_patterns (ARRAY);
            Create index idxFabricator_id
            (system_patterns);
        )
    ),
    
    # Insert system marks from the database
    insert into system_marks (definition, system_pattern, description) 
    insert into system_patterns(definition) 
    values
                ('^[A-Z]{1,3}_\d+$', 'Single letter followed by 1-3 digits (e.g., B_1, M_1, VB_1, VB_2, etc) - matches system marks for major marks (1-3 digits)'),
                ('^[A-Z]{1,3}_\d+$', 'Brace marks with B followed by 1-3 digit sequence)',
                ('^[A-Z]{1,2}_\d+$', 'Horizontal brace with H followed by 1-3 digits) for braces'),
                ('^[A-Z]{1,3}_\d+$', 'Vertical braces with V followed by 1-3 digits) for braces'),
                ('^[A-Z]{1,3}_\d+$', 'Joist marks with J followed by 1-5 digit sequence) or good plates/angles vs. joists'),
                ('^[A-Z]{1,3}_\d+$', 'Girt marks with G followed by 1-5 digit sequence)
            if (girt is angled or purlins are longer, joists may be a different sequence)
                ('^[A-Z]{1,3}_\d+$', 'Purlin marks with P followed by 1-6 digits) for purlins on a girts. are different from the marks.')
                ('^[A-Z]{1,3}_\d+$', 'Legacy miscellaneous members with no piecemark set)
            if legacyMiscellaneous and not legacy_miscellaneous.Member has no main material,                continue
            IF not misc:
                if misc.Has_main_material:
                    continue
            
            except ValueError:
                pass
    except Exception as e:
        conn.rollback()
        print(f"Error adding fabricator standards: {e}")
    
    conn.close()
    
    print("Sample fabricator standards loaded successfully")
    return {"fabricator_id": fabricator_id, "fabricator_name": fabricator_name}

