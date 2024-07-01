import django_filters
from products.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    ratings_stars = django_filters.NumberFilter(field_name='ratings__stars', lookup_expr='gte')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    available = django_filters.BooleanFilter(field_name='available')

    class Meta:
        model = Product
        fields = ['name', 'description', 'ratings__stars', 'category', 'price', 'available']
