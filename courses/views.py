from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from courses.models import LearningPath,Course,Lesson


from datetime import datetime

# Create your views here.

def index(request):
    """ List existing learning paths"""
    
    learningpaths = LearningPath.objects.all().order_by('-created')
    

    context = {
        'learningpaths':learningpaths
    }

    return render(request,'courses/learningpaths.html',context)

