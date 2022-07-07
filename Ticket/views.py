from imghdr import what
from re import T
from urllib import request
from django.http import JsonResponse, Http404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from pyrsistent import T
from .service import tkt_id
from accounts.models import UserProfile
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timezone,timedelta
import time
from time import gmtime, strftime
import datetime
from django.db.models import Q
from django.shortcuts import redirect
User = settings.AUTH_USER_MODEL

from django.core.mail import send_mail
from datetime import datetime, time


# Create your views here.

users = UserProfile.objects.filter(is_admin = True)



@login_required(login_url='/login/')
def raiseTicket(request):
    user = request.user
    userid = user
    msg = ""
    myTicket = RaiseTicket.objects.filter(user=request.user, is_active=True)
    # print(user)
    is_raise_ticket='YES'
    if request.method == "POST":
        ticket = RaiseTicketForm(request.POST, request.FILES)

        if ticket.is_valid():
            instance = ticket.save(commit=False)
            instance.user = request.user
            # instance.ticket_id=tkt_id
            txnid = tkt_id(is_raise_ticket,request.user)
            instance.ticket_id=txnid
            instance.save() 
            
            
            return HttpResponseRedirect('/')
            msg = "Thank you for raising a ticket"

            
    else:
        print("something went")
        ticket = RaiseTicketForm()
    return render(request, 'web/jinja2/ticket_raise/ticket_raise.html.j2', {'user': user, 'msg': msg, 'ticket': ticket, 'myTicket': myTicket})
    # except Exception as e:
    #    return JsonResponse({'error': 'error'}, status=400)



@login_required(login_url='/login/')

def viewRaiseTicket(request, id):
    print('hello')
    user = request.user
    admin_list = []
    users = UserProfile.objects.filter(is_admin = True)
    try:
        isadmin = UserProfile.objects.get(is_admin = True, email=request.user.email)
        isadmin = isadmin.is_admin
    except Exception as e:
        isadmin = False
        print(e)
    for admin in users:
        admin_list.append(admin.id)
    msg = ""
    subject=RaiseTicket.objects.filter(subject='subject')

    ticket = RaiseTicket.objects.get(id=id)

    admin_user = request.user.is_admin = True
    print(admin_user,8888)
    try:
        myComment = Comment.objects.filter(Q(user=ticket.assign_to.id) |Q(user=ticket.user.id) | Q(user__in=admin_list), ticket = ticket.id)
    except:
        myComment = Comment.objects.filter(Q(user=ticket.user.id) | Q(user__in=admin_list), ticket = ticket.id)
    # for i in myComment:
    #     print(i.user,00000000)
    allusers = UserProfile.objects.all()

    if request.method == "POST" and "assignForm":
        assign_to = request.POST.get('assign_to')
        status_type = request.POST.get('status_type')
        s_id = request.POST.get('s_id')
        try:
            if assign_to:
                

                assigned_at = datetime.now()
                RaiseTicket.objects.filter(id=id).update(assign_to=assign_to, assigned_date=assigned_at)
            

        except Exception as e:
            print(e)

        # try: 
   
        if status_type:
            
            print('hello3333333')
            st=RaiseTicket.objects.get(id=int(s_id))#.update(status=status_type)
            st.status = status_type
            st.save()
            
            print(st.status,676767)
            return HttpResponseRedirect('/')

        # except Exception as e:
        #     print(e)        
                

    if request.method == "POST" and "commentForm":
        ticket_id = request.POST.get('ticket')
        message = request.POST.get('message')
        cmt_obj = Comment(message=message, user=request.user, ticket=RaiseTicket.objects.get(id=ticket_id))
        cmt_obj.save()





    # myComment=Comment.objects.filter()    
    # if request.method == "POST":
    #     data = {key:request.POST[key].strip() for key in request.POST if not key == "csrfmiddlewaretoken"}
    #     print(data)
    #     ticket = RaiseTicket.objects.get(id=id)
    #     ticket.admin_response = data.get("admin_response","")
    #     if data["aprove"] == 'aproved':
    #         ticket.is_aprove = True
    #     else:
    #         ticket.is_aprove = False
    #     ticket.accepted = True
    #     ticket.updated = datetime.now()
    #     ticket.save()
    # else:
    #     pass

    # myComment = Comment.objects.filter((Q(is_active=True) & Q(user=ticket.user)) | (Q(user=admin_user) & Q(is_active=True)))



    return render(request, 'web/jinja2/ticket_raise/viewRaiseTicket.html.j2', {'comments':myComment, 'user': user, 'ticket': ticket, 'allusers': allusers,'STATUS_TYPE':STATUS_TYPE,'users':isadmin})
    # except Exception as e:
    #     return JsonResponse({'error': 'error'}, status=400)


