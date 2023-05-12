from django.db import models

# Create your models here.

class Payment(models.Model):
    CHOICE_PAYMENTS = [
        ('Boleto', 'Boleto'),
        ('Pix', 'Pix'),
        ('Cartão Débito', 'Cartão Débito'),
        ('Cartão Crédito', 'Cartão Crédito'),
    ]
    type = models.CharField(max_length=14, choices=CHOICE_PAYMENTS)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.type