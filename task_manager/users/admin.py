from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Users

# Register your models here.


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'full_name', 'timestamp')
    search_fields = ['user_name', 'full_name']
    list_filter = (('timestamp', DateFieldListFilter),)
