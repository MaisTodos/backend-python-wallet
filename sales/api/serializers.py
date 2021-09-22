from sales import models
from rest_framework import serializers
from django.core import validators
from validate_docbr import CPF
from decimal import Decimal
from django.utils import timezone


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['user', 'document', 'name']
        extra_kwargs = {
            "user": {"read_only": True},
        }
    
    def create(self, validated_data):
        document = CPF()

        if not document.validate(validated_data['document']):
            raise serializers.ValidationError('Invalid Document')
        
        return super().create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['ptype', 'value', 'qty']

class CashBackSerializer(serializers.ModelSerializer):
    CASHBACK = {
        'A': 0.15,
        'B': 0.10,
        'C': 0,
    }

    customer = CustomerSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = models.CashBack
        fields = ['sold_at', 'total', 'customer', 'products']
    
    # def cashback(self, products):
    #     cash = 0
    #     for product in products:
    #         total_by_product = float(product.get('value') * product.get('qty'))
    #         cash += total_by_product * self.CASHBACK[['A', 'B', 'C'][product.get('ptype')]]
    #     return Decimal(cash)

    def compute_total(self, products):
        total = 0
        for product in products:
            total += product.get('value') * product.get('qty')
        return total
    
    def set_products(self, products, cashback):
        for product in products:
            obj = models.Product.objects.create(**product)
            cashback.products.add(obj)
    
    def create(self, validated_data):
        total = self.compute_total(validated_data['products'])
        # cashback = self.cashback(validated_data['products'])
        # total -= cashback
        validated_data['total'] = total

        customer = validated_data['customer']
        customer['user'] = self.context['request'].user
        customer, created = models.Customer.objects.get_or_create(**customer)
        validated_data['customer'] = customer
        
        products = validated_data.pop('products')
        cashback = models.CashBack.objects.create(**validated_data)
        self.set_products(products, cashback)

        return cashback
    
    def validate(self, data):
        if data['total'] != self.compute_total(data['products']):
            raise serializers.ValidationError('Total was wrong calculated')
        if data['sold_at'] > timezone.now():
            raise serializers.ValidationError('Date cannot be after now')
        return data