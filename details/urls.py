
from django.urls import path,include
from .views import *



urlpatterns = [
    path('create',createcontainer),
    path('store',store,name='store'),
    path('',index),
    path('containerview/<int:pk>',viewcontainer,name='viewcontainer'),
    path('delete/<int:pk>',deletecontainer,name='deletecontainer'),
    path('update/<int:pk>',updatecontainer, name='updatecontainer'),
]