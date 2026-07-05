from django.contrib.auth.hashers import make_password
from django.db import migrations


def create_admin_user(apps, schema_editor):
    User = apps.get_model('core', 'User')
    username = 'Admin'
    email = 'souhail.aidi6@gmail.com'
    password = 'Admin#12345'

    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            'email': email,
            'role': 'admin',
            'is_staff': True,
            'is_superuser': True,
            'password': make_password(password),
        }
    )
    user.email = email
    user.role = 'admin'
    user.is_staff = True
    user.is_superuser = True
    user.password = make_password(password)
    user.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0004_alter_project_id_alter_user_id_car'),
    ]

    operations = [
        migrations.RunPython(create_admin_user, noop),
    ]
