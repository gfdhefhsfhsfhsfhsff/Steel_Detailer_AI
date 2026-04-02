"""
Configuration management and PostgreSQL standards repository
Version: 1.0.0-alpha
"""

import os
import re
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any

try:
    import psycopg2
    from psycopg2.extras import RealDictCursor

    PSYCOPG2_AVAILABLE = True
except ImportError:
    PSYCOPG2_AVAILABLE = False


@dataclass
class PiecemarkStandard:
    """Fabricator piecemark standard configuration"""

    fabricator_id: str
    fabricator_name: str
    major_prefixes: Dict[str, str] = field(default_factory=dict)
    minor_prefixes: Dict[str, str] = field(default_factory=dict)
    system_patterns: List[str] = field(default_factory=list)
    page_margin_inches: float = 0.5


class Config:
    """Main configuration for the QA/QC verification tool"""

    DEFAULT_SYSTEM_PATTERNS = [
        r"^[A-Z]{1,3}_\d+$",  # B_1, VB_1, M_1, C_1
        r"^[A-Z]{1,2}M_\d+$",  # BM_1, CM_1
        r"^[A-Z]{1,2}C_\d+$",  # BC_1, CC_1
        r"^[A-Z]{1,2}VB_\d+$",  # VB_1
        r"^[A-Z]{1,2}V\d+$",  # V1, V2
        r"^[A-Z]{1,2}H_\d+$",  # H_1
        r"^[A-Z]{1,2}P\d+$",  # P1, P2
        r"^[a-z]\d+$",  # p1, m1, b1
        r"^p\d+$",  # p1, p2
        r"^m\d+$",  # m1, m2
        r"^b\d+$",  # b1, b2
        r"^c\d+$",  # c1, c2
        r"^vb\d+$",  # vb1, vb2
    ]

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self._raw_config: Dict[str, Any] = {}
        self._db_conn = None
        self._piecemark_standard: Optional[PiecemarkStandard] = None

        if config_path and os.path.exists(config_path):
            self._load_from_file(config_path)

    def _load_from_file(self, path: str) -> None:
        with open(path, "r", encoding="utf-8") as f:
            self._raw_config = json.load(f)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Config":
        config = cls()
        config._raw_config = data
        return config

    # Path properties
    @property
    def data_directory(self) -> str:
        return self._raw_config.get("data_directory", "")

    @property
    def job_name(self) -> str:
        return self._raw_config.get("job_name", "Unknown Job")

    @property
    def fabricator_id(self) -> str:
        return self._raw_config.get("fabricator_id", "")

    @property
    def output_path(self) -> str:
        path = self._raw_config.get("output_path", "./qa_qc_report.html")
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        return path

    @property
    def page_margin_inches(self) -> float:
        return self._raw_config.get("page_margin_inches", 0.5)

    # Database properties
    @property
    def db_host(self) -> str:
        return self._raw_config.get("db_host", "localhost")

    @property
    def db_port(self) -> int:
        return self._raw_config.get("db_port", 5432)

    @property
    def db_name(self) -> str:
        return self._raw_config.get("db_name", "sds2_standards")

    @property
    def db_user(self) -> str:
        return self._raw_config.get("db_user", "postgres")

    @property
    def db_password(self) -> str:
        return self._raw_config.get("db_password", "")

    def connect_db(self) -> bool:
        """Connect to PostgreSQL database"""
        if not PSYCOPG2_AVAILABLE:
            print("Warning: psycopg2 not available, using defaults")
            return False
        try:
            self._db_conn = psycopg2.connect(
                host=self.db_host,
                port=self.db_port,
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
            )
            return True
        except Exception as e:
            print(f"Database connection failed: {e}")
            return False

    def disconnect_db(self) -> None:
        """Disconnect from database"""
        if self._db_conn:
            self._db_conn.close()
            self._db_conn = None

    def load_piecemark_standards(self) -> PiecemarkStandard:
        """Load piecemark standards from database or use defaults"""
        if self._piecemark_standard:
            return self._piecemark_standard

        if self._db_conn:
            try:
                cursor = self._db_conn.cursor(RealDictCursor)
                cursor.execute(
                    """
                    SELECT fabricator_id, fabricator_name, major_prefixes, 
                           minor_prefixes, system_patterns, page_margin_inches
                    FROM fabricator_standards
                    WHERE fabricator_id = %s
                """,
                    (self.fabricator_id,),
                )
                row = cursor.fetchone()
                cursor.close()

                if row:
                    self._piecemark_standard = PiecemarkStandard(
                        fabricator_id=row["fabricator_id"],
                        fabricator_name=row["fabricator_name"],
                        major_prefixes=row.get("major_prefixes", {}) or {},
                        minor_prefixes=row.get("minor_prefixes", {}) or {},
                        system_patterns=row.get("system_patterns", []) or [],
                        page_margin_inches=row.get("page_margin_inches", 0.5) or 0.5,
                    )
                    return self._piecemark_standard
            except Exception as e:
                print(f"Error loading standards from DB: {e}")

        # Fallback to defaults
        self._piecemark_standard = PiecemarkStandard(
            fabricator_id=self.fabricator_id,
            fabricator_name="Default",
            system_patterns=self.DEFAULT_SYSTEM_PATTERNS,
            page_margin_inches=self.page_margin_inches,
        )
        return self._piecemark_standard

    def get_system_patterns(self) -> List[str]:
        """Get system mark regex patterns"""
        standards = self.load_piecemark_standards()
        return (
            standards.system_patterns
            if standards.system_patterns
            else self.DEFAULT_SYSTEM_PATTERNS
        )

    def is_system_mark(self, piecemark: str) -> bool:
        """Check if a piecemark matches system mark patterns"""
        if not piecemark:
            return False
        patterns = self.get_system_patterns()
        for pattern in patterns:
            try:
                if re.match(pattern, piecemark, re.IGNORECASE):
                    return True
            except re.error:
                continue
        return False

    def validate_paths(self) -> bool:
        """Validate configuration paths exist"""
        if self.data_directory and not os.path.exists(self.data_directory):
            return False
        output_dir = os.path.dirname(self.output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        return True


def create_default_config(output_path: str = None) -> dict:
    """Create a default configuration dictionary"""
    return {
        "data_directory": "",
        "job_name": "Current Job",
        "fabricator_id": "DEFAULT",
        "output_path": output_path or "./qa_qc_report.html",
        "page_margin_inches": 0.5,
        "db_host": "localhost",
        "db_port": 5432,
        "db_name": "sds2_standards",
        "db_user": "postgres",
        "db_password": "",
    }
