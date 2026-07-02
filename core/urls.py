from django.urls import path
from core.views import home, register

urlpatterns = [
    path('', home),                 # GET /api/
    path('register/', register),   # POST /api/register/
]