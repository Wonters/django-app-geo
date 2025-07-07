from rest_framework import routers
from django.urls import path, include
from .views import *


# Routers for restframework BACKEND
router = routers.DefaultRouter()
router.register(r'peak', PeakViewSet, basename='peak')
router.register(r'geo', GeoViewSet, basename='geo')
router.register(r'rejected IP', IPRejViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('show/', ViewMap.as_view(), name='view map')
]