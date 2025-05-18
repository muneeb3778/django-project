from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.Serializer):
           
            name = serializers.CharField(max_lenght=100)
            rollno = serializers.IntegerField()
            city = serializers.CharField(max_lenght=100)

            def create(self, validated_data):                            # aur yaha bas create hi likhenge
                return Student.objects.create(**validated_data)











