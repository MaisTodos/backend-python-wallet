from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from sales.api import viewsets
from rest_framework.authtoken import views

app_name = 'sales'

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('api-token-auth/', views.obtain_auth_token),
]