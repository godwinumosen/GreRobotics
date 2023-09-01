from django.shortcuts import render,redirect

# Create your views here.

def index (request) :
    return render (request, 'robotics/index.html')