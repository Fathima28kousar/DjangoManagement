from django.db import models
from django.contrib.auth.models import *

# Create your models here.

class Employee(models.Model):
    employee = models.ForeignKey(User, on_delete = models.SET_NULL,null = True,blank = True)
    employee_name = models.CharField(max_length = 500,default="")
    employee_email = models.EmailField(max_length=255,default="")
    employee_phone = models.CharField(max_length = 15,default="")
    employee_salary = models.CharField(max_length=30,default="")
    employee_role = models.CharField(max_length=255,default="")
    employee_department = models.CharField(max_length=255,default="")
    employee_image = models.ImageField(upload_to='imageFolder')
    employee_education = models.CharField(max_length=500,default="")
    employee_location = models.CharField(max_length=400,default="")
    employee_bonus = models.CharField(max_length=200,default="")

    

