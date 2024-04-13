from rest_framework import viewsets, permissions
from colors.models import Color
from palettes.models import Palette
from colors.serializers import ColorSerializer
from colors.services.color_API_integration import get_color_name
from rest_framework.exceptions import PermissionDenied
from colors.filtersets import ColorFilterSet


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ColorFilterSet

    def get_object(self):
        obj = super().get_object()
        if obj.palette.user != self.request.user:
            raise PermissionDenied("У вас нет доступа к этому цвету")
        return obj

    def perform_create(self, serializer):
        hex_code = serializer.validated_data['hex_code']
        palette_id = serializer.validated_data['palette'].id
        palette = Palette.objects.filter(id=palette_id, user=self.request.user).first()
        if not palette:
            raise PermissionError('Нет доступа к этой палитре')
        name = get_color_name(hex_code)['value']
        serializer.save(name=name)

    def perform_update(self, serializer):
        hex_code = serializer.validated_data['hex_code']
        name = get_color_name(hex_code)['value']
        serializer.save(name=name)
