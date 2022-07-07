from logging import NullHandler
from statistics import mode
from unicodedata import name
from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission
from django.db.models.fields import CharField
from pkg_resources import resource_string
from django_countries.fields import CountryField
from filer.fields.image import FilerImageField
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from jsonfield import JSONField
from django.db.models import Sum
from model_utils import FieldTracker
from .choices import *
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
User = settings.AUTH_USER_MODEL

# Create your models here.



def validate_file_size(value):
    from django.core.exceptions import ValidationError
    filesize= value.size
    
    if filesize > 5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value





class Transporter(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    transporter_name = models.CharField(max_length=200)
    # created=models.DateTimeField(auto_now_add=True)
    mobile = models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(max_length=150,null=True,blank=True)
    address = models.TextField(max_length=500,null=True,blank=True)
    pan_no=models.CharField(max_length=50,null=True,blank=True, unique=True)
    pan_file=models.FileField(upload_to="transporter/",blank=True,null=True, validators=[validate_file_size])
    gst_no=models.CharField(max_length=50,null=True,blank=True, unique=True)
    gst_file=models.FileField(upload_to="transporter/",blank=True,null=True, validators=[validate_file_size])
    cin_no=models.CharField(max_length=50,null=True,blank=True, unique=True)
    cin_file=models.FileField(upload_to="transporter/",blank=True,null=True, validators=[validate_file_size])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.transporter_name)


class vehicleRegister(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    trransporter=models.ForeignKey(Transporter,on_delete=models.CASCADE, null=True,blank=True,)
    registeration_no=models.CharField(max_length=12, unique=True,null=True,blank=True)
    # created=models.DateTimeField(auto_now_add=True)
    rc_file = models.FileField(upload_to="file/vehicle/", blank=True, null=True, validators=[validate_file_size])
    registeration_date=models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    registered_upto=models.DateField( auto_now=False, auto_now_add=False,null=True,blank=True)
    owner_name=models.CharField(max_length=100,null=True,blank=True)
    vehicle_type=models.CharField(choices=VEHICLE_TYPE,max_length=100,blank=True,null=True)
    vehicle_model=models.CharField(max_length=50,null=True,blank=True)
    vehicle_class=models.CharField(max_length=50,null=True,blank=True)
    vehicle_color=models.CharField(max_length=50,null=True,blank=True)
    engine_no=models.CharField(max_length=50, unique=True,null=True,blank=True)
    chasis_no=models.CharField(max_length=50,unique=True,null=True,blank=True)
    rto_details=models.CharField(max_length=50,null=True,blank=True)
    fuel_type=models.CharField(choices=FUEL_TYPE,max_length=20,null=True,blank=True)
    insurance_validity = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    insurance_file = models.FileField(upload_to="file/vehicle/", blank=True, null=True, validators=[validate_file_size])
    pollution_validity = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    pollution_file = models.FileField(upload_to="file/vehicle/", blank=True, null=True, validators=[validate_file_size])
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.registeration_no)


class Driver(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    transporter_name = models.ForeignKey(Transporter, on_delete=models.CASCADE, null=True, blank=True)
    vehicle = models.ForeignKey(vehicleRegister,on_delete=models.CASCADE, blank=True)
    # created=models.DateTimeField(auto_now_add=True)
    driver_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    DOB = models.DateField(max_length=50, null=True, blank=True)
    license_no = models.CharField(max_length=50, null=True, blank=True)
    license_file = models.FileField(upload_to="file/dl/", blank=True, null=True, validators=[validate_file_size])
    aadhar_no = models.CharField(max_length=50, null=True, blank=True)
    aadhar_file = models.FileField(upload_to="file/aadhar/", blank=True, null=True, validators=[validate_file_size])
    address = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.vehicle ) + ' Driver  ' + str(self.driver_name)
    
class addTrip(models.Model):
    transporter_name=models.ForeignKey(Transporter, on_delete=models.CASCADE, null=True, blank=True)
    vehicle = models.ForeignKey(vehicleRegister,on_delete=models.CASCADE, blank=True)
    source=models.CharField(choices=SOURCE, max_length=50, blank=True,null=True)
    # created=models.DateTimeField(auto_now_add=True)
    destination=models.CharField(choices=DESTINATION, max_length=50, blank=True,null=True)
    approx_distance=models.PositiveIntegerField(blank=True, null=True)
    Fixed_amount_btw_s_d=models.PositiveIntegerField(default=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.transporter_name ) 



class productManager(models.Model):
    company_location=models.CharField(max_length=100,choices=SOURCE,blank=True,null=True)
    user_type=models.CharField(max_length=100,choices=USER_TYPE,blank=True,null=True)
    assign_to=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    module=models.CharField(max_length=100,choices=MODULE,blank=True,null=True)
    reg_no=models.ForeignKey(vehicleRegister,on_delete=models.CASCADE, blank=True)
    fuel=models.CharField(max_length=100,choices=FUEL_TYPE,blank=True,null=True)
    quantity=models.PositiveIntegerField(blank=True, null=True)
    rate=models.PositiveIntegerField(blank=True, null=True)
    amount=models.PositiveIntegerField(blank=True, null=True)
    Date=models.DateField(auto_now_add=True)
    comments=models.CharField(max_length=900,blank=True,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.module ) 

