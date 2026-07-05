from rest_framework.viewsets import ModelViewSet
from .models import Car, Project
from .serializers import CarSerializer, ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer