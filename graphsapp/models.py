from django.db import models
from pandas.core.algorithms import mode

class DataSets(models.Model):
    age = models.IntegerField(default=0)
    work= models.TextField(null=True, blank=True)
    fnlwgt = models.IntegerField(default=0)
    education = models.CharField(max_length=500,null=True,blank=True)
    education_num = models.IntegerField(default=0)
    marital_status = models.CharField(max_length=500,null=True,blank=True)
    occupation = models.CharField(max_length=500,null=True,blank=True)
    relationship = models.CharField(max_length=50,null=True,blank=True)
    race = models.CharField(max_length=100,null=True,blank=True)
    sex = models.CharField(max_length=10,null=True,blank=True)
    capital_gain = models.IntegerField(default=0)
    capital_loss = models.IntegerField(default=0)
    hours_per_week = models.IntegerField(default=0)
    native_country = models.CharField(max_length=100,null=True,blank=True)
    salary = models.CharField(max_length=100,null=True,blank=True)

