from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import GreRoboticsModel, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GreRoboticsForms, EditGreRoboticsForms
from django.urls import reverse_lazy

#def index (request) :
 #   return render (request, 'robotics/index.html',{})

def base (request):
    return render (request, 'base.html',{})

#The HomeListView
class HomeListView (ListView) :
    model = GreRoboticsModel
    template_name = 'robotics/index.html'
    ordering =['-publish_date']

#The CategoryView
def CategoryView (request, cats):
    category_posts = Category.objects.filter(category=cats)
    return render (request, 'robotics/categories.html', {'cats':cats,'category_posts':category_posts})

#The ArticleDetailView
class ArticleDetailView (DetailView):
    model = GreRoboticsModel
    template_name = 'robotics/detail.html'
    
    def ArticleDetailView(request, pk):  
        object = get_object_or_404(GreRoboticsModel, pk=pk)
        return render(request, 'detail.html', {'detail': object})

#The AddPostView    
class AddPostView (CreateView):
    model = GreRoboticsModel
    form_class = GreRoboticsForms
    template_name = 'robotics/add_post.html'  
    #fields = ('title', 'content', 'slug', 'author',)


#The AddCategoryView    
class AddCategoryView (CreateView):
    model = Category
    #form_class = GreRoboticsForms
    template_name = 'robotics/add_category.html'  
    fields = '__all__'

#The UpdatePostView    
class UpdatePostView (UpdateView):
    model = GreRoboticsModel
    form_class = EditGreRoboticsForms
    template_name = 'robotics/update_post.html'
    #fields = ('title', 'content', 'slug',)

# The DeletePostview
class DeletePostview (DeleteView):
    model = GreRoboticsModel
    template_name = 'robotics/delete_post.html' 
    success_url = reverse_lazy ('home')
    

# The Contact
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

#The About
def about (request):
    return render (request, 'robotics/about.html',{})

#Whatsapp Messages
def whatsapp_message(request):
    whatsapp_number = '+2348071719075'
    whatsapp_link = f'https://api.whatsapp.com/send?phone={whatsapp_number}'
    context = {'whatsapp_link': whatsapp_link}
    return render(request, 'whatsapp_message.html' context)
