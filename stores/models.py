from django.db import models
from profiles.models import Owner

# Create your models here.

class Store(models.Model):
    CHOICE_STORES = [
        ('Barraquinha', 'Barraquinha'),
        ('Restaurante', 'Restaurante'),
        ('Lanchonete', 'Lanchonete'),
        ('Only Delivery', 'Only Delivery'),
    ]
    owner_id = models.ForeignKey(Owner, on_delete=models.PROTECT, related_name='stores')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=CHOICE_STORES)
    is_open = models.BooleanField(default=False)
    is_main_store = models.BooleanField(default=False)
    document_number = models.CharField(max_length=255)
    start_work_hour = models.TimeField()
    close_work_hour = models.TimeField()
    logotype = models.ImageField(upload_to='logotypes/%Y/%m/%d/')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class StoreAddress(models.Model):
    store_id = models.OneToOneField(Store, on_delete=models.CASCADE, related_name='store_address')
    latitude = models.FloatField(max_length=25)
    longitude = models.FloatField(max_length=25)
    address = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    post_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    complement = models.CharField(max_length=255)

    def __str__(self):
        return self.address