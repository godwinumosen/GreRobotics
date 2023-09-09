
from django.urls import path
from . import views
from .views import HomeListView, DeletePostview
from .views import ArticleDetailView, AddPostView, UpdatePostView


urlpatterns = [
    path('base/', views.base, name='base'),
    path('', HomeListView.as_view(), name='home'),
    path('home/', HomeListView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostview.as_view(), name='delete_post'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]