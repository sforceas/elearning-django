from django.db import models

from users.models import User

# Create your models here.
class LearningPath(models.Model):
    """Learning Path model"""
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    icon=models.ImageField(upload_to= "media/icons")

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
    icon=models.ImageField(upload_to= "media/icons")
    
    duration=models.IntegerField() #Hours of content 
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
    video_path=models.URLField()
    video_file=models.FileField(upload_to='media/lessons/video')

    teacher=models.ForeignKey(User,on_delete=models.PROTECT)
    course=models.ForeignKey(Course,on_delete=models.PROTECT)

    active_flag=models.BooleanField(default=False)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.title
