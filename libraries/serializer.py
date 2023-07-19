from rest_framework import serializers
from .models import Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id','name', 'created_at', 'icon']
        read_only_fields = ['id', 'created_at' ]