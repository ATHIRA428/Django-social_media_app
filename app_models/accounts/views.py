from .forms import RegisterForm, LoginForm
from model_setup .models import User
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth import logout

def home(request):
    return render(request,'home.html')

def register(request):
    form = RegisterForm()  

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    return render(request, 'register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('home')  
