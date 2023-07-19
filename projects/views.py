from .models import Project
from technologies.models import Technology
from .serializer import ProjectSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404

class ProjectView(generics.ListCreateAPIView):
    queryset= Project.objects.all()
    serializer_class= ProjectSerializer

    # def perform_create(self, serializer):
    #     technologies_id= self.kwargs['pk']
    #     tech = get_object_or_404(Technology, id=technologies_id)
    #     serializer.save(technologies=tech)

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Project.objects.all()
    serializer_class= ProjectSerializer
