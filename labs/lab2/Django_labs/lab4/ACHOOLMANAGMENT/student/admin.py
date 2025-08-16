from django.contrib import admin

# هنا نقوم بتضمين المودل الخاص بنا الموجدود في ال students 
from .models import Students
# Register your models here.
admin.site.register(Students)