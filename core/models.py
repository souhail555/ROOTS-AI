from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('participant', 'Participant'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='participant'
    )

    def __str__(self):
        return self.username


class Project(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Car(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cars'
    )

    project = models.ForeignKey(
        Project,
        related_name='cars',
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=255)
    car_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.car_type})"
    