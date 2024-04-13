import django_filters
from django_filters.rest_framework import filterset
from colors.models import Color


class ColorFilterSet(filterset.FilterSet):
    palette_id = django_filters.NumberFilter(field_name='palette__id')

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        if request and hasattr(request, 'user'):
            self.queryset = self.queryset.filter(palette__user=request.user)

    class Meta:
        model = Color
        fields = ['palette_id']
