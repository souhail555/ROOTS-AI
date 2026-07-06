from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Project, Car
from .serializers import ProjectSerializer, CarSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Project.objects.all()

        return Project.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Car.objects.all()

        return Car.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)