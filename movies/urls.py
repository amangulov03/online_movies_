from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MovieModelViewSet

router = DefaultRouter()
router.register('', MovieModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]