from django.db import models
'''
# Create your models here.
class Teacher(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname  = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.Firstname
class Student(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.BigIntegerField()
'''
class ImageData(models.Model):
    Imagename=models.CharField(max_length=50)
    Image=models.ImageField(upload_to="img/")
