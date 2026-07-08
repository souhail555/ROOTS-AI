from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import create_sample_project

        # Keep DB writes inside post_migrate handlers, not app startup.
        post_migrate.connect(
            create_sample_project,
            sender=self,
            dispatch_uid='core.create_sample_project',
        )
