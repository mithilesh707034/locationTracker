from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=10)
    latitude=serializers.CharField(max_length=1000)
    longitude=serializers.CharField(max_length=1000)
    
    def create(self,validatedData):
        return Member.objects.create(**validatedData)
