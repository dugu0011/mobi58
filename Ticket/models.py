from ast import Raise
from distutils.command.upload import upload
import email
from enum import unique
import re
from statistics import mode
from unicodedata import name
from django.db import models
from django.conf import settings
from psutil import users
from django.core.validators import MaxValueValidator, MinValueValidator

User = settings.AUTH_USER_MODEL
# Create your models here.

CATEGORY=(('CNM','CNM'),('CNM58','CNM58'),('ULTRACON','ULTRACON'),('TECH58','TECH58'),('HR58','HR58'))
SUB_CATEGORY=(('CNM','CNM'),('CNM58','CNM58'),('ULTRACON','ULTRACON'),('TECH58','TECH58'),('HR58','HR58'))
STATUS_TYPE=(('Hold','Hold'),('Re-open','Re-open'),('Active','Active'),('Closed','Closed'),('Complete','Complete'),('WIP','WIP'))
PRIORITY_CHOICES=(('High','High'),('Low','Low'),('Medium','Medium'))
SCHEDULER_STATUS=(('Weekly','Weekly'),('Monthly','Monthly'))
TYPE=(('Query','Query'),('Suggestion','Suggestion'),('Complaint','Complaint'))
class RaiseTicket(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    img=models.ImageField(upload_to='ticket/',blank=True,null=True)
    subject=models.CharField(max_length=50)
    msg=models.TextField()
    priority= models.CharField(choices=PRIORITY_CHOICES, max_length=50, blank=True,null=True)
    category= models.CharField(choices=CATEGORY, max_length=50, blank=True,null=True)
    subcategory= models.CharField(choices=SUB_CATEGORY, max_length=50, blank=True,null=True)
    Type=models.CharField(choices=TYPE, max_length=50, blank=True,null=True, default=TYPE[0])
    # admin_response=models.CharField(max_length=500,blank=True,null=True)
    # accepted=models.BooleanField(default=False)
    # is_aprove=models.BooleanField(default=False)
    status=models.CharField(max_length=30,choices=STATUS_TYPE, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(blank=True,null=True)
    ticket_id=models.CharField(max_length=50, null=True,blank=True)
    assign_to=models.ForeignKey(User,on_delete=models.CASCADE,related_name='assigned_users', blank=True,null=True)
    assigned_date=models.DateTimeField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    time_period=models.CharField(max_length=50,choices=SCHEDULER_STATUS,blank=True,null=True)

    

    def __str__(self):
        return "Message from" + str(self.id)


class Automation(models.Model):
    subject=models.CharField(max_length=50)
    msg=models.TextField()
    assign_to=models.ForeignKey(User,on_delete=models.CASCADE,related_name='assigned_to', blank=True,null=True)
    time_period=models.CharField(max_length=50,choices=SCHEDULER_STATUS,blank=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return "Task For " + str(self.time_period)





class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # name=models.CharField(max_length=20, null=True)
    ticket = models.ForeignKey(RaiseTicket, on_delete=models.CASCADE, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    message=models.TextField(null=True)
    is_active=models.BooleanField(default=True)


class DynamicData(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    prefix_txn=models.CharField(max_length=20,null=True,blank=True,default='1000')
    is_active=models.BooleanField(default=True)


