from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission
from django.db.models.fields import CharField
from pkg_resources import resource_string
from .app_setting import *
from django_countries.fields import CountryField
from filer.fields.image import FilerImageField
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from jsonfield import JSONField
from django.db.models import Sum
from model_utils import FieldTracker

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token 
User = settings.AUTH_USER_MODEL


def validate_file_size(value):
    from django.core.exceptions import ValidationError
    filesize= value.size
    
    if filesize > 5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class State(Base):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=100, null=True)
    country = CountryField(null=True)

    def __str__(self):
        return self.name


class District(Base):
    name = models.CharField(max_length=150)
    district_state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="district_state")

    def __str__(self):
        return self.name


class City(Base):
    name = models.CharField(max_length=150)
    # city_state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="city_state")
    city_district = models.ForeignKey(District , on_delete=models.PROTECT , related_name="city_district",null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'



class UnitType(Base):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'UOM'
        verbose_name_plural = 'UOM'


class HsnCode(Base):
    name = models.CharField(max_length=200)
    percentage = models.DecimalField(max_digits=50, decimal_places=2, null=True,blank=True)
    # gst_no=models.DecimalField(max_length=50,null=True,blank=True , unique=True)
    gst_no = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    gst_file=models.FileField(upload_to="file/",blank=True,null=True, validators=[validate_file_size])

    def __str__(self):
        return f"{self.name}"

class RoleName(Base):
    role_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.role_name)

