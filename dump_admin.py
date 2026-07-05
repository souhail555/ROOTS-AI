import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()
from core.models import User

with open('admin_debug.txt', 'w') as out:
    out.write('START\n')
    try:
        users = list(User.objects.values('username', 'email', 'role', 'is_staff', 'is_superuser'))
        out.write(f'USERS {users}\n')
    except Exception as e:
        out.write(f'ERROR {type(e).__name__}: {e}\n')
    out.write('DONE\n')
