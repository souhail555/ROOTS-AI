import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()
from core.models import User

try:
    user = User.objects.get(username='Admin')
    print('FOUND', user.username, user.email, user.is_staff, user.is_superuser)
except User.DoesNotExist:
    print('NOT_FOUND')
