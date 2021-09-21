from sales import models
from rest_framework import serializers
from django.core import validators
from validate_docbr import CPF


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['user', 'document', 'name']
    
    def create(self, validated_data):
        document = CPF()

        if not document.validate(validated_data['document']):
            raise serializers.ValidationError('Invalid Document')
        
        return super().create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['product_type', 'value', 'qty']

class CashBackSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=True)
    products = ProductSerializer(many=True)
    class Meta:
        model = models.CashBack
        fields = ['sold_at', 'total', 'customer', 'products']




