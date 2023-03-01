
from django.urls import path,include
from .views import *



urlpatterns = [
    path('create',createcontainer),
    path('store',store,name='store'),
    path('',index),
    path('home',home),
    path('containerview',searchcontainer,name='searchcontainer'),
    path('containerview/<int:pk>',viewcontainer,name='viewcontainer'),
    path('update/<int:pk>',updatecontainer, name='updatecontainer'),
    path('delete/<int:pk>',deletecontainer,name='deletecontainer'),
]