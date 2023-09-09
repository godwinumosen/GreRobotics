
from django.urls import path
from . import views
from .views import HomeListView
from .views import ArticleDetailView, AddPostView, UpdatePostView


urlpatterns = [
    path('base/', views.base, name='base'),
    path('', HomeListView.as_view(), name='home'),
    path('home/', HomeListView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('contact/', views.contact, name='contact'),
]