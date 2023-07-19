from django.contrib.auth.models import AbstractUser, Permission
from django.db import models

# Create your models here.
class Account(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(null=True, default=False)
