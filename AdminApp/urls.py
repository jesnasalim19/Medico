from django.urls import path
from . import views
urlpatterns = [
  
    path('',views.adminlog),
    path('adminhome',views.adminhome),
    path('userview',views.userview),
    path('edit',views.edit),
    path('delete',views.delete),
    path('update',views.update),
    path('bookings',views.bookings),
    path('cancelbook',views.cancelbook),
    path('confirmbook',views.confirmbook),
    path('newstockview',views.newstockview),
    path('feedview',views.feedview),
   
]   
