from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from sales.api import viewsets
from rest_framework.authtoken import views