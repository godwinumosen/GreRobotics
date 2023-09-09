from django import forms
from .models import GreRoboticsModel

class GreRoboticsForms (forms.ModelForm):
    class Meta :
        model = GreRoboticsModel
        fields = ('title', 'slug', 'author','content',)
        
        widgets = {
            'title' : forms.TextInput (attrs={'class':'form-control', 'placeholder':'Your Title Message'}),
            'slug' : forms.TextInput (attrs={'class':'form-control', 'placeholder':'Your Slug Tile'}),
            'author' : forms.Select (attrs={'class':'form-control',}),
            'content' : forms.Textarea (attrs={'class':'form-control','placeholder':'Your Message Content '}),
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