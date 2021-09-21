from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Customer"))
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    document = models.CharField(verbose_name=_("CPF"), max_length=11, unique=True, validators=[MinLengthValidator(11)])

    def __str__(self):
        return self.name

class Product(models.Model):
    # Sistema de Classificação ABC : http://blog.comercialigara.com.br/curva-abc-estoque-supermercado
    TYPE = [
        ('A', _('High Priority')),
        ('B', _('Medium Priority')),
        ('C', _('Low Priority')),
    ]

    product_type = models.PositiveSmallIntegerField(choices=TYPE, verbose_name=_("Type"), default=0, null=False)
    value = models.DecimalField(max_digits=10, verbose_name=_("Value"), decimal_places=2, null=False)
    qty = models.PositiveIntegerField(null=False, verbose_name=_("Quantity"))

    def __str__(self):
        return self.product_type + " : " + self.value + " : " + self.qty
    
    @property
    def total_by_product(self):
        return self.value * self.qty

class CashBack(models.Model):
    CASHBACK = [
        ('A', 0.15),
        ('B', 0.10),
        ('C', 0),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name=_("Customer"))
    products = models.ManyToManyField(Product, verbose_name=_("Products"))
    sold_at = models.DateTimeField(default=timezone.now, verbose_name=_("Sale Date"))
    total = models.DecimalField(max_digits=10, verbose_name=_("Total"), decimal_places=2, null=False)

    def __str__(self):
        return self.customer.user.username + " : " + str(self.total)
    
    def cashback(self):
        discount = 0
        for i in self.products.all():
            discount += i.total_by_product * self.CASHBACK[i.product_type]
        return discount
    
    def clean(self):
        if self.total < 0:
            raise ValidationError(_("The total amount cannot be negative"))