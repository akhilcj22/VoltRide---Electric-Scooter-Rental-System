from django.contrib import admin
from .models import Scooter, Ride

@admin.register(Scooter)
class ScooterAdmin(admin.ModelAdmin):
    list_display = ('name', 'identifier', 'is_available', 'battery_level', 'created_at')
    list_filter = ('is_available',)
    search_fields = ('name', 'identifier')

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('user', 'scooter', 'start_time', 'end_time', 'cost')
    list_filter = ('start_time', 'end_time')
    search_fields = ('user__username', 'scooter__identifier')