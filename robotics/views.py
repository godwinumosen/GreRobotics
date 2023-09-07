from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import GREROBOTICSMODEL
# Create your views here.

def base (request):
    return render (request, 'base.html',{})

#def index (request) :
 #   return render (request, 'robotics/index.html',{})

class HomeListView (ListView) :
    model = GREROBOTICSMODEL
    template_name = 'robotics/index.html'
    ordering = ordering =['-publish_date']
