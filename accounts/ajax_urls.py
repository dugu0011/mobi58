from django.urls import path, include
from .ajax_views import *


urlpatterns = [
    #Forgot Password
    path('forgot-password/', ForgotPasswordView.as_view({'post': 'forgot_password'}),name="forgot_password_api"),
    path('reset-password/', ForgotPasswordView.as_view({'post': 'reset_password'}),name="reset_password_api"),
    path('get-product/', get_product_details, name="get_product_details"),

]