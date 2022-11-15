from .models import Products,Category
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['region','city','category','product','quantity','unit_price','ordered_date']

class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']