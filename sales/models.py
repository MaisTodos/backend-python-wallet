from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class Customer():
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Customer"))
    document = models.CharField(verbose_name=_("CPF"), max_length=20, unique=True)

    def __str__(self):
        return self.user.username

class Product():
    # Sistema de Classificação Aspinwall : https://pt.wikipedia.org/wiki/Produto_(marketing)
    TYPE = [
        ('A', _('Replacement Fee')),
        ('B', _('Gross Margin')),
        ('C', _('Buyer Goal Setting')),
        ('D', _('Duration of Product Satisfaction')),
        ('E', _('Duration of Buyer Search Behavior')),
    ]

    product_type = models.PositiveSmallIntegerField(choices=TYPE, verbose_name=_("Type"), default=0, null=False)
    value = models.DecimalField(max_digits=10, verbose_name=_("Value"), decimal_places=2, null=False)
    qty = models.PositiveIntegerField(null=False, verbose_name=_("Quantity"))

    def __str__(self):
        return self.product_type + " : " + self.value + " : " + self.qty

class CashBack():
    sold_at = models.DateTimeField(default=timezone.now, verbose_name=_("Sale Date"))
    total = models.DecimalField(max_digits=10, verbose_name=_("Total"), decimal_places=2, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name=_("Customer"))
    products = models.ManyToManyField(Product, verbose_name=_("Products"))

    def __str__(self):
        return self.customer.user.username + " : " + str(self.total)
    
    # def cashback(self):
    #     for i in self.products.all():
    #         if i.product_type == 'A':
    #             return self.total * 0.05
    
    def clean(self):
        if self.total < 0:
            raise ValidationError(_("The total amount cannot be negative"))