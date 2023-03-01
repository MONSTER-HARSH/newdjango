from django.utils import timezone
from django.db import models

# Create your models here.
class container(models.Model):
    container_s=(20,20),(40,40)
    container_status_list = ("E","Empty"),("L","laden")
    cargo_list = ("D","Dry goods"),("H","Hazardous materials"),("L","Liquid cargo")

    container_id = models.IntegerField(primary_key=True)
    container_name = models.CharField(max_length=10,default=0) 
    container_location = models.CharField(max_length=10,default=0)
    container_status = models.CharField(max_length=10, choices=container_status_list, default="E")
    container_size = models.IntegerField(choices=container_s, default=40)
    cargo = models.CharField(max_length=20, choices=cargo_list, default="D")




