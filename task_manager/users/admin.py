from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Users

# Register your models here.


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'username', 'timestamp')
    search_fields = ['first_name', 'username']
    list_filter = (('timestamp', DateFieldListFilter),)
