from django.shortcuts import render,redirect

# Create your views here.

def signup(request):

    return render(request, 'signup.html')

def login(request):

    return render(request, 'login.html')