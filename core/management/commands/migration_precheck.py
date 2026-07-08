from django.core.management.base import BaseCommand
from django.db import models

from core.models import Car, Project


class Command(BaseCommand):
    help = 'Check ownership/data consistency before or after migrations.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fail-on-issues',
            action='store_true',
            help='Exit with code 1 when any issue is found.',
        )

    def handle(self, *args, **options):
        issues = []

        project_owner_missing = Project.objects.filter(owner__isnull=True).count()
        if project_owner_missing:
            issues.append(f'Projects with missing owner: {project_owner_missing}')

        car_owner_missing = Car.objects.filter(owner__isnull=True).count()
        if car_owner_missing:
            issues.append(f'Cars with missing owner: {car_owner_missing}')

        cars_project_mismatch = Car.objects.exclude(owner_id=models.F('project__owner_id')).count()
        if cars_project_mismatch:
            issues.append(
                f'Cars where car.owner differs from project.owner: {cars_project_mismatch}'
            )

        if issues:
            self.stdout.write(self.style.WARNING('Precheck found issues:'))
            for issue in issues:
                self.stdout.write(f'- {issue}')
            if options['fail_on_issues']:
                raise SystemExit(1)
            return

        self.stdout.write(self.style.SUCCESS('Precheck passed. No ownership/data issues found.'))
