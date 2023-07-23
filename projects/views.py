from .models import Project
from technologies.models import Technology
from .serializer import ProjectSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404

class ProjectView(generics.ListCreateAPIView):
    queryset= Project.objects.all()
    serializer_class= ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Project.objects.all()
    serializer_class= ProjectSerializer
