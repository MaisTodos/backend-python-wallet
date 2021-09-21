from sales import models
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['document', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['product_type', 'value', 'qty']

class CahsBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['sold_at', 'total']




