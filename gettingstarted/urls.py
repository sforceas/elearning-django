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
    
       
    path("",courses_views.index, name="index"),


    #ADMIN
    path("admin/", admin.site.urls),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # Configurado en settings.py para mostrar media durante desarrollo


