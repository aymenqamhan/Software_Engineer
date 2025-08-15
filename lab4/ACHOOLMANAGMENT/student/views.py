from django.shortcuts import render

# Create your views here.

def base_page(request):
    return render(request, 'base.html')


def delete_student(request):
    return render(request, 'deletstudents.html')

def students_page(request):
    return render(request, 'students.html')

def teachers_page(request):
    return render(request, 'tetchers.html')