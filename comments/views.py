from django.shortcuts import redirect, render

from comments.models import Comment

# Create your views here.
#https://stackoverflow.com/questions/60497516/django-add-comment-section-on-posts-feed   

def delete_comment(request,comment_id):
    Comment.objects.filter(id=comment_id).delete()
    return redirect(request.META['HTTP_REFERER']) 