class Role(models.Model):
    CLIENT = 1
    HR = 2
    ADMIN = 3
    SUPERUSER = 4
    COMPANY1 = 5
    COMPANY2 = 6
    COMPANY3 = 7
    CUSTOMER = 8
    PRODUCT = 9
    VEHICLE = 10
    MINE = 11
    CRUSHER = 12
    OWNER = 13
    NEWUSER = 14
    MASTER = 15 
    MINE_TRANSACTION = 16
    CRUSHER_INBOUND = 17
    CRUSHER_OUTBOUND = 18
    SUBMASTER = 19
    MACHINE = 20
    DRIVER = 21
    EXPENSE = 22
    METERIAL_INWARD = 23
    INDATETIME = 24
    WB_OPERATOR = 25

    ROLE_CHOICES = ((MASTER,'master'),(SUBMASTER,'submaster'), (MINE_TRANSACTION,'mine_transaction'),
                    (CRUSHER_INBOUND,'crusher_inbound'),(CRUSHER_OUTBOUND,'crusher_outbound'),
                    (SUPERUSER,'superuser'), (ADMIN,'admin'),  (HR, 'hr'), (CLIENT,'client'), 
                    (COMPANY1,'company1'), (COMPANY2, 'company2'), (COMPANY3, 'company3'), 
                    (CUSTOMER, 'customer'), (PRODUCT, 'product'), (VEHICLE, 'vehicle'), 
                    (MINE, 'mine'), (CRUSHER, 'crusher'), (OWNER, 'owner'), (NEWUSER, 'newuser'),
                    (MACHINE,'machine'),(DRIVER, 'driver'), (EXPENSE, 'expense'),(METERIAL_INWARD,
                    'meterial_inward'),(INDATETIME,'indatetime'),(WB_OPERATOR,'wb_operator'))
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=15, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password, mobile, pin=None, **extra_fields):
        
        if not username:
            raise ValueError('User must have username')
        if not email:
            raise ValueError('User must have email address')
        
        user = self.model(
                        email=self.normalize_email(email), 
                        username=username,
                        mobile=mobile,
                        pin=pin,
                        password=password,
                        **extra_fields)
    
        user.set_password(password)
        user.save(using=self._db)
        return user    

    def create_superuser(self, email, username, mobile, password, **extra_fields):
        user = self.create_user(
                                email=self.normalize_email(email), 
                                password=password,
                                username=username,
                                mobile=mobile, 
                                **extra_fields
                                )  
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, null=True, blank=True, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=20,default=None,null=True, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now_add=True)

    is_admin =  models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)        
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user_role = models.ManyToManyField(Role, related_name='multiple_role')
    company = models.ManyToManyField('Company', null=True, blank=True, related_name="company_user")
    assign_company = models.ManyToManyField('Company', blank=True, null=True)
    name = models.CharField(max_length=100,null = True,)
    gender = models.CharField(choices=GENDER_TYPES, max_length=30, null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    father_name = models.CharField(max_length=100,null = True, blank=True)
    blood_group = models.CharField(max_length=3,choices=BLODD_GROUP_CHOICE, null = True, blank=True)
    pan_no = models.CharField(max_length=50, null=True, blank=True)
    pan_file = models.FileField(upload_to="file/", blank=True, null=True, validators=[validate_file_size])
    report_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True, related_name="report_to_user")
    remark = models.TextField(max_length=2000, null=True, blank=True)
    address = models.ManyToManyField('Address')
    status = models.CharField(max_length=200, choices=STATUS_TYPE, default='Submitted')
    leaves = JSONField(null=True, blank=True)
    pin = models.CharField(max_length=4, null=True, blank=True)
    otp = models.CharField(max_length=10,null=True,blank=True)
    mines = models.ManyToManyField('MineDetail', related_name='multiple_mines', blank=True)
    crusher = models.ManyToManyField('CrusherDetail', related_name='multiple_crushers', blank=True)
    myuser = models.BooleanField(default=False) # if True customer user exist
    #tracker = FieldTracker(fields=['user', 'email'])
    #image = FilerImageField(null=True, related_name='user_images', on_delete=models.CASCADE)

    objects = MyAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','mobile']

    # def __str__(self):
    #     return self.email

    def __str__(self):
        try:
            return str(self.email)
        except:
            return "-"    

    # def _user_get_permissions(user, obj, from_name):
    #     permissions = set()
    #     name = 'get_%s_permissions' % from_name
    #     for backend in auth.get_backends():
    #         if hasattr(backend, name):
    #             permissions.update(getattr(backend, name)(user, obj))
    #     return permissions

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def user_roles(self):
        return " | ".join([str(u) for u in self.user_role.all()])
    
    def user_company(self):
        return " | ".join([str(c) for c in self.company.all()])

    def user_assign_company(self):
        return " | ".join([str(ac) for ac in self.assign_company.all()])    
    
    def user_mines(self):
        return " | ".join([str(m) for m in self.mines.all()])

    def user_crushers(self):
        return " | ".join([str(c) for c in self.crusher.all()])    

    def add_address(self, *args, **kwargs):
        data = {
           'address':kwargs.get('address')[0],
           'country':kwargs.get('country')[0],
           'state_id':kwargs.get('state')[0],
           'district_id':kwargs.get('district')[0],
           'city_id':kwargs.get('customer-city')[0],
           'pincode':kwargs.get('pincode')[0],
        }
        if 'address_id' in kwargs:
            address = Address.objects.filter(id=kwargs.get('address_id')[0]).update(**data)
        else:
            address = Address.objects.create(**data)
            self.address.set([address])

@receiver (post_save, sender=settings.AUTH_USER_MODEL) 
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class NewCustomer(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True, related_name="parent_customer")
    # customer_name = models.CharField(max_length=200,unique=True)
    # mobile = models.CharField(max_length=20,blank=True,null=True , unique=True)
    company_name = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='company_newcustomer', null=True, blank=True)
    customer_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20,blank=True,null=True)
    customer_type = models.CharField(max_length=50,choices=COMPANY_TYPE,null=True)
    customer_category = models.CharField(max_length=50,choices=COMPANY_TYPE,null=True)
    kaata_no = models.CharField(max_length=50, blank=True, null=True)
    pan_no=models.CharField(max_length=50,null=True,blank=True)
    pan_file=models.FileField(upload_to="file/",blank=True,null=True, validators=[validate_file_size])
    email=models.EmailField(max_length=150,null=True,blank=True)
    #gst_no=models.CharField(max_length=50,null=True,blank=True , unique=True)
    gst_no=models.CharField(max_length=50,null=True,blank=True)
    gst_file=models.FileField(upload_to="file/",blank=True,null=True, validators=[validate_file_size])
    cin_no=models.CharField(max_length=50,null=True,blank=True)
    cin_file=models.FileField(upload_to="file/",blank=True,null=True, validators=[validate_file_size])
    credit_limit = models.CharField(max_length=50,null=True , blank=True)
    project_status = models.CharField(choices=PROJECT_STATUS , null=True , blank=True ,max_length=20)
    customer_mine = models.ManyToManyField('CustomerMine', blank=True)
    customer_address = models.ManyToManyField('Address', blank=True)
    remark = models.TextField(max_length=2000 ,null=True , blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="user_added_by")
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.customer_name)

    def customer_mines(self):
        return " | ".join([str(cm) for cm in self.customer_mine.all()])    
    
    def user_mines(self):
        return " | ".join([str(m) for m in self.mines.all()])    

    def add_customer_mine(self, *args, **kwargs):
        data = {
           'mine':kwargs.get('mine_name')[0],
           'mine_no':kwargs.get('mine_no')[0],
        }
        if 'address_id' in kwargs:
            cust_mine = CustomerMine.objects.filter(id=kwargs.get('customermine_id')[0]).update(**data)
        else:
            cust_mine = CustomerMine.objects.create(**data)
            self.cust_mine.set([cust_mine])            




