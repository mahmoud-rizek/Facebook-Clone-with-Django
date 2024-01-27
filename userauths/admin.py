from django.contrib import admin
from .models import User, Profile
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'username', 'email', 'gender']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'verified']
    list_editable= 'verified',

admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile,ProfileAdmin)