from xml.sax.handler import all_properties
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import AddTransporterForm
from datetime import datetime
from datetime import date
from accounts.models import UserProfile
# Create your views here.


alltransporter=Transporter.objects.all()



expiry=vehicleRegister.objects.all()
for i in expiry:
    print(i.registered_upto)


today=date.today()
if expiry==today:
    print("dugu")

else:
    print("neeraj")







@login_required(login_url='/login/')
def addTransporter(request):
    trans=Transporter.objects.filter(is_active=True)
    user=request.user
    if request.method=="POST":
        transporter_name=request.POST.get('transporter_name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        address=request.POST.get('address')
        pan_no=request.POST.get('pan_no')
        pan_file=request.FILES.get('pan_file')
        gst_no=request.POST.get('gst_no')
        gst_file=request.FILES.get('gst_file')
        cin_no=request.POST.get('cin_no')
        cin_file=request.FILES.get('cin_file')
        trans_obj = Transporter(transporter_name=transporter_name, user=request.user, mobile=mobile,email=email,address=address,pan_no=pan_no,pan_file=pan_file,
        gst_no=gst_no,gst_file=gst_file,cin_no=cin_no,cin_file=cin_file)
        trans_obj.save()

    return render(request, 'web/jinja2/mobi58/alltransporter.html.j2',{'trans':trans})



@login_required(login_url='/login/')
def addVehicle(request):
    trans=vehicleRegister.objects.filter(is_active=True)
    veh=vehicleRegister.objects.all()
    user=request.user
    alltransporter1=Transporter.objects.all()
    if request.method=="POST":
        trransporter=request.POST.get('trransporter')
        registeration_no=request.POST.get('registeration_no')
        rc_file=request.FILES.get('rc_file')
        registeration_date=request.POST.get('registeration_date')
        registered_upto=request.POST.get('registered_upto')
        owner_name=request.POST.get('owner_name')
        vehicle_type=request.POST.get('vehicle_type')
        vehicle_model=request.POST.get('vehicle_model')
        vehicle_class=request.POST.get('vehicle_class')
        vehicle_color=request.POST.get('vehicle_color')
        engine_no=request.POST.get('engine_no')
        chasis_no=request.POST.get('chasis_no')
        rto_details=request.POST.get('rto_details')
        fuel_type=request.POST.get('fuel_type')
        insurance_validity=request.POST.get('insurance_validity')
        insurance_file=request.FILES.get('insurance_file')
        pollution_validity=request.POST.get('pollution_validity')
        pollution_file=request.FILES.get('pollution_file')

        trans_obj = vehicleRegister(trransporter=Transporter.objects.get(id=int(trransporter)), user=request.user, registeration_no=registeration_no,rc_file=rc_file,registeration_date=registeration_date,registered_upto=registered_upto,owner_name=owner_name,
        vehicle_type=vehicle_type,vehicle_model=vehicle_model,vehicle_class=vehicle_class,vehicle_color=vehicle_color,engine_no=engine_no,chasis_no=chasis_no,rto_details=rto_details,fuel_type=fuel_type,insurance_validity=insurance_validity,
        insurance_file=insurance_file,pollution_validity=pollution_validity,pollution_file=pollution_file)
        trans_obj.save()

    return render(request, 'web/jinja2/mobi58/vehicle_register.html.j2',{'alltransporter1':alltransporter1,'veh':veh,'trans':trans,'VEHICLE_TYPE':VEHICLE_TYPE,'FUEL_TYPE':FUEL_TYPE})



@login_required(login_url='/login/')
def addriver(request):
    trans=Driver.objects.filter(is_active=True)
    alltransporter1=Transporter.objects.all()
    allvehicle=vehicleRegister.objects.all()
    veh=Driver.objects.all()
    user=request.user
    if request.method=="POST":
        transporter_name=request.POST.get('transporter_name')
        vehicle=request.POST.get('vehicle')
        driver_name=request.POST.get('driver_name')
        mobile=request.POST.get('mobile')
        DOB=request.POST.get('DOB')
        license_no=request.POST.get('license_no')
        license_file=request.FILES.get('license_file')
        aadhar_no=request.POST.get('aadhar_no')
        aadhar_file=request.FILES.get('aadhar_file')
        address=request.POST.get('address')
        description=request.POST.get('description')

        trans_obj = Driver(transporter_name=Transporter.objects.get(id=int(transporter_name)), user=request.user, vehicle=vehicleRegister.objects.get(id=int(vehicle)),driver_name=driver_name,mobile=mobile,DOB=DOB,
        license_no=license_no,license_file=license_file,aadhar_no=aadhar_no,aadhar_file=aadhar_file,address=address,description=description,)
        trans_obj.save()

    return render(request, 'web/jinja2/mobi58/driver.html.j2',{'alltransporter1':alltransporter1,'veh':veh,'trans':trans,'allvehicle':allvehicle})

from .choices import *
@login_required(login_url='/login/')
def adtrip(request):
    ab=100
    alltrip=addTrip.objects.all()
    veh=vehicleRegister.objects.all()
    user=request.user
    alltransporter1=Transporter.objects.all()
    if request.method=="POST":
        transporter_name=request.POST.get('transporter_name')
        vehicle=request.POST.get('vehicle')
        source=request.POST.get('source')
        destination=request.POST.get('destination')
        approx_distance=request.POST.get('approx_distance')
        Fixed_amount_btw_s_d=request.POST.get('Fixed_amount_btw_s_d')

        addtrip_obj=addTrip(transporter_name=Transporter.objects.get(id=int(transporter_name)),vehicle=vehicleRegister.objects.get(id=str(vehicle)),source=source,destination=destination,approx_distance=approx_distance,
        Fixed_amount_btw_s_d=Fixed_amount_btw_s_d)
        addtrip_obj.save()

    return render(request, 'web/jinja2/mobi58/addtrip.html',{'alltransporter1':alltransporter1,'veh':veh,'SOURCE':SOURCE,'DESTINATION':DESTINATION,'ab':ab,'alltrip':alltrip})   



@login_required(login_url='/login/')
def proManager(request):
    veh=vehicleRegister.objects.all()
    allusers = UserProfile.objects.all()
    abab=productManager.objects.all()
    if request.method=="POST":
        company_location=request.POST.get('company_location')
        print(company_location)
        user_type=request.POST.get('user_type')
        print(user_type)
        assign_to=request.POST.get('assign_to')
        print(assign_to)
        module=request.POST.get('module')
        print(module)
        reg_no=request.POST.get('reg_no')
        print(reg_no)
        fuel=request.POST.get('fuel')
        print(fuel)
        quantity=request.POST.get('quantity')
        print(quantity)
        rate=request.POST.get('rate')
        print(rate)
        amount=request.POST.get('amount')
        print(amount)
        Date=request.POST.get('Date')
        print(Date)
        comment=request.POST.get('comment')
        print(comment)

        productManager_obj=productManager(company_location=company_location,user_type=user_type,assign_to=UserProfile.objects.get(id=str(assign_to)),module=module,
        reg_no=vehicleRegister.objects.get(id=int(10)),fuel=fuel,quantity=quantity,rate=rate,amount=amount,Date=Date,comments=comment)
        productManager_obj.save()

    return render(request, 'web/jinja2/mobi58/productManager.html',{'veh':veh,'SOURCE':SOURCE,'allusers':allusers,'FUEL_TYPE':FUEL_TYPE,'USER_TYPE':USER_TYPE,'MODULE':MODULE,'abab':abab})      