class MyUser(models.Model):
    parent = models.ForeignKey('UserProfile', on_delete=models.CASCADE, null=True,blank=True, related_name="parent_myuser")
    company_name = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, related_name="myuser_company")
    name=models.CharField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=20,blank=True,null=True , unique=True)
    email=models.EmailField(max_length=150,null=True,blank=True)
    password=models.CharField(max_length=150,null=True,blank=True)
    mobile=models.CharField(max_length=150,null=True,blank=True)
    gender = models.CharField(max_length=20,blank=True,null=True)
    added_by = models.ForeignKey('UserProfile', on_delete=models.CASCADE,null=True, related_name="myuser_added_by")
    remark = models.TextField(max_length=2000 ,null=True , blank=True)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return str(self.username)    


class Company(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True, related_name="parent_company")
    name=models.CharField(max_length=200,unique=True)
    sort_name=models.CharField(max_length=50,null=True,blank=True)
    mobile = models.CharField(max_length=20,blank=True,null=True , unique=True)
    company_type = models.CharField(max_length=50,choices=COMPANY_TYPE,null=True)
    pan_no=models.CharField(max_length=50,null=True,blank=True)
    pan_file=models.FileField(upload_to="file/",blank=True,null=True, validators=[validate_file_size])
    email=models.EmailField(max_length=150,null=True,blank=True)
    # contact_no=models.CharField(max_length=20,blank=True,null=True)
    # contact_person=models.CharField(max_length=200 ,null=True)
    address = models.ManyToManyField('Address')
    contact_details = models.ManyToManyField('ContactDetail', blank=True, related_name="contact_to")
    gst_no=models.CharField(max_length=50,null=True,blank=True , unique=True)
    gst_file=models.FileField(upload_to="file/",blank=True,null=True, validators=[validate_file_size])
    msme =models.BooleanField(default=False)
    msme_file=models.FileField(upload_to="file/",blank=True,null=True, validators=[validate_file_size])
    cin_no=models.CharField(max_length=50,null=True,blank=True)
    cin_file=models.FileField(upload_to="file/",blank=True,null=True, validators=[validate_file_size])
    credit_limit = models.CharField(max_length=50,null=True , blank=True)
    project_status = models.CharField(choices=PROJECT_STATUS , null=True , blank=True ,max_length=20)
    remark = models.TextField(max_length=2000 ,null=True , blank=True)
    #products = models.ManyToManyField('Product' ,null=True,blank=True)
    source_company = models.BooleanField(default=False, null=True, blank=True)
    sale_category = models.CharField(max_length=50,choices=SALES_CATEGORY_TYPE,null=True)
    added_by = models.ForeignKey('UserProfile', on_delete=models.CASCADE,null=True, related_name="customer_added_by")
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="company_user")
    inhouse_use = models.BooleanField(default=False)

    sale_prefix = models.CharField(max_length=50 ,null=True , blank=True)
    purchase_prefix = models.CharField(max_length=50 ,null=True , blank=True)
    
    sale_transaction_no = models.CharField(max_length=50 ,null=True , blank=True)
    purchases_transaction_no = models.CharField(max_length=50 ,null=True , blank=True)
    
    prefix_invoice_no = models.CharField(max_length=50 ,null=True , blank=True)
    is_autoinvoice_no = models.BooleanField(default=True)

    is_dynamic = models.BooleanField(default=False)
    is_master = models.BooleanField(default=True)
    is_submaster = models.BooleanField(default=True)
    is_mine_transaction = models.BooleanField(default=True)
    is_crusher_inbound = models.BooleanField(default=True)
    is_crusher_outbound = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

            
