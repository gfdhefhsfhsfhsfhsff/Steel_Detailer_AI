-- PostgreSQL Schema for Fabricator Standards
-- Author: John May
-- Version: 1.0.0-alpha
-- Database: sds2_standards

-- Drop existing tables if they exist (idempotent)
DROP TABLE IF EXISTS system_marks CASCADE;
DROP TABLE IF EXISTS fabricator_standards CASCADE;

--------------------------------------------------------------------------------
-- Table: fabricator_standards
-- Stores fabricator-specific piecemarking standards.
-- Query used by qa_qc_verify/config.py:
--   SELECT fabricator_id, fabricator_name, major_prefixes,
--          minor_prefixes, system_patterns, page_margin_inches
--   FROM fabricator_standards WHERE fabricator_id = %s
--------------------------------------------------------------------------------
CREATE TABLE fabricator_standards (
    id                  SERIAL PRIMARY KEY,
    fabricator_id       VARCHAR(50) UNIQUE NOT NULL,
    fabricator_name     VARCHAR(100) NOT NULL,
    major_prefixes      JSONB DEFAULT '{}',
    minor_prefixes      JSONB DEFAULT '{}',
    system_patterns     JSONB DEFAULT '[]',
    page_margin_inches  FLOAT DEFAULT 0.5
);

--------------------------------------------------------------------------------
-- Table: system_marks
-- Regex patterns for classifying steel member piecemarks by member type.
--------------------------------------------------------------------------------
CREATE TABLE system_marks (
    id              SERIAL PRIMARY KEY,
    pattern         VARCHAR(200) NOT NULL,
    member_type     VARCHAR(50) NOT NULL,
    description     TEXT,
    example_marks   TEXT[]
);

--------------------------------------------------------------------------------
-- Indexes
--------------------------------------------------------------------------------
CREATE INDEX idx_fabricator_standards_fabricator_id ON fabricator_standards (fabricator_id);
CREATE INDEX idx_system_marks_member_type ON system_marks (member_type);

--------------------------------------------------------------------------------
-- Default system mark patterns
-- These patterns classify piecemarks into structural member categories.
-- Aligned with DEFAULT_SYSTEM_PATTERNS in qa_qc_verify/config.py.
--------------------------------------------------------------------------------
INSERT INTO system_marks (pattern, member_type, description, example_marks) VALUES

    -- Major system marks (uppercase prefix + underscore + digits)
    ('^[A-Z]{1,3}_\d+$',       'major_mark',
     'Major piecemark: 1-3 uppercase letters, underscore, 1+ digits. '
     'Covers B_1, M_1, C_1, VB_1, VB_2, etc.',
     ARRAY['B_1', 'VB_1', 'M_1', 'C_1']),

    -- Beams
    ('^B_\d+$',                 'beam',
     'Beam mark: B prefix, underscore, digits.',
     ARRAY['B_1', 'B_2', 'B_10']),

    ('^BM_\d+$',                'beam',
     'Beam miscellaneous mark: BM prefix.',
     ARRAY['BM_1', 'BM_2']),

    -- Columns
    ('^C_\d+$',                 'column',
     'Column mark: C prefix, underscore, digits.',
     ARRAY['C_1', 'C_2', 'C_10']),

    ('^CC_\d+$',                'column',
     'Column connection mark: CC prefix.',
     ARRAY['CC_1', 'CC_2']),

    -- Vertical braces
    ('^VB_\d+$',                'vertical_brace',
     'Vertical brace mark: VB prefix, underscore, digits.',
     ARRAY['VB_1', 'VB_2', 'VB_10']),

    ('^[A-Z]{1,2}VB_\d+$',     'vertical_brace',
     'Extended vertical brace mark: optional zone prefix + VB.',
     ARRAY['VB_1', 'AVB_2']),

    -- Horizontal braces
    ('^H_\d+$',                 'horizontal_brace',
     'Horizontal brace mark: H prefix, underscore, digits.',
     ARRAY['H_1', 'H_2']),

    ('^HB_\d+$',                'horizontal_brace',
     'Horizontal brace mark: HB prefix.',
     ARRAY['HB_1', 'HB_2']),

    ('^[A-Z]{1,2}H_\d+$',      'horizontal_brace',
     'Extended horizontal brace with optional zone prefix.',
     ARRAY['H_1', 'AH_2']),

    -- Joists
    ('^J\d+$',                  'joist',
     'Joist mark: J followed by 1-5 digits.',
     ARRAY['J1', 'J2', 'J15']),

    -- Girts
    ('^G\d+$',                  'girt',
     'Girt mark: G followed by 1-5 digits.',
     ARRAY['G1', 'G2', 'G15']),

    -- Purlins
    ('^P\d+$',                  'purlin',
     'Purlin mark: P followed by 1-6 digits.',
     ARRAY['P1', 'P2', 'P15']),

    -- Plates
    ('^PL\d+$',                 'plate',
     'Plate mark: PL followed by 1-3 digit sequence.',
     ARRAY['PL1', 'PL2', 'PL10']),

    ('^PL?\d+$',                'plate',
     'Plate mark: optional PL followed by digits.',
     ARRAY['P1', 'PL1', 'PL2']),

    -- Angles
    ('^[LA]\d+$',               'angle',
     'Angle mark: L or A followed by 1-4 digits.',
     ARRAY['A1', 'L1', 'A10', 'L15']),

    -- Channels
    ('^CH_\d+$',                'channel',
     'Channel mark: CH prefix.',
     ARRAY['CH_1', 'CH_2']),

    -- Stairs
    ('^ST\d+$',                 'stair',
     'Stair member: ST prefix followed by digits.',
     ARRAY['ST1', 'ST2']),

    ('^SC\d+$',                 'stair',
     'Stair connection: SC prefix.',
     ARRAY['SC1', 'SC2']),

    -- Miscellaneous
    ('^M_\d+$',                 'miscellaneous',
     'Miscellaneous member: M prefix, underscore, digits.',
     ARRAY['M_1', 'M_2', 'M_10']),

    ('^M\d+$',                  'miscellaneous',
     'Miscellaneous member: M followed directly by digits.',
     ARRAY['M1', 'M2']),

    -- HSS members
    ('^HSS\d+$',                'hss',
     'HSS (hollow structural section) member.',
     ARRAY['HSS1', 'HSS2']),

    -- Minor system marks (lowercase prefix + digits)
    ('^[a-z]\d+$',              'minor_mark',
     'Minor piecemark: single lowercase letter + digits.',
     ARRAY['p1', 'm1', 'b1', 'c1']),

    ('^p\d+$',                  'minor_plate',
     'Minor plate mark: lowercase p + digits.',
     ARRAY['p1', 'p2', 'p10']),

    ('^m\d+$',                  'minor_miscellaneous',
     'Minor miscellaneous mark: lowercase m + digits.',
     ARRAY['m1', 'm2', 'm10']),

    ('^b\d+$',                  'minor_beam',
     'Minor beam mark: lowercase b + digits.',
     ARRAY['b1', 'b2', 'b10']),

    ('^c\d+$',                  'minor_column',
     'Minor column mark: lowercase c + digits.',
     ARRAY['c1', 'c2', 'c10']),

    ('^vb\d+$',                 'minor_vertical_brace',
     'Minor vertical brace: lowercase vb + digits.',
     ARRAY['vb1', 'vb2']),

    -- Erection / drawing categories
    ('^ER\d+$',                 'erection_sheet',
     'Erection sheet mark.',
     ARRAY['ER1', 'ER2']),

    ('^DT\d+$',                 'detail_sheet',
     'Detail sheet mark.',
     ARRAY['DT1', 'DT2']),

    ('^DS\d+$',                 'detail_drawing',
     'Detail drawing mark.',
     ARRAY['DS1', 'DS2']),

    ('^SD\d+$',                 'submaterial_drawing',
     'Submaterial drawing mark.',
     ARRAY['SD1', 'SD2']);

