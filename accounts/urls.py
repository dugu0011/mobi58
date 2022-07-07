from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', homeView, name="homepage"),
    path('', indexView, name="sale-dashboard"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('forgot-password/', forgot_password, name="forgot-password"),
    path('reset-password/', reset_password, name="reset-password"),
    path('logout/', logout, name="logout"),
    path('ajax/', include('accounts.ajax_urls')),
   
]