from django.urls import path, include
from .views import *


urlpatterns = [
    path('raiseticket/',raiseTicket,name="ticket"),
    path('viewraiseticket/<int:id>/',viewRaiseTicket,name="viewRaiseTicket"),
    path('viewTicket/',viewall,name="viewticket"),
    path('assignme/',assignme,name="assignme"),
    # path('comment/',comment,name="comment"),
    # path('notifications/',all_notifications, name='all_notifications'),
    path('scheduler/',masterui, name='scheduler'),
    
    

    
]