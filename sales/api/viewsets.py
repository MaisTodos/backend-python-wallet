from sales import models
from rest_framework import viewsets
from sales.api import serializers
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from sales.views import maistodos


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
    filter_fields = ('type', 'value', 'qty')
    search_fields = ('type', 'value', 'qty')

class CashBackViewSet(viewsets.ModelViewSet):
    CASHBACK = {
        'A': 0.15,
        'B': 0.10,
        'C': 0,
    }

    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    serializer_class = serializers.CashBackSerializer
    queryset = models.CashBack.objects.all()
    filter_backends =  (SearchFilter, DjangoFilterBackend)
    filter_fields = ('sold_at', 'total')
    search_fields = ('sold_at', 'total')

    def cashback(self, products):
        cash = 0
        for product in products:
            total_by_product = float(product.get('value')) * product.get('qty')
            cash += total_by_product * self.CASHBACK[['A', 'B', 'C'][product.get('type')]]
        return cash
    
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)

        cashback = self.cashback(request.data['products'])
        response = maistodos(request, request.data['customer']['document'], cashback)

        return Response(response.json(), status=status.HTTP_201_CREATED)