--------------------------------------------------------------------------------
-- Default fabricator standard: matches DEFAULT_SYSTEM_PATTERNS in config.py
--------------------------------------------------------------------------------
INSERT INTO fabricator_standards
    (fabricator_id, fabricator_name, major_prefixes, minor_prefixes, system_patterns, page_margin_inches)
VALUES (
    'DEFAULT',
    'Default Fabricator',

    -- major_prefixes: uppercase single-letter or multi-letter prefixes for major marks
    '{"B": "Beam", "C": "Column", "VB": "Vertical Brace", "HB": "Horizontal Brace", '
    || '"J": "Joist", "G": "Girt", "P": "Purlin", "PL": "Plate", '
    || '"A": "Angle", "CH": "Channel", "M": "Miscellaneous", '
    || '"ST": "Stair", "SC": "Stair Connection", "HSS": "HSS"}'::JSONB,

    -- minor_prefixes: lowercase single-letter prefixes for minor marks
    '{"b": "Beam", "c": "Column", "p": "Plate", "m": "Miscellaneous", '
    || '"vb": "Vertical Brace", "g": "Girt"}'::JSONB,

    -- system_patterns: regex patterns matching config.py DEFAULT_SYSTEM_PATTERNS
    '["^[A-Z]{1,3}_\\\\d+$", "^[A-Z]{1,2}M_\\\\d+$", "^[A-Z]{1,2}C_\\\\d+$", '
    || '"^[A-Z]{1,2}VB_\\\\d+$", "^[A-Z]{1,2}V\\\\d+$", "^[A-Z]{1,2}H_\\\\d+$", '
    || '"^[A-Z]{1,2}P\\\\d+$", "^[a-z]\\\\d+$", "^p\\\\d+$", "^m\\\\d+$", '
    || '"^b\\\\d+$", "^c\\\\d+$", "^vb\\\\d+$"]'::JSONB,

    0.5
);

--------------------------------------------------------------------------------
-- Sample fabricator: Steel Fabricators Inc.
--------------------------------------------------------------------------------
INSERT INTO fabricator_standards
    (fabricator_id, fabricator_name, major_prefixes, minor_prefixes, system_patterns, page_margin_inches)
VALUES (
    'FAB001',
    'Steel Fabricators Inc.',

    '{"B": "Beam", "C": "Column", "VB": "Vertical Brace", "HB": "Horizontal Brace", '
    || '"J": "Joist", "G": "Girt", "P": "Purlin", "PL": "Plate", '
    || '"A": "Angle", "CH": "Channel", "M": "Miscellaneous"}'::JSONB,

    '{"p": "Plate", "m": "Miscellaneous", "b": "Beam", "c": "Column", '
    || '"vb": "Vertical Brace"}'::JSONB,

    '["^[A-Z]{1,3}_\\\\d+$", "^[A-Z]{1,2}M_\\\\d+$", "^[A-Z]{1,2}C_\\\\d+$", '
    || '"^[A-Z]{1,2}VB_\\\\d+$", "^[A-Z]{1,2}H_\\\\d+$", '
    || '"^[a-z]\\\\d+$", "^p\\\\d+$", "^m\\\\d+$", "^b\\\\d+$", '
    || '"^c\\\\d+$", "^vb\\\\d+$"]'::JSONB,

    1.0
);
