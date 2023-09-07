from django.contrib import admin
# Register your models here.
from .models import GREROBOTICSMODEL


class GREROBOTICSMODELADMIN (admin.ModelAdmin):
    list_display = ['title','content','slug','author']
    admin.site.register (GREROBOTICSMODEL)