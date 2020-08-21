from django.contrib import admin
from .models import *


class DataAdmin (admin.ModelAdmin):
    list_display = ['name']


admin.site.register (Data, DataAdmin)
