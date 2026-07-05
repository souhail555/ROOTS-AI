from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import create_sample_project, ensure_admin_user

        post_migrate.connect(create_sample_project, sender=self)
        try:
            ensure_admin_user()
        except Exception:
            pass
