from django.shortcuts import render, redirect
from .forms import Signup, loginform
from .models import UserProfile
from django.contrib import messages

def admin(request):
    return render(request, 'blog/admin.html', {'title': 'Admin'})

def index(request):
    return render(request, 'blog/home.html', {'title': 'home'}) 

def signup(request):
    
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:login')
    else:
        form = Signup()
    out = UserProfile.objects.all
    return render(request, 'blog/signin.html', {'form': form})
    return render(request, 'blog/login.html', { 'out': out})

def login(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            username == form.cleaned_data['username']
            password == form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog: home')
    else:
        form = loginform()
    return render(request, 'blog/login.html', {'title': 'Login', 'form': form})

def adminlogin(request):
    return render(request, 'blog/adminlogin.html', {'title':'Admin-Login'})