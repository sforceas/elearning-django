"""User views"""

# Django
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from courses.models import CourseProgress
# Forms
from users.forms import ProfileForm, SignupForm

# Create your views here.

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.save()

            return redirect('learningpaths')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')           

        else:
            # Return an 'invalid login' error message.
            return render(request,'users/login.html',{'error':'Invalid username or password'})
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    # Redirect to a success page
    return redirect('learningpaths')           

def signup_view(request):
    '''Signup view'''

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form':form}
    )

@login_required
def home_view(request):
    """ Student home page"""

    #Load course progress
    course_progress = list(CourseProgress.objects.filter(user=request.user,registered_flag=True).order_by('-modified'))
                                
    print(course_progress)


    context = {
        'user':request.user,
        'course_progress':course_progress,        
    }
    return render(request,'users/home.html',context)