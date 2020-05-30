from django.shortcuts import render
from .forms import RegForm, UserProfileInfoForm, UserForm
from .models import RegisterUser
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        # pass "POST" request to form

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Success
            # print on console
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()        
    return render(request, 'app/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'title': 'Register'})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print('Your account is no longer active.')
        else:
            print('Invalid try! Please register with us.')
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'app/login.html')            

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
