# home/sqlite_patch.py
import sys

try:
    import sqlite3
except Exception:
    try:
        # pysqlite3-binary installs as pysqlite3
        from pysqlite3 import dbapi2 as _dbapi2  # type: ignore
    except Exception:
        # No fallback available — re-raise original failure to preserve trace
        raise

    # Ensure both names are present so Python and C-extension lookups succeed
    sys.modules['sqlite3'] = _dbapi2
    sys.modules['_sqlite3'] = _dbapi2
