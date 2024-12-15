from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import Courses, Students


def index(request: WSGIRequest):
    courses = Courses.objects.all()
    students = Students.objects.all()
    context = {
        "courses":courses,
        "students": students
    }

    return render(request, 'index.html', context)

def posts_by_courses(request, course_id):
    courses = Courses.objects.get(id=course_id)
    students = Students.objects.filter(course_id=course_id)
    context = {
        "courses": [courses],
        "students": students
    }
    return render(request, 'index.html', context)

def posts_by_students(request, student_id):
    student = Students.objects.get(id=student_id)  
    context = {
        "student": student,
    }
    return render(request, 'students.html', context)
