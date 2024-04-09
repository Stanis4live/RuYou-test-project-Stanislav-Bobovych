from django.urls import include, path
from palettes.views import PaletteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'palettes/', PaletteViewSet, basename='palette')

urlpatterns = [
    path('', include(router.urls)),
    ]