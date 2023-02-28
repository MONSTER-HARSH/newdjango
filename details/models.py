from datetime import timezone
from django.db import models

# Create your models here.
class container(models.Model):

    container_status_list = ("E","Empty"),("L","laden")
    cargo_list = ("D","Dry goods"),("H","Hazardous materials"),("L","Liquid cargo")

    container_id = models.IntegerField(primary_key=True)
    container_name = models.CharField(max_length=10) 
    container_status = models.CharField(max_length=10, choices=container_status_list, default="E")
    container_size = models.IntegerField()
    cargo = models.CharField(max_length=20, choices=cargo_list, default="D")
    published = models.DateTimeField(default=timezone)

    def __str__(self):
        return self.container_name