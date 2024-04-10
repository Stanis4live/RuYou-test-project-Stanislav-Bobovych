from rest_framework import serializers
from colors.models import Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'palette', 'hex_code', 'name']
        read_only_fields = ['id']