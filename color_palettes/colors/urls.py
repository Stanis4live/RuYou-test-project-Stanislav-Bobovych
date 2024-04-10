from django.urls import include, path
from colors.views import ColorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'colors/', ColorViewSet, basename='color')

urlpatterns = [
    path('', include(router.urls)),
    ]