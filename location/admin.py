from django.contrib import admin
from .models import *

class LocationAdmin(admin.ModelAdmin):
    search_fields = ['latitude', 'longitude', 'uploaded_by__user__username']
    list_display = ['latitude', 'longitude', 'created_time', 'uploaded_by']

class DeviceAdmin(admin.ModelAdmin):
    search_fields = ['device_id', 'user__username']
    list_display = ['device_id', 'user', 'is_active']

class AccountAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    list_display = ['username', 'email']

admin.site.register(Location, LocationAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Account, AccountAdmin)
