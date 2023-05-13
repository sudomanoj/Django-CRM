from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been loggedin')
            return redirect('home')
        else:
            messages.error(request, 'There was an error while logging in')
            return redirect('home')
    return render(request, 'website/home.html')



def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logged out!')
    return redirect('home')

def register_user(request):
    return render(request, 'website/register.html', {})