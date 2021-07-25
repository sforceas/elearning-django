"""User admin classes"""
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Models
from users.models import Profile
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk','user','phone_number','website') # Campos que debe mostrar en el display de admin
    list_display_links=('pk','user') # Elementos linkados al detalle
    list_editable=() # Elementos editables desde admin
    
    # Creamos un buscador de usuarios segun los siguientes campos
    search_field = (
        'user__username'
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    # Creamos un filtro con los siguientes campos
    
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        
    )

    # Si queremos especificar que campos pueden modificarse desde el dashboard de Djando Admin usams fieldsets

    fieldsets = (
        ('Profile',{
            'fields':(('user'),)
        }),

        ('Extra info', {
            'fields': (
                ('website','phone_number'),
                ('biography')
            )
        }),

        ('Metadata', {
            'fields': (('created','modified'),)
        })
    )

    readonly_fields = ('created','modified','user') # Evita que estos campos se puedan modificar en el dashboard. Además evita que se generen errores al ser 'created' un campo no editable


    """
    Con el siguiente bloque, permitimos que al crear un nuevo usuario, podamos crear el profile directamente.
    """

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = list(BaseUserAdmin.list_display) + ['is_active']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)