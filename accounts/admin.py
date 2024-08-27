from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = ['email', 'name']
    ordering = ['email', 'name']
    list_filter = ['email', 'name', 'email_confirmed']
    fieldsets = [(None, {'fields': ['email', 'name', 'password', 'email_confirmed']})]
    search_fields = ['email', 'name']