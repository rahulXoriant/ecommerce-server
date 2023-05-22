import os
from rest_framework import serializers
from django.conf import settings

from products.models import Category, Product, Stock

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    isCashOnDeliveryAvailable = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'price', 'category', 'isCashOnDeliveryAvailable')

    def get_category(self, obj):
        return obj.category.name
    
    def get_price(self, obj):
        return float(obj.price)
    
    def get_isCashOnDeliveryAvailable(self, obj):
        return obj.is_cash_on_delivery_available

class StocksSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = ('id', 'amount')

    def get_id(self, obj):
        return obj.product.id
