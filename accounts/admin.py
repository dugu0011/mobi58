from django.contrib import admin
from .admin import *
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from .models import *
from import_export.admin import *
from import_export import resources

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')

admin.site.register(UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(HsnCode)
class HsnCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(RoleName)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name', 'description')


admin.site.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'pin', 'user_roles', 'user_mines', 'user_crushers', 'user_company', 'user_assign_company', 'name', 
                    'gender','birth_day', 'mobile', 'email', 'father_name', 'blood_group', 'pan_no', 
                    'pan_file', 'report_to', 'remark', 'status')
    list_filter = ('name', 'email')

admin.site.register(UserProfile, UserProfileAdmin)



class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'country', 'state', 'district', 'city')

admin.site.register(Address, AddressAdmin)

class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'country')

admin.site.register(State, StateAdmin)

class DistrictAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id', 'name', 'district_state')

admin.site.register(District, DistrictAdmin)

class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'city_district')

admin.site.register(City, CityAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'added_by', 'parent', 'company_type', 'mobile', 'email', 'pan_no', 'pan_file', 
                    'gst_no', 'gst_file',)
    list_filter = ('company_type', 'email')                

admin.site.register(Company, CompanyAdmin)

class BaseProductAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'customer_name', 'product_name', 'created_at', 'updated_at')
    list_filter = ('company_name', 'product_name')
admin.site.register(BaseProduct, BaseProductAdmin)


class ProductMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company_name', 'customer_name', 'item_name', 'sale_rate', 'bill_rate', 
    'comment', 'created_at', 'updated_at')
    list_filter = ('company_name', 'item_name')

admin.site.register(ProductMaster, ProductMasterAdmin)

class DriverMasterAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'vehicles', 'driver_name', 'license_no','aadhar_no', 'mobile',  'age', 'created_at', 'updated_at')
    list_filter = ('company_name', 'driver_name')                

admin.site.register(DriverMaster, DriverMasterAdmin)

class VehicleMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company_name', 'vehicle_no', 'vehicle_type', 'self_owner', 'customer_name', 'insurance_validity', 
    'insurance_file', 'pollution_validity', 'pollution_file', 'chassis_no', 'fuel_type', 'purchase_date', 
    'rc_no', 'rc_file', 'location', 'engine_no', 'created_at', 'updated_at')

admin.site.register(VehicleMaster, VehicleMasterAdmin)


class MineDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'mine_name', 'mine_id', 'lease_number', 'mineral_type', 'all_owner', 'kaata', 'coordinate_a', 'coordinate_b', 'coordinate_c', 'coordinate_d', 'created_at', 'updated_at')

admin.site.register(MineDetail, MineDetailAdmin)


class CrusherDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'crusher_name', 'crusher_id', 'lease_number', 'mineral_type', 'all_owner', 'kaata', 'coordinate_a', 'coordinate_b', 'coordinate_c', 'coordinate_d', 'created_at', 'updated_at')

admin.site.register(CrusherDetail, CrusherDetailAdmin)



class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'owner_name', 'percentage', 'company', 'mine_id', 'crusher_id', 'created_at', 'updated_at')

admin.site.register(Owner, OwnerAdmin)
