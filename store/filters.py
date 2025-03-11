# store/filters.py

import django_filters
from .models import Store

class StoreFilter(django_filters.FilterSet):
    store_name = django_filters.CharFilter(field_name="store_name", lookup_expr='icontains')  # Case-insensitive partial match
    address = django_filters.CharFilter(field_name="address", lookup_expr='icontains')  # Case-insensitive partial match

    class Meta:
        model = Store
        fields = ['store_name', 'address']
