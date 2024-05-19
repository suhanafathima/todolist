from django.contrib import admin
from .models import Todo

class Todoadmin (admin.ModelAdmin):
    list_display = ("title",'description','completed')

admin.site.register(Todo,Todoadmin)

