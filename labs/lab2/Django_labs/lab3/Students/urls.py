from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns = [
    path('', views.index, name='index'),

    path('home/',views.home,name='home'),
   # path('show/',views.show_students,name='show'),
    path('edit/',views.edit_students,name='edit'),
    path('delete/',views.delete_students,name='delete'),

    path('show/', views.list_students, name='show'),
    path('filters/', views.filters_demo, name='filters_demo'),
]
