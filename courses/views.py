from functools import total_ordering
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from comments.forms import CommentForm


from courses.models import LearningPath,Course,Lesson
from comments.models import AnswerComment, Comment


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

@login_required
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

    #lesson = Lesson.objects.get(pk=lesson_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk,
                                   active_flag=True,)
    
    # COMMENT FORM
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet 
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.lesson = lesson
            new_comment.user = request.user
            # Save the comment to the database
            new_comment.save()
            # Reset comment form
            new_comment = None 
            comment_form = CommentForm()  

    else: # Request method GET
        comment_form = CommentForm()      

    #LOAD COMMENTS 

    comments = list(lesson.comments.filter(active_flag=True,cathegory='comment').order_by('-created'))
    questions = list(lesson.comments.filter(active_flag=True,cathegory='question').order_by('-created'))

    # Crear lista de respuestas de comentarios
    comments_pk_list=[]
    for comment in comments:
        comments_pk_list.append(comment.pk)
    answer_comments = list(AnswerComment.objects.filter(comment__in=comments_pk_list))

    # Crear lista de respuestas de preguntas
    questions_pk_list=[]
    for question in questions:
        questions_pk_list.append(question.pk)
    answer_questions = list(AnswerComment.objects.filter(comment__in=questions_pk_list))

    context = {
        'lesson':lesson,
        'comments':comments,
        'questions':questions,
        'answer_comments':answer_comments,
        'answer_questions':answer_questions,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }


    return render(request,'courses/show_lesson.html',context)



