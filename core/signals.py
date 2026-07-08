import os

from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Project


def ensure_admin_user():
    User = get_user_model()
    usernames_raw = os.getenv('ROOTS_ADMIN_USERNAMES', 'Admin,admin')
    admin_usernames = [u.strip() for u in usernames_raw.split(',') if u.strip()]
    admin_email = os.getenv('ROOTS_ADMIN_EMAIL', 'souhail.aidi6@gmail.com')
    admin_password = os.getenv('ROOTS_ADMIN_PASSWORD', 'Admin#12345')

    created_any = False
    primary_admin = None
    for admin_username in admin_usernames:
        user, created = User.objects.get_or_create(
            username=admin_username,
            defaults={
                'email': admin_email,
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        user.email = admin_email
        user.role = 'admin'
        user.is_staff = True
        user.is_superuser = True
        user.set_password(admin_password)
        user.save()
        created_any = created_any or created
        primary_admin = primary_admin or user

    return created_any, primary_admin


@receiver(post_migrate)
def create_sample_project(sender, **kwargs):
    if sender.label != 'core':
        return

    _, admin_user = ensure_admin_user()

    if not Project.objects.exists():
        Project.objects.create(
            owner=admin_user,
            name='Roots AI Demo',
            description='A sample project to show how the dashboard and project details page work.'
        )
