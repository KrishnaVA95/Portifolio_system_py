from .models import Library
from .serializer import LibrarySerializer
from rest_framework import generics


class LibraryView(generics.ListCreateAPIView):
    queryset= Library.objects.all()
    serializer_class= LibrarySerializer


class LibraryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Library.objects.all()
    serializer_class= LibrarySerializer

