from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Todoserial
from .models import Todo

class Todoview(viewsets.ModelViewSet):
    serializer_class= Todoserial
    queryset = Todo.objects.all()
