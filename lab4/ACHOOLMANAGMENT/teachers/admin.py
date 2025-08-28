from django.contrib import admin

# Register your models here.
from .models import Teacher 

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['f_name', 'l_name', 'level', 'subject', 'status', 'age', 'report']
    list_display_links = ['l_name']
    list_editable = ['f_name', 'subject']
    search_fields = ['f_name', 'l_name', 'subject']
    fields = ['f_name', 'l_name', 'age', 'level', 'subject', 'status', 'report']
    list_filter = ['status', 'level']
    list_per_page = 10
admin.site.register(Teacher, TeacherAdmin)
