from django.urls import path
from . import views
urlpatterns = [
  
    path('shoplog',views.shoplog),
    path('shophome',views.shophome),
    path('mednewreg',views.mednewreg),
    path('salesbillnew',views.salesbillnew),
   
    
]   