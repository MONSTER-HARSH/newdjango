from django.shortcuts import render,redirect
from .models import container
# Create your views here.

from django.contrib import messages


# Create your views here.

def createcontainer(request):
    return render(request,'forms.html')

def store(request):
    container_obj = container()
    container_obj.container_name = request.POST.get('name')
    container_obj.container_location = request.POST.get('location')
    container_obj.container_status = request.POST.get('status')
    container_obj.container_size = request.POST.get('size')
    container_obj.cargo= request.POST.get('cargo')
    container_obj.save()
    messages.success(request, "container Created Successfully")
    return redirect('/')

def index(request):
    container_obj= container.objects.all()
    return render(request, 'tables.html',{'container':container_obj})

def updatecontainer(request,pk):
    container_obj = container.objects.get(container_id = pk)
    return render(request,'index.html',{'container':container_obj})

def searchcontainer(request):
    container_obj = container()
    container_obj.container_name = request.POST.get('search')
    return redirect('containerview/','search')

def viewcontainer(request, pk):
   container_obj = container.objects.get(container_id = pk)
   return render(request, 'view.html',{'container':container_obj})

def deletecontainer(request, pk):
    container_obj= container.objects.get(container_id = pk)
    container_obj.delete()
    messages.success(request, "container Deleted Successfully")
    return redirect('/')

def home(request):
    return render(request, 'home.html')
