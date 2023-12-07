from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Nadeem',
        'title': 'Aragorn the Epitime of Masculinity',
        'date': '03-07-2002',
        'read_time': '5 mins'
    },
    {
        'author': 'Fadhil',
        'title': 'Honda Cbr still Unbeatable',
        'date': '30-11-2023',
        'read_time': '10 mins'
    }
]
def admin(request):
    return render(request, 'blog/admin.html',{'title': 'Admin'})

def nadeem(request):
    return HttpResponse('<h2>Muhammed Nadeem</h2>')

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'}) 

def signup(request):
    title = "Signup"
    return render(request,'blog/signin.html',{'title': 'Signup'})

def login(request):
    return render(request, 'blog/login.html', {'title':'Login'})