from django.urls import path
from core.views import home

urlpatterns = [
    path('api/', home),
]