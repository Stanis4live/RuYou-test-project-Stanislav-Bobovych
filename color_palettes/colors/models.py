from django.db import models
from palettes.models import Palette

class Color(models.Model):
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE, related_name='colors')
    hex_code = models.CharField(max_length=7)
    name = models.CharField(max_length=100, blank=True)