@login_required(login_url='/login/')
def viewall(request):
    
    if request.user.is_admin == True:
        myTicket = RaiseTicket.objects.filter(is_active=True).order_by('created')[::-1]
    else:
        myTicket = RaiseTicket.objects.filter(
            user=request.user, is_active=True).order_by('-subject')
    ticket = RaiseTicketForm()

    return render(request, 'web/jinja2/ticket_raise/viewTicket.html.j2', {'ticket': ticket, 'myTicket': myTicket })


@login_required(login_url='/login/')
def assignme(request):
    

    if request.user.is_admin == True:
        myTicket = RaiseTicket.objects.filter(is_active=True)
    else:
        myTicket = RaiseTicket.objects.filter(
            assign_to=request.user, is_active=True)
    ticket = RaiseTicketForm()

    return render(request, 'web/jinja2/ticket_raise/viewTicket.html.j2', {'ticket': ticket, 'myTicket': myTicket})

# @login_required(login_url='/login/')
# def comment(request):
#     print('hello')
#     user = request.user
#     myComment = Comment.objects.filter(user=request.user, is_active=True)
#     print(myComment,878845)
#     if request.method == "POST":
#         name= request.POST.get('name')
#         print(name,898)
#         message= request.POST.get('message')
#         print(message,88888)
#         cmt_obj = Comment(name=name, message=message, user=request.user)
#         cmt_obj.save()
#     return render(request,'web/jinja2/ticket_raise/viewRaiseTicket.html.j2',{'myComment':myComment})





@login_required(login_url='/login/')
def masterui(request):
    user = request.user

    auto_scheduled_week_month = Automation.objects.filter(is_active=True)
    print(auto_scheduled_week_month,89898989898)
    auto_scheduled_weekly = Automation.objects.filter(is_active=True,time_period='Weekly')
    auto_scheduled_monthly = Automation.objects.filter(is_active=True,time_period='Monthly')
    print(auto_scheduled_monthly,7878)
    # date = datetime.datetime.today()
    week = datetime.today().isoweekday() ==1 
    month_day = datetime.today().day == 1
    # print(week, 9090)

    # print(week,9898)
    # auto_scheduled = Automation.objects.filter(time_period='Weekly')
    if week==True and month_day==False:

        for asw in auto_scheduled_weekly:
            sub=asw.subject
            message=asw.msg
            send_mail(
                
                sub,
                message,
                "please check you have assign a ticket"
                'no-reply@tech58.in',
                [UserProfile.objects.get(email=asw.assign_to.email)],
                fail_silently=False,
                


        
    )

            
            auto_assigned = RaiseTicket.objects.create(subject=asw.subject, msg=asw.msg, assign_to=UserProfile.objects.get(id=int(asw.assign_to.id)),
                                                    time_period=asw.time_period, user=request.user)
            print(auto_assigned)
            print("Running")
            Automation.objects.filter(is_active=True).update(is_active=False)
            print("Success")
    elif month_day==True and week==False:
        for asm in auto_scheduled_monthly:
            sub=asm.subject
            message=asm.msg
            send_mail(
                
                sub,
                message,
                "please check you have assign a ticket"
                'no-reply@tech58.in',
                [UserProfile.objects.get(email=asm.assign_to.email)],
                fail_silently=False

        
    )
            auto_assigned = RaiseTicket.objects.create(subject=asm.subject, msg=asm.msg, assign_to=UserProfile.objects.get(id=int(asm.assign_to.id)),
                                                    time_period=asm.time_period, user=request.user)
            print(auto_assigned)
            print("Running")
            Automation.objects.filter(is_active=True).update(is_active=False)
            print("Success")
            
    elif (month_day and week)==True:
        for aswm in auto_scheduled_week_month:
            sub=aswm.subject
            message=aswm.msg
            send_mail(
                
                sub,
                message,
                "please check you have assign a ticket"
                'no-reply@tech58.in',
                [UserProfile.objects.get(email=aswm.assign_to.email)],
                fail_silently=False

        
    )
            auto_assigned = RaiseTicket.objects.create(subject=aswm.subject, msg=aswm.msg, assign_to=UserProfile.objects.get(id=int(aswm.assign_to.id)),
                                                    time_period=aswm.time_period, user=request.user)
            print(auto_assigned)
            print("Running")
            Automation.objects.filter(is_active=True).update(is_active=False)
            print("Success")


    

    request.session["_message"] = {
        'type': messages.SUCCESS, 'text': 'Yeah! Tasks has been assigned successfully.'}

    return HttpResponseRedirect('/')



    