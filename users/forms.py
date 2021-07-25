"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """User form"""
    username = forms.CharField(label=False,min_length=4,max_length=50, widget = forms.TextInput(attrs={'placeholder':'Nombre de usuario','class': 'form-control','required': True}))
    password = forms.CharField(label=False,max_length=70, widget=forms.PasswordInput(attrs={'placeholder':'Escribe tu contraseña','class': 'form-control','required': True}))
    password_confirmation = forms.CharField(label=False,max_length=70, widget=forms.PasswordInput(attrs={'placeholder':'Confirma tu contraseña','class': 'form-control','required': True}))
    first_name = forms.CharField(label=False,min_length=2,max_length=50,widget = forms.TextInput(attrs={'placeholder':'Nombres','class': 'form-control','required': True}))
    last_name = forms.CharField(label=False,min_length=2,max_length=50,widget = forms.TextInput(attrs={'placeholder':'Apellidos','class': 'form-control','required': True}))
    email = forms.EmailField(label=False,min_length=6,max_length=70,widget=forms.EmailInput(attrs={'placeholder':'Correo electrónico','class': 'form-control','required': True}))

    """Validations"""

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username
    
    def clean_email(self):
        """Email must be unique"""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('Email is already in use.')
        return email

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

    def save(self):
        """Saves the new user on the DB"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()




class ProfileForm(forms.Form):
    """Profile form."""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    role = forms.CharField(max_length=100, required=False)
