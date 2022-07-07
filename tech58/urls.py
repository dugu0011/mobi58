from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#Public


##Sub-Master

# Mines Transaction



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('Ticket/',include('Ticket.urls')),
    path('mobi58/',include('mobi58.urls')) 
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
