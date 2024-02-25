from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NearMissViewSet 

router = DefaultRouter()
router.register(r'nearMiss', NearMissViewSet, basename='nearMiss')

urlpatterns = [
    path('', include(router.urls)),
]
