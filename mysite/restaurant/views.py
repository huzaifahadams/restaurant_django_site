from django.db import reset_queries
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages

from .models import Blog, Menu
#from django import HttpResponse

# Create your views here.

def index(request):
    menus= Menu.objects.all() #getting all Menus from the database
    return render(request,'index-2.html', {'menus': menus})

def about(request):
    return render(request, 'about.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def blog(request, ):
    blogs= Blog.objects.all() #get all blogs from database
    return render(request, 'blog.html', {'blogs': blogs})

def chef(request):
    return render(request, 'chef.html')

def contact(request):
    return render(request, 'contact.html')

def index2(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def reservation(request):
    return render(request, 'reservation.html')

#registering new user
def register(request):
    if request.method == 'POST':
        #fastname = request.POST['fastname'],
        #lastname = request.POST['lastname'],
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, "Email Already Used")
                return redirect('register')
            elif User.objects.filter(username = username).exists(): 
                messages.info(request, "Username Already Used")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();

                
                return redirect('login')
        else:
            messages.info(request, 'Password is not the same check and try again')
            return redirect('register')

    else:
        return render(request, 'register.html')


#login
def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
        
    else:
        return render(request, 'login.html')

#logout
def logout(request):
    auth.logout(request)

    return redirect('/')