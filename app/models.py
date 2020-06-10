from django.db import models
# Create your models here.

class Person(models.Model):
	fullname=models.CharField(max_length=50,unique=True)
	nationalid=models.CharField(max_length=14)
	age=models.IntegerField()
	gender=models.CharField(max_length=6)
	socialstatus=models.CharField(max_length=8)
	address=models.CharField(max_length=70)
	phone1=models.CharField(max_length=11)
	phone2=models.CharField(max_length=11,null=True)
	email=models.EmailField()


