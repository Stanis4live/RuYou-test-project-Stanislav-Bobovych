from rest_framework import viewsets, permissions
from .serializers import PaletteSerializer


class PaletteViewSet(viewsets.ModelViewSet):
    serializer_class = PaletteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.palettes.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
