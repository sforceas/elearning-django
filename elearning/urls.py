from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

from users import views as users_views
from courses import views as courses_views

"""
Librerias para poder visualizar imagenes o media desde el panel de administracion.
"""
from django.conf import settings
from django.conf.urls.static import static

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    
    path('',courses_views.list_paths, name="learningpaths"),   
    path('path/<int:path_pk>',courses_views.list_courses, name="courses"),
    path('course/<int:course_pk>',courses_views.list_lessons, name="lessons"),
    path('lesson/<int:lesson_pk>',courses_views.show_lesson, name="show_lesson"),

    #USERS

    path('users/login',users_views.login_view, name="login"),
    path('users/logout',users_views.logout_view, name="logout"),
    path('users/signup',users_views.signup_view, name="signup"),
    path('users/logout',users_views.update_profile, name="update_profile"),

    #ADMIN
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # Configurado en settings.py para mostrar media durante desarrollo


