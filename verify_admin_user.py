import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()
from core.models import User

out = []
try:
    user = User.objects.get(username='Admin')
    out.append(f"FOUND {user.username} {user.email} {user.is_staff} {user.is_superuser}")
except User.DoesNotExist:
    out.append('NOT_FOUND')
except Exception as e:
    out.append(f'ERROR {type(e).__name__}: {e}')
with open('admin_verify.txt', 'w') as f:
    f.write('\n'.join(out) + '\n')
