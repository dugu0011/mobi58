from django.urls import path, include
from .views import *


urlpatterns = [
    # path('', homeView, name="homepage"),
    path('adTransporter/', addTransporter, name="add-transporter"),
    path('adVehicle/', addVehicle, name="add-vehicle"),
    path('addDriver/', addriver, name="add-driver"),
    path('addtrip/', adtrip, name="add-trip"),
    path('ProductManager/', proManager, name="product-manager"),

    
    
    

    
]