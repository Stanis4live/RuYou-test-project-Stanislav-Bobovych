from rest_framework import viewsets, permissions
from colors.models import Color
from palettes.models import Palette
from colors.serializers import ColorSerializer
from colors.services.color_API_integration import get_color_name
from rest_framework.exceptions import ValidationError


class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            palette_id = self.request.query_params.get('palette_id')
            if not palette_id:
                raise ValidationError({'palette_id': 'Palette ID is required'})
            return Color.objects.filter(palette__id= palette_id, palette__user=self.request.user)
        return Color.objects.filter(palette__user=self.request.user)

    def perform_create(self, serializer):
        hex_code = serializer.validated_data['hex_code']
        palette_id = serializer.validated_data['palette'].id
        palette = Palette.objects.filter(id=palette_id, user=self.request.user).first()
        if not palette:
            raise PermissionError('No access to this palette')
        name = get_color_name(hex_code)['value']
        serializer.save(name=name)

    def perform_update(self, serializer):
        hex_code = serializer.validated_data['hex_code']
        name = get_color_name(hex_code)['value']
        serializer.save(name=name)
