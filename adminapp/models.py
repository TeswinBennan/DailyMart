from django.db import models

# Create your models here.
class cat(models.Model):
    CName=models.CharField(max_length=255)
    CImage=models.ImageField(upload_to='sample',default='null.jpg')
class add(models.Model):
    PName=models.CharField(max_length=255)
    PCat=models.CharField(max_length=255)
    PPrice=models.IntegerField(max_length=255)
    PDescription=models.CharField(max_length=255)
    PImage=models.ImageField(upload_to='sample1',default='null.jpg')