from .models import Account
from .serializer import AccountSerializer
from rest_framework import generics

class AccountView(generics.ListCreateAPIView):
    queryset= Account.objects.all()
    serializer_class= AccountSerializer

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Account.objects.all()
    serializer_class= AccountSerializer