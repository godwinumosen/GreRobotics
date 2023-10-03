from django.contrib import admin
# Register your models here.
from . import models
from .models import GreRoboticsModel
from .models import Category
    
class GreRoboticsModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','content','author','img']
admin.site.register(GreRoboticsModel, GreRoboticsModelAdmin)
    
class CategoryModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {}
    list_display = ['name']
admin.site.register(Category, CategoryModelAdmin)