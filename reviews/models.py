from django.db import models
from stores.models import Store

# Create your models here.

class Review(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='reviews')
    star_rating = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)