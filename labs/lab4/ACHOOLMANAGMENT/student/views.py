from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from .models import Students, Tetchers
# Create your views here.

def base_page(request):
    return render(request, 'base.html')


# def delete_student(request):
#     return render(request, 'deletstudents.html')

def students_page(request):
    # جلب جميع الطلاب من قاعدة البيانات
    students = Students.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students.html', context)

def teachers_page(request):
    # جلب جميع المعلمين من قاعدة البيانات
    tetchers= Tetchers.objects.all()
    context = {
        'tetchers': tetchers
    }
    return render(request,'tetchers.html',context)

def student_one(request,id):
    student = Students.objects.get(id=id)
    return render(request, 'frist_student.html', {'student': student})

def create(request):
    if request.method == "POST":
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        age = request.POST.get('age')
        lavel = request.POST.get('lavel')
        gpa = request.POST.get('gpa')
        status = True if request.POST.get('status') == 'on' else False
        reporet = request.POST.get('reporet')

        new_student = Students(
            f_name=f_name,
            l_name=l_name,
            age=age,
            lavel=lavel,
            gpa=gpa,
            status=status,
            reporet=reporet
        )
        new_student.save()
        return render(request, 'students.html', {'students': Students.objects.all()})
    return render(request,'addstudent.html')


def update_student(request, id):
    student = get_object_or_404(Students, id=id)  # يجلب الطالب أو يرجع 404 لو مش موجود

    if request.method == "POST":
        student.f_name = request.POST.get("f_name")
        student.l_name = request.POST.get("l_name")
        student.age = request.POST.get("age")
        student.lavel = request.POST.get("lavel")
        student.gpa = request.POST.get("gpa")
        student.status = True if request.POST.get("status") == "on" else False
        student.reporet = request.POST.get("reporet")

        student.save() 
        return redirect("student:students")  
    return render(request, "update_student.html", {"student": student})
 
def delete_student(request, id):
    student = get_object_or_404(Students, id=id)
    student.delete()
    return redirect("student:students")  # يرجع لصفحة الطلاب


