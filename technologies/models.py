from django.db import models


class Technology(models.Model):
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=127)
    icon = models.CharField(max_length=255, null=True)
