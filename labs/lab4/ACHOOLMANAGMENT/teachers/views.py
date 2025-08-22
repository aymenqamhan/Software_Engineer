
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher

# عرض جميع المعلمين
def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers_list.html', {'teachers': teachers})

# إضافة معلم جديد
def teacher_add(request):
    if request.method == "POST":
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        age = request.POST.get('age')
        level = request.POST.get('level')
        subject = request.POST.get('subject')
        status = True if request.POST.get('status') == 'on' else False
        report = request.POST.get('report')

        Teacher.objects.create(
            f_name=f_name,
            l_name=l_name,
            age=age,
            level=level,
            subject=subject,
            status=status,
            report=report
        )
        return redirect('teachers:list')
    return render(request, 'teachers/teacher_form.html', {'action': 'إضافة'})

# تعديل بيانات معلم
def teacher_update(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == "POST":
        teacher.f_name = request.POST.get('f_name')
        teacher.l_name = request.POST.get('l_name')
        teacher.age = request.POST.get('age')
        teacher.level = request.POST.get('level')
        teacher.subject = request.POST.get('subject')
        teacher.status = True if request.POST.get('status') == 'on' else False
        teacher.report = request.POST.get('report')
        teacher.save()
        return redirect('teachers:list')
    return render(request, 'teachers/teacher_form.html', {'teacher': teacher, 'action': 'تعديل'})

# حذف معلم
def teacher_delete(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == "POST":
        teacher.delete()
        return redirect('teachers:list')
    return render(request, 'teachers/teacher_delete.html', {'teacher': teacher})

# تفاصيل معلم
def teacher_detail(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})
