from django.contrib import admin
# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from apiapp.views import StudentViewSet

router = DefaultRouter()
router.register(r'student', StudentViewSet)

urlpatterns = [
      path('', include(router.urls)),
    ]