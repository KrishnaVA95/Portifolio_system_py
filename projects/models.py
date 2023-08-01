from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=127, unique=True)
    repository = models.CharField(max_length=255)
    deploy = models.CharField(max_length=255, null=True)
    video = models.CharField(max_length=255, null=True)
    cover = models.CharField(max_length=255, null=True)
    description = models.TextField()
    highlighted  = models.BooleanField(default=False)
    credits = ArrayField(models.CharField(max_length=255), null=True)
    content = ArrayField(models.TextField(), null=True)
    libs = models.ManyToManyField(
        "libraries.Library",
        related_name="projects"
    )
    technologies = models.ManyToManyField(
        "technologies.Technology",
        related_name="projects"
    )



