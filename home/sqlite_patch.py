# home/sqlite_patch.py
import sys
import types

# Try to use the real stdlib sqlite3 first. If that works, nothing else needed.
try:
    import sqlite3  # type: ignore
except Exception:
    # Fallback to pysqlite3's dbapi2 implementation
    try:
        from pysqlite3 import dbapi2 as pysqlite_dbapi  # type: ignore
    except Exception:
        # No stdlib sqlite3 and no pysqlite3 — re-raise so original error is visible
        raise

    # Create a single sqlite3 wrapper module that exposes dbapi2 (what Django expects)
    sqlite3_wrapper = types.ModuleType("sqlite3")
    sqlite3_wrapper.dbapi2 = pysqlite_dbapi

    # Provide a few top-level convenience attributes some code expects (if available)
    for attr in ("connect", "apilevel", "threadsafety", "paramstyle"):
        if hasattr(pysqlite_dbapi, attr):
            setattr(sqlite3_wrapper, attr, getattr(pysqlite_dbapi, attr))

    # Register modules so `import sqlite3` and internal imports of `_sqlite3` succeed
    sys.modules["sqlite3"] = sqlite3_wrapper
    sys.modules["_sqlite3"] = pysqlite_dbapi
