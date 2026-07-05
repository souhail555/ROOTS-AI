from django.test import TestCase

from .models import Car, Project


class CarModelTest(TestCase):
    def test_car_belongs_to_project(self):
        project = Project.objects.create(name="Road Trip", description="A family trip plan")
        car = Car.objects.create(name="Tesla Model 3", car_type="Electric", project=project)

        self.assertEqual(car.project, project)
        self.assertEqual(project.cars.count(), 1)