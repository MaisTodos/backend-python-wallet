from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from sales.api import viewsets
from rest_framework.authtoken import views

app_name = 'sales'

router = routers.DefaultRouter()
router.register(r'customer', viewsets.CustomerViewSet, basename='Customer')
router.register(r'product', viewsets.ProductViewSet, basename='Product')
router.register(r'cashback', viewsets.CashBackViewSet, basename='CashBack')

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('api-token-auth/', views.obtain_auth_token),
]