from dataclasses import fields
from rest_framework import serializers 
from .models import Super_Types

class Super_TypesSerializer(serializers.ModelSerializer):
    class Meta:
        models = Super_Types
        fields = ['id', 'type']
