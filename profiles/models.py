from django.db import models
from accounts.models import User

# Create your models here.

class Owner(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    alteration = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
    

class ClientUser(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_user')
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    tel_number = models.CharField(max_length=20)
    latitude = models.FloatField(max_length=25)
    longitude = models.FloatField(max_length=25)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
    