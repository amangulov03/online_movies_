from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentModelViewSet, toogle_like, FavoriteModelViewSet

router = DefaultRouter()
router.register('comments', CommentModelViewSet)
router.register('favorites', FavoriteModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('like/<int:id>/', toogle_like)
]
