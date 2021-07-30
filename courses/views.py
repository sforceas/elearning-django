from functools import total_ordering
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string


from courses.models import LearningPath,Course,Lesson


from datetime import datetime

# Create your views here.

def list_paths(request):
    """ List existing learning paths"""
    
    learningpaths = LearningPath.objects.filter(active_flag=True).order_by('-pk')

    context = {
        'learningpaths':learningpaths,
    }
    return render(request,'courses/learningpaths.html',context)

def list_courses(request,path_pk):
    """ List existing courses for a learning path"""
    
    learningpath = LearningPath.objects.get(pk=path_pk)
    courses = Course.objects.filter(learning_path=learningpath,active_flag=True).order_by('pk')
    
    def calculate_duration(courses):  
        total_duration = 0
        for course in courses:
            total_duration=total_duration+course.duration
        return total_duration

    path_duration = calculate_duration(courses)

    context = {
        'learningpath':learningpath,
        'courses':courses,
        'path_duration':path_duration,
    }
    return render(request,'courses/courses.html',context)

def list_lessons(request,course_pk):
    """ List existing lessons"""
    
    course = Course.objects.get(pk=course_pk)
    lessons = Lesson.objects.filter(course=course,active_flag=True).order_by('pk')


    context = {
        'course':course,
        'lessons':lessons,
    }
    return render(request,'courses/lessons.html',context)

@login_required
def show_lesson(request,lesson_pk):
    """ Show a lesson"""
    
    lesson = Course.objects.get(pk=lesson_pk)

    context = {
        'lesson':lesson,
    }
    return render(request,'courses/show_lesson.html',context)



