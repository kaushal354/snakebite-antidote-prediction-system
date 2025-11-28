# home/sqlite_patch.py
import sys
import types

try:
    import sqlite3  # try stdlib
except Exception:
    try:
        from pysqlite3 import dbapi2 as pysqlite_dbapi
    except Exception:
        raise

    # if pysqlite_dbapi is a module, create a small module for sqlite3 that exposes dbapi2
    sqlite3_mod = types.ModuleType("sqlite3")
    sqlite3_mod.dbapi2 = pysqlite_dbapi

    # commonly used top-level helpers that some code expects
    for attr in ("connect", "apilevel", "threadsafety", "paramstyle"):
        if hasattr(pysqlite_dbapi, attr):
            setattr(sqlite3_mod, attr, getattr(pysqlite_dbapi, attr))

    sys.modules["sqlite3"] = sqlite3_mod
    # some C extensions try to import _sqlite3 — point it to the real dbapi
    sys.modules["_sqlite3"] = pysqlite_dbapi

