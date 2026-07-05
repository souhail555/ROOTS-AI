import sqlite3
from pathlib import Path
from pprint import pformat
output = []
path = Path('db.sqlite3')
output.append(f'DB_EXISTS: {path.exists()}')
if path.exists():
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cur.fetchall()]
    output.append(f'TABLES: {tables}')
    if 'core_user' in tables:
        cur.execute('PRAGMA table_info(core_user)')
        cols = [row[1] for row in cur.fetchall()]
        output.append(f'CORE_USER_COLS: {cols}')
        cur.execute("SELECT id, username, email, password, role, is_superuser, is_staff FROM core_user")
        rows = cur.fetchall()
        output.append(f'CORE_USER_ROWS: {pformat(rows)}')
    else:
        output.append('NO core_user TABLE')
    conn.close()
with open('db_user_info.txt', 'w') as f:
    f.write('\n'.join(output) + '\n')
