from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class GREROBOTICSMODEL (models.Model):
    title = models.CharField (max_length=500)
    content = models.TextField ()
    slug = models.SlugField (max_length=200)
    img = models.ImageField ( upload_to= 'image/')
    publish_date = models.DateTimeField (auto_now_add= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering =['-publish_date']
    
    def __str__(self):
        return self.title
    
     
    def get_absolute_url(self):
        return reverse ('detail', args=(str(self.id)))
    
    @property
    def image_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url
    