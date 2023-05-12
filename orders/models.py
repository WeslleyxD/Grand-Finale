from django.db import models
from profiles.models import ClientUser
from stores.models import Store
from payments.models import Payment
from coupons.models import Coupon
from products.models import Product

# Create your models here.

class Order(models.Model):
    CHOICE_ORDERS = [
        ('Pago', 'Pago'),
        ('Cancelado', 'Cancelado'),
        ('Processando', 'Processando'),
        ('Ativo', 'Ativo'),
    ]

    client_user_id = models.ForeignKey(ClientUser, on_delete=models.CASCADE, related_name='orders')
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders')
    payment_id = models.ForeignKey(Payment, on_delete=models.PROTECT, related_name='orders')
    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT, related_name='orders')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=12, choices=CHOICE_ORDERS)
    time = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.client_user_id.name} - {self.store_id.name}'

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    time = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)