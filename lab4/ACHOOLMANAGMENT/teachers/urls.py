from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('', views.teachers_list, name='list'),
    path('add/', views.teacher_add, name='teacher_add'),
    path('update/<int:id>/', views.teacher_update, name='update'),
    path('delete/<int:id>/', views.teacher_delete, name='delete'),
    path('detail/<int:id>/', views.teacher_detail, name='detail'),
]
