from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db import models

from core.models import Car, Project


class Command(BaseCommand):
    help = 'Repair ownership inconsistencies in a safe, explicit way.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would change without writing to the database.',
        )
        parser.add_argument(
            '--apply',
            action='store_true',
            help='Apply changes to the database.',
        )
        parser.add_argument(
            '--fallback-username',
            type=str,
            default='Admin',
            help='User assigned when fallback ownership is needed.',
        )

    @transaction.atomic
    def handle(self, *args, **options):
        dry_run = options['dry_run']
        apply_changes = options['apply']

        if dry_run and apply_changes:
            raise CommandError('Use either --dry-run or --apply, not both.')
        if not dry_run and not apply_changes:
            raise CommandError('Specify one mode: --dry-run or --apply.')

        fallback_username = options['fallback_username']
        user_model = get_user_model()
        fallback_user = user_model.objects.filter(username=fallback_username).first()
        if not fallback_user:
            raise CommandError(
                f'Fallback user "{fallback_username}" does not exist. '
                'Create it first or use --fallback-username with an existing user.'
            )

        project_updates = 0
        car_updates = 0

        projects_without_owner = Project.objects.filter(owner__isnull=True)
        for project in projects_without_owner:
            project_updates += 1
            if apply_changes:
                project.owner = fallback_user
                project.save(update_fields=['owner'])

        cars_without_owner = Car.objects.filter(owner__isnull=True)
        for car in cars_without_owner:
            car_updates += 1
            if apply_changes:
                car.owner = car.project.owner if car.project and car.project.owner_id else fallback_user
                car.save(update_fields=['owner'])

        mismatched_cars = Car.objects.exclude(owner_id__isnull=True).exclude(project__owner_id__isnull=True).exclude(
            owner_id=models.F('project__owner_id')
        )
        for car in mismatched_cars:
            car_updates += 1
            if apply_changes:
                car.owner = car.project.owner
                car.save(update_fields=['owner'])

        mode = 'DRY RUN' if dry_run else 'APPLIED'
        self.stdout.write(self.style.SUCCESS(
            f'{mode}: repaired projects={project_updates}, cars={car_updates}.'
        ))
