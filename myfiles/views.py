from django.shortcuts import render
from .models import *
# Create your views here.

def home(malumot):
    cars = Cars.objects.all()
    return render(malumot,'index.html',{"cars":cars})

def home2(malumot):
    return render(malumot,'index2.html')