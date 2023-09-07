
from django.urls import path
from . import views
from .views import HomeListView


urlpatterns = [
    path('base/', views.base, name='base'),
    path('', HomeListView.as_view(), name='home'),
    path('home/', HomeListView.as_view(), name='home'),
]