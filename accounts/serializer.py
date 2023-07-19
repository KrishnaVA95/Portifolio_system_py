from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Account.objects.all())])
    class Meta:
        model = Account
        fields = ['id', 'name',  'email', 'password', 'is_admin']
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True}}
        def create(self, validated_data: dict) -> Account:
            return Account.objects.create_user(**validated_data)