class Address(Base):
    address = models.TextField(max_length=500,null=True,blank=True)
    country = CountryField(null=True)
    state = models.ForeignKey('State', on_delete=models.CASCADE, null=True, related_name="company_state")
    district = models.ForeignKey('District', on_delete=models.CASCADE, null=True, related_name="company_district")
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True, related_name="company_city")
    latitude = models.DecimalField(max_digits=20, decimal_places=5, default=0.00000)
    longitude = models.DecimalField(max_digits=20, decimal_places=5, default=0.00000)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    is_shipping_address = models.BooleanField(default=False)
    is_billing_address = models.BooleanField(default=False)
    address_type = models.CharField(choices=ADDRESS_TYPE, max_length=300, null=True, blank=True)


    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
    
    def get_full_address(self):
        try:
            return self.address+','+self.city.name+','+self.state.name+","+str(self.country.name)+','+self.pincode
        except :
            return ''


class Category(Base):
    name = models.CharField(max_length=150,)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class ContactDetail(Base):
    name = models.CharField(max_length=150,)
    designation = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=150,)
    company = models.ForeignKey(Company , on_delete=models.CASCADE , null=True, related_name="contact")

    def __str__(self):
        return f"{self.name}"


class AdminDetails(Base):
    mobile=models.CharField(max_length=20, null=True, blank=True)
    email=models.EmailField(max_length=100, null=True, blank=True)
    trigger_type = models.CharField(max_length=50,choices=TRIGGER_TYPE, default='customer')

    def __str__(self):
        return f"{self.trigger_type}" 

    class Meta:
        verbose_name = 'Admin Details'
        verbose_name_plural = 'Admin Details'
















PRODUCT_CATEGORY = (('Boulder', 'Boulder'), ('10MM', '10MM'),('20MM', '20MM'),('DUST', 'DUST'))
CM_CATEGORY = (('crusher', 'Crusher'), ('mines', 'Mines'))
VEHICLE_TYPE = (('camel_cart', 'Camel Cart'),('pickup', 'Pick Up'),('tractor', 'Tractor'),('truck 6 tyres', 'Truck 6 Tyres'), 
('truck 10 tyres', 'Truck 10 Tyres'), ('truck 12 tyres', 'Truck 12 Tyres'), 
('truck 14 tyres', 'Truck 14 Tyres'), ('truck 16 tyres', 'Truck 16 Tyres'),
('truck 18 tyres', 'Truck 18 Tyres'), ('truck 20 tyres', 'Truck 20 Tyres'),
('truck 22 tyres', 'Truck 22 Tyres'), ('truck 24 tyres', 'Truck 24 Tyres'),
('trailer', 'Trailer'))
FUEL_TYPE = (('deisel', 'Diesel'), ('petrol', 'Petrol'),('cng', 'CNG'),('electric', 'Electric'))

class BaseProduct(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="user_product_base")
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_product_base', null=True, blank=True)
    customer_name = models.ForeignKey(NewCustomer, on_delete=models.CASCADE, related_name='customer_product_basbe', null=True, blank=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.product_name)

