from rest_framework import serializers
from .models import Palette


class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = ['id', 'name', 'user']
        read_only_fields = ['id', 'user']