from django.contrib import admin
from sales import models
from reversion.admin import VersionAdmin

@admin.register(models.Customer)
class CustomerAdmin(VersionAdmin):
    pass

@admin.register(models.Product)
class ProductAdmin(VersionAdmin):
    pass

@admin.register(models.CashBack)
class CashBackAdmin(VersionAdmin):
    pass