class ProductMaster(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="user_products_master")
    product_category = models.ForeignKey(BaseProduct, on_delete=models.CASCADE, related_name="category_products_master", blank=True, null=True)
    crusher_mine = models.CharField(max_length=100, choices=CM_CATEGORY, blank=True, null=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_products', null=True, blank=True)
    customer_name = models.ForeignKey(NewCustomer, on_delete=models.CASCADE, related_name='customer_products', null=True, blank=True)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    sale_rate = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    bill_rate = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    gst_percent = models.CharField(max_length=255, blank=True, null=True)
    sale_royalty_charges = models.CharField(max_length=50, null=True, blank=True)
    bill_royalty_charges = models.CharField(max_length=50, null=True, blank=True)
    base_sale_rate = models.CharField(max_length=50, null=True, blank=True)
    base_bill_rate = models.CharField(max_length=50, null=True, blank=True)
    unit_type = models.ForeignKey(UnitType, related_name="product_unit", on_delete=models.CASCADE, verbose_name="UOM", null=True, blank=True)
    hsn_code = models.ForeignKey('HsnCode', on_delete=models.CASCADE,null=True, related_name="product_hsn_code")
    comment = models.TextField(null=True, blank=True)
    is_gst = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.item_name)

class DriverMaster(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="user_driver_master")
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_driver', null=True, blank=True)
    customer_name = models.ForeignKey(NewCustomer, on_delete=models.CASCADE, related_name='customer_driver', null=True, blank=True)
    vehicle = models.ManyToManyField('VehicleMaster', blank=True)
    driver_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    license_no = models.CharField(max_length=50, null=True, blank=True)
    license_file = models.FileField(upload_to="file/dl/", blank=True, null=True, validators=[validate_file_size])
    aadhar_no = models.CharField(max_length=50, null=True, blank=True)
    aadhar_file = models.FileField(upload_to="file/aadhar/", blank=True, null=True, validators=[validate_file_size])
    address = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.driver_name)

    def vehicles(self):
        return " | ".join([str(vm) for vm in self.vehicle.all()])


