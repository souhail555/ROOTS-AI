from pathlib import Path
text = '''from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, ProjectViewSet
from .views_auth import RegisterView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
'''
Path('core/urls.py').write_text(text, encoding='utf-8')
print('OK')
