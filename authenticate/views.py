from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm
from home import views
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http.response import HttpResponse, HttpResponseForbidden

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse(views.home))
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {'form':form})


def update_user(request, user_id):
    if request.user.is_staff:
        user = User.objects.get(pk=user_id)
        form = RegisterForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse(registered_users_view))
        
        return render(request, 'register/register.html', {'form':form, 'update':True})
    else:
        return HttpResponseForbidden("<h1>Access Forbidden</h1>")
    
    

def remove_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect(reverse(registered_users_view))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username, password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def registered_users_view(request):
    if request.user.is_staff:
        users = User.objects.all()
        return render(request, 'register/registered_users.html', {'users':users})
    else:
        return redirect(reverse('home'))