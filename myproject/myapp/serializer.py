
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User 

class courseSerializer(serializers.ModelSerializer):
      class Meta:
             model= Course
             fields= ["id",'title','description']



class lessonSerializer(serializers.ModelSerializer):
      Course=courseSerializer(read_only=True)
      class Meta:
             model= Lesson
             fields= ["id",'title','content','Course']


class DepartmentSerializer(serializers.ModelSerializer):
      class Meta:
             model= Department
             fields= ["dep","deptname"]

class EmployeeSerializer(serializers.ModelSerializer):
      dep=DepartmentSerializer(read_only=True)          # ye return karta he pura object jiska bhi foreign key match ho jata he uska aur attribute ka naam uska hi hona chahiye jo bhi foreign key he
      print('sddddddddddddsd',dep)              
      class Meta:
             model= Employee
             fields= ['id','name','salary','dep']


class UserSerializer(serializers.ModelSerializer):
       class Meta:
              model=User
              fields=['username','password']










class SongSerializer(serializers.ModelSerializer):
       class Meta:
              model=Song
              fields=["id",'title',"singer","duration"]

class SingerSerializer(serializers.ModelSerializer):
       singby = SongSerializer(many=True,read_only=True)
       class Meta:
              model=Singer
              fields=["id","name","gender","singby"]




