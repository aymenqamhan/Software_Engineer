from django.urls import path
from . import views  # إذا كان urls داخل نفس التطبيق

app_name = 'student'
urlpatterns = [
    path('', views.base_page, name='base'),
    path('deletstudents/', views.delete_student, name='deletstudents'),
    path('tetchers/', views.teachers_page, name='tetchers'),
    path('all/', views.students_page, name='students'),
    path('one/<int:id>/', views.student_one, name='frist_student'), 
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('add/', views.create, name='add_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),   
]


