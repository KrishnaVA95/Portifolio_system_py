from .models import Technology
from .serializer import TechnologySerializer
from rest_framework import generics


class TechnologyView(generics.ListCreateAPIView):
    queryset= Technology.objects.all()
    serializer_class= TechnologySerializer


class TechnologyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Technology.objects.all()
    serializer_class= TechnologySerializer

