import re
from .models import *
import datetime
import json
from django.core.exceptions import PermissionDenied

import calendar 
from django.db.models import Count , Q
from django.conf import settings
from urllib.request import urlopen
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from filer.models import Image as FilerImage
from django.core.files import File
from filer.models import Folder
from django.utils.text import slugify
import string
import random
import requests
import os
# from hr.models import Expense, LeaveRequest, LeaveReversal,EmployeeDetails





def get_context(request=None , **kwargs):
    # context = {}
    # return context
    try:
        type_msg = 'None'
        text = None
        if request.session.get("_message", None) is not None:
            msg = request.session.pop("_message")
            if msg.get("type") == "success" or msg.get("type") == "SUCCESS" or str(msg.get("type")) == "25":
                type_msg = "toastrsuccess"
            else:
                type_msg = "toastrerror"
            text = msg.get("text")
        
        kwargs.update({
                'title': '',
                type_msg : text ,
                'today':datetime.date.today(),
            })
    except:
        pass

    try:
        user = request.user.user_profile
        is_team_lead = UserProfile.objects.filter(report_to=user).exists()
        kwargs.update({
            'user_name':user.name,
            'user_type':user.user_type,
            'is_team_lead':is_team_lead,
            'profile' : user,
        })
        # if is_team_lead:
        #     expenses = Expense.objects.filter(employee__report_to=user,status='PD').count()
        #     leave_requests = LeaveRequest.objects.filter(requestee=user,status='PD').count()
        #     leave_reversals = LeaveReversal.objects.filter(employee__report_to=user,status='PD').count()
        #     kwargs.update({
        #         'expenses':expenses,
        #         'leave_requests':leave_requests,
        #         'leave_reversals' : leave_reversals,
        #     })

        # employee = EmployeeDetails.objects.filter(employee=user).first()
        # if employee:
        #     kwargs.update({
        #         'is_employee_verified' : employee.is_verified,
        #         'joined_date' : employee.joining_date,
        #     })

    except Exception as e:
        pass

    return kwargs

