from django.shortcuts import render,redirect

# Create your views here.


def index (request) :
    return render (request, 'robotics/index.html',{})

def base (request):
    return render (request, 'base.html',{})
