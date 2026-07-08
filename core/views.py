from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Car, Project
from .serializers import CarSerializer, ProjectSerializer


def is_admin_user(user):
    return bool(
        user
        and user.is_authenticated
        and (user.is_superuser or user.is_staff or getattr(user, 'role', None) == 'admin')
    )


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if is_admin_user(self.request.user):
            return Project.objects.all().select_related('owner')
        return Project.objects.filter(owner=self.request.user).select_related('owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if is_admin_user(self.request.user):
            return Car.objects.all().select_related('owner', 'project')
        return Car.objects.filter(owner=self.request.user).select_related('owner', 'project')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)