from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.contrib.humanize.templatetags.humanize import naturaltime as django_naturaltime
import datetime
#from core.models import *
from django.conf import settings
from django.apps import apps
import os
import base64
from django_middleware_global_request.middleware import get_request
from django.utils import timezone


def naturaltime(value):
    """return the human readable time format"""
    return django_naturaltime(value)


def convert_to_list(value):
    if value:
        return list(map(int, value.split(',')))
    else:
        return []

def naturaldateyear(value):
    try:    
        return value.strftime("%d %b %Y")
    except:
        return "-"

def datetimelist(value):
    print(value.time().strftime("%H:%M"))
    data = [value.strftime("%d %b %Y"),value.time().strftime("%I:%M %p")]
    return data

def time_m(value):
    time = timezone.localtime(value)
    data = time.time().strftime("%I:%M %p")
    return data


def htmldate(value):
    try:
        return value.strftime("%Y-%m-%d")
    except:
        return value

def get_base_url():
    try:
        request = get_request()
        return request.META['HTTP_HOST']
    except Exception as e:
        print(e)
        return BASE_URL


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'get_base_url':get_base_url,
        'filter': getter_multiple_obj,

    })
    env.filters['naturaltime'] = naturaltime
    env.filters['convert_to_list'] = convert_to_list
    env.filters['naturaldateyear']=naturaldateyear
    env.filters['datetimelist']=datetimelist
    env.filters['time_m']=time_m
    
    
    env.filters['htmldate']=htmldate
    

    return env

def getter_multiple_obj(app_name, model_name, **kwargs):
    """function to get the single model object based on the filter"""
    __class = apps.get_model(app_label=app_name, model_name=model_name)
    return __class.objects.filter(**kwargs)


