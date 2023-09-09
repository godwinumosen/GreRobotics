from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import GreRoboticsModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GreRoboticsForms, EditGreRoboticsForms
from django.urls import reverse_lazy
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
    template_name = 'robotics/detail.html'
    
    def ArticleDetailView(request, pk):  
        object = get_object_or_404(GreRoboticsModel, pk=pk)
        return render(request, 'detail.html', {'detail': object})
    
class AddPostView (CreateView):
    model = GreRoboticsModel
    form_class = GreRoboticsForms
    template_name = 'robotics/add_post.html'  
    #fields = ('title', 'content', 'slug', 'author',)
    
class UpdatePostView (UpdateView):
    model = GreRoboticsModel
    form_class = EditGreRoboticsForms
    template_name = 'robotics/update_post.html'
    #fields = ('title', 'content', 'slug',)

class DeletePostview (DeleteView):
    model = GreRoboticsModel
    template_name = 'robotics/delete_post.html' 
    success_url = reverse_lazy ('home')
    

#contact
def contact (request):
    email='grerobotics@gmail.com'
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        messages.success(request, f'Your email was sent Successfully we will get back to you {message_name}..!')
        return redirect('/home')
    else:
        context={
            'email':email
        }
        return render(request, 'robotics/contact.html',context)
    
def about (request):
    
    return render (request, 'robotics/about.html',{})