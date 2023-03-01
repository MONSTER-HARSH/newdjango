from django.contrib import admin
from .models import container
# Register your models here.
@admin.register(container)

class containerAdmin(admin.ModelAdmin):
    list_display=( 'container_id', 'container_name','container_location', 'container_status', 'container_size', 'cargo',)

