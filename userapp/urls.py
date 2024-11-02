from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('reg',views.reg),
    path('log',views.log),
    path('home',views.home),
    path('newstockview',views.newstockview),
    path('personal',views.personal),
    path('medsearch',views.medsearch),
    path('dissearch',views.dissearch),
    path('addtocart',views.addtocart),
    path('viewcart',views.viewcart),
    path('cartdelete',views.cartdelete),
    path('paydirect',views.paydirect),
    path('pay',views.pay),
    path('feedback',views.feedback),
    path('userbill',views.userbill),
]