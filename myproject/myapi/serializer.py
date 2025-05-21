from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.Serializer):
           
            name = serializers.CharField(max_length=100)
            rollno = serializers.IntegerField()
            city = serializers.CharField(max_length=100)

            def create(self, validate_data):                            # aur yaha bas create hi likhenge
                return Student.objects.create(**validate_data)
            
            def update(self,instance,validated_data):                  
                    instance.name=validated_data.get('name',instance.name)         # instance isme purana object araha he aur validated_data isme naya object araha he aur validated_data.get('name',instance.name) ye jo likha he iska matlab agar 'name' he to ye daldo nahi to ye instance.name daldo
                    instance.rollno=validated_data.get('rollno',instance.rollno)
                    instance.city=validated_data.get('city',instance.city)
                    instance.save()
                    return instance









