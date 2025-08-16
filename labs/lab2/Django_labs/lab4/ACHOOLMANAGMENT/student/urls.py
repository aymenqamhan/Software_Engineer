from django.urls import path
from . import views  # إذا كان urls داخل نفس التطبيق

urlpatterns = [
    path('base/', views.base_page, name='base'),
    path('deletstudents/', views.delete_student, name='deletstudents'),
    path('tetchers/', views.teachers_page, name='tetchers'),
    path('', views.students_page, name='students'),
]


