from django.db import models


class Library(models.Model):
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=127, unique=True)
    icon = models.CharField(max_length=255, null=True)