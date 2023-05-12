from django.db import models

# Create your models here.

class Coupon(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    validate = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name