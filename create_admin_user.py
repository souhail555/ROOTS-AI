import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()
from core.models import User

username = 'Admin'
password = 'Admin#12345'
email = 'souhail.aidi6@gmail.com'

user, created = User.objects.get_or_create(
    username=username,
    defaults={
        'email': email,
        'role': 'admin',
        'is_staff': True,
        'is_superuser': True,
    }
)
user.email = email
user.role = 'admin'
user.is_staff = True
user.is_superuser = True
user.set_password(password)
user.save()
with open('admin_result.txt', 'w') as out:
    out.write(f"OK {'created' if created else 'updated'} {user.username} {user.email} {user.is_staff} {user.is_superuser}\n")