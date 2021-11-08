from django.core.files.storage import default_storage
from django.db import models
#from embed_video.fields import EmbedVideoField

from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField

from users.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class LearningPath(models.Model):
    """Learning Path model"""
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    icon=CloudinaryField('Path Icon',blank=True, folder= '/learning_paths/icons/')
    thumbnail=CloudinaryField('Path Thumbnail',blank=True, folder= '/learning_paths/thumbnails/')

    active_flag=models.BooleanField(default=False)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return title."""
        return self.title
    
class Course(models.Model):
    """Course model"""
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    icon=CloudinaryField('Course Icon',blank=True, folder= '/courses/icons/')
    thumbnail=CloudinaryField('Course Thumbnail',blank=True, folder= '/courses/thumbnails/')
    
    duration=models.IntegerField(blank=True) #Hours of content 
    teacher=models.ForeignKey(User,on_delete=models.PROTECT)
    learning_path=models.ForeignKey(LearningPath,on_delete=models.PROTECT)
    
    active_flag=models.BooleanField(default=False)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.title

class Lesson(models.Model):
    """Lesson model"""
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    video_url=models.URLField(blank=True)
    thumbnail=CloudinaryField('Thumbnail',blank=True, folder= '/lessons/thumbnails/')
    attached_files=CloudinaryField('Attached files (.zip)',blank=True,folder='/lessons/attached_files/')

    teacher=models.ForeignKey(User,on_delete=models.PROTECT)
    course=models.ForeignKey(Course,on_delete=models.PROTECT)

    active_flag=models.BooleanField(default=False)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.title

class CourseProgress(models.Model):
    """Tracking of a user progress on a course"""
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    completed_lessons=models.ManyToManyField(Lesson,related_name='completed_lessons')
    last_lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='last_lesson')

    approved_flag=models.BooleanField(default=False)
    registered_flag=models.BooleanField(default=True)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return 'Progress in {} by {}'.format(self.course.title,self.user.username) 