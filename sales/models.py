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
        return self.user.username + " : " + self.name

class Product(models.Model):
    # Sistema de Classificação ABC : http://blog.comercialigara.com.br/curva-abc-estoque-supermercado
    TYPE = [
        (0, _('Class A - High Priority')),
        (1, _('Class B - Medium Priority')),
        (2, _('Class C - Low Priority')),
    ]

    ptype = models.PositiveSmallIntegerField(choices=TYPE, verbose_name=_("Type"), default=0, null=False)
    value = models.DecimalField(max_digits=10, verbose_name=_("Value"), decimal_places=2, null=False)
    qty = models.PositiveIntegerField(null=False, verbose_name=_("Quantity"))

    def __str__(self):
        return self.TYPE[self.product_type][-1] + " : " + str(self.value) + " : " + str(self.qty)
    
    @property
    def total_by_product(self):
        return self.value * self.qty

class CashBack(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name=_("Customer"))
    products = models.ManyToManyField(Product, verbose_name=_("Products"))
    sold_at = models.DateTimeField(default=timezone.now, verbose_name=_("Sale Date"))
    total = models.DecimalField(max_digits=10, verbose_name=_("Total"), default=0, decimal_places=2, null=False)

    def __str__(self):
        return self.customer.name + " : " + str(self.total)

    def clean(self):
        if self.total < 0:
            raise ValidationError(_("The total amount cannot be negative"))
        
    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)