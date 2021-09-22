from sales import models
from rest_framework import viewsets
from sales.api import serializers
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    serializer_class = serializers.CustomerSerializer
    filter_backends =  (SearchFilter, DjangoFilterBackend)
    filter_fields = ('document', 'name')
    search_fields = ('document', 'name')
    queryset = models.Customer.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    filter_backends =  (SearchFilter, DjangoFilterBackend)
    filter_fields = ('product_type', 'value', 'qty')
    search_fields = ('product_type', 'value', 'qty')

class CashBackViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    serializer_class = serializers.CashBackSerializer
    queryset = models.CashBack.objects.all()
    filter_backends =  (SearchFilter, DjangoFilterBackend)
    filter_fields = ('sold_at', 'total')
    search_fields = ('sold_at', 'total')



    # def create(self, request, *args, **kwargs):
    #     total = self.compute_total(request.data['products'])
    #     cashback = self.cashback(request.data['products'])
    #     total -= cashback

    #     request.data['total'] = total

    #     return super().create(request, *args, **kwargs)