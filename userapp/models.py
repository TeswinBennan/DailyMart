from django.db import models
from adminapp.models import *

# Create your models here.
class reg(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    Phone=models.IntegerField(max_length=255)
    Password=models.CharField(max_length=255)

class cont(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    message=models.TextField(max_length=255)

class cartdata(models.Model):
    cartuser=models.ForeignKey(reg,on_delete=models.CASCADE)
    cartproduct=models.ForeignKey(add,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0)

class checkout(models.Model):
    usercheckout=models.ForeignKey(reg,on_delete=models.CASCADE)
    checkoutcart=models.ForeignKey(cartdata,on_delete=models.CASCADE)
    address=models.CharField(max_length=25)
    city=models.CharField(max_length=25)
    country=models.CharField(max_length=25)
    postcode=models.CharField(max_length=25)
    