from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'cnic_card', 'states', 'Date_Time', 'location', 'p_images']
