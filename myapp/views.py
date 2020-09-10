from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def signinpage(request):
    return render(request,'signin.html')

def signuppage(request):
    return render(request,'signup.html')