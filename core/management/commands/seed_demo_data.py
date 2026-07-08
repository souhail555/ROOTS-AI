from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import Car, Project


class Command(BaseCommand):
    help = "Create deterministic demo users, projects, and cars (idempotent)."

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=2, help='Number of demo users')
        parser.add_argument('--projects-per-user', type=int, default=2, help='Projects to create per user')
        parser.add_argument('--cars-per-project', type=int, default=2, help='Cars to create per project')
        parser.add_argument('--password', type=str, default='Demo#12345', help='Password for demo users')

    @transaction.atomic
    def handle(self, *args, **options):
        users_count = max(1, options['users'])
        projects_per_user = max(1, options['projects_per_user'])
        cars_per_project = max(1, options['cars_per_project'])
        password = options['password']

        user_model = get_user_model()
        car_types = ['Toyota', 'Mitsubishi', 'Proton', 'Honda', 'Nissan', 'Mazda']

        created_users = 0
        created_projects = 0
        created_cars = 0

        for i in range(1, users_count + 1):
            username = f'demo_user_{i}'
            user, user_created = user_model.objects.get_or_create(
                username=username,
                defaults={
                    'email': f'{username}@example.com',
                    'role': 'participant',
                    'is_active': True,
                },
            )
            if user_created:
                user.set_password(password)
                user.save(update_fields=['password'])
                created_users += 1

            for p in range(1, projects_per_user + 1):
                project_name = f'Demo Project {i}-{p}'
                project, project_created = Project.objects.get_or_create(
                    owner=user,
                    name=project_name,
                    defaults={
                        'description': f'Seeded project for {username}',
                    },
                )
                if project_created:
                    created_projects += 1

                for c in range(1, cars_per_project + 1):
                    car_name = f'Demo Car {i}-{p}-{c}'
                    car_type = car_types[(c - 1) % len(car_types)]
                    _, car_created = Car.objects.get_or_create(
                        owner=user,
                        project=project,
                        name=car_name,
                        defaults={'car_type': car_type},
                    )
                    if car_created:
                        created_cars += 1

        self.stdout.write(self.style.SUCCESS(
            f'Seed complete. Created users={created_users}, projects={created_projects}, cars={created_cars}.'
        ))
