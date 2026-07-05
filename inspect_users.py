import sqlite3
from pathlib import Path
path = Path('db.sqlite3')
print('DB_EXISTS', path.exists())
if not path.exists():
    raise SystemExit(1)
conn = sqlite3.connect(path)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [row[0] for row in cur.fetchall()]
print('TABLES', tables)
for t in ['core_user', 'auth_user', 'django_user', 'auth_user_groups', 'django_session']:
    if t in tables:
        print('HAS_TABLE', t)
        cur.execute(f'PRAGMA table_info({t})')
        print('COLS', [r[1] for r in cur.fetchall()])
        try:
            cur.execute(f"SELECT id, username, email, password, role, is_superuser, is_staff FROM {t}")
        except sqlite3.OperationalError:
            cur.execute(f"SELECT id, username, email, password, is_superuser, is_staff FROM {t}")
        for row in cur.fetchall():
            print('USER_ROW', row)
conn.close()