from django.contrib import admin
from mobi58.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.



class transporterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('transporter_name','mobile','email')
admin.site.register(Transporter,transporterAdmin)

class vehicleRegisterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('trransporter','owner_name')
admin.site.register(vehicleRegister,vehicleRegisterAdmin)

class driverAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('transporter_name','vehicle','driver_name')
admin.site.register(Driver,driverAdmin)


class addTripAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('transporter_name','vehicle','source','destination')
admin.site.register(addTrip,addTripAdmin)

admin.site.register(productManager)