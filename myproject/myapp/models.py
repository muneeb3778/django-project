from django.db import models

# Create your models here.
# yaha pe database structure banta he

class Course(models.Model):                                   # ye Model datatypes ke liye he
    title = models.CharField(max_length=100,null=True)        # CharField ye varchar ki tarah hota he
    description = models.CharField(max_length=100)



class Lesson(models.Model):
    Course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100)



class Department(models.Model):                                        # parent (refrenced) table
    dep=models.AutoField(primary_key=True)
    deptname=models.CharField(max_length=100)

    def __str__(self):
        return self.deptname

class Employee(models.Model):                                           # child (refrencing) table
    dep=models.ForeignKey(Department,on_delete=models.CASCADE)          # yaha attribute ka vo hi name rakhenge jaha parent table me jisko bhi foreign key rakhna he aur jo delete castade he vo isliye he taki agar department se delete kare to employee se bhi hojay      
    name=models.CharField(max_length=100)
    salary=models.IntegerField()

    def __str__(self):
        return self.name






class Singer(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Song(models.Model):
    title=models.CharField(max_length=100)
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='sungby')
    duration=models.IntegerField()

    def __str__(self):
        return self.title





