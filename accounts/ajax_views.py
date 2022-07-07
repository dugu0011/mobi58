from accounts.models import *
from django.contrib.auth.models import User
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.decorators import api_view
import json
from django.db.models import Q , Count , Sum
from .utils import *
from django.db.models.functions import ExtractWeekDay
from datetime import datetime , date , timedelta
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import requests

#from accounts.models import GSTDetails


def get_states(request, country_code):
    data = []
    try:
        states = State.objects.filter(country=country_code).order_by('name')
        print(country_code)
        data = get_dict(states)
    except:
        print(request.GET)
    print(data)
    return JsonResponse(data, safe=False)


def get_cities(request, state_id=None):
    data = []
    if state_id:
        cities = City.objects.filter(city_district__district_state__id=state_id).order_by('name')
        data = get_dict(cities)
    else :
        cities = City.objects.all()
    print("data",data)
    return JsonResponse(data, safe=False)


def get_districts(request, state_id=None):
    data = []
    if state_id:
        districts = District.objects.filter(district_state__id=state_id).order_by('name')
        data = get_dict(districts)
    else :
        districts = District.objects.all()
    return JsonResponse(data, safe=False)


def get_district_cities(request, district_id=None):
    data = []
    if district_id:
        cities = City.objects.filter(city_district__id=district_id).order_by('name')
        data = get_dict(cities)
    else :
        cities = City.objects.all()
    print("data",data)
    return JsonResponse(data, safe=False)

def get_dict(queryset):
    """
    return queryset dict
    """
    data = []
    if queryset:
        for q in queryset:
            x = dict()
            x['id'] = q.id
            x['name'] = q.name
            data.append(x)
    return data

@api_view(('GET',))
def validate_unique_mobile(request):
    mobile = request.GET.get('mobile')
    c_mobile = request.GET.get('c_mobile')
    already_exist = 'false'
    if c_mobile and UserProfile.objects.filter(Q(mobile=c_mobile)).exists() :
        already_exist = 'true'
    if mobile and Company.objects.filter(Q(mobile=mobile)).exists():
        already_exist = 'true'
    data = {
        "already_exist":already_exist,
    }
    response = HttpResponse(
            json.dumps(data),
            content_type="application/json"
    )
    return response



@api_view(('GET',))
def validate_unique_company(request):
    c_name = request.GET.get('c_name')
    already_exist = 'false'
    if c_name and Company.objects.filter(Q(name=c_name)).exists():
        already_exist = 'true'
    data = {
        "already_exist":already_exist,
    }
    response = HttpResponse(
            json.dumps(data),
            content_type="application/json"
    )
    return response


@api_view(('GET',))
def validate_unique_user_email(request):
    email = request.GET.get('email')
    already_exist = 'false'
    if email and UserProfile.objects.filter(Q(email=email)).exists():
        already_exist = 'true'
    data = {
        "already_exist":already_exist,
    }
    response = HttpResponse(
            json.dumps(data),
            content_type="application/json"
    )
    return response



@api_view(('GET',))
def get_clients_of_company(request):
    id = request.GET.get('comp_id')
    company = Company.objects.get(id=id)
    user_profile = UserProfile.objects.filter(company=company, user_type="client")
    user = UserProfileSerializer(user_profile, many=True).data
    data = {"user": user}
    response = HttpResponse(
            json.dumps(data),
            content_type="application/json"
    )
    return response


@api_view(('GET',))
def get_gst_info(request):
    try:
        gst_no = request.GET.get('gst_no')
        auth_url = 'https://commonapi.mastersindia.co/oauth/access_token'
        headers = {"Content-Type": "application/json"}
        post_data = {
                        "username": "cto@tech58.in",
                        "password": "Pawan@123",
                        "client_id": "GkOhWSetKHmFVUqrHM",
                        "client_secret": "2NevkSk3B6BxKOMvq4r2FtA9",
                        "grant_type": "password"
                    }

        response = requests.post(auth_url, headers=headers, data=json.dumps(post_data))
        access_token = response.json()['access_token']
        # token_type = response.json()['token_type']
        authorization = 'Bearer' + ' ' + access_token
        url = 'https://commonapi.mastersindia.co/commonapis/searchgstin?gstin=%s' % gst_no
        headers = {'Content-Type': 'application/json', 'Authorization': authorization, 'client_id': "GkOhWSetKHmFVUqrHM"}
        resp_data = requests.get(url, headers=headers)
        dt = resp_data.json().get('data')['tradeNam']
        # response = HttpResponse(resp_data.text, content_type="application/json")

        gst_obj = GSTDetails.objects.filter(gst_id = gst_no ).first()
        if gst_obj:
            gst_obj.no_of_used +=1
            gst_obj.save()
        elif resp_data and resp_data.json():
            GSTDetails.objects.create(gst_id=gst_no ,gst_details=resp_data.json(),
                no_of_used = 1)
        return Response(
            data={'status': True, 'data': dt}, 
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
                    data={'status': False, 'message': str(e)}, 
                    status=status.HTTP_400_BAD_REQUEST
        )
        


@api_view(('GET',))
def get_product_details(request):
    try:
        id = request.GET.get('product_id')
        product = Product.objects.get(id=id)
        product_serialize = ProductSerializer(product).data
        data = {"product": product_serialize}
    except Exception as e:
        print(e)
        data = {}
    response = HttpResponse(
            json.dumps(data),
            content_type="application/json"
    )
    return response



class ForgotPasswordView(viewsets.ViewSet):
    def forgot_password(self, request, **kwargs):
        """
        API to user forgot password
        """
        try:
            data = request.data
            username = data.get('username')
            profile = None
            if is_mobile(username):
                profile = UserProfile.objects.get(mobile=username)
            else:
                profile = UserProfile.objects.get(user__username=username)
            from random import randint
            otp = randint(100000, 999999)
            profile.otp = otp
            profile.save()
            dict_to_send = {"email": profile.email,"subject": "Tech58 - Reset Password OTP !","otp":otp ,
                "template_name": 'email/reset-password.html'}
            send_email(dict_to_send)
            return Response(data={'status': True,'message': 'otp sent successfully.'}, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    data={'status': False, 'message': str(e)}, 
                    status=status.HTTP_400_BAD_REQUEST)

    def reset_password(self, request, **kwargs):
        """
        API to user reset password
        """
        try:
            data = request.data
            otp = data.get('otp')
            username = data.get('username')
            res = {}
            profile = None
            if is_mobile(username):
                profile = UserProfile.objects.get(mobile=username)
            else:
                profile = UserProfile.objects.get(user__username=username)
            if otp == profile.otp:
                res.update({'is_verified':True})
                profile.otp = None
                profile.save()
                request.session['reset_password_user'] = profile.user.id
                return Response(data={'status': True,'data': res,}, 
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    data={'status': False, 'message': 'not verified'}, 
                    status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                    data={'status': False, 'message': str(e)}, 
                    status=status.HTTP_400_BAD_REQUEST)

