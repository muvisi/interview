from django.shortcuts import render

# Create your views here.
from form1A.models import RegisterForm1A
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import  Form1Aserializer
from rest_framework import viewsets
from django.contrib.auth.models import User
class Form1AViewset (viewsets.ModelViewSet):
     queryset=RegisterForm1A.objects.all()
     serializer_class=Form1Aserializer