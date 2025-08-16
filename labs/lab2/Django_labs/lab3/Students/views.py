from django.shortcuts import render
from datetime import datetime, timedelta


def index(request):
    return render(request, 'index.html')  # مباشرة دون مسار فرعي

def home(request):
    return render(request, 'home.html')  # صفحة رئيسية لتطبيق الطلاب

def show_students(request):
    return render(request, 'showstudents.html')  # عرض الطلاب`)

# def edit_students(request):
#     return render(request, 'editstudents.html')

def delete_students(request):
    return render(request, 'deletestudent.html')



# داله للتعاكل مع المتغيرات 

def list_students(request):
    students = {
        "name": "Aymen",
        "marks": [30, 55.77, 88, 99],
        "eachsub": {
            "software_engineer": 90,
            "math": 80,
            "english": 70,
            "arabic": 60
        }
    }
    return render(request, 'showstudents.html', students)

#داله للتعامل مع الفلاتر 
def index(request):
    name={"fname":"Aymen"}
    return render(request, 'index.html',name)

# للتعامل مع جمل التحكم 

def edit_students(request):
    students_data = {
        "total": "343",
        "marks": [30, 55.77, 88, 99],
        "eachsub": {
            "software_engineer": 90,
            "math": 80,
            "english": 70,
            "arabic": 60
        }
    }
    return render(request, 'editstudents.html', students_data)

def filters_demo(request):
    context = {
        "fname": "ahmed",
        "text": "Django is an amazing web framework",
        "multiline_text": "Line one\nLine two\nLine three",
        "number": 5,
        "pi": 3.14159265,
        "file_size": 2048000,
        "big_number": 123456789,
        "small_number": 4,
        "today": datetime.now().date(),
        "now": datetime.now(),
        "past_date": datetime.now() - timedelta(days=2),
        "future_date": datetime.now() + timedelta(hours=5),
        "mylist": ["Ali", "Mona", "Sara"],
        "value_none": None,
        "is_active": True,
        "html_text": "<strong>Hello HTML</strong>",
        "count": 3,
        "complex_data": {"name": "Ali", "age": 25, "skills": ["Python", "Django"]}
    }
    return render(request, "filters_demo.html", context)
