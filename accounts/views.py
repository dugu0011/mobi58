from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login as auth_login , authenticate
from django.utils.translation import activate
from Ticket.models import RaiseTicket

from Ticket.forms import RaiseTicketForm
from .models import *

from .utils import *
# from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import Http404
from django.db.models import Q
from django_countries import countries
from django.contrib import messages
from django.db.models import Sum, Count
from datetime import timedelta , datetime
from django.utils import timezone
import string
import json
#from .serializers import *
from django.shortcuts import get_object_or_404

from django.conf import settings
User = settings.AUTH_USER_MODEL





@login_required(login_url='/login/')
def indexView(request , **kwargs):
    context = get_context(request , **kwargs)
    get_company=request.GET.get('company')
    print(get_company)
    own_roles = []
    obj1 = None
    try:
        UserProfile.objects.get(email=request.user, is_superuser=True)
    except:
        print("Data Not found!")
    try:    
        obj = UserProfile.objects.get(email=request.user)#, is_verified=True)
        own_roles = obj.user_role.all()
        own_roles = [i.get_id_display() for i in own_roles]
    except:
        print("Sorry! You don't have any Role.")
    all_company = []
    company = Company.objects.filter(added_by=request.user)
    for c in company:
        all_company.append(c.id)
    # total_mines = MineTransaction.objects.filter(company_name=get_company,moved_to_crusher=True, is_active=True).count()
    total_ticket = RaiseTicket.objects.filter(user=request.user).count()
    all_ticket = RaiseTicket.objects.filter(is_active=True).count()
    assign_me = RaiseTicket.objects.filter(assign_to=request.user,is_active=True).count()
    notification = RaiseTicket.objects.filter(assign_to=request.user,is_active=True)
    myTickets_all = RaiseTicket.objects.filter(is_active=True).order_by('created')[::-1]
    myTicket = RaiseTicket.objects.filter(
        user=request.user, is_active=True).order_by('created')[::-1]
    myTickets = RaiseTicket.objects.filter(
        assign_to=request.user, is_active=True).order_by('created')[::-1]
    

    ticket = RaiseTicketForm()



    user = request.user
    # try:
    # user = User.objects.get(id=request.user.id)
    # print(user,87845)
    msg = ""
    myTicket1 = RaiseTicket.objects.filter(user=request.user, is_active=True)
    # print(user)
    if request.method == "POST":
        ticket = RaiseTicketForm(request.POST, request.FILES)

        if ticket.is_valid():
            instance = ticket.save(commit=False)
            instance.user = request.user
            # instance.ticket_id=tkt_id
            instance.save()
            msg = "Thank you for raising a ticket"
            return HttpResponseRedirect('')
    else:
        print("something went")
        ticket = RaiseTicketForm()




    return render(request, 'web/jinja2/mobi58/alltransporter.html.j2', {'own_roles': own_roles, 'assign_me':assign_me, 
                                                        'company':company,'total_ticket':total_ticket,'notification':notification,
                                                        'myTicket':myTicket, 'myTickets':myTickets,'ticket':ticket,'user': user, 'msg': msg,'all_ticket':all_ticket,'myTickets_all':myTickets_all})


def signup_view(request, **kwargs):
    """View for Registration """
    if request.user and request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        birth_day = request.POST.get('birth_day')
        mobile = request.POST.get('customer-mobile')
        email = request.POST.get('customer-email')
        father_name = request.POST.get('father')
        password = request.POST.get('password')    
        email = email.lower()

        u = UserProfile.objects.filter(Q(email=email)| Q(username=username))
        if u:
            return HttpResponseRedirect("/login/")
        else:
        #     user = UserProfile.objects.create_user(username=username, email=email, password=password)
        # user.is_active = True
        # user.save()
            user_roles = [15,]  
            userprofile = UserProfile.objects.create_user(username=username, email=email, password=password, name=name, gender=gender, 
                                        birth_day=birth_day, mobile=mobile, father_name=father_name, 
                                        is_superuser=True)
            userprofile.save()
            
            userprofile.user_role.set(user_roles)
            userprofile.save()
        # msg = '<h4>YOUR ACCOUNT WILL BE ACTIVATE WITHIN 24 HOURS.</h4><a href="/">Home</a>'
        # return HttpResponse(msg)
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return HttpResponseRedirect('/')  
    else:
        return render(request, 'web/jinja2/signup.html.j2')


def login_view(request, **kwargs):
    """ View to handle login for user  """
    if request.user and request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        u = None
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            u = UserProfile.objects.get(username=username)
        except:
            try:
                u = UserProfile.objects.get(email=username)
            except:
                return HttpResponseRedirect('/login/')    
        
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
        return HttpResponseRedirect('/')        
    else:
        return render(request, 'web/jinja2/login.html.j2')


def forgot_password(request,**kwargs):
    """
    Function for forgot password
    """
    return render(request, "web/jinja2/forgot-password.html.j2")


def reset_password(request,**kwargs):
    """
    Function for reset password
    """
    user_id = request.session.get('reset_password_user')
    if user_id:
        context = get_context(request , **kwargs)
        if request.POST:
            data = request.POST
            password = data.get('password')
            if password and len(password) >7:
                user = User.objects.get(id=int(user_id))
                user.set_password(password)
                user.save()
                del request.session['reset_password_user']
                request.session["_message"] = {
                    'type': messages.SUCCESS, 'text': 'Password reset successfully.'}
                return redirect('login')
            else:
                request.session["_message"] = {
                    'type': messages.ERROR, 'text': 'Password must be minimum length of 8.'}
                return redirect('reset-password')

        return render(request, "web/jinja2/reset-password.html.j2", context)
    else:
        raise Http404


def logout(request):
    auth.logout(request)
    request.session["_message"] = {
                        'type': messages.SUCCESS, 'text': 'Logged out successfully.'}
    # messages.success(request, 'Logged out successfully.')
    return redirect('/')