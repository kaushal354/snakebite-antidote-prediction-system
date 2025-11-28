# home/sqlite_patch.py
import sys
import types

try:
    # Try normal stdlib first (if available)
    import sqlite3  # type: ignore
except Exception:
    # Try pysqlite3 fallback
    try:
        from pysqlite3 import dbapi2 as pysqlite_dbapi  # type: ignore
    except Exception:
        # No fallback available — re-raise original import error to preserve trace
        raise

    # Build a lightweight sqlite3 wrapper module with a dbapi2 attribute
    sqlite3_wrapper = types.ModuleType("sqlite3")
    # dbapi2 attribute expected by Django: `from sqlite3 import dbapi2 as Database`
    sqlite3_wrapper.dbapi2 = pysqlite_dbapi

    # Copy some helpful convenience attributes (so code expecting them works)
    for name in ("connect", "paramstyle", "apilevel", "threadsafety"):
        if hasattr(pysqlite_dbapi, name):
            setattr(sqlite3_wrapper, name, getattr(pysqlite_dbapi, name))

    # Register both names so imports of sqlite3 and _sqlite3 resolve properly
    sys.modules["sqlite3"] = sqlite3_wrapper
    sys.modules["_sqlite3"] = pysqlite_dbapi
