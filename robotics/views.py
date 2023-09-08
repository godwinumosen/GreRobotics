from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import GreRoboticsModel
# Create your views here.


#def index (request) :
 #   return render (request, 'robotics/index.html',{})

def base (request):
    return render (request, 'base.html',{})

class HomeListView (ListView) :
    model = GreRoboticsModel
    template_name = 'robotics/index.html'
    ordering =['-publish_date']

class ArticleDetailView (DetailView):
    model = GreRoboticsModel
    template_name = 'robotics/article_details.html'
    
    
    