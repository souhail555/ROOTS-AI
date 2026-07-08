from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Car, Project


class CarModelTest(TestCase):
    def test_car_belongs_to_project(self):
        user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123"
        )
        project = Project.objects.create(
            owner=user,
            name="Road Trip",
            description="A family trip plan"
        )
        car = Car.objects.create(
            owner=user,
            name="Tesla Model 3",
            car_type="Electric",
            project=project
        )

        self.assertEqual(car.project, project)
        self.assertEqual(project.cars.count(), 1)


class AccessControlTests(APITestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user_a = user_model.objects.create_user(
            username='alice',
            password='pass12345',
            role='participant',
        )
        self.user_b = user_model.objects.create_user(
            username='bob',
            password='pass12345',
            role='participant',
        )
        self.admin_user = user_model.objects.create_user(
            username='admin_user',
            password='pass12345',
            role='admin',
            is_staff=True,
        )

        self.project_a = Project.objects.create(
            owner=self.user_a,
            name='Project A',
            description='Owned by Alice',
        )
        self.project_b = Project.objects.create(
            owner=self.user_b,
            name='Project B',
            description='Owned by Bob',
        )

        Car.objects.create(
            owner=self.user_a,
            project=self.project_a,
            name='Alice Car',
            car_type='Toyota',
        )
        Car.objects.create(
            owner=self.user_b,
            project=self.project_b,
            name='Bob Car',
            car_type='Honda',
        )

    def test_regular_user_sees_only_owned_projects(self):
        self.client.force_authenticate(user=self.user_a)
        response = self.client.get('/api/projects/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.project_a.id)

    def test_admin_sees_all_projects(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get('/api/projects/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project_ids = {item['id'] for item in response.data}
        self.assertIn(self.project_a.id, project_ids)
        self.assertIn(self.project_b.id, project_ids)
        self.assertGreaterEqual(len(response.data), 2)

    def test_regular_user_cannot_add_car_to_other_users_project(self):
        self.client.force_authenticate(user=self.user_a)
        response = self.client.post(
            '/api/cars/',
            {
                'project': self.project_b.id,
                'name': 'Unauthorized Car',
                'car_type': 'Mitsubishi',
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('project', response.data)