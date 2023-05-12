from django.db import models
from stores.models import Store

# Create your models here.

class Category(models.Model):
    CHOICES_CATEGORIES = [
            ('Vegano', 'Vegano'),
            ('Vegetais', 'Vegetais'),
            ('Carnes', 'Carnes'),
            ('Lanches', 'Lanches'),
            ('Creps', 'Creps'),
            ('Massas', 'Massas'),
        ]
    name = models.CharField(max_length=10, choices=CHOICES_CATEGORIES)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Product(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=255)
    is_available = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name