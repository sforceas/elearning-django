from django.db import models

from users.models import User
from courses.models import Lesson

# Create your models here.
class Comment(models.Model): 
    id = models.BigAutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="usernames")
    body = models.TextField()
    cathegory = models.CharField(max_length=255, choices=[('comment','Comment'),('question','Question'),],default='comment') #TEMPORAL
    
    active_flag = models.BooleanField(default=True) 

    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {}'.format(self.user) 


class AnswerComment(models.Model):
    comment = models.ForeignKey(Comment,related_name='answer_comment',on_delete=models.CASCADE,)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField() 
    
    active_flag = models.BooleanField(default=True) 

    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    
    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Answer to comment by {}'.format(self.user) 