class VehicleMaster(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="user_vehicles_master")
    vehicle_no = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    driver_name = models.ManyToManyField(DriverMaster, blank=True)
    vehicle_type = models.CharField(max_length=200, choices=VEHICLE_TYPE, null=True, blank=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companys_master', null=True, blank=True)
    customer_name = models.ForeignKey(NewCustomer, on_delete=models.CASCADE, related_name='customer_vehicle', null=True, blank=True)
    insurance_validity = models.CharField(max_length=100, null=True, blank=True)
    insurance_file = models.FileField(upload_to="file/", blank=True, null=True, validators=[validate_file_size])
    pollution_validity = models.CharField(max_length=100,null=True, blank=True)
    pollution_file = models.FileField(upload_to="file/", blank=True, null=True, validators=[validate_file_size])
    chassis_no = models.CharField(max_length=255, null=True, blank=True)
    engine_no = models.CharField(max_length=255, null=True, blank=True)
    fuel_type = models.CharField(max_length=200, choices=FUEL_TYPE, default='deisel')
    purchase_date = models.CharField(max_length=100, null=True, blank=True)
    rc_no = models.CharField(max_length=255, null=True, blank=True)
    rc_file = models.FileField(upload_to="file/", blank=True, null=True, validators=[validate_file_size])
    location = models.TextField(null=True, blank=True)
    assigned_to = models.CharField(max_length=255, null=True, blank=True)
    self_owner = models.BooleanField(default=False) # select for internal and external vehicle
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return str(self.vehicle_no)


    

sequence_number = 1000
def mine_unique_id():
    global sequence_number
    sequence_number += 1
    unique_id = "cmp_" + str(sequence_number)
    return unique_id

class MineDetail(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="user_mines_detail")
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_mines_detail', null=True, blank=True)
    customer_name = models.ManyToManyField(NewCustomer, blank=True)
    mine_name = models.CharField(max_length=255, null=True, blank=True)
    mine_id = models.CharField(max_length=255, null=True, blank=True, default=mine_unique_id)
    lease_number = models.CharField(max_length=255, null=True, blank=True)
    mineral_type = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ManyToManyField('Owner', blank=True)
    address = models.TextField(null=True, blank=True)
    coordinate_a = models.CharField(max_length=255, null=True, blank=True)
    coordinate_b = models.CharField(max_length=255, null=True, blank=True)
    coordinate_c = models.CharField(max_length=255, null=True, blank=True)
    coordinate_d = models.CharField(max_length=255, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    na = models.BooleanField(default=True) 

    def __str__(self):
        return str(self.mine_name)

    def kaata(self):
        return " | ".join([str(ct) for ct in self.customer_name.all()])   

    def all_owner(self):
        return " | ".join([str(own) for own in self.owner.all()])     

    def add_owner(self, *args, **kwargs):
        data = {
           'owner':kwargs.get('owner_name')[0],
           'percentage':kwargs.get('percentage')[0],
        }
        if 'address_id' in kwargs:
            owner = Owner.objects.filter(id=kwargs.get('owner_id')[0]).update(**data)
        else:
            owner = Owner.objects.create(**data)
            self.owner.set([owner])


sequence_number = 1000
def crusher_unique_id():
    global sequence_number
    sequence_number += 1
    unique_id = "cmp_" + str(sequence_number)
    return unique_id

class CrusherDetail(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="user_crushers_detail")
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_crushers_detail', null=True, blank=True)
    customer_name = models.ManyToManyField(NewCustomer, blank=True)
    crusher_name = models.CharField(max_length=255, null=True, blank=True)
    crusher_id = models.CharField(max_length=255, null=True, blank=True, default=crusher_unique_id())
    lease_number = models.CharField(max_length=255, null=True, blank=True)
    mineral_type = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ManyToManyField('Owner', blank=True)
    address = models.TextField(null=True, blank=True)
    coordinate_a = models.CharField(max_length=255, null=True, blank=True)
    coordinate_b = models.CharField(max_length=255, null=True, blank=True)
    coordinate_c = models.CharField(max_length=255, null=True, blank=True)
    coordinate_d = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    na = models.BooleanField(default=True)

    def __str__(self):
        return str(self.crusher_name)

    def kaata(self):
        return " | ".join([str(ct) for ct in self.customer_name.all()])

    def all_owner(self):
        return " | ".join([str(own) for own in self.owner.all()])        
    
    def add_owner(self, *args, **kwargs):
        data = {
           'owner':kwargs.get('owner_name')[0],
           'percentage':kwargs.get('percentage')[0],
        }
        if 'address_id' in kwargs:
            owner = Owner.objects.filter(id=kwargs.get('owner_id')[0]).update(**data)
        else:
            owner = Owner.objects.create(**data)
            self.owner.set([owner])


class Owner(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="user_owners")
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    percentage = models.CharField(max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='owner_companys')
    customer_name = models.ForeignKey(NewCustomer, on_delete=models.CASCADE, related_name='customer_owner', null=True, blank=True)
    mine_id = models.ForeignKey(MineDetail, on_delete=models.CASCADE, null=True, blank=True, related_name='owner_mines')
    crusher_id = models.ForeignKey(CrusherDetail, on_delete=models.CASCADE, null=True, blank=True, related_name='owner_crusher')
    address = models.TextField(null=True, blank=True)
    def __str__(self):
        return str(self.owner_name)


class CustomerMine(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="user_customermine")
    customer_name = models.ForeignKey(NewCustomer, on_delete=models.CASCADE, null=True,  related_name="new_customermine")
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=True,  related_name="company_customermine")
    mine_name = models.CharField(max_length=50, null=True, blank=True)
    mine_no = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.mine_name)       


class MineralType(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="user_mineral")
    name=models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class PowerFactor(Base):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    kvah=models.CharField(blank=True, max_length=20, null=True)
    kwh= models.CharField(blank=True, max_length=20, null=True)
    netkvah= models.CharField(blank=True, max_length=20, null=True)
    netkwh=models.CharField(blank=True, max_length=20, null=True)
    lockkvah= models.CharField(blank=True, max_length=20, null=True)
    lockkwh= models.CharField(blank=True, max_length=20, null=True)
    power= models.CharField(blank=True, max_length=20, null=True)
    dailykwh= models.CharField(blank=True, max_length=20, null=True)
    dailykvah= models.CharField(blank=True, max_length=20, null=True)
    dailypower= models.CharField(blank=True, max_length=20, null=True)
    added_by=models.ForeignKey(null=True, on_delete=models.CASCADE, related_name='power_added_by', to=settings.AUTH_USER_MODEL)
    company_name= models.ForeignKey(null=True, on_delete=models.CASCADE, related_name='power_company', to='accounts.Company')