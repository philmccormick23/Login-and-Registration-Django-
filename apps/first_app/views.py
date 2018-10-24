from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string
import random
from .models import User
# the index function is called when root is visited

def index(request):
    dictionary = {
        'users' : User.objects.all()
    }
    
    return render(request, 'index.html', dictionary)

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        u=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['id']=u.id
        request.session['name']=u.first_name
        
        return redirect('/success')

def success(request):
    return render(request,'success.html')

def login(request):
    users=User.objects.all()
    for thing in users:
        if request.POST['email'] == thing.email and request.POST['password'] == thing.password:
            u=User.objects.get(email=request.POST['email'])
            request.session['id']=u.id
            request.session['name']=u.first_name 
    return redirect('/success')