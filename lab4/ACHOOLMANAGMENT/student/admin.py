from django.contrib import admin
from .models import Students

# هنا نقوم بتضمين المودل الخاص بنا الموجدود في ال students 
#Register your models here.
#admin.site.register(Students)
#admin.site.register(Tetcher)


class StudentAdminForm(admin.ModelAdmin): 
    list_display=['f_name','l_name','gpa','status','age','reporet'] 
    list_display_links=['l_name'] 
    list_editable=['f_name','gpa','status'] 
    search_fields=['f_name','l_name'] 
    fields=['f_name','l_name','gpa'] 
    list_filter=['status','gpa'] 
    list_per_page=2
admin.site.register(Students,StudentAdminForm) 

