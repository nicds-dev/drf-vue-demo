from rest_framework import serializers
from django_filters import rest_framework as filters
from products.models import Product, Category

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
        }

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'image', 'name', 'category', 'category_name', 'description', 'price', 'stock')
        filterset_class = ProductFilter

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'