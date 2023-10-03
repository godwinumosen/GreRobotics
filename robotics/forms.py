from django import forms
from .models import GreRoboticsModel, Category

#choices = [('Robotics','Robotics'), ('Programing Language','Programing Language'), ('Coding Machine','Coding Machine'),]
choices = Category.objects.all().values_list('name','name')

choice_list = []
for items in choices:
    choice_list.append(items)
class GreRoboticsForms (forms.ModelForm):
    class Meta :
        model = GreRoboticsModel
        fields = ('title', 'slug', 'author','category','content',)
        
        widgets = {
            'title' : forms.TextInput (attrs={'class':'form-control',}),
            'slug' : forms.TextInput (attrs={'class':'form-control', }),
            'author' : forms.Select (attrs={'class':'form-control',}),
            'category' : forms.Select (choices=choice_list, attrs={'class':'form-control',}),
            'content' : forms.Textarea (attrs={'class':'form-control'}),
        }
        
        
class EditGreRoboticsForms (forms.ModelForm):
    class Meta :
        model = GreRoboticsModel
        fields = ('title', 'slug','content',)
        
        widgets = {
            'title' : forms.TextInput (attrs={'class':'form-control', 'placeholder':'Your Title Message'}),
            'slug' : forms.TextInput (attrs={'class':'form-control', 'placeholder':'Your Slug Tile'}),
            #'author' : forms.Select (attrs={'class':'form-control',}),
            'content' : forms.Textarea (attrs={'class':'form-control','placeholder':'Your Message Content '}),
        }