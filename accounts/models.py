from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from django.utils.translation import gettext_lazy as _


class UserType(models.Model):
    CHOICE_NAMES = [
        ('owner', 'owner'),
        ('user', 'user')
    ]

    user_type = models.CharField(max_length=6, choices=CHOICE_NAMES)

    def __str__(self):
        return self.user_type


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)
    user_type_id = models.ForeignKey(UserType, null=True, blank=True, on_delete=models.SET_NULL, related_name='users')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.email