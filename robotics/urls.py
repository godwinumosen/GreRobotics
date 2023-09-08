
from django.urls import path
from . import views
from .views import HomeListView
from .views import ArticleDetailView


urlpatterns = [
    path('base/', views.base, name='base'),
    path('', HomeListView.as_view(), name='home'),
    path('home/', HomeListView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]