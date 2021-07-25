"""Course admin classes"""
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

#Django
from django.contrib import admin

#Models
from courses.models import LearningPath, Course

# Inlime models

class CourseInline(admin.StackedInline):
    model = Course
    extra=0
    can_delete = False
    verbose_name = 'Course'
    verbose_name_plural = 'Courses'
    
# Register your models here.

@admin.register(LearningPath)
class LearningPathAdmin(admin.ModelAdmin):
    """LearningPath admin"""
    list_display = ('pk','title','active_flag') # Campos que debe mostrar en el display de admin
    list_display_links=('pk','title') # Elementos linkados al detalle
    list_editable=() # Elementos editables desde admin
    
    inlines=[CourseInline]


    # Creamos un buscador de usuarios segun los siguientes campos
    search_field= (
        'title',
    )

    # Creamos un filtro con los siguientes campos
    list_filter = (
        'created',
        'modified',        
    )

    readonly_fields = ('created','modified')



@admin.register(Course)
class Course(admin.ModelAdmin):
    """Course admin"""
    list_display = ('pk','title','learning_path','active_flag') # Campos que debe mostrar en el display de admin
    list_display_links=('pk','title','learning_path') # Elementos linkados al detalle
    list_editable=() # Elementos editables desde admin
    
    search_field= (
        'title',
    )

    list_filter = (
        'created',
        'modified',        
    )

    readonly_fields = ('created','modified')

