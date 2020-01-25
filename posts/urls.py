from django.urls import path, include
from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet


router = SimpleRouter()
router.register('', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]
